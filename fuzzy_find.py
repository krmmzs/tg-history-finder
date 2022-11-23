#!/usr/bin/env python3

# python fuzzy find from csv

import sys
import pandas as pd
from thefuzz import fuzz


rank = dict()


def fuzzy_find(csv_file, msg):
    df = pd.read_csv(csv_file)
    global rank
    for (index, row) in df.iterrows():
        msg_content = row["msg_content"]
        value = fuzz.partial_ratio(msg, msg_content)
        if value == 0:
            continue
        item = tuple(row)
        rank[item] = value

    rank = sorted(rank.items(), key=lambda x: x[1], reverse=True)
    for item in rank:
        print(item[0])


if __name__ == "__main__":
    fuzzy_find(sys.argv[1], sys.argv[2])
