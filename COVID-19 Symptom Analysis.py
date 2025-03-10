#pip install openai==0.28
import openai
import pandas as pd
import matplotlib.pyplot as plt


omicrondata = pd.read_csv('Omicron_ChatGPT_Med_Sym_NorMed.csv')
def askgpt(context_str):
    QUESTION = "These values are symptoms that Covid-19 patients felt. Reformat them into a list format of ['answer1','answer2','answer3'] with no bullets or slashes. If there is a spelling error you may fix it. If no symptoms were given, output the word 'None' and nothing else. Do this with no introductory or concluding remarks."
    context_str = f"""{context_str}"""
    openai.api_key = #Insert API key here
    response = openai.ChatCompletion.create(
    model="gpt-4o", # do not pass in model by args
    messages=[
                {"role": "system", "content": context_str},
                {"role": "user", "content": QUESTION},
        ]
    )


    return response['choices'][0]['message']['content']
omicrondata["formatsymptom"] = omicrondata["symptom"][:100].apply(askgpt)
for i in range(len(omicrondata["formatsymptom"][:100])):
    answer = str(omicrondata["formatsymptom"][i])
    answer = answer.lower()
    a = answer[0]
    if a != 'n' and a != '[':
        answer = answer.replace(a,'')
        answer = answer.replace('.','')
        answer = answer.replace(' ','')
    omicrondata.loc[i,"formatsymptom"] = answer
omicrondata["formatsymptom"][:100]
# #omicrondata["answer"] = omicrondata["body"].apply(askgpt)
# #askgpt("List the symptoms that COVID-19 patients felt since his diagnosis of COVID-19 based on the context in a list format as ['answer','answer2']. Please list without any introductory or concluding remarks, if no symptoms were mentioned,return 'None'", "I got COVID and I had a fever and a bad cough")


from wordcloud import WordCloud
words_list = []
for i in omicrondata['formatsymptom'][:100]:
    i = str(i)
    i = i.replace('[','')
    i = i.replace(']','')
    i = i.replace("'",'')
    i = i.replace('nan','')
    i = i.replace('none','')
    words_list.append(str(i))
word_string = ' '.join(words_list)
wordcloud = WordCloud(width=800,height=800,background_color='white',min_font_size=1).generate(word_string)
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()
plt.savefig("./")

import seaborn as sns

symptom_list = word_string.split(',')
keywords = ['cough','fever','sore','breath','aches','taste','smell','fatigue','nose','nausea','headache']
counter = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(symptom_list)):
    for j in range(len(keywords)):
        if keywords[j] in symptom_list[i]:
            counter[j]+=1
plt.figure(figsize=(10,6))
sns.barplot(x=keywords,y=counter)

def askgpt(context_str):
    QUESTION = "These values are symptoms that Covid-19 patients felt. Sort the symptom into one of the following categories seperated by parenthesis and a singular number: (1.fever or chills) (2.cough) (3.shortness of breath or difficulty breathing) (4.sore throat) (5.congestion or runny nose) (6.new loss of taste or smell) (7.fatigue) (8.muscle or body aches) (9.headache) (10.nausea or vomiting) (11. diarrhea). Return the number of the category you have associated the input with. It should only be ONE number that is between 1 and 11 that the response fits the best with and don't inlude characters 'n' and '\'. If nothing fits, output the number 0 and nothing else. Do this with no introductory or concluding remarks."
    context_str = f"""{context_str}"""
    openai.api_key = #Insert API key here
    response = openai.ChatCompletion.create(
    model="gpt-4o", # do not pass in model by args
    messages=[
                {"role": "system", "content": context_str},
                {"role": "user", "content": QUESTION},
        ]
    )


    return response['choices'][0]['message']['content']
omicrondata["category"] = omicrondata["formatsymptom"][:100].apply(askgpt)
omicrondata["2"] = omicrondata["category"]
acceptnumbers = [0,1,2,3,4,5,6,7,8,9,10,11]
for i in range(len(omicrondata["2"][:100])):
     answer = str(omicrondata["2"][i])
     answer = answer.replace('\n','')
     newanswer = int(answer[0])
     if newanswer not in acceptnumbers:
        newanswer = answer.replace(answer,'0')
     omicrondata.loc[i,"2"] = newanswer
categories = ['other','fever or chills', 'cough','shortness of breath/difficulty breathing','sore throat', 'congestion or runny nose',
              'new loss of taste or smell', 'fatigue', 'muscle or body aches', 'headache', 'nausea or vomiting', 'diarrhea']
counter = [0,0,0,0,0,0,0,0,0,0,0,0]
for numb in omicrondata["2"][:100]:
    numb = int(numb)
    counter[numb] += 1
plt.figure(figsize=(18,6))
sns.barplot(x=categories,y=counter)
plt.xticks(rotation=45)

