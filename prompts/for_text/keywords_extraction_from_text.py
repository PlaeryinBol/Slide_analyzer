prompt_template = """
### This task is very important for my career and I'll pay you $20 for the perfect solution! ###
You are a presentation creator with an excellent understanding of presentation logic.
### Instructions ###
* You should give me the top-{MAX_VALUE} keywords from the slide text.
* But these keywords should not be just words found in the text - they must be thoughts, feelings,
or associations that came to your mind while you reading the text
* Keyword length should not be more than 4 words!
* STRONGLY IMPORTANT: all keywords must be in English, even if the slide text is in another language
- otherwise you will be penalized!
* Use this json-format to answer:
{{
"result": [<keyword 1>, <keyword 2>, ..., <keyword {MAX_VALUE}>]
}}
### Examples ###
### Example 1 ###
Slide text: "Yellow alarm clock"
Output json: {{
"result": ['alarm', 'time to get up', 'morning', 'wake up', 'time management', 'productivity',
'daily schedule', 'time is money', 'ringing sound', 'time for action']
}}
### Example 2 ###
Slide text: "Money"
Output json: {{
"result": ['financial independence', 'investment', 'bribe', 'bank account', 'bribery', 'greed',
'economy', 'salary', 'money management']
}}
-------------
### Slide text ###
"{INPUT_TEXT}"
### Before you form json, read all the information above carefully twice, keep it in mind,
then take a deep breath, process in your mind all the possible variations for jsons,
choose the best output json that meets ALL the instructions and return this json below ###
"""
