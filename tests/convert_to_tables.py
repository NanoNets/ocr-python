from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('REPLACE_API_KEY')

tables_json = model.convert_to_tables('table2.png')

# print the json
import json
print(json.dumps(tables_json, indent=2))