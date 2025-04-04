import pytesseract
import cv2
import pandas as pd
import os
from pdf2image import convert_from_path

# Configure path for Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Change this based on OS

def extract_text_from_image(image_path):
    # Load image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Preprocess image (optional: improve OCR accuracy)
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Perform OCR
    extracted_text = pytesseract.image_to_string(img, config='--psm 6')  # psm 6 is good for tables
    return extracted_text

def parse_text_to_table(text):
    rows = text.split("\n")
    data = [row.split() for row in rows if len(row.split()) > 3]  # Ignore empty or non-table lines
    return data

def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False, header=False)
    print(f"✅ Data saved to {output_file}")

# Process all uploaded images
image_files = ["/mnt/data/image.png"]  # Change to multiple files if needed

all_data = []
for img_file in image_files:
    text = extract_text_from_image(img_file)
    table_data = parse_text_to_table(text)
    all_data.extend(table_data)

# Save extracted table to Excel
save_to_excel(all_data, "/mnt/data/extracted_bank_statement.xlsx")
