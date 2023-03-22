import openai
openai.api_key = "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"  # supply your API key however you choose
f = open("prueba2.m4a", "rb")

transcript= openai.Audio.transcribe("whisper-1", f)
print(transcript.text)

while True:
    prompt=transcript.text
   

    completion= openai.Completion.create(engine="text-davinci-003",
                            prompt=prompt,
                            n=1,
                            max_tokens=2048)
    print(completion.choices[0].text)
    prompt=input("Pulsa exit para salir")
    if prompt=="exit":
        break
