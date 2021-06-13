import re


class Parser:
    def __init__(self, path: str):
        self.path = path
        # Регулярка, задающая условную конструкцию
        self.if_construct = r"ЕСЛИ( {1,}).+\1(<|>|<=|>=|==|!=)\1\d\1ТО"

    def parse(self):
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    for_work = line.strip()

        except FileNotFoundError as error:
            print(error)
