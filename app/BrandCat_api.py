from fastapi import FastAPI,HTTPException
from BrandCat import generate_keywords, generate_branding_snippet
app = FastAPI()

MAX_INPUT_LENGTH = 32

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet}

@app.get("/generate_keyword")
async def generate_keyword_api(prompt: str):
    validate_input_length(prompt)
    keyword = generate_keywords(prompt)
    return {"keyword": keyword}

@app.get("/generate_keyword_snippet")
async def generate_keyword_api(prompt: str):
    validate_input_length(prompt)
    keyword = generate_keywords(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keyword": keyword}

def validate_input_length(prompt: str):
    if(len(prompt) >= MAX_INPUT_LENGTH):
        raise HTTPException(status_code = 400,
        detail = f"input length is too long. Must be under {MAX_INPUT_LENGTH}")
    

# uvicorn BrandCat_api:app --reload