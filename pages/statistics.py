import streamlit as st
import json
from multi_elo import EloPlayer, calc_elo
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


st.header('Statistics')

k_factor = 16


race_data_file = 'race_data/race_data.json'

players = {}

with open(race_data_file, 'r', encoding='utf8') as f:
    data = json.load(f)

tournaments = data['tournaments']

race_id = 1

for tournament in tournaments:
    races = tournament['races']

    for race in races:

        positions = race['positions']

        # Sorted copy (does not modify original)
        sorted_positions = sorted(positions, key=lambda x: x["position"])

        elo_players = []

        for player in sorted_positions:
            name = player['name']
            if name not in players:
                players[name] = {
                    'name': name,
                    'elo': 1500,
                    'history': [(race_id-1, 1500)]
                }

            elo_players.append(EloPlayer(place=player['position'], elo=players[name]['elo']))

        new_elos = calc_elo(elo_players, k_factor)

        for i in range(len(new_elos)):
            elo = new_elos[i]

            name = sorted_positions[i]['name']

            player = players[name]

            player['elo'] = elo
            player['history'].append((race_id, elo))

        # st.write(new_elos)

        race_id += 1

elo_dict = {'name': [], 'elo': [], 'last_change': []}
for name, info in players.items():
    elo_dict['name'].append(name)
    elo_dict['elo'].append(info['elo'])
    elo_dict['last_change'].append(info['history'][-1][1] - info['history'][-2][1])

st.dataframe(elo_dict)


colors = {
    "Jānis": "yellow",
    "Klāvs": "grey",
    "Miks": "orange",
    "Dāvis": "blue",
    "Andris A.": "red",
    "Alec": "green",
    "Toms": "purple",
    "Andris K.": "pink",
}


fig, ax = plt.subplots(figsize=(9, 5))

for player, info in players.items():
    history = info["history"]          # [(race_id, elo), ...]
    x = [h[0] for h in history]        # race_id
    y = [h[1] for h in history]        # elo

    ax.plot(
        x,
        y,
        marker='o',
        label=player,
        color=colors.get(player, "black")   # <--- use player color
    )

ax.set_ylim(1300, 1700)                # FIXED Y range
ax.set_xlabel("Race ID")
ax.set_ylabel("ELO")
ax.set_title("Player ELO History")
ax.grid(True)
ax.legend()

st.pyplot(fig)


rows = []

for player, info in players.items():
    for race, elo in info["history"]:
        rows.append({
            "player": player,
            "race": race,
            "elo": elo
        })

df = pd.DataFrame(rows)

colors = {
    "Jānis": "yellow",
    "Klāvs": "grey",
    "Miks": "orange",
    "Dāvis": "blue",
    "Andris A.": "red",
    "Alec": "green",
    "Toms": "purple",
    "Andris K.": "pink",
}

fig = px.line(
    df,
    x="race",
    y="elo",
    color="player",
    markers=True,
    color_discrete_map=colors
)

st.plotly_chart(fig, width='content')