# demonstrate objects
import os
import nfl_data_py as nfl
import pandas as pd
z = 2
z / 3

# import packages
# make sure you installed both packages using pip in the terminal
year = 2022

# Load data from the package
chap_1_file = f"./data/pbp_py_chap_1_{year}.csv"

if os.path.isfile(chap_1_file):
    print("Reading from local file...")
    pbp_py = pd.read_csv(chap_1_file, low_memory=False)
else:
    print("Downloading data...")
    pbp_py = nfl.import_pbp_data([year])
    pbp_py.to_csv(chap_1_file)

# filter out passing data
filter_crit = 'play_type == "pass" & air_yards.notnull()'
pbp_py_p = (
    pbp_py.query(filter_crit)
    .groupby(["passer_id", "passer"])
    .agg({"air_yards": ["count", "mean"]})
)

# format and print data for passing plays
pbp_py_p.columns = list(map("_".join, pbp_py_p.columns.values))
sort_crit = "air_yards_count > 100"
print(
    pbp_py_p.query(sort_crit)
    .sort_values(by="air_yards_mean", ascending=[False])
    .to_string()
)
