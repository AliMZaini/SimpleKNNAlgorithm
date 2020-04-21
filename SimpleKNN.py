import pandas


def get_data_frame(url):
    return pandas.read_csv(url)


def distance(a, b):
    distance_square = 0
    for a_feature, b_feature in zip(a, b):
        distance_square += (a_feature - b_feature) ** 2
    return distance_square ** 0.5


def mode(data):
    return max(set(data), key=data.count)


def is_smaller_find(find, closest_rows):
    classifications = closest_rows[0]
    distances = closest_rows[1]
    # Check for Nones before finding rows to replace
    for classification in classifications:
        if classification is None:
            return classifications.index(classification)

    smallest_distance_index = distances.index(max(distances))
    if find < distances[smallest_distance_index]:
        return smallest_distance_index


def predict(features, df):
    # [classification, distance]
    closest_rows = [[None, None, None, None, None], [None, None, None, None, None]]  # k = 5

    for row in df.values:
        row_classification = row[0]
        row_distance = distance(features, row[1::])

        replace_index = is_smaller_find(row_distance, closest_rows)
        if replace_index is not None:
            closest_rows[0][replace_index] = row_classification
            closest_rows[1][replace_index] = row_distance

    return mode(closest_rows[0])


print(predict([30, 100], get_data_frame("weight-height.csv")))
