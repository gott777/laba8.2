def check_query(query):
    elements = query.split(', ', 1)  # Разделяем только по первой запятой и пробеле
    if len(elements) > 1:
        return elements[1]
    else:
        return 'Некорректный запрос'

# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)
