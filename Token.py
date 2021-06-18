import TokenTypes


class Token:
    """Класс, описывающий токен языка"""

    def __init__(self, type_: TokenTypes.TokenType, text: str, position: int):
        """Конструктор класса Token. Инициализирует новый экземпляр типом токена,
        текстом, который содержит токен, и позицией в коде"""
        self.type = type_
        self.text = text
        self.position = position
