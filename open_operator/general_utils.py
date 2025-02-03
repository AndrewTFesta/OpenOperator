"""
@title

@description

"""
import json
import time
from copy import copy
from datetime import datetime
from zoneinfo import ZoneInfo


def filter_dict(data, pass_keys):
    if isinstance(data, str):
        data = json.loads(data)

    filtered_data = {
        field_name: field_val
        for field_name, field_val in data.items()
        if field_name in pass_keys
    }
    return filtered_data

def time_tag(tz_str='GMT'):
    time_zone = ZoneInfo(tz_str)
    curr_time = time.time()
    date_time = datetime.fromtimestamp(curr_time, tz=time_zone)
    time_str = date_time.strftime("%Y-%m-%d-%H-%M-%S")
    return time_str

def extract_field(data, field_name):
    data = copy(data)
    for each_root_key, each_root_val in data.items():
        if isinstance(each_root_val, list):
            replaced_vals = []
            for each_val in each_root_val:
                each_val = extract_field(each_val, field_name)
                replaced_vals.append(each_val)
            data[each_root_key] = replaced_vals
        elif isinstance(each_root_val, dict) and field_name in each_root_val:
            data[each_root_key] = each_root_val[field_name]
        elif isinstance(each_root_val, dict):
            data[each_root_key] = extract_field(each_root_val, field_name)
    return data

def run_with_retry(command_func, num_attempts=5, raise_error=False):
    result_info = None
    failures = []
    for _ in range(num_attempts):
        try:
            result_info = command_func()
            break
        except Exception as e:
            print(e)
            failures.append(e)
    else:
        failure_message = f'Failed to execute command `{command_func.__name__}` after {num_attempts} attempts'
        if raise_error:
            raise RuntimeError(failure_message)
        else:
            print(failure_message)
    return result_info