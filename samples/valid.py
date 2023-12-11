import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLSchema

# Load the XML schema
schema = XMLSchema("./cap-library/schema/cap11.xsd")
# Parse the XML document
file_name = sys.argv[1]
tree = ET.parse(file_name)
# Validate the XML document
if not tree.validate(schema):
  raise ValueError('The XML document is invalid.')

