import torch


def RSE(r, g):
    a = torch.sqrt(torch.sum((r - g) ** 2)) / torch.sqrt(torch.sum(r ** 2))
    return a


a = torch.tensor([5.1, 6, 4.8, 15, 2, 0.5, 2, 1, 3, 0.5])
b = torch.tensor([4.8525, 5.9507, 4.6706, 15.7001, 1.9826, 0.3764, 2.0246, 0.9412,
                  2.8909, 0.4567])

c = RSE(a, b)
print(c)
