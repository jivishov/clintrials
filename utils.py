import openai
from streamlit import secrets, markdown

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

def add_copyright():
    markdown(
        """
        <style>
            [data-testid="stSidebar"]::before {
                content: "© Emil Jivishov https://www.linkedin.com/in/jivishov";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 14px;
                position: relative;
                top: 50px;
                cursor: pointer;
            }
        </style>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                let sidebar = document.querySelector('[data-testid="stSidebar"]');
                if (sidebar) {
                    sidebar.addEventListener('click', function(event) {
                        if (event.target.textContent === "© Emil Jivishov") {
                            window.open("https://www.linkedin.com/in/jivishov/", "_blank");
                        }
                    });
                }
            });
        </script>
       """,
        unsafe_allow_html=True,
    )
    #markdown('<a href="https://www.linkedin.com/in/jivishov/" target="_blank">© Emil Jivishov</a>', unsafe_allow_html=True)
