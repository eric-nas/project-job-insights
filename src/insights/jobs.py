from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path) as archive:
            reader = csv.DictReader(archive)

            for row in reader:
                self.jobs_list.append(row)

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for jobs in self.jobs_list:
            job_types.add(jobs['job_type'])
        return list(job_types)



    def filter_by_multiple_criteria(
            self, jobs: List[Dict], criteria: Dict) -> List[dict]:
        filter_jobs = list()
        for job in jobs:
            if job['industry'] == criteria['industry'] or job['job_type'] == criteria['job_type']:
                filter_jobs.append(job)
        return filter_jobs
