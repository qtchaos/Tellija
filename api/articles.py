"""
Retrieves articles from the given API.
"""
import requests

ITERATION = 0
OLD_ID = 0


def fetch():
    global OLD_ID
    global ITERATION
    articles = requests.get(
        "https://services.postimees.ee/rest/v1/sections/81/articles?limit=1"
    ).json()
    if articles[0]["id"] == OLD_ID:
        return False
    print(f"ID's don't match. {OLD_ID} -> {articles[0]['id']}")
    OLD_ID = articles[0]["id"]
    ITERATION += 1
    return articles
