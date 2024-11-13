from lxml import etree
from saxonche import PySaxonProcessor

# 1. XPath
DIRNAME = './xslt_subxml/'
xml_file = DIRNAME + 'airport.xml' 
tree = etree.parse(xml_file)

LargeEUairports = tree.xpath("//Airport_Code[continent='EU' and type='large_airport']")

print("Aeroportos da Europa:")
for airport in LargeEUairports:
    name = airport.find("name").text
    continent = airport.find("iso_country").text
    print(f"Nome: {name}, País: {continent}")


# 2. XQuery
proc = PySaxonProcessor(license=False)
xqproc = proc.new_xquery_processor()
xml_file_path = 'file:./xslt_subxml/airport.xml'

xquery = '''
    for $airport in doc("''' + xml_file_path + '''")//Airport_Code
    where $airport/iso_country = "PT"
    return <result>
                { $airport/name }
                { $airport/ident }
           </result>
'''

xqproc.set_query_content(xquery)
result_string = xqproc.run_query_to_string()

# remove xml declaration
result_string = result_string.replace('<?xml version="1.0" encoding="UTF-8"?>', '')

# create root element
result_string = f"<root>{result_string}</root>"
result_tree = etree.fromstring(result_string)


print("\nUsando saxonche (XQuery): Aeroportos em Portugal:")
for result in result_tree.xpath('//result'):
    nome = result.xpath('./name/text()')[0]
    ident = result.xpath('./ident/text()')[0]
    print(f'Aeroporto: {nome}, Código: {ident}')