from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('REPLACE_API_KEY')

# formatting enabled
model.convert_to_txt('test.png', output_file_name='output.txt')

# formatting = lines
# model.convert_to_txt('test.png', formatting='lines', output_file_name='output.txt')

# formatting = none
# model.convert_to_txt('test.png', formatting='none', output_file_name='output.txt')