import spacy
from spacy.matcher import Matcher
import  read_file
import mobile_email
import name
import  find_skills
import find_education


nlp = spacy.load('en_core_web_sm'
                 '+'
                 ' gsw 0 ')
matcher = Matcher(nlp.vocab)

text = read_file.docs_to_text('/home/shubham/projects/cvparser/resumes/pdf/1.pdf')
name = name.extract_name(text,nlp,matcher)
mobileNo,email = mobile_email.get_mobile_email(text)
skills_list = find_skills.get_skills(text)
education = find_education.extract_education(text)


print(name,mobileNo,email,skills_list,'\n', education)