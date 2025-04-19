from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"app": "v1.0.0"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)