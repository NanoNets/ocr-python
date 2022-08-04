Python OCR Nanonets
================

.. image:: https://img.shields.io/pypi/v/ocr-nanonets-wrapper.svg?color=green
   :target: https://pypi.python.org/pypi/ocr-nanonets-wrapper

This package is an optical character recognition (OCR) tool for python.
It reads plain text and tables from image & PDF files using an OCR engine and provides intelligent post-processing options to ensure you get OCR results in formats you want.

.. image:: https://i.postimg.cc/59ZZmyrt/Screenshot-2022-07-12-at-11-37-27-PM.png
   :target: https://nanonets.com/?&utm_source=wrapper
   


- This package works on an OCR engine from `Nanonets <https://nanonets.com/?&utm_source=wrapper>`_.
- We help businesses Automate Manual Data Entry Using AI and reduce turn around times and the manual effort required.
- More than 1000 enterprises convert PDF documents and images to actionable text using Intelligent Document Processing from Nanonets.



Installation
-----

The package requires `Python 3 <https://www.python.org/downloads/>`_ to run.

You can use pip to install:


.. code-block:: bash

    pip install ocr-nanonets-wrapper

Authentication
-----

This software is perpetually free :)

You can get your free API key (with unlimited requests) by creating a free account on `https://app.nanonets.com/#/keys <https://app.nanonets.com/#/keys?utm_source=wrapper>`_.

.. code-block:: python

    from nanonets import NANONETSOCR
    model = NANONETSOCR()
    model.set_token('REPLACE_API_KEY')


Usage
-----

.. code-block:: python

    # Initialise
    from nanonets import NANONETSOCR
    model = NANONETSOCR()
    
    # Authenticate
    # This software is perpetually free :)
    # You can get your free API key (with unlimited requests) by creating a free account on https://app.nanonets.com/#/keys.
    model.set_token('REPLACE_API_KEY')
    
    # PDF / Image to String
    string = model.convert_to_string('INPUT_FILE')
    print(string)
    
    # PDF / Image to TXT File
    model.convert_to_txt('INPUT_FILE', output_file_name = 'OUTPUTNAME.txt')

    # PDF / Image to Boxes 
    # each element contains predicted word and bounding box information
    # bounding box information
    boxes = model.convert_to_boxes('test.png')
    for box in boxes:
        print(box)

    # PDF / Image to CSV
    # This method extracts tables from your file and prints them in a .csv file.
    model.convert_to_csv('INPUT_FILE', output_file_name = 'OUTPUTNAME.csv')

    # PDF / Image to Tables
    # This method extracts tables from your file and returns a json object.
    import json
    tables_json = model.convert_to_tables('INPUT_FILE')
    print(json.dumps(tables_json, indent=2))

    # PDF / Image to Searchable PDF
    model.convert_to_searchable_pdf('INPUT_FILE', output_file_name = 'OUTPUTNAME.pdf')

    # PDF / Image to Raw OCR Engine Output
    import json
    pred_json = model.convert_to_prediction('INPUT_FILE')
    print(json.dumps(tables_json, indent=2))    

**Note**

convert_to_string() and convert_to_txt() methods have two optional parameters - 

1. **formatting**

- ```lines and spaces``` : all formatting enabled

- ```none``` (DEFAULT) : single space separated text with all formatting removed

- ```lines``` : single space separated text with different lines separated with newline character 

- ```pages``` (ONLY FOR pdf_to_string) : list of page wise single space separated text with all formatting removed

2. **line_threshold**

- You can add ``line_threshold='high'`` as a parameter while calling the method which in few cases can improve reading flowcharts and diagrams.

TESTING
-------

To make getting started easier for you, there is a bunch of sample code along with sample input files.
Clone the repo and test out the code.

LICENSE
-------

**MIT**

**This software is perpetually free :)**


Have Advanced Intelligent Document Processing Needs ? Want to Automate Manual Data Entry Using AI ?
------------
We provide OCR and IDP solutions customised for various use cases - invoice automation, Receipt OCR, purchase order automation, accounts payable automation, ID Card OCR and many more.

- Visit `nanonets.com <https://nanonets.com/?&utm_source=wrapper>`_ for enterprise OCR and IDP solutions.
- Sign up on `app.nanonets.com/#/signup <https://app.nanonets.com/#/signup?&utm_source=wrapper>`_ to start a free trial.
