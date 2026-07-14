import math
import random

import streamlit as st
import json

from constants import UPGRADE_COUNT


st.set_page_config(layout="wide")

garage_data_file = 'race_data/garage.json'
drivers_data_file = 'race_data/drivers.json'

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

taken_upgrades = []

with st.expander("See current cards"):

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
            taken_upgrades.append(i)

        for i in sponsorships:
            cols[idx].image(
                f"assets/sponsorships/sponsorship-{i}.png",
            )
            idx += 1

with st.expander("Select Drivers"):
    with open(drivers_data_file, 'r', encoding='utf8') as f:
        data = json.load(f)

        drivers = []

        for driver in data["drivers"]:
            if st.checkbox(label=f"{driver}"):
                drivers.append(driver)

        form = st.form("New Driver")
        driver = form.text_input(label="Name", value="Driver Name")
        if form.form_submit_button():
            drivers.append(driver)


st.write(drivers)

taken_upgrades.sort()

st.write(taken_upgrades)

available_upgrade_ids = []

for upgrade_id in range(1, UPGRADE_COUNT + 1):
    available_upgrade_ids.append(upgrade_id)
    available_upgrade_ids.append(upgrade_id)

for upgrade_id in taken_upgrades:
    available_upgrade_ids.remove(upgrade_id)

st.write(available_upgrade_ids)

driver_count = len(drivers)

draft_upgrade_count = driver_count + 3

st.write(f"Drawing {draft_upgrade_count} draft upgrades")

upgrades_per_row = st.slider(
    label="Cards per row",
    value=4,
    min_value=1,
    max_value=10,
)

seed = st.number_input(
    "Seed",
    value=12345,
    step=1
)

rng = random.Random(seed)

drafted = rng.sample(available_upgrade_ids, k=draft_upgrade_count)
drafted.sort()

rows = math.ceil(len(drafted) / upgrades_per_row)

card_index = 0

for row in range(rows):
    cols = st.columns(upgrades_per_row)

    for col in cols:
        if card_index < len(drafted):
            with col:
                number = drafted[card_index]

                st.image(
                    f"assets/upgrades/upgrade-{number}.png",
                    width='content'
                )

                card_index += 1
