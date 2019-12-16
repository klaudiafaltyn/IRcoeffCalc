from xlrd import open_workbook

class Person:
    name: str
    born_year : int
    death_year : int
    mother : str
    father : str
    children : list

class Arm(object):
    def __init__(name, born_year, death_year, mother, father, children):
        self.name = name
        self.born_year = born_year
        self.death_year = death_year
        self.mother = mother
        self.father = father
        self.children = children

    def __str__(self):
        return("Arm object:\n"
               "  Arm_id = {0}\n"
               "  DSPName = {1}\n"
               "  DSPCode = {2}\n"
               "  HubCode = {3}\n"
               "  PinCode = {4} \n"
               "  PPTL = {5}"
               .format(self.name, self.born_year, self.death_year,
                       self.mother, self.father, self.children))



population = []
load_from_excel(population)

wb = open_workbook('Habsburgowie.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Arm(*values)
        items.append(item)

for item in items:
    print (item)
    print("Accessing one single value (eg. DSPName): {0}".format(item.dsp_name))
    print