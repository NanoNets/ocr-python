from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('REPLACE_API_KEY')

boxes = model.convert_to_boxes('test.png')
for box in boxes:
    print(box)