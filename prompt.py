wordToExcelPrompt = """ As an AI model expert, your task is to format the given data into a structured table.
Table will have the below columns.
Questions A  B  C  D  Correct Answers
Data should be aligned appropriately in the above columns.
The final response should be a list  with all the informations neeede to create pandas dataframe with the mentioned columns and its corresponding data.
DO NOT ADD ANYTHING ADDITIONAL APART FROM THE DATA INT HE FINAL RESPONSE.
Here is the {data}
"""
# The final response should be a dataframe with the mentioned columns and its corresponding data.

languageTranslation = """As an AI language expert you are tasked to translate the given table into the mentioned language.
The final response should be a LIST with all the informations required to create pandas dataframe directly with the mentioned columns and its corresponding data.
The language to be translated into is {language}.

Column Name in the dataframe should always be followed as given below without fail:
Questions A  B  C  D  Correct Answers
Questions columns should have the questions.
and the columns A, B, C, D should have the corresponding options and
Correct Answer column should have the correct answer corresponding to the question

Here is the {dataTable} to be translated.
"""

