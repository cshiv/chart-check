import requests
import re
import predefined

# Check if tag matches pattern based on regular expression comparison
def is_valid_tag(tag,pattern):
    return re.match(pattern, tag)


# Sort Based on semantic versioning
def get_latest_semantic_tag(valid_tags):    
    return max(valid_tags, key=lambda s: list(map(int, re.findall(r'\d+', s))))

# Fetch the file from github based on repo,tags,path and returns the content of file
def fetch_file_from_tag(repo,token,tag,path):
    url= f"{predefined.GIT_RAW_URL}/{repo}/refs/tags/{tag}/{path}"
    # Fetch the CRD
    headers = {
        'Authorization': f'token {token}'
    }    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure we raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file from GitHub: {e}")
        return None

# For the given repo return the latest tag
# By default get_latest_semantic_version function is used for getting the latest semnatic version.
# and the tags are filtered based on the semantic versioning(X.Y.Z). 
# If the valid tags need to be filtered based on a different pattern, use the pattern as an argument
# If latest tag needs to be figured out in a different way like latest tagged date,commit date
# or a different way ,add a function and pass the function name as a parameter
# 

def fetch_latest_tag(repo, token,get_latest_func=get_latest_semantic_tag,pattern=r"^v(\d+)\.(\d+)\.(\d+)$"):
    # GitHub API URL for fetching tags
    url = f"{predefined.GIT_API_URL}/repos/{repo}/tags"
    headers = {
        'Authorization': f'token {token}'
    }
    try:
        valid_tags = []
        page= 1
        while True:           
            response = requests.get(url,headers=headers, params={"per_page": 100, "page": page})
            # response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            if not response.json():
              break
            tags = response.json()
            if not tags:
                print("No tags found in the repository.")
                return None
            valid_tags.extend(tag['name'] for tag in tags if is_valid_tag(tag['name'],pattern))

            page=page+1

        if len(valid_tags)==0:
            print("No valid tags found in the repository.")
            return None
        # Sort valid tags to find the latest one
        # latest_tag = max(valid_tags, key=lambda s: list(map(int, s[1:].split('.'))))
        return get_latest_func(valid_tags)    

    # except requests.exceptions.RequestException as e:
    except Exception as e:
        print(f"Error fetching tags: {e}")
        return None    
    
    
    
