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
        return set(row["job_type"] for row in self.jobs_list)  # type: ignore
        # just to show to myself that i know other ways to do it:
        # unique_job_types = []
        # for row in self.jobs_list:
        #     if row["job_type"] not in unique_job_types:
        #         unique_job_types.append(row["job_type"])
        # return unique_job_types

    def filter_by_multiple_criteria(self, list: List[Dict], filter_criteria: dict) -> List[dict]:  # type: ignore
        return [
            row for row in list if row["industry"] == filter_criteria["industry"] and row["job_type"] == filter_criteria["job_type"]   # type: ignore
        ]
        # just to show to myself that i know other ways to do it:
        # filtered_list = []
        # for row in list:  # type: ignore
        #     if row["industry"] == filter_criteria["industry"] and row["job_type"] == filter_criteria["job_type"]:
        #         filtered_list.append(row)  # type: ignore
        # return filtered_list  # type: ignore


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
