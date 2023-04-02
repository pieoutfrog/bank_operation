from utils import utils

all_data = utils.load_data("operations.json")
executed_data = utils.get_state(all_data)
final = utils.all_data(executed_data)

'''Запуск циклов по импортированным функциям'''

for i in final:
    print(i)
