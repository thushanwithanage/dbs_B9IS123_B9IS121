from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"data": "Thushan Withanage (20058324) Network Systems and Administration assignment"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)