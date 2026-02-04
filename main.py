from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "rain api is running 🌧️"}
