import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom

def csv_to_xml(csv_file, xml_file, objname):
    # create root element
    root = ET.Element("root")

    # read csv
    with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        # foreach line in csv file, an object is created
        for line in reader:
            obj = ET.Element(objname)

            # add fields to object
            for field, value in line.items():
                element = ET.SubElement(obj, field)
                element.text = value

            root.append(obj)

    ET.ElementTree(root)

    # minidom do apply 'Enter' indentation
    xml_string = ET.tostring(root, encoding='utf-8')
    xml_pretty = minidom.parseString(xml_string).toprettyxml(indent='  ')

    with open(xml_file, mode='w', encoding='utf-8') as xmlfile:
        xmlfile.write(xml_pretty)

    print("XML file created successfully! - {}".format(xml_file))


csvname = input("Enter the csv file name(with extension): ")
xmlname = input("Enter the result xml file name(with extension): ")
objname = input("What does the csv keep: ")

if csvname == '' or xmlname == '' or objname == '':
    print("Please enter a valid file name!")
    exit()

if csvname == xmlname:
    print("Please enter different file names!")
    exit()

if not csvname.endswith('.csv'):
    print("Please enter a valid csv file!")
    exit()

if not xmlname.endswith('.xml'):
    print("Please enter a valid xml file!")
    exit()

if objname == '':
    objname = 'object'

if any(char.isspace() for char in objname):
    print("Please enter a valid object name!")
    exit()

csv_to_xml(csvname, xmlname, objname)
