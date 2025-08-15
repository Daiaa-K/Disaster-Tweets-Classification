from pydantic import BaseModel, Field
from typing import List

class TextRequest(BaseModel):
    texts: List[str] = Field(..., description="List of Texts to be Classified")
    
    class Config:
        json_schema_extra = {
            "example":{
                "texts": [
                    "Arsonist sets cars ablaze at dealership",
                    "Social media went bananas after Chuba Hubbard announced Monday evening his plans to return to #okstate"
                ]
            }
        }
        

class TextPrediction(BaseModel):
    text: str
    prediction: str
    probability: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "Arsonist sets cars ablaze at dealership",
                "prediction": "disaster",
                "probability": 0.95
            }
        }
        

class PredictionsResponse(BaseModel):
    predictions: List[TextPrediction] = Field(..., description="List of Predictions for the Input Texts")
    
    class Config:
        json_schema_extra = {
            "example": {
                "predictions": [
                    {
                        "text": "Arsonist sets cars ablaze at dealership",
                        "prediction": "disaster",
                        "probability": 0.95
                    },
                    {
                        "text": "Social media went bananas after Chuba Hubbard announced Monday evening his plans to return to #okstate",
                        "prediction": "non-disaster",
                        "probability": 0.85
                    }
                ]
            }
        }