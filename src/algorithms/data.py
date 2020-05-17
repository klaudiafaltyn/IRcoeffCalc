from xlrd import open_workbook

class Person(object):
    def __init__(self, name, born_year, death_year, mother, father, children):
        self.name = name
        self.born_year = born_year
        self.death_year = death_year
        self.mother = mother
        self.father = father
        self.children=[]
        if children is not None:
            self.children = [i.strip() for i in children.split(",")]



def load_from_xls(people, src):
    wb = open_workbook(src)
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        rows = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(number_of_columns):
                value  = (sheet.cell(row,col).value)
                if len(str(value)) < 2:
                    values.append(None)
                else:
                    values.append(str(value))
            person = Person(*values)
            people.append(person)