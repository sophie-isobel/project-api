def vectorize(rows: tuple) -> set:
    vectors = {}
    for (id, value) in rows:
        vectors.setdefault(id, set()).add(value)

    return list(vectors.values())

def overlap(u: set, v: set) -> float:
    return len(u & v) / len(u | v)

def most_similar(one: set, many: tuple):
    return max(
        (overlap(one, candidate), candidate) 
        for candidate in vectorize(many)
    )

