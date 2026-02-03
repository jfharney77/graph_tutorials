from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import argparse

app = FastAPI()


class EchoRequest(BaseModel):
    echostring: str


@app.post("/")
async def echo_endpoint(request: EchoRequest):
    return {"message": f"hello hello {request.echostring}"}


def main():
    parser = argparse.ArgumentParser(description="Echo Service")
    parser.add_argument("service_port", type=int, help="Port for the service to run on")
    args = parser.parse_args()
    
    uvicorn.run(app, host="0.0.0.0", port=args.service_port)


if __name__ == '__main__':
    main()
