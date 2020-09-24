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
        return value
    return stdout_thief


@xcli
def azcli(commands):
    return json.loads(get_default_cli().invoke(commands))

#e.g get policy def list
outpout_data = azcli(['policy', 'definition', 'list'])

print(outpout_data[0])
