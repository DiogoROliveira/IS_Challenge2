from lxml import etree
import os

def xslt_transform(xml_base, xslt, output_path):

    transform = etree.XSLT(xslt)    
    sub_xml = transform(xml_base)

    with open(output_path, "wb") as f:
        f.write(etree.tostring(sub_xml, pretty_print=True, encoding="UTF-8", xml_declaration=True))

    print(f"Sub-XML created successfully: {output_path}")

DIRNAME = './tool_files/'
RESULTDIR = './xslt_subxml/'
os.makedirs(RESULTDIR, exist_ok=True)

xmlfile = input("Enter the xml file name(with extension): ")
result = input("Enter the result xml file name(with extension): ")

if not xmlfile or not result:
    print("Por favor, insira nomes de arquivos válidos!")
    exit()

if not xmlfile.endswith('.xml'):
    print("Por favor, insira um arquivo XML válido!") 
    exit()

xml_base = etree.parse(xmlfile)
xslt = etree.parse(os.path.join(DIRNAME, "filter.xsl"))
output_path = os.path.join(RESULTDIR, result)

xslt_transform(xml_base, xslt, output_path)
