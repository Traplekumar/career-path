import json
import requests
from bs4 import BeautifulSoup
from metaphor_python import Metaphor


with open('constants.json') as file:
    data = json.load(file)
    METAPHOR_KEY = data["METAPHOR_KEY"]
    WEBPAGE_TOKEN_LIMIT = data["WEBPAGE_TOKEN_LIMIT"]
    WEBPAGE_INIT_LINE_SKIP = data["WEBPAGE_INIT_LINE_SKIP"]


def getPrompt(career):
    metaphorPrompt = f"Here is a blog post about guide to become {career}:"
    return metaphorPrompt


def search(prompt):
    metaphor = Metaphor(METAPHOR_KEY)
    search_response = metaphor.search(prompt, use_autoprompt=True)

    searchUrl = ""
    for r in search_response.results:
        if "medium" not in str(r.url):
            searchUrl = r.url
            try:
                print(searchUrl)
                data = requests.get(searchUrl)
                return data
            except:
                pass
    return -1


def getWebdata(data):
    soup = BeautifulSoup(data.content, features="html.parser")
    lines = soup.find('body').stripped_strings
    wordCounter = 600
    lineCounter = -20
    text = ""
    for line in lines:
        lineCounter += 1
        if lineCounter>0 and wordCounter>0:
            text += line
            text += "\n"
            lineLenght = len(line.split(' '))
            wordCounter -= lineLenght

    return text