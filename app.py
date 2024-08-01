from fastapi import FastAPI
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-small")
app=FastAPI()
@app.get("/")
def home():
    return {"message":"Hello"}

@app.get("/generate")
def generate(text:str):
    output=pipe(text)
    return {"output":output[0]['generated_text']}