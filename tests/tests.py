from utils.utils import load_data,get_state,all_data


def test_load_data():
 assert len(load_data("test_json.json")) == 2


def test_get_state(test_data):
 assert get_state(load_data("test_json.json")) == [test_data[0]]


def test_all_data():
 assert all_data(get_state(load_data("operations.json"))) == ['08.12.2019 Открытие вклада\n'
                                                              'Anonymous        -> Счет ****************5907\n'
                                                              '41096.24 USD\n',
                                                              '07.12.2019 Перевод организации\n'
                                                              'Visa Classic 2842 8*********9012 -> Счет ****************3655\n'
                                                              '48150.39 USD\n',
                                                              '19.11.2019 Перевод организации\n'
                                                              'Maestro 7810 8*********5568 -> Счет ****************2869\n'
                                                              '30153.72 руб.\n',
                                                              '13.11.2019 Перевод со счета на счет\n'
                                                              'Счет 3861 1*********5566 -> Счет ****************8125\n'
                                                              '62814.53 руб.\n',
                                                              '05.11.2019 Открытие вклада\n'
                                                              'Anonymous        -> Счет ****************8381\n'
                                                              '21344.35 руб.\n']