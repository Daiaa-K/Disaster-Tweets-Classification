from typing import List, Dict, Union
from core.config import tokenizer,model, SEQ_LEN, TARGET_MAPPING
from services.textprocessor import TextProcessor
import keras

class Classification:
    def __init__(self):
        self.processor = TextProcessor()
        self.model = model
        self.tokenizer = tokenizer
        self.seq_len = SEQ_LEN
        self.target_mapping = TARGET_MAPPING
        
    def classify_texts(self,texts: List[str]) -> List[Dict[str,Union[str,float]]]:
        """
        Classify a list of texts and return predictions with probabilities.
        """
        
        cleaned_texts = [self.processor.preprocess_text(text) for text in texts]
        sequences = self.tokenizer.texts_to_sequences(cleaned_texts)
        padded_sequences = keras.preprocessing.sequence.pad_sequences(sequences, maxlen=self.seq_len, padding='post', truncating='post')
        
        results = self.model.predict(padded_sequences)
        predicted_labels = results.argmax(axis=1)
        
        predictions = []
        for i,text in enumerate(texts):
            predictions.append({
                "text": text,
                "prediction":self.target_mapping[predicted_labels[i]],
                "probability":  max(results[i][0], 1 - results[i][0])
            })
            
        return predictions