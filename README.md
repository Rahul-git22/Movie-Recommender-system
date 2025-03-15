# Movie-Recommender-system

A web-based movie recommender system built using Python, Streamlit, and a collaborative filtering approach.

## Project Overview

This project implements a movie recommender system using collaborative filtering based on movie metadata. The system recommends movies similar to the one selected by the user. The recommendation engine is built using Python, and the web interface is created with Streamlit.

## Features

- **User-friendly Web Interface**: Built with Streamlit for easy interaction.
- **Dynamic Recommendations**: Provides real-time movie recommendations based on user input.
- **Scalable**: Can be easily extended to include more movies and features.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Streamlit
- Pandas
- Scikit-learn
- Pickle

You can install the required packages using pip:

```bash
pip install streamlit pandas scikit-learn
```
## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommender-system.git
```
2. Navigate to the project directory:
```bash
cd movie-recommender-system
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Ensure you have the movie_list.pkl and similarity.pkl files in the project directory. These files contain the movie data and the similarity matrix, respectively.
2. Run the Streamlit app:
```bash
streamlit run app.py
```
3. Open the provided URL in your web browser (usually http://localhost:8501).
4. Select a movie from the dropdown menu and click the "Show Recommendations" button to see the recommended movies.

## Running the Streamlit App
To run the Streamlit app locally, follow these steps:
1. Open a terminal and navigate to the project directory.
2. Run the following command:
```bash
streamlit run app.py
```
Open the URL provided by Streamlit in your web browser.

## Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a pull request










