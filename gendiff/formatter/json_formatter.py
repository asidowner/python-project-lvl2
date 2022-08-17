import json


def get_formatted_data(diff_list: list):
    return json.dumps(diff_list, check_circular=True, sort_keys=True)
