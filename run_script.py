from loadData import load_pdf
from functionsGPT import comprehend_data

file = input("Type in file path of Research paper: ")

paper = load_pdf(file)

output = comprehend_data(paper)

print(output)