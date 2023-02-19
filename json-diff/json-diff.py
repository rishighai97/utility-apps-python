from deepdiff import DeepDiff
# ["\['metric-id'\]", "\['metric-id2'\]"]
import json
import re

TYPE_CHANGES_KEY = "type_changes"
VALUES_CHANGED_KEY = "values_changed"
DICT_ITEM_ADDED_KEY = "dictionary_item_added"
DICT_ITEM_REMOVED_KEY = "dictionary_item_removed"


def generate_diff(json1, json2, exclude_regex_paths=[]):
    difference = DeepDiff(json1, json2, exclude_regex_paths=exclude_regex_paths)
    return {
        TYPE_CHANGES_KEY: generate_type_changes(difference)
    }


def generate_type_changes(difference):
    if TYPE_CHANGES_KEY in difference.keys():
        result_set = []
        for field in difference[TYPE_CHANGES_KEY]:
            result_set.append({
                "Field Name": field,
                "Old Type": str(difference[TYPE_CHANGES_KEY][field]["old_type"]),
                "New Type": str(difference[TYPE_CHANGES_KEY][field]["new_type"]),
                "Old Value": str(difference[TYPE_CHANGES_KEY][field]["old_value"]),
                "New Value": str(difference[TYPE_CHANGES_KEY][field]["new_value"]),
            })
        return result_set
    else:
        print('TYPE CHANGES key is absent')
        return []


def generate_value_type(difference):
    if VALUES_CHANGED_KEY in difference.keys():
        result_set = []
        for field in difference[VALUES_CHANGED_KEY]:
            result_set.append({
                "Field Name": field,
                "Old Value": str(difference[VALUES_CHANGED_KEY][field]["old_value"]),
                "New Value": str(difference[VALUES_CHANGED_KEY][field]["new_value"]),
            })
        return result_set
    else:
        print('VALUES CHANGED key is absent')
        return []


def generate_dictionary_item_added(difference):
    if DICT_ITEM_ADDED_KEY in difference.keys():
        result_set = []
        for val in difference[DICT_ITEM_ADDED_KEY]:
            result_set.append({
                "Item Added": str(val)
            })
        return result_set
    else:
        print('DICTIONARY ITEM ADDED key is absent')
        return []


def generate_dictionary_item_removed(difference):
    if DICT_ITEM_REMOVED_KEY in difference.keys():
        result_set = []
        for val in difference[DICT_ITEM_REMOVED_KEY]:
            result_set.append({
                "Item Removed": str(val)
            })
        return result_set
    else:
        print('DICTIONARY ITEM REMOVED key is absent')
        return []