import torch
import numpy as np

def compute_average_feature_vector(features, labels):
    unique_labels = torch.unique(labels)
    average_vectors = {}
    for label in unique_labels:
        category_features = features[labels == label]
        average_vector = torch.mean(category_features, dim=0)
        average_vectors[label.item()] = average_vector
    return average_vectors

# Example usage:
average_vectors = compute_average_feature_vector(features, labels)
print(average_vectors)
