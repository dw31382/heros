#!/usr/bin/env python3

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# import datetime
# now = str(datetime.datetime.now())
# user = os.getenv("USER")

memory = []

def remember(x):
    memory.append(x)

def gpt3(user_input):

    characters = [len(m) for m in memory]
    tokens = (sum(characters) / 4)

    if tokens > 500:
        while tokens > 500:
            temp = sorted(memory, key=len, reverse=True)
            for i in range(0, 3):
                if memory[memory.index(temp[i])] == memory[-1]:
                    pass
                else:
                    del memory[memory.index(temp[i])]
            characters = [len(m) for m in memory]
            tokens = (sum(characters) / 4)

    prompt = ""
    for x in memory:
        prompt += x
    
    prompt += user_input

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt = prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    output = response.choices[0]["text"]
    # z = ' '.join(y.split()).replace('\n','')
    remember(prompt)
    remember(output)

    return(output)

while True:
    # get user input
    user_input = input("# ")
    print(gpt3(user_input))
    # print(memory)
