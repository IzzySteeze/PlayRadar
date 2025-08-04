import streamlit as st
import requests
import pandas as pd

# ----- CONFIG -----
API_KEY = "29ef4aa2a7a643c990186cf0b5a2b9cc"
BASE_URL = "https://api.rawg.io/api/games"

# ----- PAGE SETUP -----
st.set_page_config(page_title="PlayRadar", page_icon="🎮")
st.title("🎮 PlayRadar")
st.subheader("Discover what's trending in the gaming world, in real time!")

# ----- FILTER OPTIONS -----
platforms = {
    "All": None,
    "PC": 4,
    "PlayStation 5": 187,
    "Xbox Series X": 186,
    "Nintendo Switch": 7
}

genres = {
    "All": None,
    "Action": "action",
    "RPG": "role-playing-games-rpg",
    "Adventure": "adventure",
    "Shooter": "shooter",
    "Strategy": "strategy"
}

st.sidebar.header("🎮 Filter Games")
selected_platform = st.sidebar.selectbox("Platform", list(platforms.keys()))
selected_genre = st.sidebar.selectbox("Genre", list(genres.keys()))

# ----- API REQUEST -----
params = {
    "key": API_KEY,
    "page_size": 10,
    "ordering": "-added"  # Recently popular
}

if platforms[selected_platform]:
    params["platforms"] = platforms[selected_platform]

if genres[selected_genre]:
    params["genres"] = genres[selected_genre]

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    games = data["results"]

    st.markdown("### 🔥 Trending Games Right Now")

    for game in games:
        st.markdown(f"**{game['name']}**")
        st.write(f"⭐ Rating: {game['rating']} | 📅 Released: {game.get('released', 'N/A')}")
        if game.get("background_image"):
            st.image(game["background_image"], width=600)
        st.markdown("---")
else:
    st.error("Failed to fetch game data. Please check your API key or try again later.")

# ----- FOOTER -----
st.caption("🚀 Powered by RAWG • Brought to you by PlayRadar")
