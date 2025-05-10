# 🎬 Movie Recommender System — Collaborative Filtering (Cosine Similarity)

This project demonstrates a **movie recommender system** using the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/), based on **collaborative filtering** with **cosine similarity** between movies.

---

## 📂 Dataset

We use the MovieLens 100K dataset which includes:

- `u.data`: user ratings (user_id, item_id, rating, timestamp)
- `u.item`: metadata for each movie (item_id, title, genres, etc.)

⚠️ These files are tab-separated and not in CSV format.


## 🧠 Methodology

- Create a **user-item matrix** from ratings data.
- Convert it into a **movie-user matrix** for item-based collaborative filtering.
- Use **cosine similarity** to find movies that are often rated similarly.
- Recommend top similar movies based on user input.


## 💻 How to Run

1. Clone this repo and unzip the MovieLens 100K dataset inside the project directory.
2. Install required libraries using:

```bash
pip install -r requirements.txt
```
3. Run the main Python script or use it in a Jupyter Notebook or Google Colab.


## 🚀 Example Output

```bash
get_similar_movies("Star Wars (1977)")
```

```bash
Empire Strikes Back, The (1980)    0.795
Return of the Jedi (1983)         0.758
Raiders of the Lost Ark (1981)    0.712
Fugitive, The (1993)              0.703
Jurassic Park (1993)              0.699
```


## 🔍 Key Learnings

- Collaborative filtering works on the assumption that similar users rate similar items.
- Cosine similarity allows us to measure how "alike" two movies are based on user ratings.
- It works well when there's enough overlap in user ratings.

## ⚠️ Limitations

- Cold Start: Doesn't work well for new users or movies with few ratings.
- Sparse Matrix: Many movies are unrated by most users.
- Accuracy can be improved using Matrix Factorization (SVD) or Neural Collaborative Filtering.

---

Thank you for reading.








