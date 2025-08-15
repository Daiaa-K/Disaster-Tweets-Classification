import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from core.config import EMOTICON_MAPPING

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english')) - {'no', 'not', 'nor', 'none', 'never'}
        self.lemmatizer = WordNetLemmatizer()
        self.emoticon_mapping = EMOTICON_MAPPING
        
    def extract_hashtags(self,text):
        """Extract hashtags from the text and return them as a list of tokens."""
        hashtags = re.findall(r"#\w+",text)
        hashtags_tokens = [tag[1:] for tag in hashtags]
        return hashtags_tokens
    
    def replace_emoticons(self,text):
    # Escape characters for regex
        for emoticon, word in self.emoticon_mapping.items():
            pattern = re.escape(emoticon)
            text = re.sub(pattern, word, text)

        return text
    
    def preprocess_text(self,text):
        """
        Preprocess the input text by:
        - Lowercasing
        - Replacing emoticons with words
        - Replacing contractions
        - Extracting hashtags as special tokens
        - Removing URLs
        - Removing @user tags
        - Removing specific punctuation but keeping apostrophes for contractions
        - Removing standalone numbers
        - Normalizing whitespace
        - Reducing repeated characters (e.g., helloooo → helloo)
        - Tokenizing
        - Removing stopwords
        - Removing short words
        - Lemmatizing
        - Adding back hashtag tokens
        """
        
        # Lowercase
        text = text.lower()

        # Replace emoticons
        text = self.replace_emoticons(text)

        # Replace contractions
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"'s", " is", text)
        text = re.sub(r"'re", " are", text)
        text = re.sub(r"'m", " am", text)

        # Extract hashtags as special tokens
        hashtag_tokens = self.extract_hashtags(text)
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+', '', text)

        # Remove @user tags
        text = re.sub(r'@\w+', '', text)

        # Remove specific punctuation but keep apostrophes for contractions
        text = re.sub(r'[^\w\s\']', ' ', text)

        # Remove standalone numbers
        text = re.sub(r'\b\d+\b', '', text)

        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        # Reduce repeated characters (e.g., helloooo → helloo)
        text = re.sub(r'(.)\1{2,}', r'\1\1', text)

        # Tokenize
        tokens = word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words('english')) - {'no', 'not', 'nor', 'none', 'never'}
        tokens = [word for word in tokens if word not in stop_words]

        # Remove short words
        tokens = [word for word in tokens if len(word) >= 2]

        # Lemmatize
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

        # Add back hashtag tokens
        tokens.extend(hashtag_tokens)
        
        return tokens

