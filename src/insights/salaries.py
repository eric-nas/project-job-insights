from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        filter_salary = 0
        for job in self.jobs_list:
            if (
                job['max_salary'].isdigit() and
                int(job['max_salary']) > filter_salary
            ):
                filter_salary = int(job['max_salary'])
        return filter_salary

    def get_min_salary(self) -> int:
        filter_salary = 999999999999
        for job in self.jobs_list:
            if (
                job['min_salary'].isdigit() and
                int(job['min_salary']) < filter_salary
            ):
                filter_salary = int(job['min_salary'])
        return filter_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        maximo = job.get('max_salary')
        minimo = job.get('min_salary')

        if maximo is None or minimo is None:
            raise ValueError('Salary_Range não especificado')
        if not (isinstance(maximo, (int, str)) and
                isinstance(minimo, (int, str)) and
                isinstance(salary, (int, str))
                ):
            raise ValueError('Voce não está usando números')
        if minimo > maximo:
            raise ValueError('max_salary deve ser maior que min_salary')
        maximo = int(maximo)
        minimo = int(minimo)
        salary = int(salary)
        return maximo >= salary >= minimo

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_jobs = []
        if (
            salary is None or salary == '' or
            isinstance(salary, (list, dict)) or
            callable(salary)
        ):
            return filtered_jobs

        for job in jobs:
            if (
                isinstance(job.get('min_salary'), (int, str)) and
                isinstance(job.get('max_salary'), (int, str))
            ):
                min_salary = int(job['min_salary'])
                max_salary = int(job['max_salary'])

                if min_salary <= int(salary) <= max_salary:
                    filtered_jobs.append(job)

        return filtered_jobs
