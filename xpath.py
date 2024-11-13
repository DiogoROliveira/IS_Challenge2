from lxml import etree

DIRNAME = './xslt_subxml/'


xml_file = DIRNAME + 'airport.xml' 
tree = etree.parse(xml_file)

EUairports = tree.xpath("//Airport_Code[continent='EU']")

print("Aeroportos da Europa:")
for airport in EUairports:
    name = airport.find("name").text
    continent = airport.find("iso_country").text
    print(f"Nome: {name}, País: {continent}")