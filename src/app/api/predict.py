from fastapi import APIRouter, HTTPException
from services.classification import Classification
from schemas.schemas import  TextRequest , PredictionsResponse

router = APIRouter()

classifier = Classification()

@router.post("/predict",description="Classify a list of texts and return predictions with probabilities.",response_model=PredictionsResponse)
async def predict(request: TextRequest):
    """
     Endpoint to Classify a list of texts and return predictions with probabilities.
    """
    
    try:
        predictions = classifier.classify_texts(request.texts)
        return PredictionsResponse(predictions=predictions)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))