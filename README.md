# SimpleKNNAlgorithm
A simple implementation of the k-nearest neighbours algorithm in Python.

Works with CSV files that are formatted as such:
* have the classifications in the first column
* columns after the first one will be considered for attributes in that order (explained further in the example below)

# Usage
```
python SimpleKNN.py -d <data_url> -k <k_value> -q <query_features>
```

If a k-value is not provided, 11 is used by default. The query should be a list of values separated by a comma and no spaces.

The query features will be assumed to be in the same order as the data in the provided csv.

e.g.
```
python SimpleKNN.py -d weight-height.csv -k 5 --features 70,170
```

I've included some other sets you can use in the folder "DemoDataSets", although they are not all actually good use cases for this algorithm.

# Sources
weight-height.csv : https://www.kaggle.com/mustafaali96/weight-height/version/1
heart.csv : https://www.kaggle.com/ronitf/heart-disease-uci
london / seattle data : http://insideairbnb.com/get-the-data.html (I have edited the data)
k-nearest neighbors algorithm : https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
