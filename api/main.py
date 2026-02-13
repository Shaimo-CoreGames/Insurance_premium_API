# we used rf model that not only gives prediction but can also give its score
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict, Model_name, MODEL_version, model

app = FastAPI()

@app.get('/')
def home(): 
    return JSONResponse(status_code=200, content={'message': 'Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions.'})

#  Machine readable endpoint
@app.get('/health') # used by AWS load balancer to check if the app is running fine or not
def health_check(): 
    return JSONResponse(status_code=200, content={'status': 'ok', 'model': Model_name, 'version': MODEL_version, 'model_loaded': model is not None})


@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict(user_input)
        return JSONResponse(status_code=200, content=prediction)
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

