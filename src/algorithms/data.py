from xlrd import open_workbook

class Person(object):
    def __init__(self, name, born_year, death_year, mother, father):
        self.name = name.strip() if name is not None else None
        self.born_year = int(float(born_year)) if born_year is not None else None
        self.death_year = int(float(death_year)) if death_year is not None else None
        self.mother = mother.strip() if mother is not None else None
        self.father = father.strip() if father is not None else None

    def __repr__(self):
        return ("%s\n%s-%s" % (self.name, self.born_year, self.death_year))


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