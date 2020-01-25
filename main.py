import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("suicide_rates.csv")
data = data[
    [
        "country",
        "year",
        "sex",
        "age",
        "suicides_no",
        "population",
        "suicides/100k pop",
        "gdp_for_year ($)",
        "gdp_per_capita ($)",
    ]
]


suicides_italy = data.loc[data["country"] == "Sweden"]

per_year = {}
for year, n in suicides_italy.groupby("year"):
    per_year[year] = n["suicides_no"].sum()
sa = pd.Series(per_year)

sa.plot(kind="bar")
plt.show()
