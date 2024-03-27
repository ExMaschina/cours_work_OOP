import os.path
import config
import requests
from src.vacancy import Vacancy

class ApiHH:

    def __init__(self):
        self.vacancies = []

    def get_vacancy(self, job_name):
        '''Получение вакансии из сайта и приведение её в удобный формат'''
        response = requests.get(
            f'https://api.hh.ru/vacancies?per_page=100&page=0&text={job_name}&search_field=name')  # &text={job_name}search_field=name') #получаем страницу
        response_data = response.json()  # оборачиваем в json
        # print(response_data)
        for item in response_data['items']:  # цикл по json [items]
            print(item)
            id = item['id']
            name = item['name']
            alternate_url = item['alternate_url']
            salary = item.get('salary', 0)
            print(salary)
            if salary:
                salary_from = salary.get('from', 0)
                salary_to = salary.get('to', 0)
                if not salary_from:
                    salary_from = 0
                if not salary_to:
                    salary_to = 0
            else:
                salary_from = 0
                salary_to = 0
            responsibility = item['snippet']['responsibility']
            vacancy = Vacancy(
                id = id,
                name = name,
                alternate_url = alternate_url,
                salary_from = salary_from,
                salary_to = salary_to,
                responsibility = responsibility)
            self.vacancies.append(vacancy)


            # self.vacancies.append({'id': item['id'],
            #                        'name': item['name'],
            #                        'alternate_url': item['alternate_url'],
            #                        'salary': item.get('salary', 0),
            #                        'responsibility': item['snippet']['responsibility']})

    def save_json(self, vacancy_json):
        json_file = os.path.join(config.VACANCIES_DATA_PATH, f'Vacancy.json')
        vacancy_list = []
        for item in vacancy_json:
            if item['salary']:
                pass

# api1 = APIHH()
# api1.get_vacancies("Водитель")
# print(api1.vacancies)
