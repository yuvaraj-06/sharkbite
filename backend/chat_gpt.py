
import os
import random
import openai
from dotenv import load_dotenv

#load_dotenv() 
API_KEY_LIST = ["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"]
print(API_KEY_LIST)
# API_KEY = "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"  # "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"
 
defaultPrompt_single = """Act as an Shark Tank USA Judge ,shark Kevin O'Leary,Mark Cuban,Lori Greiner will give his point of view in a sarcastic terms  and  whether they will offer and if yes how much would they be willing to offer for the idea human pitches for
Human : {}
"""

class GPT:

    def __init__(self) :

        self.api_keys=API_KEY_LIST
        self.choice = [0]
        

    def query(self,prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """
        print(self.api_keys)
        api_key=self.api_keys[random.choice(self.choice)]
        openai.api_key = api_key
        kwargs = {
            "engine": "text-davinci-003",
            "best_of": 1,
            "temperature": 0.71,
            "max_tokens": 500,
            "top_p": 1,
            "frequency_penalty": 0.36,
            "presence_penalty": 0.75,
            "stop": ["Input:"],
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        result = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0]["text"].strip()
        if result:
            return result
        return "Sorry Please Add Some More Information To Generate Conversation"


    def main_gpt(self,name):
        
        prompt = defaultPrompt_single.format(name )
        res=self.query(prompt)
        data={} 
        try:
            for i in (res.split("\n\n")):
                x=i.index(":")
                data[i[:x]]=i[x+1:].replace("\"","")
        except:
            print(res)
            print("--------------error-------------------------")

        return data
