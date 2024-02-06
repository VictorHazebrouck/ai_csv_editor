import ollama

def ask_ai(context, prompt, information):

    concat_prompt = f"CONTEXT: You will be provided with row values from a csv file. Each column is separated by a '|' and is available after 'DATA: '. ALWAYS provide ONLY the result of the prompt, no instructions or explanations, just a value(i.e: 'translate to french' -> ALWAYS provide ONLY the translated value || 'concat values' -> ALWAY provide ONLY the result value of the concatenation || DO NOT EVER provide further instructions, context, or say you do not know ). {context}; PROMPT: {prompt}; DATA: {information}"


    return "success"
    # try:
    #     return ollama.generate(
    #         model='mistral:instruct',
    #         prompt=concat_prompt
    #     )['response']
    
    # except ollama.ResponseError as e:
    #     print('Error:', e.error)
    #     if e.status_code == 404:
    #         return ollama.pull('mistral:instruct')
    #     else:
    #         return e.error