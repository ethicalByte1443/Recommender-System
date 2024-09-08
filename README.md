# Movie Recommendation System

## Overview

This repository contains a movie recommendation system built using various machine learning techniques and natural language processing (NLP) methods. The system recommends movies based on content filtering and cosine similarity. The project was implemented using **Jupyter Notebook** and involves several key machine learning and NLP libraries.

![Types of Recommendation Systems](https://github.com/ethicalByte1443/Recommender-System/blob/main/Photos/Types%20of%20System.png)

## What is a Recommender System?

A **Recommender System** is a subclass of information filtering systems that seeks to predict the preference or rating a user would give to an item. Recommender systems are widely used in applications like movie recommendations, shopping suggestions, and more.

There are primarily three types of recommender systems:
1. **Collaborative Filtering**: Recommends items based on user-item interactions.
2. **Content-based Filtering**: Recommends items similar to what the user liked in the past.
3. **Hybrid Systems**: Combine collaborative and content-based approaches.

In this project, I focused on **content-based filtering**, where recommendations are made based on the features of the movies, such as genre, cast, crew, and more.

## Project Approach

The system works by suggesting movies that share similar features with the movie a user has watched or liked. Here's how I tackled the problem:

1. **Data Cleaning**: Cleaned and preprocessed the movie dataset, including removing null values, handling missing data, and formatting the movie features.
   
2. **Feature Engineering**: Extracted important features like the movie's title, genre, director, cast, and keywords from the dataset.

3. **Vectorization**:
   - Utilized **CountVectorizer** from the `sklearn` library to convert textual data (like genre, director, cast) into a matrix of token counts.
   - Applied **PorterStemmer** from the `nltk` library to reduce words to their base or root form.

4. **Similarity Calculation**:
   - Computed **Cosine Similarity** between movie vectors to measure how similar two movies are. The higher the cosine similarity, the more likely the movies are to be recommended together.

5. **Pickle for Serialization**: The trained model and its components (like vectorizer, cosine similarity matrix) were saved using **Pickle** for future use without needing to retrain the model every time.

6. **API Integration**: Used various API keys to fetch additional data like movie posters and information that are presented to the user.

## Key Features

- **Numpy**: For handling large arrays and performing mathematical operations efficiently.
- **JSON**: To store and retrieve movie data in a structured format.
- **CountVectorizer**: For converting text data into numerical vectors based on word frequency.
- **PorterStemmer (NLP)**: For stemming words to reduce redundancy in the text data.
- **Cosine Similarity**: For measuring similarity between movies based on their vectorized features.
- **Pickle**: To save and load the trained model and vectorizer, improving performance by avoiding retraining.
  
## Results and Evaluation

The model successfully recommends movies based on the content similarity. For instance, when a user likes a movie, similar movies based on genre, director, and keywords are suggested. The system is scalable and can easily be extended to handle larger datasets.



