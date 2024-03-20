
class Vacancy:

    def __init__(self, id, name, alternate_url, salary, responsibility):
        self.id = id
        self.name = name
        self.alternate_url = alternate_url
        self.salary = salary
        self.responsibility = responsibility
        #self.salary_to = salary_to
        # self.validate_data()

    # def validate_data(self):
    #     if not self.salary_from:
    #         self.salary_from = 0
    #     if not self.salary_to:
    #         self.salary_to = 0

    @classmethod
    def cast_to_object_list(cls, a_list):
        '''Преобразование набора данных из JSON в список объектов'''
        current_list = []
        for item in a_list:
            current_list.append(cls(item['id'], item['name'], item['alternate_url'], item['salary'], item['responsibility']))
        return current_list

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.name}, {self.alternate_url}, {self.salary}, {self.responsibility})'
