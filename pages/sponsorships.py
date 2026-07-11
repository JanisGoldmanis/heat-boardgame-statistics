import streamlit as st
import math

from constants import SPONSORSHIP_COUNT

st.set_page_config(layout="wide")

st.header("All Upgrades")
sponsorships_per_row = st.slider(
    label="Cards per row",
    value=11,
    min_value=1,
    max_value=20,
    width=500
)

rows = math.ceil(SPONSORSHIP_COUNT / sponsorships_per_row)

image_num = 1

for row in range(rows):
    cols = st.columns(sponsorships_per_row, width="stretch")

    for col in cols:
        if image_num <= SPONSORSHIP_COUNT:
            with col:
                st.image(f"assets/sponsorships/sponsorship-{image_num}.png")
            image_num += 1