import json


def load_data(filename):
    '''Загрузка файлов из json'''
    with open(filename) as f:
        raw_data = json.load(f)
        return raw_data


def get_state(dates):
    '''Сортировка только по исполненным операциям'''
    executed_operations = []
    for state in dates:
        if state.get("state"):
            if state["state"] == "EXECUTED":
                executed_operations.append(state)
    return executed_operations


def all_data(executed_data):
    '''Создаю список, в который помещаю все отредактированные объекты'''
    list_of_data = []
    sorted_operations = sorted(executed_data, key=lambda i: i['date'], reverse=True)
    first_five = sorted_operations[0:5]
    for i in first_five:
        sum_of_operation = (i['operationAmount']['amount'])
        currency_of_operation = (i['operationAmount']['currency']['name'])
        date = i.get('date')
        formated_date = date.replace('-', '.')
        sender = str([i.get('from')]).replace('None', 'Anonymous')
        sender = sender.replace('[', '')
        sender = sender.replace("]", '')
        sender = sender.replace("'", '')
        card_letters = sender.split()
        card_letters.pop()
        formated_card_letters = " ".join(card_letters)
        if formated_card_letters == "":
            formated_card_letters = 'Anonymous'
        card_number = sender.split()[-1]
        if card_number == "Anonymous":
            card_number = ''
        recipient = i.get('to')
        recipient_name = recipient.split()
        recipient_name.pop()
        formated_recipient_name = " ".join(recipient_name)
        recipient_number = recipient.split()[-1]
        private_recipient_number = '*' * len(recipient_number[:-4]) + recipient_number[-4:]
        split_number = card_number[0:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:16]
        private_number = split_number[:6] + (len(split_number[6:-4]) * '*') + split_number[-4:]
        list_of_data.append(f"{formated_date[8:10]}.{formated_date[5:7]}.{formated_date[0:4]} {i.get('description')}\n{formated_card_letters} {private_number} -> {formated_recipient_name} {private_recipient_number}\n{sum_of_operation} {currency_of_operation}\n")
    return list_of_data