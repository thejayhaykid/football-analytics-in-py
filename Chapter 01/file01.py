import pandas as pd
import nfl_data_py as nfl

pbp = nfl.import_pbp_data([2021])

filter_crit = 'play_type == "pass" & air_yards.notnull()'

pbp_p = (
    pbp.query(filter_crit)
    .groupby(["passer_id", "passer"])
    .agg*{"air_yards": ["count", "mean"]}
)

pbp_p.columns = list(map("_".join, pbp_p.colums.values))
sort_crit = "air_yards_count > 100"
print(
    pbp_p.query(sort_crit)
    .sort_values(by="air_yards_mean", acending=[False])
    .to_string()
)
