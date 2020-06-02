import numpy as np
from heapq import heappush, heappushpop
def hc(data, k):
    y = dis_similarity(data)
    n = int(np.ceil(np.sqrt(y.shape[0] * 2)))
    out = nn_chain(y, n)
    children = out[:, :2].astype(np.int, copy=False)
    return list(hc_cut(k, children,data.shape[0]))
 
def hc_cut(n_clusters, children, n_leaves):
    nodes = [-(max(children[-1]) + 1)]
    for _ in range(n_clusters - 1):
        these_children = children[-nodes[0] - n_leaves]
        heappush(nodes, -these_children[0])
        heappushpop(nodes, -these_children[1])
    label = np.zeros(n_leaves, dtype=np.intp)
    for i, node in enumerate(nodes):
        label[hc_get_descendent(-node, children, n_leaves)] = i
    return label
 
def dis_similarity(data,p = 2):
    dis = []
    for i in range(data.shape[0]):
        for j in range(i+1,data.shape[0]):
            sub = np.subtract(data[i],data[j])
            tmp = 0
            for s in sub :
                tmp += abs(s)**p
            tmp = tmp**(1/p)
            dis.append(tmp)
    return np.array(dis)
 
def hc_get_descendent(node, children, n_leaves):
    ind = [node]
    if node < n_leaves:
        return ind
    descendent = []
    i, n_indices = 1,1
    while n_indices:
        i = ind.pop()
        if i < n_leaves:
            descendent.append(i)
            n_indices -= 1
        else:
            ind.extend(children[i - n_leaves])
            n_indices += 1
    return descendent
 
def condensed_index(n, i, j):
    if i < j:
        return n * i - (i * (i + 1) // 2) + (j - i - 1)
    elif i > j:
        return n * j - (j * (j + 1) // 2) + (i - j - 1)
    else:
        return 0
 
class LinkageUnionFind():
 
    def __init__(self,n=0):
        self.parent = np.arange(2 * n - 1, dtype=np.intc)
        self.next_label = n
        self.size = np.ones(2 * n - 1, dtype=np.intc)
 
    def merge(self,x, y):
        self.parent[x] = self.next_label
        self.parent[y] = self.next_label
        size = self.size[x] + self.size[y]
        self.size[self.next_label] = size
        self.next_label += 1
        return size
 
    def find(self,x):
        p = x
        while self.parent[x] != x:
            x = self.parent[x]
        while self.parent[p] != x:
            p, self.parent[p] = self.parent[p], x
        return x
 
def label(Z, n):
    uf = LinkageUnionFind(n)
    for i in range(n - 1):
        x, y = int(Z[i, 0]), int(Z[i, 1])
        x_root, y_root = uf.find(x), uf.find(y)
        if x_root < y_root:
            Z[i, 0], Z[i, 1] = x_root, y_root
        else:
            Z[i, 0], Z[i, 1] = y_root, x_root
        Z[i, 3] = uf.merge(x_root, y_root)
 
def nn_chain(dists, n):
    Z_arr = np.empty((n - 1, 4))
    Z = Z_arr
 
    D = dists.copy()  # Distances between clusters.
    size = np.ones(n, dtype=np.intc)  # Sizes of clusters.
 
    # Variables to store neighbors chain.
    cluster_chain = np.ndarray(n, dtype=np.intc)
    chain_length = 0
 
    for k in range(n - 1):
        if chain_length == 0:
            chain_length = 1
            for i in range(n):
                if size[i] > 0:
                    cluster_chain[0] = i
                    break
 
        # Go through chain of neighbors until two mutual neighbors are found.
        while True:
            x = cluster_chain[chain_length - 1]
            if chain_length > 1:
                y = cluster_chain[chain_length - 2]
                current_min = D[condensed_index(n, x, y)]
            else:
                # current_min = NPY_INFINITYF
                current_min = np.inf
            for i in range(n):
                if size[i] == 0 or x == i:
                    continue
                dist = D[condensed_index(n, x, i)]
                if dist < current_min:
                    current_min = dist
                    y = i
            if chain_length > 1 and y == cluster_chain[chain_length - 2]:
                break
            cluster_chain[chain_length] = y
            chain_length += 1
 
        # Merge clusters x and y and pop them from stack.
        chain_length -= 2
        # This is a convention used in fastcluster.
        if x > y:
            x, y = y, x
        # get the original numbers of points in clusters x and y
        nx = size[x]
        ny = size[y]
        # Record the new node.
        Z[k, 0] = x
        Z[k, 1] = y
        Z[k, 2] = current_min
        Z[k, 3] = nx + ny
        size[x] = 0  # Cluster x will be dropped.
        size[y] = nx + ny  # Cluster y will be replaced with the new cluster
        # Update the distance matrix.
        for i in range(n):
            ni = size[i]
            if ni == 0 or i == y:
                continue
            D[condensed_index(n, i, y)] = max(D[condensed_index(n, i, x)],D[condensed_index(n, i, y)])
    # Sort Z by cluster distances.
    order = np.argsort(Z_arr[:, 2], kind='mergesort')
    Z_arr = Z_arr[order]
    # Find correct cluster labels inplace.
    label(Z_arr, n)

    return Z_arr
