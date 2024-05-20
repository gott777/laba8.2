# ЛР8.2 Строки и форматирование

## Задача 1
Допишите код функции penult_word() так, чтобы она возвращала третье с конца слово из любой фразы, переданной в аргументе.

quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = ...
    return ...

#Вызовы функции готовы к работе, не изменяйте их!

#Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

#То же, но с аргументом quote_2.
print(penult_word(quote_2))

#То же с аргументом quote_3.
print(penult_word(quote_3))

## Задача 2

В коде приготовлен список запросов к Анфисе queries. Необходимо определить, какие из них адресованы Анфисе, а какие — другим людям.

Напишите функцию check_query(), которая принимает запрос как параметр, анализирует его и возвращает одну из двух строк:

строку ‘запрос к Анфисе’, если запрос начинается со слова ‘Анфиса’,
или строку ‘запрос к кому-то ещё’, если запрос начинается с любого другого слова.
Код вызова функции и вывода результатов на экран уже написан в теле программы.

def check_query(query):
#Допишите код тела функции
    elements  = ...
    if ...
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'

#Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

#Напечатаем результат.
#Переберём список вопросов в цикле
for q in queries:
    # Каждый из вопросов передадим аргументом
    # в функцию check_query()
    result = check_query(q)
    # И для каждого вызова напечатаем вопрос и, через дефис - вердикт программы
    print(q, '-', result)
    
## Задача 3

Анфиса научилась отличать своё имя от других. Теперь надо научить её извлекать суть запроса.

Перепишите функцию check_query() так, чтобы при любом запросе она «отрезала» от строки имя и возвращала только запрос, без имени.

Например, если Анфисе пришёл запрос «Толя, что это за ерунда?» — функция check_query() должна вернуть строку ‘что это за ерунда?’.

def check_query(query):
    elements  = query.split(', ')
    # Напишите код функции


#Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)
    
## Задача 4

Упростим и улучшим код Анфисы.

При выводе перечня друзей или городов Анфиса применяет циклы, объединяя ключи или значения словаря в одну строку, через пробел.

Но теперь в вашем арсенале есть метод join(), он решает ту же задачу: создаёт строку из элементов последовательности.

Уберите из кода циклы, в которых создаётся перечень друзей и перечень городов, а эти перечни создайте с помощью метода join(). Имена друзей и названия городов должны быть разделены запятыми и пробелом.

#Анфиса должна вернуть примерно такие строки:
#В ответ на запрос 'Кто все мои друзья?'-
Твои друзья: Серёга, Соня, Миша, ...

#В ответ на запрос 'Где все мои друзья?' -
Твои друзья в городах: Омск, Москва, Челябинск, ... 
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        # Из словаря DATABASE создайте строку с помощью join();
        # имена друзей разделите запятой и пробелом.
        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
        friends_string = ''

        # Этот цикл больше не понадобится, удалите его
        for friend in DATABASE:
            friends_string += friend + ' '

        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        # Из сета unique_cities создайте строку с помощью join();
        # названия городов разделите запятой и пробелом.
        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
        cities_string = ''

        # Этот цикл больше не понадобится, удалите его
        for city in unique_cities:
            cities_string += city + ' '

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))
