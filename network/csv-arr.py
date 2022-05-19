import csv
import torch
import pandas as pd

targets = []
with open(r"C:\Users\Dell\Desktop\geometric_parameters.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        targets.append(row)


# targets = torch.tensor(targets, dtype=torch.float32)
# print(targets[0])


def load_csv(path):
    data_read = pd.read_csv(path)
    list = data_read.values.tolist()
    data = torch.tensor(list)
    return data

# targets = load_csv(r"C:\Users\Dell\Desktop\geometric_parameters.csv")
# print(targets[0])
