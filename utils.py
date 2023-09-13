import openai
from streamlit import secrets

openai.api_key = secrets["CT-OPENAI_API_KEY"]
def GPT4_Interpretation(test_name, test_specific_content):
    response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You will be provided with the CSV format results of {test_name} of a clinical trial and your task is to explain them in a concise way."},
                    {"role": "user", "content": f"Here are the results of the {test_name}: {test_specific_content}"}
                ],
                temperature=0.7,
                max_tokens=1024
            )
    return response