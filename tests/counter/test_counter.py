from src.pre_built.counter import count_ocurrences


def test_counter():
    file = "data/jobs.csv"
    assert count_ocurrences(file, "Python") == 1639
    assert count_ocurrences(file, "JavaScript") == 122
