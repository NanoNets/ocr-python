Python OCR
================

.. image:: https://img.shields.io/pypi/v/ocr-nanonets-wrapper.svg?color=green
   :target: https://pypi.org/project/ocr-nanonets-wrapper/

This python package is an OCR library which reads all text & tables from image & PDF files using an OCR engine & provides intelligent post-processing options to save OCR results in formats you want.

|

.. image:: https://uploads-ssl.webflow.com/60545d366101292fb9c8e98e/60545d36610129d15ec8e9c6_logo-white.svg
   :target: https://nanonets.com/?&utm_source=wrapper
   
|
Installation
-----

The package requires `Python 3 <https://www.python.org/downloads/>`_ to run.

You can use `pip <https://pip.pypa.io/en/stable/installation/>`_ to install:

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

You can refer the code shared below or `directly use code from here <https://github.com/NanoNets/ocr-python-nanonets/blob/main/tests/alltests.ipynb>`_.

.. code-block:: python

    # Initialise
    from nanonets import NANONETSOCR
    model = NANONETSOCR()
    
    # Authenticate
    # This software is perpetually free :)
    # You can get your free API key (with unlimited requests) by creating a free account on https://app.nanonets.com/#/keys?utm_source=wrapper.
    model.set_token('REPLACE_API_KEY')
    
    # PDF / Image to Raw OCR Engine Output
    import json
    pred_json = model.convert_to_prediction('INPUT_FILE')
    print(json.dumps(pred_json, indent=2))
    
    # PDF / Image to String
    string = model.convert_to_string('INPUT_FILE')
    print(string)
    
    # PDF / Image to TXT File
    model.convert_to_txt('INPUT_FILE', output_file_name = 'OUTPUTNAME.txt')

    # PDF / Image to Boxes 
    # each element contains predicted word and bounding box information
    # bounding box information denotes the spatial position of each word in the file
    boxes = model.convert_to_boxes('test.png')
    for box in boxes:
        print(box)

    # PDF / Image to CSV
    # This method extracts tables from your file and prints them in a .csv file.
    # NOTE : This particular function is a trial offering 1000 pages of use. 
    # To use this at scale, please create your own model at app.nanonets.com --> New Model --> Tables.
    model.convert_to_csv('INPUT_FILE', output_file_name = 'OUTPUTNAME.csv')

    # PDF / Image to Tables
    # This method extracts tables from your file and returns a json object.
    # NOTE : This particular function is a trial offering 1000 pages of use. 
    # To use this at scale, please create your own model at app.nanonets.com --> New Model --> Tables.
    import json
    tables_json = model.convert_to_tables('INPUT_FILE')
    print(json.dumps(tables_json, indent=2))

    # PDF / Image to Searchable PDF
    model.convert_to_searchable_pdf('INPUT_FILE', output_file_name = 'OUTPUTNAME.pdf')  

Testing
-------

To make getting started easier for you, there is a bunch of sample code along with sample input files.

- Clone or download the repo and open the /tests folder.
- `all_tests.ipynb <https://github.com/NanoNets/ocr-python-nanonets/blob/main/tests/alltests.ipynb>`_ is a python notebook containing testing for all methods in the package.
- convert_to_{METHOD}.py files are python files corresponding to each method in the package individually.

**Note**

convert_to_string() and convert_to_txt() methods have two optional parameters - 

1. **formatting =**

- ```lines and spaces``` : default, all formatting enabled

- ```none``` : space separated text with formatting removed

- ```lines``` : space separated text with lines separated with newline character 

- ```pages``` : list of page wise space separated text

2. **line_threshold =**

- ```low``` : default
- ```high``` : You can add ``line_threshold='high'`` as a parameter while calling the method which in few cases can improve reading flowcharts and diagrams.


Advanced Functions
------------
If extracting flat fields, tables and line items from PDFs and images is your use case, I will strongly advice you to create your own model by signing up on `app.nanonets.com <https://app.nanonets.com/#/signup?utm_source=wrapper>`_ and using our advanced API. This will improve functionalities, accuracy and response times significantly. Once you have created your account and model, you can use `API documentation present here <https://app.nanonets.com/documentation#operation/OCRModelLabelFileByModelIdPost>`_ to extract flat fields, tables and line items from any PDF or image.

Nanonets
------------
We help businesses automate Manual Data Entry Using AI and reduce turn around times & manual effort required. More than 1000 enterprises use Nanonets for Intelligent Document Processing. We have generated incredible ROIs for our clients.

We provide OCR and IDP solutions customised for various use cases - invoice automation, Receipt OCR, purchase order automation, accounts payable automation, ID Card OCR and many more.

- Visit `nanonets.com <https://nanonets.com/?&utm_source=wrapper>`_ for enterprise OCR and IDP solutions.
- Sign up on `app.nanonets.com/#/signup <https://app.nanonets.com/#/signup?&utm_source=wrapper>`_ to start a free trial.


License
-------

**MIT**

**This software is perpetually free :)**
