import spacy
from spacy.matcher import Matcher

import find_education
import find_skills
import mobile_email
import name
import read_file

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

text = read_file.read_file('/home/shubham/projects/cvparser/resumes/docx/2.docx')
name = name.extract_name(text, nlp, matcher)
mobileNo, email = mobile_email.get_mobile_email(text)
skills_list = find_skills.get_skills(text)
education = find_education.extract_education(text)

print(f'Name: {name}\nMobile No. : {mobileNo}\nEmail Id: {email}\nSkills : {skills_list}\nEducation : {education}')
