
from flask import Flask, render_template, request
from utils.fetch_papers import get_research_papers

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    papers = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('query')
        papers = get_research_papers(query)
    return render_template('index.html', papers=papers, query=query)

if __name__ == '__main__':
    app.run(debug=True)
