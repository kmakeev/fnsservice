import pdfkit
from fns.models import СвЮЛ, Документ
import os
from django.core.management.base import BaseCommand, CommandError
from lxml import etree

def xslt_process(xml_file, xsl_file):
    dom = etree.fromstring(xml_file)
    xslt = etree.parse(xsl_file)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    # print(etree.tostring(newdom, pretty_print=True))
    return etree.tostring(newdom, pretty_print=True, encoding='utf-8')
    # newdom.write(output_file, pretty_print=True)


class Command(BaseCommand):
    help = "test PDF Converter"

    def handle(self, *args, **options):
        print('In convert')

        xsl_data = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\..\\..\\xsl\\onePDF.xsl"
        tmp = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\..\\..\\tmp\\"

        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.50in',
            'margin-bottom': '0.75in',
            'margin-left': '1.00in',
            'footer-right': 'E-System. Страница [page] из [toPage]',
            'encoding': "utf-8"
        }

        body = """
            <html>
              <head>
              <meta charset="utf-8">
              <style type="text/css">
                    table { counter-reset: item; }
                    td.num:before {
                    content: counters(item, ".") " ";
                    counter-increment: item;
                   }
                   tr, td, th, tbody, thead, tfoot {
                        page-break-inside: avoid !important;
                   }
              </style>
              </head>
            """
        try:
            doc = Документ.objects.get(ИдДок='ad11205a-d2fa-4d85-8cc0-6ee400022864')
            file_name = tmp + doc.ИдДок + '.pdf'
            html_egrul = xslt_process(doc.СвЮЛ_XML, xsl_data).decode('utf-8')
            body = body + html_egrul + '</html>'
            pdfkit.from_string(body, file_name, options=options)
            print('File save', file_name)
        except:
            print('Error get document')



