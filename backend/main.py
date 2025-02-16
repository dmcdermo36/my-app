from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI (database rem33oved)!"}

# Add the new endpoint here, BEFORE wrapping with Mangum
@app.get("/test")
async def test_endpoint():
    return {"message": "This is the updated /test endpoint!"}

handler = Mangum(app)

def main(event, context):
    return handler(event, context)
