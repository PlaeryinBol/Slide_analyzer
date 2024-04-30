import base64
import io
import json
import logging
import re
from typing import Any, List, Str, Union

import pandas as pd
from json_repair import repair_json
from PIL import Image
from tqdm import tqdm

import config
from chat import OpenaiChat

logger = logging.getLogger()
logger.handlers = []
file_handler = logging.FileHandler(filename="app.log", mode="w")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)


class SlideAnalyzer():
    def __init__(self, data_list) -> None:
        self.data_list = data_list
        self.openai_chat = OpenaiChat(config.OPENAI_MODEL)

    def repair_completion(self, completion: Str) -> Str:
        """Fixes json string (removing text before the first '{' and after the last '}' and etc.)."""
        completion = re.sub(r'}[^}]*$', r'}', re.sub(r'^[^{]*', '', completion, flags=re.DOTALL))
        repaired_completion = repair_json(completion, return_objects=True)
        return repaired_completion

    def resize_image(self, image_path: Str) -> Any:
        """Image resize with maintaining the proportions."""
        image = Image.open(image_path)
        width, height = image.size

        if width > height:
            new_width = config.IMG_SIZE[0]
            new_height = int(height * (config.IMG_SIZE[0] / width))
        else:
            new_width = int(width * (config.IMG_SIZE[0] / height))
            new_height = config.IMG_SIZE[0]

        resized_image = image.resize((new_width, new_height))
        return resized_image

    def extract_data(self, input_data: Union[Str, Any], prompt_template: Str,
                     temperature: float, result_count: int) -> List[Str]:
        """Extracting target data from single text/image via chatgpt."""
        prompt_template = prompt_template.format(INPUT_TEXT=input_data, MAX_VALUE=result_count)

        if not config.CHAT_WITH_IMAGE:
            logger.info(f"Slide text:\n{input_data}")
            input_data = None

        completion = self.openai_chat.chat(prompt_template, temperature, input_data)

        try:
            cleared_result = self.repair_completion(completion)
            # for markup target result is json dict
            if config.MODE == 'markup_extraction':
                result = [json.dumps(cleared_result, indent=4)]
                logger.info(f"Result:\n{result[0]}\n{'-' * 30}")
            else:
                if result_count > 1:
                    result = [el.replace("'", '').replace('"', '').strip().lower()
                              for el in cleared_result['result'][:result_count]]
                    result = result + [None] * (result_count - len(result))
                else:
                    result = [cleared_result['result'].replace("'", '').replace('"', '').strip().lower()]
                logger.info(f"Result:\n{json.dumps(result, indent=4)}\n{'-' * 30}")
        except Exception as e:
            logger.error(f"Error: {e} for \n{completion}{'-' * 30}")
            result = [None] * result_count
        return result

    def extraction(self, prompt_template: Str, temperature: float, result_count: int) -> Any:
        """Extracting target data for bunch of text/image paths, packing to dataframe."""
        results = []
        for _, data in enumerate(tqdm(self.data_list)):
            try:
                if config.CHAT_WITH_IMAGE:
                    logger.info(f"Image:\n{data}\n")
                    resized_image = self.resize_image(data)
                    with io.BytesIO() as buffer:
                        resized_image.save(buffer, format="PNG")
                        data = base64.b64encode(buffer.getvalue()).decode("utf-8")
                extracted_data = self.extract_data(data, prompt_template, temperature, result_count)
            except Exception as e:
                logger.error(f"Error: {e} for \n{data}")
                extracted_data = None
            results.append(extracted_data)

        if result_count > 1:
            column_names = [f'{config.MODE}_{i}' for i in range(1, result_count + 1)]
        else:
            column_names = [config.MODE]

        result_df = pd.DataFrame(results, columns=column_names)
        return result_df
