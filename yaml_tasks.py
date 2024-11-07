import yaml
from functools import reduce
import predefined
import git_tasks as gt
import re

# Helper function to extract field from yaml hierarchy
def get_nested_value(data, key_path):
    # key_path has to be a list ["path1","child-path1"]
    return reduce(lambda data, key: data.get(key) if isinstance(data, dict) else None, key_path, data)

# Cleanup Schema with known rules
def cleanup_schema(schema):
    if 'status' in schema: del schema['status']  # Remove Status 
    return schema

# Only one version is stored in etcd, which is usually the Latest and Greatest.
def get_latest_version_schema(crd):
    versions = crd.get('spec', {}).get('versions', [])
    for _, version in enumerate(versions):
        if version.get('storage', False):  # Version where 'storage' is True is checked
            schema = get_nested_value(version,["schema","openAPIV3Schema","properties"])
            return schema     
    return None  


def get_parsed_fields(crd):
    schema=get_latest_version_schema(crd)
    if schema is None:
        print("Unable to get the schema")
        return None
    schema=cleanup_schema(schema)
    crd_name=get_nested_value(crd,["metadata","name"])
    if crd_name is None:
        print("Unable to get the CRD Name")
    fields=parse_schema(schema,crd_name,'')
    if not fields:
        return None
    return fields

# Function iteratively checks for the all the nodes and prints the possible key
# Child nodes are checked by using the "properties" string which is used in open API schema
# Function also checks for IGNORE_CRD_PATH defined in predefined path to ignore any paths which 
# are known to be handled by operator or which users have no control.
def parse_schema(schema,crd_name, prefix=''):
    fields = []  
    if isinstance(schema, dict):
        for key, value in schema.items():
            current_field = f"{prefix}.{key}" if prefix else key
            # List will contain a list of dict (property, type , conditions)
            if "properties" not in value and type(value)==dict:                
                if not any(re.search(s,current_field) for s in predefined.IGNORE_CRD_PATH[crd_name]):
                    # print(current_field)
                    fields.append({"path":current_field,"type": value.get("type"),"condition": None})  # Append current field to output                
            if "properties" in value:
                fields.extend(parse_schema(value.get("properties"),crd_name, current_field))  # Extend with parsed output
            if "items" in value:
                if "properties" in value.get("items"):                    
                    fields.extend(parse_schema(value.get("items").get("properties"),crd_name, current_field))  # Extend with parsed output
    elif isinstance(schema, list):
        for index, item in enumerate(schema):
            current_field = f"{prefix}[{index}]"
            fields.extend(parse_schema(item, crd_name,current_field))  # Extend with parsed output
    return fields  

def filter_defined_crds(crd_file):
    try:
        all_crd = yaml.safe_load_all(crd_file)
    except yaml.YAMLError as e:
        print(f"Error parsing the crd.yaml file: {e}")
        return None
    for crd in all_crd:
        crd_name=get_nested_value(crd,["metadata","name"])
        # Value add with backup and restore charts are minimal. Considering the DB Cluster Resource only
        if crd_name and crd_name in predefined.IGNORE_CRD_PATH:
            print(f"Parsing CRD {crd_name}") 
            return crd     
    print("No crd defined in KNOWN_CRD_PATH is found")      
    return None
