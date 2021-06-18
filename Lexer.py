import os
import re


class Lexer:
    """Класс, описывающий лексический анализатор кода"""

    def __init__(self, path: str):
        """Конструктор класса Lexer. Задает путь до файла с кодом, начальную позицию
        в этом файле и список прочтенных токенов"""
        self.path = path
        self.position = 0
        self.tokens_list = []

        # Регулярка, задающая возможное выражение
        self.expression = fr'{self.variable} +(=) +{self.number} +(+|-|*|/|%) +{self.number}'
        # Регулярка, задающая функцию вывода

        # Ниже навороты, которые реализую потом
        """
        # Регулярка, задающая первую строку условной конструкции
        self.if_construct = fr'ЕСЛИ +{self.variable} +(<|>|<=|>=|==|!=) +{self.number} +ТО *\n'
        """

    def lexical_analysis(self) -> (None, list):
        """Метод, осуществляющий лексический анализ кода из файла"""
        if not os.path.isfile(self.path):
            print('Не существует файла по указанному пути!')
            return None

        with open(self.path, 'r') as file:
            for line in file:
                for_work = line.strip()
                # Дальнейшая работа со строкой
