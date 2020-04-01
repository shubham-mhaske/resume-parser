import string

import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords


def get_skills(text):
    stop_words = set(stopwords.words('english'))
    a = word_tokenize(text)
    filtered_text = [i for i in a if not i in stop_words and not i in string.punctuation]

    skills = pd.read_csv('/home/shubham/projects/cvparser/skills.csv')  # enter the filepath of skills.cs
    skills = skills.Skillset
    skills = skills.to_list()

    user_skills = []
    for i in filtered_text:
        if i.lower() in skills:
            user_skills.append(i.lower())
    return set(user_skills)
