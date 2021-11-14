import numpy as np

predictions = np.array([1, 1, 1])
labels = np.array([1, 2, 3])

error = (1 / 3) * np.sum(np.square(predictions - labels))
print(error)



