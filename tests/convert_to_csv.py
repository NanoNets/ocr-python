from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('REPLACE_API_KEY')

model.convert_to_csv('table.png', output_file_name='output.csv')