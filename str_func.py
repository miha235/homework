def to_uppercase2(input_string):
    """
        Преобразует строку в заглавные буквы.

        Args:
            s (str): Входная строка.

        Returns:
            str: Строка, преобразованная в заглавные буквы.
    """
    return input_string.upper()


def capitalize_words(sentence):
    """
    Capitalizes the first letter of each word in a sentence.

    :param sentence: The input sentence.
    :return: The modified sentence with the first letter of each word capitalized.
    """
    return ' '.join(word.capitalize() for word in sentence.split())
