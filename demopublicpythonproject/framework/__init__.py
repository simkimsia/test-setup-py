"""``demopublicpythonproject.framework`` implements the logic for this project
"""
from pyfiglet import figlet_format


def hello_world_logo():
    return figlet_format("Hello World", font="slant")

def main():  # pragma: no cover
    """Main entry point.
    """
    print(hello_world_logo())
