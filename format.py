def open_file(filename):
  file = open(filename, "r")
  lines = file.read().getlines()
  return lines

open_file(filename="4_30.txt")