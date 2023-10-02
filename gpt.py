import json
import openai

# with open('constants.json') as file:
#     data = json.load(file)
#     OPENAI_KEY = data["OPENAI_KEY"]
    

def createPrompt(abt, exp, edu, certi, text, career):
    prompt = f"""I will provide two documents. First is my LinkedIn profile and second is webpage data. You have to understand my profile and webpage data and tell me a executable step by step process to become {career} from WHAT I ALREADY KNOW. Give the steps under the heading CAREER PATH. You have to be polite and advising while replying.
    Here is my LinkedIn profile 
    "About
    {abt if abt!=-1 else "Nothing mentioned on LinkedIn"}

    Internships and Projects
    {exp if exp!=-1 else "Nothing mentioned on LinkedIn"}

    Educational Background
    {edu if edu!=-1 else "Nothing mentioned on LinkedIn"}

    Courses and Certification
    {certi if certi!=-1 else "Nothing mentioned on LinkedIn"}"

    And here is the webpage data
    "{text}"
    Give the career path output in maximum of 30 words limit.
    Once done tell my only the strenghts related to {career} in maximum of 50 words limit. Give the output in way that someone is advising me. Give the advise under STRENGHTS headline and remove  any unnecessary comment. 
    Once done create another headline AREAS OF IMPROVEMENT. This section will have maximum 30 words limit, apart from previous section. In this section tell me about the things which I can improve in my linkedin profile to make it stronger. Also add complementary 3-4 lines telling why strong profile is important. Give the output in such way that someone is giving me advice in a polite way. 
    Consider each headline in the output as a different module having independent word limits that I mentioned above. Also keep bullet numbering (1, 2, 3,...) order for each point in the modules."""
    
    return prompt

def getResponse(abt, exp, edu, certi, text, career):
    openai.api_key = OPENAI_KEY
    prompt = createPrompt(abt, exp, edu, certi, text, career)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    response = completion.choices[0].message.content
    return response