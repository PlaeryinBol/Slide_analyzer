from . import for_text, for_image

mapping_dict = {
    'keywords_extraction': {
        'from_text_template': for_text.keywords_extraction_from_text.prompt_template,
        'from_image_template': for_image.keywords_extraction_from_image.prompt_template,
        'temperature': 0.5,
        'count': 10
    },
    'markup_extraction': {
        'from_text_template': for_text.markup_extraction_from_text.prompt_template,
        'from_image_template': for_image.markup_extraction_from_image.prompt_template,
        'temperature': 0.2,
        'count': 1
    },
    'title_extraction': {
        'from_text_template': for_text.title_extraction_from_text.prompt_template,
        'from_image_template': for_image.title_extraction_from_image.prompt_template,
        'temperature': 0.2,
        'count': 1
    },
    'objects_extraction': {
        'from_text_template': for_text.objects_extraction_from_text.prompt_template,
        'from_image_template': for_image.objects_extraction_from_image.prompt_template,
        'temperature': 0.5,
        'count': 10
    },
    'summary_extraction': {
        'from_text_template': for_text.summary_extraction_from_text.prompt_template,
        'from_image_template': for_image.summary_extraction_from_image.prompt_template,
        'temperature': 0.2,
        'count': 1
    },
    'industries_extraction': {
        'from_text_template': for_text.industries_extraction_from_text.prompt_template,
        'from_image_template': for_image.industries_extraction_from_image.prompt_template,
        'temperature': 0.5,
        'count': 4
    },
    'professions_extraction': {
        'from_text_template': for_text.professions_extraction_from_text.prompt_template,
        'from_image_template': for_image.professions_extraction_from_image.prompt_template,
        'temperature': 0.5,
        'count': 4
    },
    'locations_extraction': {
        'from_text_template': for_text.locations_extraction_from_text.prompt_template,
        'from_image_template': for_image.locations_extraction_from_image.prompt_template,
        'temperature': 0.5,
        'count': 4
    }
}
