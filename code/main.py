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
        engine="text-davinci-003", # or "text-davinci-004" for GPT-4, for example
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
    input_file = '../data.json'
    output_file = '../output.txt'  # Changed to .txt
    
    # Load prompt from JSON file
    prompt_data = read_prompt_from_json(input_file)
    prompt = prompt_data.get('prompt', '')
    
    # Query OpenAI API with the prompt
    response = query_openai_api(prompt)
    
    # Extract only the text response to save to text file
    scenario_text = response['choices'][0]['text']
    
    # Write the response to a text file
    write_output_to_txt(output_file, scenario_text)
    
    print(f"Response written to {output_file}")

if __name__ == '__main__':
    main()
