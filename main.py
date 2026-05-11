import streamlit as st


pages = {
    "Statistics": [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/statistics.py", title="Statistics"),
    ],
    "Tournaments": [
        st.Page("pages/tournaments.py", title="Tournaments"),
    ],
}

pg = st.navigation(pages)
pg.run()