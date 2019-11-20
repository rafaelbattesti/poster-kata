import src.extract as extract


def test_get_films():
    f = extract.get_films()
    if f is not None:
        assert True
    else:
        assert False
