import pandas as pd

loc_data = pd.read_csv("../data/loc_brightkite.csv")

loc = loc_data["locid"].tolist()
loc = set(loc)

print(len(loc))