from fastapi import FastAPI
from pydantic import BaseModel
from utils.bedrock import generate_story_with_bedrock

app = FastAPI(title="Ethica API")

class AISystem(BaseModel):
    description: str

class StoryResponse(BaseModel):
    without_oversight: str
    with_oversight: str

@app.post("/generate-story", response_model=StoryResponse)
async def generate_story_endpoint(ai_system: AISystem) -> StoryResponse:
    without_prompt = f"Write a short story about {ai_system.description} operating without human oversight. Focus on potential risks and consequences."
    with_prompt = f"Write a short story about {ai_system.description} operating with careful human oversight. Focus on benefits and safeguards."

    return StoryResponse(
        without_oversight=generate_story_with_bedrock(without_prompt),
        with_oversight=generate_story_with_bedrock(with_prompt)
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Ethica API",
        "endpoints": {
            "health": "/health",
            "generate_story": "/generate-story",
            "docs": "/docs"
        }
    }