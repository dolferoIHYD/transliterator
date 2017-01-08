# coding: utf-8

import unidecode

def transliteration(word):
    """Транслитератор

        Принимает на вход слово (строку), пробелы заменяет на "_",
        а слова заменяет на кирилицу. Кроме того, возвращает все в нижнем
        регистре. Используется для переработки имен (названий и т.д.) в Slug
    """
    result = unidecode.unidecode(word).lower()
    arr = result.split()
    result = '_'.join(arr)
    return(result)

