import utils

all_data = utils.load_data("operations.json")
executed_data = utils.get_state(all_data)

sorted_operations = sorted(executed_data, key=lambda i: i['date'], reverse=True)
first_five = sorted_operations[0:5]


def all_data(first_five):
    for i in first_five:
        sum_of_operation = (i['operationAmount']['amount'])
        currency_of_operation = (i['operationAmount']['currency']['name'])
        date = i.get('date')
        sender = str([i.get('from')]).replace('None', 'Anonymous')
        sender = sender.replace('[', '')
        sender = sender.replace("]", '')
        sender = sender.replace("'", '')
        formated_date = date.replace('-', '.')
        for val in sender:
            if val is int:

        if sender is None:
            sender.replace('Отправитель неизвестен')
        descripton = str(i.get('description')).replace("'", "")
        print(f"""{formated_date[8:10]}.{formated_date[5:7]}.{formated_date[0:4]} {i.get('description')}
{sender} -> {i.get('to')}
{sum_of_operation} {currency_of_operation}""", '\n')


all_data(first_five)