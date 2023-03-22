import openai

openai.api_key = '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'


while True:
    question = input("crea unas pregunta: ")
    value = input("introduce el complemento ")
    prompt=question+" "+value
    if prompt=="exit":
        break

    completion= openai.Completion.create(engine="text-davinci-003",
                            prompt=prompt,
                          
                            n=1,
                            max_tokens=2048)
    print(completion.choices[0].text)

