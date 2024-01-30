import openai
import openai
import sys

API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

def extract_last_ps_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find the last occurrence of "PS>"
    last_ps_prompt_index = content.rfind("PS>")
    
    # Extract text from the last PS prompt to the end
    if last_ps_prompt_index != -1:
        extracted_text = content[last_ps_prompt_index:]
        return extracted_text
    else:
        return "No 'PS>' prompt found in the file."

if __name__ == "__main__":
    chat_log = []
    file_path = "./error.txt"
    #Variable that holds error
    result = extract_last_ps_prompt(file_path)
    
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{
        "role": "user", 
        "content": result,
    }]
)

chat_log.append({"role": "user", "content": result})

initial = response.choices[0].message.content

chat_log.append({"role": "assistant", "content": initial})

def print_green(text):
    print("\033[92m {}\033[00m" .format(text))

print_green(initial.strip("\n").strip())

while True:
    user_message = input()
    if user_message.lower() == "q":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat_log
        )
        assistant_response = response.choices[0].message.content
        print_green("BugOracle: " + assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
