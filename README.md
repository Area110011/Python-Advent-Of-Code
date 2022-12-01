# Advent of Code template project
A template project for adventofcode.com

There is a template file for each day with the following structure:
```python
class FirstDay(AdventOfCodeTask):
    def __init__(self):
        super().__init__(day=1, file=__file__)

    def run(self):
        return []
```

Implement the current day's code in the `run()` method of each day & return a list of lines to be printed.

To open files relative to the current `challenge.py` more easily, you can use the `get_relative_file_path(filename: str)` method. Example:
```
days/
├─ first/
│  ├─ challenge.py
│  ├─ input
```
```python
    def run(self):
        with open(self.get_relative_file_path("input"), "r") as f:
```
