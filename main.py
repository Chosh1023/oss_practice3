from fastapi import FastAPI
from grade import func

import uvicorn 

app = FastAPI()

@app.get("/")
async def welcome()-> dict:
    return{
        "msg" : "Hello world"
    }

app.include_router(func)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
