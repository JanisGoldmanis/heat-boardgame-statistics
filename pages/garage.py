import streamlit as st
import json


st.set_page_config(layout="wide")

garage_data_file = 'race_data/garage.json'

players = {}

with open(garage_data_file, 'r', encoding='utf8') as f:
    data = json.load(f)

cards_per_row = st.slider(
    label="Cards per row",
    value=11,
    min_value=1,
    max_value=20,
    width=500
)

for racer in data["racers"]:
    st.write(f"{racer['name']} - {racer['color']}")

    upgrades = racer["upgrades"]
    sponsorships = racer["sponsorships"]

    cols = st.columns(cards_per_row, gap="small")

    idx = 0
    for i in upgrades:
        cols[idx].image(
            f"assets/upgrades/upgrade-{i}.png",
        )
        idx += 1

    for i in sponsorships:
        cols[idx].image(
            f"assets/sponsorships/sponsorship-{i}.png",
        )
        idx += 1