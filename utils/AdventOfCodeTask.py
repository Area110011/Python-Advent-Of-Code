import shutil


class TxtFormat:
    MAGENTA = '\033[95m'
    AQUA = '\033[94m'
    CYAN = '\033[96m'
    LIME = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    RESET_ALL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class AdventOfCodeTask:
    def __init__(self, day: int, file: str):
        self.day = day
        self.file = file

        # Automatically print the result of run()
        self.print_formatted_result(self.run())

    def print_formatted_result(self, lines: [str]):
        heading = f"DAY {self.day}"
        print(f"\n{TxtFormat.YELLOW}{TxtFormat.BOLD}" + f"* {heading} *".center(shutil.get_terminal_size().columns, '-')
              + TxtFormat.RESET_ALL)
        for line in lines:
            print(line)
        print(f"{TxtFormat.YELLOW}{TxtFormat.BOLD}" + "".center(shutil.get_terminal_size().columns, '-')
              + TxtFormat.RESET_ALL)

    def get_relative_file_path(self, filename: str):
        from os import path
        return path.join(path.dirname(self.file), filename)

    def run(self) -> []:
        return []
