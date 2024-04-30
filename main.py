import os
from glob import glob

import pandas as pd

import config
from analyzer import SlideAnalyzer
from prompts.prompts_mapping import mapping_dict


def run() -> None:
    """Run data extration."""
    # depending on the type of input data, create a dataframe with texts/paths to images
    if not config.CHAT_WITH_IMAGE:
        df = pd.read_table(config.DF_PATH)
        texts = df['text'].tolist()
        anlzr = SlideAnalyzer(texts)
    else:
        images = glob(config.IMAGE_DIR + '/*')
        # if necessary, create df with paths to images in folder with this images
        if not os.path.exists(os.path.join(config.IMAGE_DIR, 'paths_df.tsv')):
            df = pd.DataFrame({'path': images})
            df.to_csv(os.path.join(config.IMAGE_DIR, 'paths_df.tsv'), sep='\t', index=False)
        else:
            df = pd.read_table(os.path.join(config.IMAGE_DIR, 'paths_df.tsv'))
            images = df['path'].tolist()
        anlzr = SlideAnalyzer(images)

    prompt_template = mapping_dict[config.MODE]['from_text_template'] \
        if not config.CHAT_WITH_IMAGE else mapping_dict[config.MODE]['from_image_template']
    temperature = mapping_dict[config.MODE]['temperature']
    result_count = mapping_dict[config.MODE]['count']

    extracted_data = anlzr.extraction(prompt_template, temperature, result_count)
    result_df = pd.concat([df, extracted_data], axis=1)
    result_df.to_csv(config.OUT_DF, sep='\t', index=False)


if __name__ == "__main__":
    run()
