import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
import  pandas as pd

def get_skills(text):
    stop_words = set(stopwords.words('english'))
    a = word_tokenize(text)
    filtered_text = [i for i in a if not i in stop_words and not i in string.punctuation]

    skills = pd.read_csv('/home/shubham/projects/cvparser/skills.csv')
    skills = skills.Skillset
    skills = skills.to_list()

    user_skills =[]
    for i in filtered_text:
        if i.lower() in skills:
            user_skills.append(i.lower())
    user_skills = set(user_skills)
    return list(user_skills)
