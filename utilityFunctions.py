import re

def cleanResp(resp):
    try:
        career = re.findall("(CAREER PATH:)((.|\n)*)(STRENGTHS:)", resp)[0][1]
        strength = re.findall("(STRENGTHS:)((.|\n)*)(AREAS OF IMPROVEMENT:)", resp)[0][1]
        improvement = re.findall("(AREAS OF IMPROVEMENT:)((.|\n)*)", resp)[0][1]
        return career, strength, improvement
    except:
        return -1, -1, -1
