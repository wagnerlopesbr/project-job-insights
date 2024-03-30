from typing import List, Dict
import csv
import json


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()  # type: ignore

    def read(self, path: str) -> List[Dict]:  # type: ignore
        with open(path, mode="r", encoding="utf-8", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            self.jobs_list = list(reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:  # type: ignore
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:  # type: ignore
        pass


def format_to_json(data: List[Dict]) -> str:  # type: ignore
    if not data:
        raise ValueError("No data to process")

    return json.dumps(data, indent=2)


def format_to_csv(data: List[Dict], path: str) -> None:  # type: ignore
    if not data:
        raise ValueError("No data to process")

    headers = list(data[0].keys())  # type: ignore

    with open(path, mode="w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)  # type: ignore
        writer.writeheader()
        for row in data:  # type: ignore
            writer.writerow(row)  # type: ignore


if __name__ == "__main__":
    jobs = ProcessJobs()
    jobs.read("data/req02jobs.csv")  # type: ignore
    print(format_to_json(jobs.jobs_list))  # type: ignore
    format_to_csv(jobs.jobs_list, "data/jobs_output.csv")  # type: ignore
