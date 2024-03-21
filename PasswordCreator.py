# https://docs.python.org/3/library/secrets.html

import string
import secrets
import random

def randomPass():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    return(password)

def informedPass():
    word = str(input("Please input a word:"))
    password = ''
    translationdict = {'e':'3','E':'3','Z':'2','l':'1','L':'1','o':'0','O':'0','S':'5','s':'5','a':'@'}
    pwordalphabet = (string.punctuation)
    pwordalphabet = pwordalphabet.replace('&','0')
    for i in range(len(word)):
        if (word[i] in translationdict):
            word = word.replace(word[i],translationdict[word[i]],i-1)
    print(word)
   
    frontComponent = ''.join(secrets.choice(pwordalphabet) for i in range(2))
    backComponent = ''.join(secrets.choice(pwordalphabet) for i in range(2))
    password = ''.join((frontComponent,word,backComponent))

    return(password)
print(informedPass())