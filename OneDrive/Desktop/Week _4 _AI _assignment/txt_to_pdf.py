from fpdf import FPDF

# Read the ethical reflection text
with open('Ethical_Reflection.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=12)

# Split text into lines and add to PDF
for line in text.split('\n'):
    pdf.multi_cell(0, 10, line)

pdf.output('Ethical_Reflection.pdf')
print('PDF created: Ethical_Reflection.pdf')
