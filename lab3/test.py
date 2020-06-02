import numpy as np
import submission as submission

data = np.loadtxt('asset/data.txt', dtype = float)
# print(data)
def dot_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

k = 3
# print(submission.hc(data, k))
lst = submission.hc(data, k)
print(lst)
def compute_error(data, labels, k):
    # print(labels)
    n, d = data.shape
    # print(n,d)
    centers = []
    for i in range(k):
        centers.append([0 for j in range(d)])
    # print(centers)
    for i in range(n):
        centers[labels[i]] = [x + y for x, y in zip(centers[labels[i]], data[i])]
        # print(centers[labels[i]])
    # print(centers)
    error = 0
    for i in range(n):
        error += dot_product(centers[labels[i]], data[i])
    return error 
    
error = compute_error(data, [2, 0, 1, 2, 0], k)
# print(error)