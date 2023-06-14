import openai
from TTS import TTS
openai.api_key = "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"
dialogue_history="history dialogue is here:\'\'\'"
def askChatGPT(question):
    global dialogue_history
    prompt = dialogue_history+'\'\'\'\n'+question
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    dialogue_history=dialogue_history+"\n-"+question+"\n-"+message
    TTS(message)

if __name__=="__main__":

    while(1):
        i=str(input('你提问:'))
        askChatGPT(i)
        i=''
    '''
    while(1):
        i=str(input('llll'))
        TTS(i)
    '''