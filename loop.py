file_handler = open('daaligbe.txt')
for cheese in file_handler:
    if cheese.startswith('D'):
        print(cheese.strip())
print(file_handler)