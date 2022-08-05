from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('REPLACE_API_KEY')

string1 = model.convert_to_string('test.png')
print(string1)

print('\n\n\n')

string2 = model.convert_to_string('test.png', formatting='lines')
print(string2)

print('\n\n\n')

string3 = model.convert_to_string('test.png', formatting='none')
print(string3)