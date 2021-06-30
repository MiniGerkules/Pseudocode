import os
import re
import TokenTypes


class Lexer:
    """Класс, описывающий лексический анализатор кода"""

    def __init__(self, path: str):
        """Конструктор класса Lexer. Задает путь до файла с кодом, начальную позицию
        в этом файле, списоки всех возможных и прочтенных токенов"""
        self.path = path
        self.position = 0
        self.all_tokens = []
        self.tokens_list = []

        # Определяем все возможные токены в программе
        with open('TokenTypes.py', 'r') as tokens:
            # Вытаскиваем все имена токенов
            tokens_names = re.findall(r'class ([A-Za-z]\w+)\(?.*\)?:', tokens.read())
            # Добавляем в список всех токенов объект класса с именем token_name, если класс не абстрактный
            for token_name in tokens_names:
                if token_name != 'TokenTypes':
                    self.all_tokens.append(globals()[token_name]())

        print(f'Все токены:\n{self.all_tokens}')

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
                line = line.strip()
                for token in self.all_tokens:
                    # Перебираем все регулярки токенов
                    result = re.search(token.type.return_regex(), line)
