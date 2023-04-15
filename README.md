# Porfiry
A script that uses LangChain to allow you to ask ChatGPT questions about a large text file (like Dostoevsky's "Crime and Punishment") 
and get textually-supported responses. 

Adapted from tutorial on LangChain at (https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)

A nifty feature: The script actually shows you where in the text it got the answer from. How cool!
## To Run
`python3 porfiry.py`

## To change text file
Edit line 9 of `porfiry.py` to the path name of your text file

## Warning
- Must have OpenAI key as environment variable. How? Check out: (https://www.immersivelimit.com/tutorials/adding-your-openai-api-key-to-system-environment-variables)
- Must install dependencies with pip
- If you give ChatGPT a long Russian novel with many words, like C&P, as the text file, it may be more "expensive" than the average ChatGPT interaction (I spent ~$2.50 making this and messing around with it).
