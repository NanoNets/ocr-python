from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('REPLACE_API_KEY')

model.convert_to_searchable_pdf('test2.png', output_file_name='output.pdf')