from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('REPLACE_API_KEY')

pred_json = model.convert_to_prediction('test.png')

# print the json
import json
print(json.dumps(pred_json, indent=2))