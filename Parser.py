import typing
import Token
import TokenTypes


class Parser:
    """Класс, описывающий статический анализатор кода"""
    def __init__(self, tokens_list: tuple[Token.Token]):
        self.tokens_list = tokens_list
        self.index = 0
        self.scope: dict[str, int] = {}

    def match(self, expected: tuple[TokenTypes.TokenType]) -> typing.Optional[Token.Token]:
        """
            Метод, проверяющий на соответствие тип текущего токена и хотя бы одного из ожидаемых. Если
            тип текущего токена содержится в списке ожидаемых, возвращаем текущий токен, иначе -- None
        """
        if self.index < len(self.tokens_list):
            current = self.tokens_list[self.index]
            if current in expected:
                self.index += 1
                return current

        return None

    def require(self, expected: tuple[TokenTypes.TokenType]) -> Token.Token:
        """
            Метод, производящий запрос к списку токенов на соответствие типа текущего токена и одного
            из ожидаемых типов
        """
        returned = self.match(expected)
        if returned is None:
            raise ValueError(f'Ожидалось {" ".join(str(x) for x in expected)}, встречено '
                             f'{self.tokens_list[self.index]}')

        return returned
