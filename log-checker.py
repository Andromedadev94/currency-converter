
from pathlib import Path
path_of_log = Path.home()/"Desktop"/"dll"/"random_server.log"
with open(path_of_log, "r") as file_log:
    number_of_info = 0
    number_of_warning = 0
    number_of_error = 0
    number_of_lines = 0
    for line in file_log:
        number_of_lines += 1
        number_of_error += line.count("ERROR")
        number_of_warning += line.count("WARNING")
        number_of_info += line.count("INFO")
print(f"Number of INFO: {number_of_info}")
print(f"Number of WARNING: {number_of_warning}")
print(f"Number of ERROR: {number_of_error}")
print(f"Total number of lines: {number_of_lines}")