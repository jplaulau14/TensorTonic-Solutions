def baseline_predict(ratings_matrix: list, target_pairs: list) -> list:
    def bias(values, mu):
        observed = [x for x in values if x != 0]
        return sum(observed) / len(observed) - mu if observed else 0.0

    observed = [x for row in ratings_matrix for x in row if x != 0]
    mu = sum(observed) / len(observed)
    user_bias = [bias(row, mu) for row in ratings_matrix]
    item_bias = [bias(col, mu) for col in zip(*ratings_matrix)]
    return [mu + user_bias[u] + item_bias[i] for u, i in target_pairs]