prompt_template = """
### This task is very important for my career and I'll pay you $20 for the perfect solution! ###
You are a presentation creator with an excellent understanding of presentation logic.
### Instructions ###
* You should give me the most appropriate title for input text.
* Use this json-format to answer:
{{
"result": <title>
}}
* STRONGLY IMPORTANT: never translate text - keep the original language (otherwise you will be penalized)!
-------------
### Input text ###
"{INPUT_TEXT}"
### Before you form json, read all the information above carefully twice, keep it in mind,
then take a deep breath, process in your mind all the possible variations for jsons,
choose the best output json that meets ALL the instructions and return this json below ###
"""
