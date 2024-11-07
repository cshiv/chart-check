
import re
import predefined

def add_helm_paths(cr_name):
    return predefined.ADD_HELM_PATH[cr_name]

# Function parses the helm template of CRD and derives all the possible keys which can be used 
# by the user

def derive_template_fields(template):
    stack = []  # Stack to keep track of hierarchy with full paths
    lines = template.splitlines()
    template_fields=[]
    for line in lines:
        # Ignore empty lines
        if not line.strip():
            continue
        # Ignore template syntax of pattern {{ }} and which doesn't have key 
        if ":" not in line and re.search(r"{{.*?}}", line):
            continue
        # Ignore any hard coded values
        if ":" not in line and not re.search(r"{{.*}}", line):
            continue
        # Ignore any ':' within template syntax
        if re.search(r"(?<!}})\s*{{\s*[^:}]+:\s*[^}]+}}\s*(?!{{)", line):
            continue

        # Calculate the indentation level (number of leading spaces)
        indentation = len(line) - len(line.replace("-", " ", 1).lstrip())
        key = line.lstrip().split(":")[0].lstrip("-").strip()  

        # Adjust the stack based on current indentation
        while stack and stack[-1][1] >= indentation:
            stack.pop()

        # Construct the full path for the current key
        if stack:
            full_path = f"{stack[-1][0]}.{key}"
        else:
            full_path = key

        # Print the full path for the current key
        template_fields.append(full_path)
        # print(full_path)

        # If string is a key, add to stack
        if line.strip().endswith(":"):
            stack.append((full_path, indentation))
    return template_fields

# Parse the template of the chart and return all the possible fields
def parse_template(template,cr_name):
    template_fields=derive_template_fields(template)
    helm_path_additions=add_helm_paths(cr_name)
    if helm_path_additions:
        template_fields.extend(helm_path_additions)
    if len(template_fields)==0:
        print("No fields parsed from the template")
        return None
    return template_fields

