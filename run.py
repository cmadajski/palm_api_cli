import google.generativeai as palm
import os
import yaml

def read_yaml(yamlFile: str) -> dict:
    with open(yamlFile, 'r') as f:
        yamlDict = yaml.safe_load(f)
    return yamlDict

if __name__ == "__main__":
    # get PaLM API key from environment variable
    palm.configure(api_key=os.getenv('palm_key'))
    # read config data from yaml
    config = read_yaml('config.yaml')
    # to get text generation models
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    # get user prompt
    prompt = input('Enter a prompt: ')
    # send data to the PaLM API if all required data is present
    if prompt:
        # send query data to PaLM API
        completion = palm.generate_text(model=model, prompt=prompt, temperature=config['temp'], max_output_tokens=config['max_output_tokens'])
        # print API response
        print(completion.result)
    # print an error message if prompt is empty
    else:
        print("No prompt provided. A prompt is required to use the PaLM API.")
