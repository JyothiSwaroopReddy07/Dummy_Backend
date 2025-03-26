from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://gasstation_vqo1_user:IgcV8M86MP058fjt1r4hIACFfe4JPUKD@dpg-cvhofp2qgecs73d2tie0-a.oregon-postgres.render.com/gasstation_vqo1")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()