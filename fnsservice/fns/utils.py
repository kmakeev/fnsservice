import os
import re
from lxml import etree


def printProgressBar (iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    end = '\r'
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end)
    # Print New Line on Complete
    if iteration == total:
        print()


def check_ogrn(ogrn):
    len_ogrn = len(ogrn)
    if len_ogrn not in (13, 15) or not re.fullmatch('[0-9]*', ogrn):
        return False

    def ogrn_csum(ogrn):
        if len_ogrn == 13:
            delimeter = 11
        else:
            delimeter = 13
        return str(int(ogrn[:-1]) % delimeter % 10)

    return ogrn_csum(ogrn) == ogrn[-1]


def check_inn(inn):
    if len(inn) not in (10, 12) or not re.fullmatch('[0-9]*', inn):
        return False

    def inn_csum(inn):
        k = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
        pairs = zip(k[11 - len(inn):], [int(x) for x in inn])
        return str(sum([k * v for k, v in pairs]) % 11 % 10)

    if len(inn) == 10:
        return inn[-1] == inn_csum(inn[:-1])
    else:
        return inn[-2:] == inn_csum(inn[:-2]) + inn_csum(inn[:-1])


def xslt_process(xml_file, xsl_file):
    dom = etree.fromstring(xml_file)
    xslt = etree.parse(xsl_file)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    # print(etree.tostring(newdom, pretty_print=True))
    return etree.tostring(newdom, pretty_print=True, encoding='utf-8')
    # newdom.write(output_file, pretty_print=True)