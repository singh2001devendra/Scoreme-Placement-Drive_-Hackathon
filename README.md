Bank Statement OCR Extraction

This project extracts tabular transaction data from bank statement images and saves it into an Excel file.

Features

Uses Tesseract-OCR for text extraction from images.

Processes multiple images to extract structured transaction data.

Saves extracted data in Excel format for easy analysis.

Supports preprocessing to improve OCR accuracy.

Prerequisites

Install Dependencies

Ensure you have the required libraries installed:
[](pip install pytesseract opencv-python pandas pdf2image)

Install Tesseract-OCR

Download Tesseract-OCR

Set the path in the script:
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  

How to Use

1. Place Images

Ensure your bank statement images are stored in the /mnt/data/ directory.

2. Run the Script

Execute the Python script to process images and extract data:
python extract_bank_statement.py

3. Output

The extracted transactions are saved as an Excel file:
/mnt/data/extracted_bank_statement.xlsx

Improvements

Enhance OCR accuracy with better preprocessing.

Support batch processing for multiple images.

Convert PDF bank statements directly using pdf2image.

License

This project is licensed under the MIT License.

Author

Developed by Devendra Singh Thakur
