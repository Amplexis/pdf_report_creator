from reportlab.lib.styles import ParagraphStyle

styles = {
    'main_header': ParagraphStyle(
        'default',
        fontName='Helvetica',
        fontSize=14,
        leading=-1,
        leftIndent=-40,
        spaceBefore=20,
        spaceAfter=20,
        textColor=(33 / 256, 127 / 256, 156 / 256)
    ),
    'section_header': ParagraphStyle(
        'default',
        fontName='Helvetica',
        leftIndent=-40,
        fontSize=14,
        textColor=(24/256, 142/256, 206/256)
    ),
    'paragraph_style': ParagraphStyle(
        'default',
        fontName='Helvetica',
         fontSize=10,
         leading=12,
         leftIndent=-40,
         rightIndent=0,
         firstLineIndent=0,
         spaceBefore=0,
         spaceAfter=0,
         textColor=(0/256, 0/256, 0/256),
         backColor=None,
         wordWrap=None,
         borderWidth= 0,
         borderPadding= 0,
         borderColor= None,
         borderRadius= None
    )
}
