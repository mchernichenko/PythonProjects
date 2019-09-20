def search4volwes(phrase: str) -> set:
    """Возвращает гласные, найденные в указанной фразе."""
    volwes = set('aeiou')
    return volwes.intersection(set(phrase))


def search2letters(phrase: str, letters: str='aeiou') -> set:
    """Возвращает множетсво букв из 'letters',
    найденных в указанной фразе"""
    return set(letters).intersection(set(phrase))
