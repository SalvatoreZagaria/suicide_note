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
    ]
]
