from transliterate import translit


def transliterate_to_slug(text: str) -> str:
    return translit(text, language_code='ru', reversed=True).lower().replace(" ", "-")
