from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:  # type: ignore
        return list(
            set(row["industry"]
                for row in self.jobs_list  # type: ignore
                if row.get("industry")  # type: ignore
                )
            )  # type: ignore
        # unique_industries = []
        # for row in self.jobs_list:
        #     industry = row.get("industry")
        #     if industry not in unique_industries:
        #         unique_industries.append(industry)
        # return list(unique_industries)
