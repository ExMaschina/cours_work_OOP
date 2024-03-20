from src.api import ApiHH
from src.vacancy import Vacancy


api1 = (ApiHH())
api1.get_vacancies("Водитель")

vacancies_list = Vacancy.cast_to_object_list(api1.vacancies)
print(vacancies_list)
