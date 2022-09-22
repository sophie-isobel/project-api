import similar 

example = [
    ("User1", "FilmA"), 
    ("User1", "FilmB"), 
    ("User2", "FilmC"), 
    ("User2", "FilmD")#,
#    ("User3", "FilmE")
]


def test_sampledataset():
    assert len(example) == 4 #5
    #assert ("User3", "FilmE") in example

def test_vectorize():
    assert [{"FilmA", "FilmB"}, {"FilmC", "FilmD"}] == similar.vectorize(example)

def test_most_similar():
    assert (1.0, {"FilmA", "FilmB"}) == similar.most_similar({"FilmA", "FilmB"}, example)
    assert (0.5, {"FilmA", "FilmB"}) == similar.most_similar({"FilmA"}, example)
    assert (0.5, {"FilmC", "FilmD"}) == similar.most_similar({"FilmC"}, example)

def test_overlap():
    assert 1 == similar.overlap({"FilmA", "FilmB"}, {"FilmA", "FilmB"})
    assert 0 == similar.overlap({"FilmA", "FilmB"}, {"FilmC", "FilmD"})