import base64
import io
import re
from typing import Any, Dict, Str, Tuple

import gradio as gr
from json_repair import repair_json

import config
from chat import OpenaiChat
from prompts.prompts_mapping import mapping_dict


def extract(model: Str, task: Str, text_data: Str, image: Any) -> Tuple[Dict, str]:
    """Interface for easy manual testing."""

    # check for data type & model compatibility
    if ('gpt-4' not in model and not text_data) or ('gpt-4' in model and text_data) \
            or ('gpt-4' not in model and image) or (not text_data and not image):
        return None, "Model and transmitted data are incompatible - you should change model or input data"

    error = None
    try:
        openai_chat = OpenaiChat(model)
        prompt_template = mapping_dict[task]['from_text_template'] \
            if 'gpt-4' not in model else mapping_dict[task]['from_image_template']
        temperature = mapping_dict[task]['temperature']
        count = mapping_dict[task]['count']
        prompt_template = prompt_template.format(INPUT_TEXT=text_data, MAX_VALUE=count)

        if 'gpt-4' in model:
            with io.BytesIO() as buffer:
                image.save(buffer, format="PNG")
                image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
        else:
            image_data = None

        completion = openai_chat.chat(prompt_template, temperature, image_data)
        completion = re.sub(r'}[^}]*$', r'}', re.sub(r'^[^{]*', '', completion, flags=re.DOTALL))
        result = repair_json(completion, return_objects=True)
        assert isinstance(result, dict), "Empty completion"
    except Exception as e:
        error = str(e)
        result = None
    return result, error


if __name__ == "__main__":
    gr.Interface(
        fn=extract,
        inputs=[
            gr.Radio(["gpt-3.5-turbo", 'gpt-4-turbo'], value="gpt-3.5-turbo", label="Model"),
            gr.Radio(["keywords_extraction", 'markup_extraction', 'title_extraction', 'objects_extraction',
                      'summary_extraction', 'industries_extraction', 'professions_extraction',
                      'locations_extraction'], label="Task"),
            gr.Textbox(label="Input Text"),
            gr.Image(label="Slide", type="pil", shape=(config.IMG_SIZE[0], config.IMG_SIZE[1]))
        ],
        outputs=[
            gr.JSON(label="Result"),
            gr.Textbox(label="Error")
        ],
        allow_flagging='never',
        title="Extractor"
    ).launch(server_name='127.0.0.1', server_port=7860)
