prompt_template = """
### This task is very important for my career and I'll pay you $20 for the perfect solution! ###
You are a presentation maker with vast experience.
### Instructions ###
* You need to predict from the information of the attached slide which location its creator might be from.
* Predicted locations should be as specific as possible - predict a specific country if it is impossible,
if not - predict the location (some examples: “USA”, “Latin America”, “South African Republic”, “Far East”,
“Australia”, “Africa”, “Near East”, “Asia”, etc.)
* You need to predict no more than {MAX_VALUE} possible locations.
* Use this json-format to answer:
{{
"result": [<variant 1>, <variant 2>, ..., <variant {MAX_VALUE}>]
}}
-------------
### Before you form json, read all the information above carefully twice, keep it and information from the attached
slide in mind, then take a deep breath, process in your mind all the possible variations for jsons,
choose the best output json that meets ALL the instructions and return this json below ###
"""
