def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if samples==[]:
        return []
    unique_samples=set(samples)

    return sorted([(elem, samples.count(elem)/len(samples) ) for elem in unique_samples ])

    