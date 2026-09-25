def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    def mean(values):
        observed = [x for x in values if x != 0]
        return sum(observed) / len(observed) if observed else 0.0

    if mode == "user":
        means = [mean(row) for row in ratings_matrix]
        return [[x if x != 0 else means[i] for x in row] for i, row in enumerate(ratings_matrix)]
    means = [mean(col) for col in zip(*ratings_matrix)]
    return [[x if x != 0 else means[j] for j, x in enumerate(row)] for row in ratings_matrix]