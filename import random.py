import random
import os

def main():
    # Выводим текущую рабочую директорию и текстовые файлы
    current_dir = os.getcwd()
    print(f"Текущая папка: {current_dir}")
    print("Файлы в текущей папке:")
    
    text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    for file in text_files:
        print(f"  - {file}")
    
    # Запрашиваем имя файла у пользователя
    file_name = input('Введите имя файла: ')
    
    # Читаем файл с обработкой ошибок
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text_content = file.read()
        print(f"Файл '{file_name}' успешно прочитан!")
        
    except FileNotFoundError:
        print(f"ОШИБКА: Файл '{file_name}' не найден в текущей папке!")
        print("Возможные решения:")
        print("1. Переместите файл в папку:", current_dir)
        print("2. Укажите полный путь к файлу")
        return
    
    # Строим цепь Маркова
    words = text_content.split()
    markov_chain = build_markov_chain(words)
    
    # Находим слова с заглавной буквы для стартовых слов
    capitalized_words = get_capitalized_words(words)
    
    if not capitalized_words:
        print("В тексте нет слов с заглавной буквы для начала генерации!")
        return
    
    # Генерируем текст
    start_word = random.choice(capitalized_words)
    try:
        length = int(input('Введите желаемое количество слов в тексте: '))
    except ValueError:
        print("Ошибка: введите целое число!")
        return
    
    generated_text = generate_text(markov_chain, start_word, length)
    print(' '.join(generated_text))

def build_markov_chain(words):
    """Строит цепь Маркова из списка слов"""
    chain = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        if current_word not in chain:
            chain[current_word] = []
        chain[current_word].append(next_word)
    
    return chain

def get_capitalized_words(words):
    """Возвращает список слов, начинающихся с заглавной буквы"""
    return [word for word in words if word and word[0].isupper()]

def generate_text(chain, start_word, length):
    """Генерирует текст на основе цепи Маркова"""
    result = [start_word]
    current_word = start_word
    
    for _ in range(length - 1):
        if current_word in chain and chain[current_word]:
            next_word = random.choice(chain[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            print("Цепочка оборвалась на слове:", current_word)
            break
    
    return result

if __name__ == "__main__":
    main()