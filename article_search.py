import requests

def search_articles(researcher: str):
    url = "https://api.semanticscholar.org/graph/v1/author/search"
    params = {
        "query": researcher,
        "limit": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    if not data.get("data"):
        return []
    
    author_id = data["data"][0]["authorId"]
    paper_url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
    paper_response = requests.get(paper_url, params={"limit": 10, "fields": "title"})
    paper_response.raise_for_status()
    paper_response_data = paper_response.json()
    
    return [paper["title"] for paper in paper_response_data.get("data", [])]