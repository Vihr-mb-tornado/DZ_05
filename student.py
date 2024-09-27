import datetime
class Student:
    #- ім'я;
    #- рік народження;
    #- група;
    #- середній бал.
    name = ''
    birth = 2008
    group = "В21958"
    average_score = 0

    def __init__(self, name, birth, group, average_score):
        self.name = name
        self.birth = birth
        self.group = group
        self.average_score = average_score

    def show_stats(self):
        print(self)

    def __str__(self):
        return f' -< {self.name} >- \n' \
            f' Рік народження: {self.birth}\n'\
            f' Група: {self.group}\n'\
            f' Середній бал: {self.average_score}\n'

    def get_age(self):
        return datetime.date.today().year-self.birth