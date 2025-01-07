import os
import pandas as pd
import numpy as np
import nfl_data_py as nfl
import seaborn as sns
import matplotlib.pyplot as plt

seasons = range(2016, 2022 + 1)


def divide():
    print('\n-------------------------------------------------------------------')


# import data
chap_2_file = "./data/pbp_py_chap_2.csv"

if os.path.isfile(chap_2_file):
    print("Loading file...")
    pbp_py = pd.read_csv(chap_2_file, low_memory=False)
else:
    print("Downloading data...")
    seasons = range(2016, 2022 + 1)
    pbp_py = nfl.import_pbp_data(seasons)
    print("Saving data to local file...")
    pbp_py.to_csv(chap_2_file)

print("Only pass plays...")
pbp_py_p = pbp_py\
    .query("play_type == 'pass' & air_yards.notnull()")\
    .reset_index()

print("Are they long or short?")
pbp_py_p["pass_length_air_yards"] = np.where(
    pbp_py_p["air_yards"] >= 20, "long", "short"
)

print("Null is incomplete, 0 yards replacement...")
pbp_py_p["passing_yards"] = \
    np.where(
        pbp_py_p["passing_yards"].isnull(), 0, pbp_py_p["passing_yards"]
)

divide()
print("Describing short passes...")
print(pbp_py_p.query('pass_length_air_yards == "short"')
      ["passing_yards"].describe())

print("\nEPA on short passes")
print(pbp_py_p.query('pass_length_air_yards == "short"')
      ["epa"].describe())

divide()
print("Describing long passes...")
print(pbp_py_p.query('pass_length_air_yards == "long"')
      ["passing_yards"].describe())

print("\nEPA on long passes")
print(pbp_py_p.query('pass_length_air_yards == "long"')
      ["epa"].describe())

divide()
sns.displot(data=pbp_py, x="passing_yards")
plt.show()
