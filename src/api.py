import requests


class ApiHH:

    def __init__(self):
        self.vacancies = []

    def get_vacancies(self, job_name):
        '''Получение вакансии из сайта и приведение её в удобный формат'''
        response = requests.get(f'https://api.hh.ru/vacancies?per_page=100')  # &text={job_name}search_field=name') #получаем страницу
        response_data = response.json() # оборачиваем в json
        #print(response_data)
        for item in response_data['items']:   # цикл по json [items]
            self.vacancies.append({'id': item['id'],
                                   'name': item['name'],
                                   'alternate_url': item['alternate_url'],
                                   'salary': item['salary'],
                                   'responsibility': item['snippet']['responsibility']})


# api1 = APIHH()
# api1.get_vacancies("Водитель")
# print(api1.vacancies)
