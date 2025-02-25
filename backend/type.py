from pydantic import BaseModel


class CodeInput(BaseModel):
    language: str
    code: str


class CodeRequest(BaseModel):
    prompt: str

