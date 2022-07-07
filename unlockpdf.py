import os, pikepdf

# Change to the folder containing the password protected PDFs
folder = "/Users/gijomathew/Important/Bank/"

pdfs = [os.path.join(folder, x) for x in os.listdir(folder)]

# Change to the PDF password
pwd = "password"
for pdf in pdfs:
    curr_pdf = pikepdf.open(pdf, password=pwd)
    # Put appropriate folder where you want the unlocked PDFs to be saved
    curr_pdf.save(
        f"/Users/gijomathew/Important/BankUnlocked/{curr_pdf.filename.replace(folder ,'')}"
    )
