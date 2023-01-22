
import os
import random
import openai
from dotenv import load_dotenv

# load_dotenv()
API_KEY_LIST = os.getenv('API_KEY_LIST').split(',')

# API_KEY = "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"  # "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"

# defaultPrompt_single = """ Give me the serious  angry reactions of Shark Tank US Judges,  kevin o'leary and Mark Cuban , Lori Greiner after pitching the idea considering  the pitch , probelm it solves and also see if there are any users already , also equity and the amount asked and they give their serious and angry reactions
# Pitch : {}
# """

basePrompt = """
You are Kevin O'Leary, an investor judging the TV show Shark Tank. Investors come up on the stage and pitch their business ideas to you and you must give an opinion on it along with an optional offer, discretionary to you. This is done alongside other investors, sometimes sparking a bidding war for companies which you think have great potential. Act as Kevin only and all your further answers will be as him. Do not break character. You may act in sarcasm, honesty, straightforwadedness or any other strong emotion you think appropriate to the pitch. Give details about why you think the idea might be good or bad and who it might resonate with and who might be the target audience. You also understand when the pitch is made in joke and unserious. Respond to these types of pitches angrily. Finally decide on a valuation for the business based on the current revenue and growth and present your offer in format $X for Y percent equity. Read the pitch below and respond:
Pitch: {} 
Kevin:
"""


class GPT:

    def __init__(self):

        self.api_keys = API_KEY_LIST
        self.choice = [0]

    def query(self, prompt, myKwargs={}):
        """
        Wrapper for the API to save the prompt and the result
        """
        print(self.api_keys)
        api_key = self.api_keys[random.choice(self.choice)]
        openai.api_key = api_key
        kwargs = {
            "engine": "text-davinci-003",
            "best_of": 1,
            "temperature": 0.7,
            "max_tokens": 512,
            "top_p": 1,
            "frequency_penalty": 0.5,
            "presence_penalty": 0,
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        result = openai.Completion.create(
            prompt=prompt, **kwargs)["choices"][0]["text"].strip()
        if result:
            return result
        return "Sorry Please Add Some More Information To Generate Conversation"

    def askGPT(self, pitch):

        prompt = basePrompt.format(pitch)
        res = self.query(prompt)
        data = {
            "result": {
                "Kevin O'Leary": res,
            }
        }
        return data
