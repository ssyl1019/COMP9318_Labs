## import modules here
import numpy as np
from sklearn.cluster import AgglomerativeClustering
################# Question 1 #################

def hc(data, k):# do not change the heading of the function
    # pass # Replace this line with your implementation...
    clustering = AgglomerativeClustering(n_clusters=k,linkage='complete').fit(data)
    return clustering.labels_