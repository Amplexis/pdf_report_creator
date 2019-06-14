from os import path
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle
from src.current_week import current_week
from src.import_data import fetch_data, load_text
from resources.styles import styles


project_dir = path.dirname(__file__)
output_dir = path.join(project_dir, 'output')
data_dir = path.join(project_dir, 'resources', 'data')
logo = path.join(project_dir, 'resources', 'images', 'generic-logo.jpg')
example_pdf = path.join(output_dir, 'report.pdf')
data1 = path.join(data_dir, 'table_1_data.txt')
week = current_week()


WIDTH, HEIGHT = letter
LIGHT_BLUE = (111/256, 189/256, 231/256)
DARK_BLUE = (24/256, 142/256, 206/256)
LIGHT_GREEN = (168/256, 207/256, 92/256)
DARK_GREEN = (95/256, 175/256, 64/256)


spacer = Spacer(WIDTH, .25 * inch)
spacer_small = Spacer(WIDTH, .15 * inch)


style_section_header = styles['section_header']
paragraph_style = styles["paragraph_style"]

section_header_1 = Paragraph('Main Header and/or Report Topic', style_section_header)
section_header_2 = Paragraph('Table 1 - Brief Description of Data', style_section_header)
section_header_3 = Paragraph('Table 2 - Brief Description of Data', style_section_header)


paragraph_data = load_text(data_dir, "intro_paragraph.txt")
paragraph = Paragraph(paragraph_data, paragraph_style)


data1 = fetch_data(data_dir, 'table_1_data.txt')
table_1 = Table(data1, (2*inch, .91 * inch, .91 * inch, .91 * inch, .91 * inch, .91 * inch, .91 * inch, ))
table_1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (6, 0), DARK_GREEN),
    ('FONT', (0, 0), (6, 0), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0, 0), (6, 0), colors.white),
    ('ALIGN', (0, 0), (6, 0), 'CENTER'),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOX', (0, 0), (-1, -1), 1, colors.black)
]))


data2 = fetch_data(data_dir, "table_2_data.txt")
table_2 = Table(data2, (3.5 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch), repeatRows=1)
table_2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (4, 0), DARK_GREEN),
    ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
    ('ALIGN', (0, 0), (4, 0), 'CENTER'),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ('FONT', (0, 0), (4, 0), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0, 0), (4, 0), colors.white),
    ('FONT', (0, 1), (0, 1), 'Helvetica-Bold'),
    ('FONT', (0, 6), (0, 6), 'Helvetica-Bold'),
    ('FONT', (0, 23), (0, 23), 'Helvetica-Bold'),
    ('LEFTPADDING', (0, 2), (0, 5), 25),
    ('LEFTPADDING', (0, 7), (0, 7), 25),
    ('LEFTPADDING', (0, 11), (0, 11), 25),
    ('LEFTPADDING', (0, 15), (0, 15), 25),
    ('LEFTPADDING', (0, 19), (0, 19), 25),
    ('LEFTPADDING', (0, 24), (0, 29), 25),
    ('LEFTPADDING', (0, 8), (0, 10), 50),
    ('LEFTPADDING', (0, 12), (0, 14), 50),
    ('LEFTPADDING', (0, 16), (0, 18), 50),
    ('LEFTPADDING', (0, 20), (0, 22), 50),
    ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOX', (0, 0), (-1, -1), 1, colors.black)
]))


def page_one(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 14)
    canvas.drawString(WIDTH - 8.0 * inch, HEIGHT - .65 * inch, 'Generic Company')
    canvas.drawString(WIDTH - 8.0 * inch, HEIGHT - .90 * inch, 'Very Important Report')
    canvas.drawString(WIDTH - 8.0 * inch, HEIGHT - 1.15 * inch, week)
    canvas.drawImage(logo, WIDTH - 2.65 * inch, HEIGHT - 1.2 * inch, width=2.25 * inch, height=0.75 * inch)
    canvas.setLineWidth(5)
    canvas.setStrokeColorRGB(95 / 256, 175 / 256, 64 / 256, 1.0)
    canvas.line(.5 * inch, HEIGHT - 1.25 * inch, 8 * inch, HEIGHT - 1.25 * inch)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(.5 * inch, 0.25 * inch, "Page 1")
    canvas.restoreState()


def all_other_pages(canvas, doc):
    canvas.saveState()
    canvas.drawImage(logo, WIDTH - 2.65 * inch, HEIGHT - 1.0 * inch, width=2.25 * inch, height=0.75 * inch)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(.5 * inch, 0.25 * inch, "Page {}".format(doc.page))
    canvas.restoreState()


def initalize():
    doc = SimpleDocTemplate(example_pdf, pagesize=letter, allowSplitting=1)
    story = []
    story.append(spacer)
    story.append(spacer_small)
    story.append(section_header_1)
    story.append(spacer_small)
    story.append(paragraph)
    story.append(spacer_small)
    story.append(spacer)
    story.append(section_header_2)
    story.append(spacer_small)
    story.append(table_1)
    story.append(spacer_small)
    story.append(spacer_small)
    story.append(section_header_3)
    story.append(spacer_small)
    story.append(table_2)
    doc.build(story, onFirstPage=page_one, onLaterPages=all_other_pages)
