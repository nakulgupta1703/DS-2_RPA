import  PyPDF2
import re
def extract_invoice_details(pdf_path):

    pdfFileObj = open(pdf_path, 'rb')

    pdf_document = PyPDF2.PdfReader(pdfFileObj)

    invoice_number = ""
    invoice_date = ""
    gross_amount = ""
    net_quantity = ""
    total_amount = ""
    tax_percentage = ""

    for page_num in range(len(pdf_document.pages)):
        page = pdf_document.pages[page_num]
        text = page.extract_text()
        text_list = text.splitlines()
        invoice_number_match = text_list[0]
        invoice_date_match = text_list[1]

        i = 6
        net_quantity_match = 0
        gross_amount_match = 0
        while text_list[i][0].isdigit():
            net_quantity_match += int(text_list[i].split()[1])
            gross_amount_match += int(text_list[i].split()[3][3:])
            i+=1

        total_amount_match = text_list[-1].split()[-1]
        tax_percentage_match = 0

    pdfFileObj.close()

    return {
        "Invoice Number": invoice_number_match,
        "Invoice Date": invoice_date_match,
        "Gross Amount": gross_amount_match,
        "Net Quantity": net_quantity_match,
        "Total Amount": total_amount_match,
        "Tax Percentage": tax_percentage_match,
    }

pdf_path = "C:\AB InBev\Invoice_A00001_ABC Agencies.pdf"
invoice_details = extract_invoice_details(pdf_path)

for key, value in invoice_details.items():
    print(f"{key}: {value}")
