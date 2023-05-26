import google.generativeai as palm
import os

def setup():
    # get PaLM API key from environment variable
    palm.configure(api_key=os.getenv('palm_key')
    # get text generation models
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    # set reasonable defaults for temp and max_output_tokens
    temp = 0
    max_token = 800

if __name__ == "__main__":
    setup()
    prompt = input('Enter a prompt: ')
    completion = palm.generate_text(model=model, prompt=prompt, temperature=temp, max_output_tokens=max_token)
    print(completion.result)
