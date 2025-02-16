from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mangum import Mangum

app = FastAPI()

# Update CORS settings to allow your Vite server on port 5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Changed from 3000 to 5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- SQLAlchemy Setup ---
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Example model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI running as a serverless function!"}

handler = Mangum(app)

def main(event, context):
    return handler(event, context)
