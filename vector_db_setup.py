import chromadb
from chromadb.utils import embedding_functions
import json
import os
from typing import List, Dict

# Set the custom API base URL and the key for your environment
import openai
openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = "voc-00000000000000000000000000000000abcd.12345678"

# Pass the key and the base URL to the embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai.api_key,
    api_base=openai.api_base,
    model_name="text-embedding-ada-002"
)

def create_and_populate_db(listings: List[Dict]) -> chromadb.Collection:
    client = chromadb.Client()
    
    try:
        client.delete_collection(name="real_estate_listings")
        collection = client.create_collection(name="real_estate_listings", embedding_function=openai_ef)
        print("Recreated collection 'real_estate_listings'.")
    except Exception:
        collection = client.create_collection(name="real_estate_listings", embedding_function=openai_ef)
        print("Created new collection 'real_estate_listings'.")

    ids = [str(i) for i in range(len(listings))]
    documents = [f"Neighborhood: {l['neighborhood']} | Price: {l['price']} | Bedrooms: {l['bedrooms']} | Bathrooms: {l['bathrooms']} | House Size: {l['house_size_sqft']} sqft | Description: {l['description']} | Neighborhood Description: {l['neighborhood_description']}" for l in listings]
    metadatas = listings

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Successfully added {len(listings)} listings to ChromaDB.")
    return collection

if __name__ == "__main__":
    with open("listings.json", "r") as f:
        all_listings = json.load(f)

    collection = create_and_populate_db(all_listings)