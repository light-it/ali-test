import ast
import os


def env(key, default=None):
    try:
        value = os.environ[key]
        return ast.literal_eval(value)
    except KeyError:
        return default
    except (SyntaxError, ValueError):
        return value
