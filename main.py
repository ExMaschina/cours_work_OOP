from src.api import ApiHH
from src.vacancy import Vacancy


api1 = (ApiHH())
api1.get_vacancies("Водитель")

vacancies_list = Vacancy.cast_to_object_list(api1.vacancies)
print(vacancies_list)

def user_interaction():
    user_request = input('Введите поисковый запрос: ')
    user_top = int(input('Количество вакансий для вывода в топ N: '))
    filter_words = input('Введите ключевые слова для фильтрации вакансий: ').split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 30000 - 250000


    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
