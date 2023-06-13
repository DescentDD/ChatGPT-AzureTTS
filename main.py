import openai
from TTS import TTS
openai.api_key = "你的api-key"
def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    TTS(message)

if __name__=="__main__":
    while(1):
        i=str(input('你提问:'))
        askChatGPT(i)