import csv
import torch

data = []
s11 = []
parameters = []
with open(r"C:\Users\Dell\Desktop\s11.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        s11.append(row)

targets = torch.tensor(s11, dtype=torch.float32)
print(s11)
