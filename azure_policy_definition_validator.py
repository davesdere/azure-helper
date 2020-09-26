# azure_policy_definition_validator.py
# David Cote 2020 - Ca va bien aller
from azure.cli.core import get_default_cli
import json
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-i', '--input', help='Input file to validate JSON format')
my_parser.add_argument('-v', '--verbose', help='Verbosity level')
args = my_parser.parse_args()

def pull_pol_def_list_from_az_to_file(fileName="az_policy_definition_list.json"):
    try:
        with open(fileName, 'w') as outfile:
            get_default_cli().invoke(['policy', 'definition', 'list'], out_file=outfile)
            print('Azure Defintion Policies List written to az_policy_definition_list.json')
    except:
        print('Something went wrong.')#json.dump(data, outfile)

def load_def_policy_list(fileName = "az_policy_definition_list.json"):
    try:
        with open(fileName, "r") as read_file:
            ref_data = json.load(read_file)
            return ref_data
    except:
        print(f'{fileName} doesnt exists')

def show_me_the_money(fileName="az_policy_definition_list.json"):
    with open(fileName, "r") as read_file:
        ref_data = json.load(read_file)

    for item in ref_data:
        if 'parameters' in list(item.keys()):
            #print(item['parameters'])
            if item['parameters'] is not None and 'effect' in item['parameters']:
                if item['parameters']['effect'] is not None and 'allowedValues' in item['parameters']['effect']:
                    print(f"{item['id']}: {item['parameters']['effect']['allowedValues']}")
#data[0]
def validate_allowed_value(a_value, an_id, ref_data):
    for item in ref_data:
        if an_id in item['id']:
            if 'parameters' in list(item.keys()):
                #print(item['parameters'])
                if item['parameters'] is not None and 'effect' in item['parameters']:
                    if item['parameters']['effect'] is not None and 'allowedValues' in item['parameters']['effect']:
                        if a_value in item['parameters']['effect']['allowedValues']:
                            print(f"{item['id']}: {item['parameters']['effect']['allowedValues']}")
                            print(f'{a_value} is an allowed value in {item["id"]}')
                            return True
                        else:
                            print(f"{a_value} is NOT an allowed value in {item['id']}/n Allowed values : {item['parameters']['effect']['allowedValues']}")
                            return False
                else:
                    print(f"This policy has a None parameter and no effect ")
            else:
                print('This policy doesnt take a parameter')
    return False

def test_validate_allowed_value():
    with open("az_policy_definition_list.json", "r") as read_file:
        ref_data = json.load(read_file)
    a_value = 'Disabled'
    an_id = "/providers/Microsoft.Authorization/policyDefinitions/0004bbf0-5099-4179-869e-e9ffe5fb0945"
    an_id_2 = "/providers/Microsoft.Authorization/policyDefinitions/00379355-8932-4b52-b63a-3bc6daf3451a"
    an_id_3 = "/providers/Microsoft.Authorization/policyDefinitions/013e242c-8828-4970-87b3-ab247555486d"
    an_id_4 = "/providers/Microsoft.Authorization/policyDefinitions/cee51871-e572-4576-855c-047c820360f0"
    print(validate_allowed_value(a_value, an_id, ref_data))
    print(validate_allowed_value(a_value, an_id_2, ref_data))
    print(validate_allowed_value(a_value, an_id_3, ref_data))
    print(validate_allowed_value(a_value, an_id_4, ref_data))

test_validate_allowed_value()
