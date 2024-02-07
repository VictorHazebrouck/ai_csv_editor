from ollama import Client
from flask import current_app

client = Client(host="http://ollama:11434")

def ask_ai(context, prompt, information):

    concat_prompt = f"CONTEXT: You will be provided with row values from a csv file. Each column is separated by a '|' and is available after 'DATA: '. ALWAYS provide ONLY the result of the prompt, no instructions or explanations, just a value(i.e: 'translate to french' -> ALWAYS provide ONLY the translated value || 'concat values' -> ALWAY provide ONLY the result value of the concatenation || DO NOT EVER provide further instructions, context, or say you do not know ). {context}; PROMPT: {prompt}; DATA: {information}"

    try:
        response = client.generate(
            model="mistral:instruct",
            prompt=concat_prompt,
            stream=False
        )

        current_app.logger.info(response)
        return response['response']

    except Exception as e:
        current_app.logger.error(f"An error occurred: {str(e)}")
        current_app.logger.info('Pulling mistral:instruct')
        client.pull('mistral:instruct')
        raise e