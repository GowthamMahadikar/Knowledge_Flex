from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize app
app = FastAPI(title="Text Generation API")

# Load model (can take time first run)
generator = pipeline(
    "text-generation",
    model="gpt2"
)

class TextRequest(BaseModel):
    prompt: str
    max_length: int = 100

class TextResponse(BaseModel):
    generated_text: str

@app.post("/generate", response_model=TextResponse)
def generate_text(request: TextRequest):
    output = generator(
        request.prompt,
        max_length=request.max_length,
        num_return_sequences=1
    )
    return {"generated_text": output[0]["generated_text"]}
