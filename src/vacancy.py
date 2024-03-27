class Vacancy:

    def __init__(self, id, name, alternate_url, salary_from, salary_to, responsibility):
        self.id = id
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        # self.validate_salary()
        self.responsibility = responsibility
        # self.validate_data()

    # def validate_salary(self):
    #     if not self.salary:
    #         self.salary = {'from': 0,
    #                        'to': 0
    #                        }


    @classmethod
    def cast_to_object_list(cls, a_list):
        '''Преобразование набора данных из JSON в список объектов'''
        current_list = []
        for item in a_list:
            current_list.append(
                cls(item['id'], item['name'], item['alternate_url'], item['salary'], item['responsibility']))
        return current_list


    def __repr__(self):
        stars = '***' * 60
        return f'\n{self.__class__.__name__} {self.id}\n {self.name}\n {self.alternate_url}\n {self.salary}\n {self.responsibility}\n {stars}\n'

    # def __lt__(self, other):
    #     return self.salary < other.salary

