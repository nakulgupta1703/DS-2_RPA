import fitz  # PyMuPDF library
import re

def extract_invoice_details(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Initialize variables to store extracted details
    invoice_number = ""
    invoice_date = ""
    gross_amount = ""
    net_quantity = ""
    total_amount = ""
    tax_percentage = ""
    
    # Iterate through pages
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text("text")
        
        # Extracting details using regular expressions
        invoice_number_match = re.search(r"Invoice Number: (\w+)", text)
        invoice_date_match = re.search(r"Invoice Date: (\d{2}/\d{2}/\d{4})", text)
        gross_amount_match = re.search(r"Gross Amount: (\$\d+\.\d+)", text)
        net_quantity_match = re.search(r"Net Quantity: (\d+)", text)
        total_amount_match = re.search(r"Total Amount: (\$\d+\.\d+)", text)
        tax_percentage_match = re.search(r"Tax Percentage: (\d+%)", text)
        
        # Update variables if matches are found
        if invoice_number_match:
            invoice_number = invoice_number_match.group(1)
        if invoice_date_match:
            invoice_date = invoice_date_match.group(1)
        if gross_amount_match:
            gross_amount = gross_amount_match.group(1)
        if net_quantity_match:
            net_quantity = net_quantity_match.group(1)
        if total_amount_match:
            total_amount = total_amount_match.group(1)
        if tax_percentage_match:
            tax_percentage = tax_percentage_match.group(1)
    
    # Close the PDF file
    pdf_document.close()
    
    # Return extracted details
    return {
        "Invoice Number": invoice_number,
        "Invoice Date": invoice_date,
        "Gross Amount": gross_amount,
        "Net Quantity": net_quantity,
        "Total Amount": total_amount,
        "Tax Percentage": tax_percentage,
    }

# Example usage
pdf_path = "C:\AB InBev\Invoice_A00001_ABC Agencies.pdf"
invoice_details = extract_invoice_details(pdf_path)

# Display extracted details
for key, value in invoice_details.items():
    print(f"{key}: {value}")