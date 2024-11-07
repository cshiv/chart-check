import yaml
import sys
import predefined    
import yaml_tasks as yt
import git_tasks as gt
import template_tasks as tt



def main():   
    # Parse only for the variables listed in ITEMS_TO_PARSE variable
    for item in predefined.ITEMS_TO_PARSE:
        # Parse Helm Template

        # Get the latest tag from the helm charts repo matching specific pattern
        latest_chart_tag= gt.fetch_latest_tag(predefined.GIT_HELM_REPO,predefined.TOKEN,pattern=item["tag_pattern"])
        if latest_chart_tag is None:
            print(f"Unable to fetch the latest tags of helm charts repo {predefined.GIT_HELM_REPO}")
            sys.exit(-1)

        # Get the template file of the Custom Resource
        template_file=gt.fetch_file_from_tag(predefined.GIT_HELM_REPO,predefined.TOKEN,latest_chart_tag,item["template_file"])
        if template_file is None:
            print(f"Unable to fetch the template file from git repo {predefined.GIT_HELM_REPO}")
            sys.exit(-1)

        # Get the list of fields added in the Helm chart
        template_fields=tt.parse_template(template_file,item["cr_name"])
        if template_fields is None:
            print(f"Unable to parse and extract fields from the template file")
            sys.exit(-1)

        # Parse CRD

        crd_repo=item["crd_repo"]
        
        # Get latest tag of repo where crd.yaml is present
        latest_crd_tag=gt.fetch_latest_tag(crd_repo,predefined.TOKEN)
        if latest_crd_tag is None:
            print(f"Unable to get the latest tag for the repo {crd_repo}")
            sys.exit(-1)

        # Get CRD from the crd.yaml file of the latest tag
        crd_file=gt.fetch_file_from_tag(crd_repo,predefined.TOKEN,latest_crd_tag,predefined.GIT_REPO_CRD_PATH)
        if crd_file is None:
            print(f"Unable to fetch CRD for the repo {crd_repo}")
            sys.exit(-1)

        # Checking and filter for the defined CRDs only
        crd=yt.filter_defined_crds(crd_file)
        if crd is None:
            print(f"Expected CRD not found from repo {crd_repo} with tag {latest_crd_tag}")
            sys.exit(-1)

        crd_name=yt.get_nested_value(crd,["metadata","name"])
        # Parse Schema of the CRD
        # crd_fields will be of format { path,type,condition}
        # path - path from root where the fields are present
        # type - indicates if it's a string,bool,object
        # condition - None as of now, reserved for future use
        crd_fields=yt.get_parsed_fields(crd)
        if crd_fields is None:
            print(f"Unable to parse the fields for CRD {crd_name}")
            sys.exit(-1)

        missing_fields = []
        for item in crd_fields:
            if item["path"] not in template_fields:
                missing_fields.append(item["path"])

        print(f"=======  Missing Fields for {crd_name}  =============")
        print(missing_fields)

if __name__ == "__main__":
    main()
