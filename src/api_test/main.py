from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
PORT = 6001

class EchoRequest(BaseModel):
    echostring: str


@app.post("/")
async def echo_endpoint(request: EchoRequest):
    return {"message": f"hello {request.echostring}"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == '__main__':
    main()