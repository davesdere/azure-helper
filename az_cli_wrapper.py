# Davesdere - David Cote - 2020
# Ca va bien aller
import functools
import io
import json
import sys
from azure.cli.core import get_default_cli

def xcli(func):
    old_stdout = None
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def stdout_thief(*args, **kwargs):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout        
        func(*args, **kwargs)
        value = new_stdout.getvalue().strip("'")
        sys.stdout = old_stdout
        try:
            value = json.loads(value)
        except:
            skeleton = """
                {"result": ""}
            """
            skeleton = json.loads(skeleton)
            skeleton['result'] = value
        return value
    return stdout_thief

@xcli
def test_non_json_response():
    b ="#"*80
    print(b)
    assert type(print(b)) == type(json.loads('test'))

@xcli
def azcli(commands):
    z = get_default_cli().invoke(commands)
    return z

@xcli
def test_valid_json_response():
    json_data = azcli(['policy', 'definition', 'list'])
    print(json_data[0])
    assert type(json_data) == type(json.loads('test'))
