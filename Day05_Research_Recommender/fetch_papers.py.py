import requests

def fetch_papers(query):
    # URL for Semantic Scholar API (this can be changed to arXiv if needed)
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5'

    try:
        # Send a GET request to the Semantic Scholar API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        papers = []
        for paper in data.get('data', []):
            paper_info = {
                'title': paper.get('title', 'No Title Available'),
                'abstract': paper.get('abstract', 'No Abstract Available'),
                'authors': [author.get('name') for author in paper.get('authors', [])],
                'url': f"https://www.semanticscholar.org/paper/{paper.get('paperId')}"
            }
            papers.append(paper_info)

        return papers

    except requests.exceptions.RequestException as e:
        print(f"Error fetching papers: {e}")
        return []

# Example usage
if __name__ == "__main__":
    query = "Natural Language Processing"
    papers = fetch_papers(query)
    for paper in papers:
        print(paper)
