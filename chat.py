import logging
import time
from typing import Any, Str

import httpx
from openai import OpenAI, OpenAIError

import config


class OpenaiChat():
    def __init__(self, model) -> None:
        self.client = OpenAI(api_key=config.OPENAI_API_KEY, http_client=httpx.Client(proxies=config.PROXY))
        self.model = model

    def chat(self, prompt: Str, temperature: float, bytes_image: Any = None) -> Str:
        """Openai chat request."""
        content = [{"type": "text", "text": prompt}]

        if bytes_image:
            image_data = {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{bytes_image}",
                    "detail": config.IMG_DETAIL
                    }
                }
            content.append(image_data)

        try:
            completion = self.client.chat.completions.create(model=self.model,
                                                             temperature=temperature,
                                                             response_format={"type": "json_object"},
                                                             messages=[{"role": "assistant", "content": content}])
            return completion.choices[0].message.content

        except OpenAIError as e:
            retry_time = e.retry_after if hasattr(e, 'retry_after') else 30
            logging.warning(f"Error occurred: {e}. Retrying in {retry_time} seconds...")
            time.sleep(retry_time)
            return self.chat(prompt, temperature, bytes_image)
