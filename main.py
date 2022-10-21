import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.responses import PlainTextResponse, JSONResponse

from models import Expression

EXCEPTION_MESSAGE = "Exception: {0}"

app = FastAPI()


@app.exception_handler(Exception)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, ValidationError):
        message = exc.errors()[0]['msg']
    else:
        message = str(exc)
    if request.method == "GET":
        return PlainTextResponse(message, status_code=400)
    elif request.method == "POST":
        return JSONResponse(dict(Exception=message), status_code=400)


@app.get("/")
@app.get("/index")
async def calc_get():
    response = "Hello World"
    return response


@app.get("/eval")
async def calc_get(expression: Expression = Depends(Expression)):
    response = "{0} = {1}".format(expression.phrase, expression.calculate())
    return PlainTextResponse(response)


@app.post("/eval")
async def calc_post(expression: Expression):
    response = dict(result="{0} = {1}".format(expression.phrase, expression.calculate()))
    return JSONResponse(response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
