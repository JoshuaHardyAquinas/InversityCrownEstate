# Script to test slicing off quotation marks at the start
from slice import slice

file_path = input("Input: ")

file_path = slice(file_path)

print(file_path)