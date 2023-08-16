import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text, num_keywords=5):
    # Tokenize the text
    words = word_tokenize(text)
    
    # Filter out stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Calculate word frequency
    fdist = FreqDist(filtered_words)
    
    # Get the most common words as keywords
    keywords = fdist.most_common(num_keywords)
    
    return [keyword for keyword, freq in keywords]

# print(extract_keywords("3 men killed when trying to east sushi with their family"))