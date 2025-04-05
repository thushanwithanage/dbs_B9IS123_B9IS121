from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "20058324 Networking assignment"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)