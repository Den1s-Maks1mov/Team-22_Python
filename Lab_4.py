# Відкриття файлу та зчитування всього вмісту
with open('Lab4_text.txt', 'r', encoding='utf-8') as file:
   string = file.read()

# Підрахунок речень за допомогою розбиття тексту на символи .
def count_sentences(string): 
    sentences = string.split('.')
    return len([s for s in sentences if s.strip()])

# Підрахунок кількості слів
def count_words(string):
    words = string.split()
    return len(words)

# Підрахунок кількості конкретного слова
def count_specific_word(string, word):
    words = string.lower().split()
    return words.count(word.lower())

num_sentences = count_sentences(string)
print(f"Кількість речень: {num_sentences}")
num_words = count_words(string)
print(f"Кількість слів: {num_words}")
word = input("Введіть слово для підрахунку: ")
count = count_specific_word(string, word)
print(f"Кількість слова '{word}': {count}")
