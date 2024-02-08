# Cucumber Test Cases Generation with OpenAI

This guide will help you set up a Python environment on a Windows system and run the `demo.py` script to generate Cucumber test cases using OpenAI's API.

## Prerequisites

Before you begin, ensure you have Python installed on your Windows machine. This guide will use `pyenv-win` to manage Python versions and `virtualenv` to create a virtual environment for the project.

## Setup

Follow these steps to set up your environment and install the necessary packages:

1. **Install `pyenv-win`:**

    `pyenv-win` is a Windows port of `pyenv` for Python version management. Install it with the following command:

    ```bash
    pip install pyenv-win
    ```

2. **Install `virtualenv`:**

    `virtualenv` is a tool to create isolated Python environments. Install it with the following command:

    ```bash
    pip install virtualenv
    ```

3. **Create a Virtual Environment:**

    Navigate to your project directory and create a new virtual environment called `venv`:

    ```bash
    virtualenv venv
    ```

4. **Activate the Virtual Environment:**

    Activate the virtual environment to use it:

    ```bash
    .\venv\Scripts\activate
    ```

5. **Install Packages:**

    Install `typer`, `openai`, `python-dotenv`, and the specific version of `openai` required for the script:

    ```bash
    pip install typer openai python-dotenv
    pip install openai==0.28
    ```

## Running the Script

With the environment set up and the packages installed, you can now run the `demo.py` script.

1. **Environment Variables:**

    Before running the script, make sure you have set your OpenAI API key in an `.env` file or as an environment variable:

    ```plaintext
    OPENAI_API_KEY='your-api-key-here'
    ```

2. **Run the Script:**

    Execute `demo.py` using Python:

    ```bash
    python demo.py llms
    ```

3. **Check Output:**

    After running the script, check the output for the generated Cucumber test cases. The output will be displayed in the terminal or saved to a specified file, depending on the script's implementation.


Certainly! Below is a breakdown of the code for someone new to the OpenAI API, followed by a sample README in markdown format.

### Explaining the Code

For someone new to the OpenAI API, the following is an explanation of what the provided Python script does:

1. **Environment Setup:**
   The script starts by loading environment variables from a `.env` file using the `load_dotenv()` function. This is where the OpenAI API key is securely stored and accessed.

```python
from dotenv import load_dotenv

load_dotenv()  # This will load all environment variables from a .env file
```

2. **API Key Configuration:**
   The script then sets the `openai.api_key` variable to the value obtained from the environment variables. This key authenticates requests to the OpenAI API.

```python
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
```

3. **Reading the Input Data:**
   The `read_prompt_from_file` function reads the contents of `data.txt`, which contains the test case that needs to be converted into a Gherkin scenario.

```python
def read_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
```

4. **Making the API Call:**
   The `query_openai_chat_api` function sends the test case to the OpenAI API using the `v1/chat/completions` endpoint. It specifies the model to use and sets a limit of 150 tokens for the response length.

```python
def query_openai_chat_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
```

5. **Processing the API Response:**
   The main function orchestrates the script by calling the functions to read the test case, send it to the API, and then process the response. If the API call is successful, the response is written to `output.txt`.

```python
def main():
    prompt_file_path = 'data.txt'
    output_file_path = 'output.txt'
    
    test_case_prompt = read_prompt_from_file(prompt_file_path)
    response = query_openai_chat_api(test_case_prompt)
    
    if response:
        scenario_text = response['choices'][0]['message']['content']
        write_scenario_to_file(output_file_path, scenario_text)
        print(f"Generated Cucumber Scenario written to {output_file_path}")
    else:
        print("No response was returned from the API.")
```

6. **Writing Output:**
   The `write_scenario_to_file` function takes the generated scenario content and writes it to `output.txt`.

```python
def write_scenario_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
```

7. **Running the Script:**
   Finally, the `if __name__ == '__main__':` part checks if the script is being run directly (not imported) and, if so, calls the `main()` function to execute the code.

```python
if __name__ == '__main__':
    main()
```

### README.md in Markdown Format

```markdown
# Automated Gherkin Scenario Generation

Automate the conversion of test cases into Gherkin scenarios for BDD with the power of OpenAI's language models.

## Setup

1. Clone this repository.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install openai python-dotenv
   ```
4. Create a `.env` file in the project root with your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Place your test case in `data.txt`.
2. Run `main.py` to generate the Gherkin scenario:
   ```bash
   python code/main.py
   ```
3. Find the generated scenario in `output.txt`.

## Understanding the Code

The script `main.py` performs the following actions:

- Reads a test case from `data.txt`.
- Sends the test case to the OpenAI API.
- Writes the resulting Gherkin scenario to `output.txt`.

Refer to the comments in the code for a detailed walkthrough.

## Contributing

Contributions to enhance this automation script are welcome! Please fork the repository and submit a pull request with your improvements.

## License

Distributed under the MIT License. See `LICENSE` for more information.

