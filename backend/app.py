from fastapi import FastAPI
from run_code import run_code as code_runner
from automated_gen import generate_code as ai_code_generator
from type import *


app = FastAPI()


@app.get('/')
def test_api_running():
    return {"message": "API is running correctly!"}

@app.post("/run-code/")
def run_code(code_input: CodeInput):
    result = code_runner(code=code_input.code, language=code_input.language)
    return {"message": "Code received successfully", "language": code_input.language, "code": code_input.code, "result": result}


@app.post("/generate-code/")
def generate_code(code_request: CodeRequest):
    result = ai_code_generator(prompt=code_request.prompt)
    return {"message": "Code generated successfully", "prompt": code_request.prompt, "result": result}
