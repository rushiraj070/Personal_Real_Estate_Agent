import os
import json
import pandas as pd
import openai
from pydantic import BaseModel, Field
from typing import List
import chromadb
from chromadb.utils import embedding_functions

# Set the custom API base URL and the key for your environment
openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = "voc-00000000000000000000000000000000abcd.12345678"

# Pass the key and the base URL to the embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai.api_key,
    api_base=openai.api_base,
    model_name="text-embedding-ada-002"
)
client = chromadb.Client()
collection = client.get_collection(name="real_estate_listings", embedding_function=openai_ef)

def get_user_preferences() -> str:
    questions = [
        "How big do you want your house to be?",
        "What are 3 most important things for you in choosing this property?",
        "Which amenities would you like?",
        "Which transportation options are important to you?",
        "How urban do you want your neighborhood to be?"
    ]
    answers = []
    print("Welcome to HomeMatch! Please answer a few questions about your dream home.")
    for q in questions:
        answer = input(f"\n{q}\n> ")
        answers.append(answer)

    return " ".join(answers)

def find_matching_listings(query: str, num_results: int = 3) -> pd.DataFrame:
    results = collection.query(
        query_texts=[query],
        n_results=num_results
    )
    
    matched_listings = results['metadatas'][0]
    return pd.DataFrame(matched_listings)

def personalize_description(listing: dict, preferences: str) -> str:
    messages = [
        {"role": "system", "content": f"You are a real estate agent. Rewrite the following real estate listing description to highlight aspects that would appeal to a buyer with these preferences: '{preferences}'. Do not change any factual information like the number of bedrooms, bathrooms, price, or location. Ensure the tone is appealing and personalized."},
        {"role": "user", "content": f"Original Listing Description: {listing['description']}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    user_preferences_text = get_user_preferences()
    
    print("\nSearching for homes that match your preferences...")
    
    matched_df = find_matching_listings(user_preferences_text)
    
    print("\nFound the following matching listings:")
    print(matched_df[['neighborhood', 'price', 'bedrooms', 'bathrooms']])
    
    for index, row in matched_df.iterrows():
        print("-" * 50)
        print(f"\nOriginal Listing from {row['neighborhood']}:")
        print(row['description'])
        
        personalized_desc = personalize_description(row.to_dict(), user_preferences_text)
        
        print("\nPersonalized Description for you:")
        print(personalized_desc)