import requests
import json


class HH:

    def __init__(self):
        self.vacancies = []

    def get_vacancy(self, job_name):
        response = requests.get(f'https://api.hh.ru/vacancies?per_page=100&page=0&text={job_name}&search_field=name')
        body_dict = response.json()
        for item in body_dict['items']:
            self.vacancies.append({
                'id': item['id'],
                'name': item['name'],
                'salary': item['salary'],
                'alternate_url': item['alternate_url'],
                'responsibility': item['snippet']['responsibility']
            })
        for item in self.vacancies:



        # with open("body_dic1t", "w", encoding="utf-8") as file:
        #     json.dump(body_dict, file)
        #
        #
        #
        # with open('response_data.json', 'w') as file:
        #     json.dump(response_data, file)


class Vacancy:

    def __init__(self, id, name, salary, alternate_url, responsibility):
        self.id = id
        self.name = name
        self.salary = salary
        self.alternate_url = alternate_url
        self.responsibility = responsibility


job_name = input('Вакансия? ')
api1 = HH()
api1.get_vacancy(job_name)
