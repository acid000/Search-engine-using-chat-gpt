from django.shortcuts import render
import os 
import openai
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("OPENAI_KEY",None)

def chatbot(request):
    chatbot_response=None
    if api_key is not None and request.method=='POST':
        openai.api_key=api_key
        question=request.POST.get('question')
        response=openai.Completion.create(
            engine='text-davinci-003',
            prompt=question,
            max_tokens=256,
            temperature=0.5
        )
        #print(response)
        chatbot_response=response["choices"][0]["text"]

    return render(request,"main.html",{'chatbot_response':chatbot_response})    

