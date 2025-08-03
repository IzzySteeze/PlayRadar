import streamlit as st
import pandas as pd

# ---------- App Title & Branding ----------
st.set_page_config(page_title="PlayRadar", page_icon="🎮")
st.title("🎮 PlayRadar")
st.subheader("Discover what’s trending in the world of gaming!")

# ---------- Sample Trending Game Data ----------
games = [
    {"Title": "Elden Ring", "Genre": "RPG", "Platform": "PC", "Rating": 9.5, "Release": "2022"},
    {"Title": "God of War: Ragnarok", "Genre": "Action", "Platform": "PS5", "Rating": 9.8, "Release": "2022"},
    {"Title": "The Legend of Zelda: Tears of the Kingdom", "Genre": "Adventure", "Platform": "Switch", "Rating": 9.7, "Release": "2023"},
    {"Title": "Starfield", "Genre": "Sci-Fi", "Platform": "Xbox", "Rating": 8.5, "Release": "2023"},
    {"Title": "Hogwarts Legacy", "Genre": "Fantasy", "Platform": "PC", "Rating": 8.2, "Release": "2023"},
]

df = pd.DataFrame(games)

# ---------- Sidebar Filters ----------
st.sidebar.header("🎮 Filter Games")
platform = st.sidebar.selectbox("Platform", ["All", "PC", "PS5", "Xbox", "Switch"])
genre = st.sidebar.selectbox("Genre", ["All", "Action", "RPG", "Adventure", "Sci-Fi", "Fantasy"])

# ---------- Apply Filters ----------
filtered_df = df.copy()
if platform != "All":
    filtered_df = filtered_df[filtered_df["Platform"] == platform]
if genre != "All":
    filtered_df = filtered_df[filtered_df["Genre"] == genre]

# ---------- Show Filtered Results ----------
st.markdown("### 🎯 Trending Games")
if filtered_df.empty:
    st.warning("No games found for the selected filters.")
else:
    st.dataframe(filtered_df.reset_index(drop=True))

# ---------- Footer ----------
st.markdown("---")
st.caption("🚀 Powered by PlayRadar • More features and live data coming soon!")
