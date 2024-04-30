prompt_template = """
### This task is very important for my career and I'll pay you $20 for the perfect solution! ###
You are a presentation creator with an excellent understanding of presentation logic.
### Instructions ###
* You should give me the top-{MAX_VALUE} most appropriate 3D objects on a transparent background,
which I can insert into this slide.
* Sort them so that the most suitable objects come first.
* You should answer only in English using the following json-format:
{{
"result": [<object 1>, <object 2>, ..., <object {MAX_VALUE}>]
}}
### Examples ###
#### Example 1 ####
Slide text: "Locate Data Sources and Plan Data Transformations"
Output json:
{{
"result": ["Globe", "Flowchart", "Magnifying Glass", "File Folders", "Server Racks",
"Transformation Arrows", "Data Points", "Planning Calendar"]
}}
### Examples ###
#### Example 2 ####
Slide text: "Social and Environmental Responsibility"
Output json:
{{
"result": ["Solar Panel", "Wind Turbine", "Recycled Plastic Bottle", "Compost Bin",
"Rooftop Garden", "Electric Car", "Bicycle", "Rainwater Harvesting System", "LED Light Bulb"]
}}
-------------
### Slide text ###
"{INPUT_TEXT}"
### Before you form json, read all the information above carefully twice, keep it in mind,
then take a deep breath, process in your mind all the possible variations for jsons,
choose the best output json that meets ALL the instructions and return this json below ###
"""
