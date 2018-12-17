from PyPDF2 import PdfFileReader, PdfFileWriter
from django.conf import settings
import os

class RpsSource(object):

    def __init__(self, pdf_path, pdf_start, pdf_end):
        self.pdf_path = pdf_path
        self.start_page = pdf_start
        self.end_page = pdf_end
    

def make_rps(name,*args):
    media_path = os.path.join(settings.MEDIA_ROOT)
    rps_result = os.path.join(media_path, "rps", name+".pdf")
    with open(rps_result,'wb') as result:
        writer = PdfFileWriter()

        for i in args:
            source_path = os.path.join(media_path,i.pdf_path)
            reader = PdfFileReader(open(source_path,'rb'))

            for j in range(i.start_page-1,i.end_page-1):
                writer.addPage(reader.getPage(j))
        
        writer.write(result)