"""
        Эта программа будет транслировать язык псевдокода в C или Python. В процессе транслита будет проверяться
    правильность написанных выражений, а также, если встретится ошибка, выводится строчка и место, в которой
    она была замечена. Более полная информация находится на сайте https://github.com/MiniGerkules/Pseudocode.git
"""

import Lexer


def main():
    """Точка входа в программу"""
    lexer = Lexer.Lexer(r'testCode.txt')
    lexer.lexical_analysis()


if __name__ == "__main__":
    main()