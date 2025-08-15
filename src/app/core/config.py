from dotenv import load_dotenv
import os
import keras
import pickle

load_dotenv()

#load environment variables
APP_NAME  = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

# Define paths and load model
SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTIFACTS_DIR = os.path.join(SRC_DIR, "artifacts")

MODEL_NAME = "rnn_embedding_model.keras"
MODEL_PATH = os.path.join(ARTIFACTS_DIR, MODEL_NAME)
TOKENIZER_PATH = os.path.join(ARTIFACTS_DIR, "tokenizer.pickle")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = keras.models.load_model(MODEL_PATH)

if not os.path.exists(TOKENIZER_PATH):
    raise FileNotFoundError(f"Tokenizer file not found at {TOKENIZER_PATH}")

with open(TOKENIZER_PATH, 'rb') as handle:
    tokenizer = pickle.load(handle)

# Constants for text processing and model configuration
EMBED_DIM = 128
SEQ_LEN = 100
MAX_WORDS = 5000

BATCH_SIZE = 32
EPOCHS = 15
NUM_CLASSES = 2

# Mappings for target labels and emoticons
TARGET_MAPPING = {
    1:"disaster",
    0:"non-disaster"
}

EMOTICON_MAPPING = {
    ":)": "Happy",
    ":(": "Sad",
    ":D": "Very Happy",
    ":|": "Neutral",
    ":O": "Surprised",
    "<3": "Love",
    ";)": "Wink",
    ":P": "Playful",
    ":/": "Confused",
    ":*": "Kiss",
    ":')": "Touched",
    "XD": "Laughing",
    ":3": "Cute",
    ">:(": "Angry",
    ":-O": "Shocked",
    ":|]": "Robot",
    ":>": "Sly",
    "^_^": "Happy",
    "O_o": "Confused",
    ":-|": "Straight Face",
    ":X": "Silent",
    "B-)": "Cool",
    "<(‘.'<)": "Dance",
    "(-_-)": "Bored",
    "(>_<)": "Upset",
    "(¬‿¬)": "Sarcastic",
    "(o_o)": "Surprised",
    "(o.O)": "Shocked",
    ":0": "Shocked",
    ":*(": "Crying",
    ":v": "Pac-Man",
    "(^_^)v": "Double Victory",
    ":-D": "Big Grin",
    ":-*": "Blowing a Kiss",
    ":^)": "Nosey",
    ":-((": "Very Sad",
    ":-(": "Frowning",
    }
