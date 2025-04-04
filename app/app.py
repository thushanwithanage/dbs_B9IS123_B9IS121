from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from Python FastAPI on EC2! v1"}

# Note: FastAPI does not use app.run; instead, you run it with an ASGI server like uvicorn.