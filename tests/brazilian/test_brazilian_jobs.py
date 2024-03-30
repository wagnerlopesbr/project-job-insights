from src.pre_built.brazilian_jobs import read_brazilian_file  # type: ignore


def test_brazilian_jobs():
    br_jobs_path = "tests/mocks/brazilians_jobs.csv"
    br_jobs = read_brazilian_file(br_jobs_path)  # type: ignore

    # verify that the function returns a list of dictionaries
    assert isinstance(br_jobs, list)  # type: ignore

    # verify that the list contains dictionaries
    assert all(isinstance(job, dict) for job in br_jobs)  # type: ignore

    # verify that the dictionaries have the expected keys
    expected_keys = {"title", "salary", "type"}
    assert all(
        set(job.keys()) == expected_keys for job in br_jobs)  # type: ignore

    # verify that the dictionaries still have the expected keys
    translation = {"title": "Maquinista", "salary": "2000", "type": "trainee"}
    assert br_jobs[0] == translation
