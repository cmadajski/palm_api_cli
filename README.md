# Google PaLM via Command Line

Interact with the Google PaLM API using a Python script.
For now, this is merely a proof-of-concept and has no practical use.

## API Details

There are 3 main API categories at the current time:

- text generation
- chat generation
- embeddings service

Text generation is used for discrete queries that only involve a single request/response pair.
Chat generation is more conversational since it can keep track of previous prompts.
Embeddings are useful for NLP tasks (semantic search, summarization, classification, clustering, etc.).

## Python Specific Nuances

In order to access the API, you need a PaLM API key. Ideally, the key is saved as an evironment variable 
then pulled into the script using the OS module:

`palm.configure(api_key=os.getenv('my_palm_api_key')`

All the currently available models can be viewed using `palm.list_models()`

For simple text generation, use `response = palm.generate_text()` with at least a model and a prompt to get a response.
The response can be accessed via the `response.result` attribute.

For continuous conversations, use `response = palm.chat(messages="initial message here")` to start a conversation and 
use `response.reply()` for all subsequent model interactions. Use `response.last` to see the most recent model response.
Conversation history can be accessed in `response.messages` where author 0 is the user and author 1 is the model.
If you change the candidate_count to a value above 1, you can view alternative responses with `response.candidates`.

## Prompt Design Principles

All prompting insights pulled from [Google's documentation](https://developers.generativeai.google/guide/prompt_best_practices).

- when establishing a pattern for the model to follow, use positive patterns (do this) rather than negative patterns (don't do this)
- when seeking completion of a partial input, make sure to include enough partial input to establish a clear pattern of behavior that 
the model can then replicate in subsequent iterations
- providing prefixes can help specify what you want from the model (answer is: , English: , French: , JSON: , etc.)

