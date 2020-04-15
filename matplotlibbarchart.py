import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
# plt.xkcd()  # comic sytle for non serious style

data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])


# print(languages)
# print(popularity)

languages.reverse()
popularity.reverse()

# barhorizontal
plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("No. of People who use")

# plt.legend()
# plt.xticks(ticks=x_indexes, labels=ages_x)
# plt.grid(True)
plt.tight_layout()

# plt.savefig("plot.png")
plt.show()
