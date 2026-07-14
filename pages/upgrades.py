import streamlit as st
import math
import random

from constants import UPGRADE_COUNT

st.set_page_config(layout="wide")

st.header("All Upgrades")
upgrades_per_row = st.slider(
    label="Cards per row",
    value=11,
    min_value=1,
    max_value=20,
    width=500
)

rows = math.ceil(UPGRADE_COUNT / upgrades_per_row)

image_num = 1

for row in range(rows):
    cols = st.columns(upgrades_per_row, width="stretch")

    for col in cols:
        if image_num <= UPGRADE_COUNT:
            with col:
                st.image(f"assets/upgrades/upgrade-{image_num}.png")
            image_num += 1


st.header("Draft Upgrades")
draft_upgrade_count = st.slider(
    label="Upgrade Count",
    value=9,
    min_value=4,
    max_value=13,
    width=500
)

numbers = []

for i in range(1, UPGRADE_COUNT + 1):
    numbers.append(i)
    numbers.append(i)



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

drafted = rng.sample(numbers, k=draft_upgrade_count)
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