import spacy
from spacy.matcher import Matcher
import  read_file
import mobile_email
import name
import  find_skills


nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

text = read_file.docs_to_text('/home/shubham/projects/cvparser/resumes/docs/2.doc')
name = name.extract_name(text,nlp,matcher)
mobileNo,email = mobile_email.get_mobile_email(text)
skills_list = find_skills.get_skills(text)


print(name,mobileNo,email,skills_list)