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
        return value
    return stdout_thief


@xcli
def run_azcli(commands):
    z = get_default_cli().invoke(commands)
    return z

#e.g get policy def list
outpout_data = run_azcli(['policy', 'definition', 'list'])
json_data= json.loads(outpout_data)

print(json_data[0])
