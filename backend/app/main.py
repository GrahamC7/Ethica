from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ethica API")

class AISystem(BaseModel):
    description: str

class StoryResponse(BaseModel):
    without_oversight: str
    with_oversight: str

@app.post("/generate-story", response_model=StoryResponse)
async def generate_story(ai_system: AISystem) -> StoryResponse:
    # placeholder response until Bedrock integration is implemented
    return StoryResponse(
        without_oversight="Story about AI without oversight...",
        with_oversight="Story about AI with human oversight..."
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}