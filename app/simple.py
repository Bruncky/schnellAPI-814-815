from fastapi import FastAPI

app = FastAPI()

# define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': 'hello'}

@app.get('/predict')
def predict(day_of_week, time):
    # Load model
    # Make prediction
    # Return prediction
    prediction = int(day_of_week) * int(time)

    return {'wait': prediction}
