import json
import openai
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Load your OpenAI API key from .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

def read_prompt_from_json(file_path):
    """Reads a JSON file containing the prompt for OpenAI API."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_output_to_txt(file_path, text):
    """Writes the API response to a text file."""
    with open(file_path, 'w') as file:
        file.write(text)

def query_openai_api(prompt):
    """Sends a prompt to the OpenAI API and returns the response."""
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-0125",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response

def main():
    # Define the paths relative to the 'code' directory
    input_file = '../data.txt'  # Using .txt file for input
    output_file = '../output.txt'
    
    # Load test case data from text file
    test_case_data = read_prompt_from_txt(input_file)
    
    # Format the prompt with the test case data
    prompt_template = ("Convert the following test case into a Gherkin Cucumber scenario: "
                       "{test_case_data} "
                       "Please write the scenario in a way that includes background, "
                       "scenario outline, and examples where appropriate.")
    formatted_prompt = prompt_template.format(data=test_case_data)
    
    # Query OpenAI API with the formatted prompt
    response = query_openai_api(formatted_prompt)
    
    # Extract only the text response to save to text file
    scenario_text = response['choices'][0]['text']
    
    # Write the response to a text file
    write_output_to_txt(output_file, scenario_text)
    
    print(f"Response written to {output_file}")

if __name__ == '__main__':
    main()
