import string
def sort_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    text = text.translate
    text = text
    # Розділяємо рядок на слова та створюємо множину для унікальних слів
    words = text.split()
    unique_words = set(words)
    # Сортуємо унікальні слова
    sorted_words = sorted(unique_words)
    return sorted_words
# Користувач вводить текст
input_text = str(input("Введіть текст: "))
result = sort_words(input_text)
print(result)
