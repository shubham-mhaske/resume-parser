import pandas as pd

education = pd.read_csv('/home/shubham/projects/cvparser/education2.csv')
education = education.Qualifications.to_list()

education = map(lambda x: x.lower(), education)


def rep(x):
    x = x.replace('(', 'in ')
    x = x.replace(')', '')
    return x


education = map(rep, education)

education = list(education)


def extract_education(resume_text):
    edu_list = []
    for i in education:
        if i.lower() in resume_text:
            edu_list.append(i)
    return edu_list
