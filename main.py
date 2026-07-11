import streamlit as st


pages = {
    "Statistics": [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/statistics.py", title="Statistics"),
    ],
    "Tournaments": [
        st.Page("pages/tournaments.py", title="Tournaments"),
        st.Page("pages/garage.py", title="Garage"),
    ],
    "Upgrades": [
        st.Page("pages/upgrades.py", title="Upgrades"),
        st.Page("pages/sponsorships.py", title="Sponsorships"),
    ]
}

pg = st.navigation(pages)
pg.run()