import xml.etree.ElementTree as ET
from collections import defaultdict

def create_sub_xml_by_category(base_xml, category):
    xml_tree = ET.parse(base_xml)
    xml_root = xml_tree.getroot()
    
    # dictionary to store elements by category
    elements_by_category = defaultdict(list)
    
    # group elements by category
    for airport in xml_root.findall("Airport_Code"):
        category_value = airport.find(category).text
        elements_by_category[category_value].append(airport)
    
    # create a sub-XML file for each category
    for category_value, elements in elements_by_category.items():
        sub_xml_root = ET.Element(xml_root.tag)
        for elem in elements:
            sub_xml_root.append(elem)
        
        # save the sub-XML file
        sub_xml_tree = ET.ElementTree(sub_xml_root)
        sub_xml_filename = f"{category_value}_{base_xml}" 
        sub_xml_tree.write(sub_xml_filename, encoding="utf-8", xml_declaration=True)
        print(f"Sub-XML file created: {sub_xml_filename}")

# Example usage
create_sub_xml_by_category("airport_code_upd.xml", "type")
