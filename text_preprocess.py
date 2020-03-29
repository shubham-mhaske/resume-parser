import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

#nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
a= word_tokenize(text)