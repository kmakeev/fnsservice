from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.template import loader
import pdfkit
from fns.models import Документ
import os
import shutil
from lxml import etree


def xslt_process(xml_file, xsl_file):
    dom = etree.fromstring(xml_file)
    xslt = etree.parse(xsl_file)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    # print(etree.tostring(newdom, pretty_print=True))
    return etree.tostring(newdom, pretty_print=True, encoding='utf-8')
    # newdom.write(output_file, pretty_print=True)

class PDFView(View):

    def get(self, request, id, *args, **kwargs):
        # form = InputForm()
        print('in pdfView', id)
        xsl_data = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/../xsl/onePDF.xsl"
        tmp = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/../tmp/"

        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.50in',
            'margin-bottom': '0.75in',
            'margin-left': '1.00in',
            #'footer-right': 'E-System. Страница [page] из [toPage]',
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
                       table, tr, td, th, tbody, thead, tfoot {
                            page-break-inside: avoid !important;
                       }
                  </style>
                  </head>
                """
        try:
            doc = Документ.objects.get(ИдДок=str(id))
        except:
            return HttpResponseBadRequest('Ошибка при создании PDF файла')
        file_name = tmp + doc.ИдДок + '.pdf'
        if not os.path.exists(file_name):
            html_egrul = xslt_process(doc.СвЮЛ_XML, xsl_data).decode('utf-8')
            body = body + html_egrul + '</html>'
            pdfkit.from_string(body, file_name, options=options)
        try:
            f = open(file_name, 'rb')
        except IOError:
            return HttpResponseBadRequest('Ошибка при создании PDF файла')
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + doc.ИдДок + '.pdf'
        shutil.copyfileobj(f, response)
        return response




