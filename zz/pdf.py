from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from django.conf import settings

def get_pdf_piece(name,pdf,start_page,end_page):
    pdf_source = os.path.join(settings.BASE_DIR, 'media',str(pdf))
    pdf_result_name = os.path.join(settings.BASE_DIR, 'media', 'rps', name+'.pdf')
    with open(pdf_source, 'rb') as origin:
        reader = PdfFileReader(origin)
        writer = PdfFileWriter()

        for i in range(start_page,end_page):
            writer.addPage(reader.getPage(i))
        
        with open(pdf_result_name,'wb') as result:
            writer.write(result)
        
        return pdf_result_name
    
    
    
