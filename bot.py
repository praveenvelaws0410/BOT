# Example code for a Telegram GIF Searcher Bot
# Built using FastAPI and Giphy API

import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

class GifSearchRequest(BaseModel):
    query: str

def search_gif(query: str) -> str:
    # Replace with your Giphy API key
    api_key = os.getenv("1f9ba190-c513-471b-a573-b8d008bb52fe")
    url = f"https://api.giphy.com/v1/gifs/search?q={query}&api_key={api_key}&limit=1"
    response = requests.get(url)
    data = response.json()
    if "data" in data and data["data"]:
        gif_url = data["data"][0]["images"]["original"]["url"]
        return gif_url
    else:
        return "No matching GIFs found."

@app.post("/search_gif/")
def get_gif(search_request: GifSearchRequest):
    query = search_request.query
    gif_url = search_gif(query)
    return {"gif_url": gif_url}

