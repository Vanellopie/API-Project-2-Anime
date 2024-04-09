from supabase import create_client, Client
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, HTTPException
from typing import List

# https://docs.render.com/deploy-fastapi

supabase_url: str = "https://pudktqwdyxdtkyxgxqzj.supabase.co"
supabase_key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB1ZGt0cXdkeXhkdGt5eGd4cXpqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTAzODE1MzMsImV4cCI6MjAyNTk1NzUzM30._MzX-DYB7YOtSKrJPxUxXDSQFmS6HVBj0AdJJ6ShfWE"

supabase: Client = create_client(supabase_url, supabase_key)

class AnimeList(BaseModel):
    id: Optional[int] = None
    Name: Optional[str] = None
    Score: Optional[int] = None
    Genres: Optional[int] = None
    # English_name: Optional[str] = None
    Type: Optional[str] = None
    Episodes: Optional[float] = None
    Source: Optional[str] = None
    

app = FastAPI()

@app.post("/anime_lists/", response_model=AnimeList)
def create_anime_lists(anime_lists: AnimeList):
    data = anime_lists.dict(exclude_unset=True)
    inserted_data = supabase.table("anime_lists").insert(data).execute()
    if inserted_data.data:
        return inserted_data.data[0]
    else:
        raise HTTPException(status_code=400, detail="Error inserting data")

@app.get("/anime_lists/", response_model=List[AnimeList])
def read_anime_lists():
    data = supabase.table("anime_lists").select("*").execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=400, detail="Error reading data")
    

@app.put("/anime_lists/{anime_lists_id}", response_model=AnimeList)
def update_anime_lists(anime_lists_id: int, anime_lists: AnimeList):
    data = anime_lists.dict(exclude_unset=True)
    updated_data = supabase.table("animes_lists").update(data).eq("id", anime_lists_id).execute()
    if updated_data.data:
        return updated_data.data[0]
    else:
        raise HTTPException(status_code=400, detail="Error updating data")

@app.delete("/anime_lists/{anime_lists_id}", response_model=List[AnimeList])
def delete_anime_lists(anime_lists_id: int):
    deleted_data = supabase.table("anime_lists").delete().eq("id", anime_lists_id).execute()
    if deleted_data.data:
        return deleted_data.data
    else:
        raise HTTPException(status_code=400, detail="Error deleting data")
