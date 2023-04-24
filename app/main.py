from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/healthchecker")
def root():
    return {"Welcome Message": "Welcome back Captain!!"}
