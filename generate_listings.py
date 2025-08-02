import os
import openai
from pydantic import BaseModel, Field
from typing import List
import json
import pandas as pd

# Set the custom API base URL and the key for your environment
openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = "voc-00000000000000000000000000000000abcd.12345678"

class Listing(BaseModel):
    neighborhood: str
    price: str
    bedrooms: int
    bathrooms: int
    house_size_sqft: int = Field(alias="House Size")
    description: str
    neighborhood_description: str = Field(alias="Neighborhood Description")

    class Config:
        populate_by_name = True

def generate_listings(num_listings: int = 10) -> List[dict]:
    messages = [
        {"role": "system", "content": f"You are a real estate expert. Generate a list of {num_listings} diverse and realistic real estate listings. Each listing must have a neighborhood, price, number of bedrooms, number of bathrooms, house size in square feet, a detailed description, and a neighborhood description. Return the output as a JSON array of objects."},
        {"role": "user", "content": "Generate the listings and format them as a JSON array of objects."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
    )
    
    response_content = response.choices[0].message.content
    
    try:
        listings_data = json.loads(response_content)
    except json.JSONDecodeError:
        print("Error: Could not parse LLM response as JSON.")
        return []

    return listings_data

if __name__ == "__main__":
    generated_listings = generate_listings(num_listings=10)

    with open("listings.json", "w") as f:
        json.dump(generated_listings, f, indent=4)

    print(f"Generated {len(generated_listings)} listings and saved them to listings.json")