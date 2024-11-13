import xmlschema

def validate_xml(xml_file, xsd_file):
    try:
        # load the schema
        schema = xmlschema.XMLSchema(xsd_file)

        if schema.is_valid(xml_file):
            print("XML file is valid!")
        else:
            print("XML file is invalid!")
            for error in schema.iter_errors(xml_file):
                print(error)

    except Exception as e:
        print("An error occurred:", e)


__dirname = './tool_files/'

xmlfile = input("Enter the xml file name(with extension): ")
xsdfile = open(__dirname + "schema.xsd", "r")

validate_xml(xmlfile, xsdfile)
