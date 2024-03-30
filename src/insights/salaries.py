from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:  # type: ignore
            salary = job.get("max_salary")  # type: ignore
            if salary.isdigit():  # type: ignore
                salary = int(salary)  # type: ignore
                max_salary = max(max_salary, salary)
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for job in self.jobs_list:  # type: ignore
            salary = job.get("min_salary")  # type: ignore
            if salary.isdigit():  # type: ignore
                salary = int(salary)  # type: ignore
                min_salary = min(min_salary, salary)
        return min_salary  # type: ignore

    def matches_salary_range(
            self, job: Dict,  # type: ignore
            salary: Union[int, str]) -> bool:  # type: ignore
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("Min and max salary must be present in job")

        if not (
            str(job["min_salary"]).isdigit() and  # type: ignore
            str(job["max_salary"]).isdigit()  # type: ignore
        ):
            raise ValueError("Min and max salary must be integers")

        min_salary = int(job["min_salary"])  # type: ignore
        max_salary = int(job["max_salary"])  # type: ignore

        if min_salary > max_salary:
            raise ValueError("Min salary can't be greater than max salary")

        if not (
            isinstance(salary, int)
            or (isinstance(salary, str) and salary.isdigit())  # type: ignore
        ):
            raise ValueError(
                "Salary must be an integer or a string representing a number"
            )

        salary = int(salary)

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
