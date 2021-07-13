import os
import re
import Token
import TokenTypes


class Lexer:
    """Класс, описывающий лексический анализатор кода"""

    def __init__(self, path: str):
        """Конструктор класса Lexer. Задает путь до файла с кодом, начальную позицию
        в этом файле, списоки всех возможных и прочтенных токенов"""
        self.code = ''
        self.path = path
        self.position = 0
        self.all_tokens = []
        self.tokens_list = []

        # Определяем все возможные токены в программе
        with open('TokenTypes.py', 'r', encoding='utf-8') as tokens:
            # Вытаскиваем все имена токенов
            tokens_names = re.findall(r'class ([A-Za-z]\w+)\(?.*\)?:', tokens.read())
            tokens_names.remove('TokenType')
            # Добавляем в список всех токенов объект класса с именем token_name, если класс не абстрактный
            for token_name in tokens_names:
                self.all_tokens.append(getattr(TokenTypes, token_name)())

        print(f'Все токены:\n{self.all_tokens}')

        # Регулярка, задающая возможное выражение
        # self.expression = fr'{self.variable} +(=) +{self.number} +(+|-|*|/|%) +{self.number}'
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

        with open(self.path, 'r', encoding='utf-8') as file:
            self.code = file.read()
        while self.next_token():
            print('Процесс идет')
        self.tokens_list = filter(lambda elem: elem.type != TokenTypes.Space, self.tokens_list)
        return self.tokens_list

    def next_token(self) -> bool:
        if self.position == len(self.code):
            return False

        for token in self.all_tokens:
            result = re.match(token.regex, self.code[self.position:])
            if result is not None:
                self.tokens_list.append(Token.Token(token, result.group(), self.position))
                self.position += len(result.group())
                return True

        raise SyntaxError(f'На позиции {self.position} обнаружена ошибка!')
