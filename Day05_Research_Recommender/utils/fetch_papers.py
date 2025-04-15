
import requests

def get_research_papers(query):
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,abstract,authors,url'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        papers = []
        for paper in data.get('data', []):
            papers.append({
                'title': paper.get('title', 'No title'),
                'abstract': paper.get('abstract', 'No abstract available.'),
                'authors': ', '.join([author['name'] for author in paper.get('authors', [])]),
                'url': paper.get('url', '#')
            })
        return papers
    except Exception as e:
        print("Error fetching papers:", e)
        return []
