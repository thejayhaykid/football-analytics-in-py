import os
import pandas as pd
import numpy as np
import nfl_data_py as nfl
import seaborn as sns
import matplotlib.pyplot as plt

seasons = range(2016, 2022 + 1)


def divide(title=None):
    line_length = 67
    print('\n' + '-' * line_length + '\n')
    if title:
        padding = (line_length - len(title) - 2) // 2
        extra_dash = '-' if (line_length - len(title) - 2) % 2 != 0 else ''
        print(f"{'-' * padding} {title} {'-' * padding}{extra_dash}")
        print('\n' + '-' * line_length + '\n')


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

divide("Only pass plays...")
pbp_py_p = pbp_py\
    .query("play_type == 'pass' & air_yards.notnull()")\
    .reset_index()

divide("Are they long or short?")
pbp_py_p["pass_length_air_yards"] = np.where(
    pbp_py_p["air_yards"] >= 20, "long", "short"
)

print("Null is incomplete, 0 yards replacement...")
pbp_py_p["passing_yards"] = \
    np.where(
        pbp_py_p["passing_yards"].isnull(), 0, pbp_py_p["passing_yards"]
)

divide("Describing short passes...")
print(pbp_py_p.query('pass_length_air_yards == "short"')
      ["passing_yards"].describe())

divide("EPA on short passes")
print(pbp_py_p.query('pass_length_air_yards == "short"')
      ["epa"].describe())

divide("Describing long passes...")
print(pbp_py_p.query('pass_length_air_yards == "long"')
      ["passing_yards"].describe())

print("\nEPA on long passes")
print(pbp_py_p.query('pass_length_air_yards == "long"')
      ["epa"].describe())

# divide("Plot 1")
sns.displot(data=pbp_py, x="passing_yards")
plt.savefig('data/chapter_02_plot_1.png')

# divide("Plot 2")
pbp_py_p_short = pbp_py_p.query('pass_length_air_yards == "short"')

pbp_py_hist_short = sns.displot(
    data=pbp_py_p_short, binwidth=1, x="passing_yards")
pbp_py_hist_short.set_axis_labels(
    "Yards gained (or lost) during a passing play", "Count")
plt.savefig('data/chapter_02_plot_2.png')

# divide("Plot 3")
pbp_py_p_long = pbp_py_p.query('pass_length_air_yards == "long"')

pbp_py_hist_long = sns.displot(
    data=pbp_py_p_long, binwidth=1, x="passing_yards")
pbp_py_hist_long.set_axis_labels(
    "Yards gained (or lost) during a passing play", "Count")
plt.savefig('data/chapter_02_plot_3.png')

# divide("Boxplot 1")
pass_boxplot = sns.boxplot(
    data=pbp_py_p, x="pass_length_air_yards", y="passing_yards")
pass_boxplot.set(xlabel="Pass length (long >= 20 yards, short < 20 yards)",
                 ylabel="Yards gained (or lost) during a passing play",)
plt.savefig('data/chapter_02_boxplot_1.png')

divide("Group by")
pbp_py_p_s = pbp_py_p.groupby(["passer_id", "passer", "season"])\
    .agg({"passing_yards": ["mean", "count"]})
pbp_py_p_s.columns = list(map("_".join, pbp_py_p_s.columns.values))
pbp_py_p_s.rename(columns={"passing_yards_mean": "ypa",
                  "passing_yards_count": "n"}, inplace=True)
print(pbp_py_p_s.describe())
