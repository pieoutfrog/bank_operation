import utils

all_data = utils.load_data("operations.json")
executed_data = utils.get_state(all_data)

sorted_operations = sorted(executed_data, key=lambda i: i['date'], reverse=True)
first_five = sorted_operations[0:5]
print(first_five)

for i in first_five:
    date = i.get('date')
    formated_date = date.replace('-', '.')
    print(f"""{formated_date[8:10]}.{formated_date[5:7]}.{formated_date[0:4]} {i.get('description')}
{i.get('from')} -> {i.get('to')}""", '\n')


# for values in first_five.items():
#     print(values)
