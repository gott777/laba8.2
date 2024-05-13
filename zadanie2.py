def check_query(query):
    elements = query.split()
    if elements[0].lower() == 'анфиса,':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'

queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '-', result)
