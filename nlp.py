import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def extract_intent_and_time(text):
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_tokens = [w for w in tokens if not w in stop_words]

    time_match = re.search(r'\b\d{1,2}:\d{2}\b', text)
    if not time_match:
        return None, None

    time = time_match.group()
    intent = ' '.join(filtered_tokens).replace(time, '').strip()

    return intent, time
