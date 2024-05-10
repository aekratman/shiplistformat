def open_file(filename):
    with open(filename, "r") as f:
        all_lines = f.readlines()
    return all_lines

open_file(filename="/Users/abbeykratman/Downloads/4_30.txt")
