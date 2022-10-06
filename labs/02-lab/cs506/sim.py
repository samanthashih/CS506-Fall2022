from queue import Empty


def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if len(x) < 2 or len(y) < 2:
        raise ValueError()
    return abs(x[1]-x[0]) +  abs(y[1]-y[0]) 

def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersection
    return intersection // union

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
