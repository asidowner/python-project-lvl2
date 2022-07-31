import json


def formatter(diff_list: list):
    return json.dumps(diff_list, check_circular=True, sort_keys=True)
