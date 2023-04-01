import json
from datetime import datetime


def load_data(raw_data):
    with open("operations.json") as f:
        raw_data = json.load(f)
        return raw_data


def get_state(dates):
    executed_operations = []
    for state in dates:
        if state.get("state"):
            if state["state"] == "EXECUTED":
                executed_operations.append(state)
    return executed_operations

# def printed_operations():
