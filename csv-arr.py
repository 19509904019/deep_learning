import csv
import torch

targets = []
with open(r"C:\Users\Dell\Desktop\geometric_parameters.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        targets.append(row)

targets = torch.tensor(targets, dtype=torch.float32)
print(targets[0])