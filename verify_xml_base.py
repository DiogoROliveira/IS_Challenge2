import xmlschema

def validate_xml(xml_file, xsd_file):
    try:

        schema = xmlschema.XMLSchema(xsd_file)

        if schema.is_valid(xml_file):
            print("XML file is valid!")
        else:
            print("XML file is invalid!")
            for error in schema.iter_errors(xml_file):
                print(error)

    except Exception as e:
        print("An error occurred:", e)


xmlfile = input("Enter the xml file name(with extension): ")
xsdfile = input("Enter the xsd file name(with extension): ")

validate_xml(xmlfile, xsdfile)