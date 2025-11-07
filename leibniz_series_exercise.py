def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        leibniz_series.append(((-1) ** i) / (2 * i + 1))
    return 4 * sum(leibniz_series)
