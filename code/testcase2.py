import openai
import os
from dotenv import load_dotenv
load_dotenv()  # This will load all environment variables from a .env file

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')  # Ensure you have set your API key in your environment variables

def query_openai_chat_api(prompt):
    """Sends a prompt to the OpenAI API using the `v1/chat/completions` endpoint and returns the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust to the correct chat model you have access to
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150  # Set the maximum number of tokens to generate
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    test_case_prompt = """
    Convert the following test case into a Gherkin Cucumber scenario:

    GIVEN I have a gas contract
    AND it has two valid meter reads with thermal properties
    AND EE gpke.degreeDaysPlus.value = 0
    AND I let the system estimate a third meter read
    AND the outcome can be validated positively with the Excel attached
    WHEN I set EE gpke.degreeDaysPlus.value = X (other than 0)
    AND I let the system estimate the third meter read again
    THEN the results differ by the value X

    Please write the scenario in a way that includes background, scenario outline, and examples where appropriate.
    """
    
    response = query_openai_chat_api(test_case_prompt)
    
    if response:
        messages = response.get('messages', [])
        if messages:
            # Assuming the last message is the completion
            scenario_text = messages[-1].get('content', '')
            print("Generated Cucumber Scenario:")
            print(scenario_text)
        else:
            print("No messages returned in the response.")
    else:
        print("No response was returned from the API.")

if __name__ == '__main__':
    main()
