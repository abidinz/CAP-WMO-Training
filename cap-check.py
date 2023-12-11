import sys
import xmlschema


file_name = sys.argv[1]
cap_version = sys.argv[2]
schema = xmlschema.XMLSchema(f"./cap-library/schema/{cap_version}.xsd")

print(schema.is_valid(file_name))
