import google.generativeai as palm
import os
import yaml

# app config
valid_text_input = ['text', 't', 'txt']
valid_chat_input = ['chat', 'c', 'ch']
valid_chat_exit = ['exit', 'Exit', 'q', 'quit', 'Q', 'Quit']

def read_yaml(yamlFile: str) -> dict:
    with open(yamlFile, 'r') as f:
        yamlDict = yaml.safe_load(f)
    return yamlDict

if __name__ == "__main__":
    # get PaLM API key from environment variable
    palm.configure(api_key=os.getenv('palm_key'))
    # read config data from yaml
    config = read_yaml('config.yaml')
    # determine which generation method is desired
    generation_method = input("Choose a generation method (text or chat): ")
    # TEXT GENERATION
    if generation_method in valid_text_input:
        # to get text generation models
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name
        # get user prompt
        prompt = input('Enter a prompt: ')
        print('-' * 100)
        # send data to the PaLM API if all required data is present
        if prompt:
            # send query data to PaLM API
            completion = palm.generate_text(model=model, prompt=prompt, temperature=config['temp'], max_output_tokens=config['max_output_tokens'])
            # print API response
            print(completion.result)
        # print an error message if prompt is empty
        else:
            print("No prompt provided. A prompt is required to use the PaLM API.")
    # CHAT GENERATION
    elif generation_method in valid_chat_input:
        continue_chat = True
        # start chat conversation
        chat_start_message = input('Start conversation: ')
        print('-' * 100)
        if chat_start_message in valid_chat_exit:
            continue_chat = False
        elif not chat_start_message: 
            print('Prompt is empty. Use "quit" or "exit" to end chat.')
        else:
            response = palm.chat(messages=chat_start_message)
            print(f'PaLM: {response.last}')
            print('-' * 100)
            while continue_chat:
                chat_reply_message = input('Next query: ')
                print('-' * 100)
                if chat_reply_message in valid_chat_exit:
                    continue_chat = False
                elif not chat_reply_message:
                    print('Prompt is empty. Use "quit" or "exit" to end chat.')
                else:
                    response = response.reply(chat_reply_message)
                    print(f'PaLM: {response.last}')
                    print('-' * 100)
    # GENERATION NOT SUPPORTED
    else:
        print(f'Generation method "{generation_method}" is not supported.')

