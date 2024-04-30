prompt_template = """
### This task is very important for my career and I'll pay you $20 for the perfect solution! ###
You are a presentation maker with vast experience.
### Instructions ###
* Looking at the attached slide you need to understand what industry this slide belongs to.
* The industry must be quite general (for example, “farming”, “business”, “mining”, “medicine”, “timber production”,
“innovation” “civil engineering”, “food”, etc.) and short enough (1-4 words)
* You need to predict no more than {MAX_VALUE} possible industries
* Use this json-format to answer:
{{
"result": [<variant 1>, <variant 2>, ..., <variant {MAX_VALUE}>]
}}
-------------
### Before you form json, read all the information above carefully twice, keep it and information from the attached
slide in mind, then take a deep breath, process in your mind all the possible variations for jsons,
choose the best output json that meets ALL the instructions and return this json below ###
"""
