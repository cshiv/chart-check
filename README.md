
# Introduction

In the operator development process, Kubernetes manifests are developed first and then translated into Helm charts. This approach introduces the possibility of omitting fields due to manual errors. If any fields were historically omitted, they will continue to be absent.

This program scans both the Custom Resource Definition (CRD) and the templates in the Helm chart for the corresponding Custom Resource. If any fields that should be present in the Helm chart are missing, they will be highlighted.

This ensures that no fields from the CRD are missed in the Helm templates.

# How it works

Program gets the latest tag for both the CRD and the Helm Chart template for the Database. Latest tag is derived based on the semantic versioning of the tag.
Program parses the CRD object(OpenAPI V3 Schema) and lists all the possible fields from the CRD.On the other hand, template related to the respectibe Custom Resource are scanned. 
If there are any fields which needs to be omitted in the process, it can be configured as described in the below sections.


# ALL THE CONFIGURATIONS POSSIBLE

All the configurable sections are present [here](https://github.com/cshiv/chart-check/blob/2ca719b5f999592d8cb99071709adbc12fc29a6e/src/predefined.py#L1).
Some important configurations are 

<strong>IGNORE_CRD_PATH:</strong> There are several fields which are managed by the operators and which users have no control. Without this configuration, script will highlight these fields as missing from the helm chart. This is predominantly a one time activity and to make it easier, it takes regular expression , so we don’t need to put every single field. However if there are any new fields added to the CRD which cannot be managed by the user, this needs to be added here.
<strong>ADD_HELM_PATH:</strong> Very similar to IGNORE_CRD_PATH and probably this will never be used, but I wanted to keep this buffer in case we find something in future. IGNORE_CRD_PATH excludes things from CRD fields, ADD_HELM_PATH adds fields in Helm template fields. Missing fields is calculated by CRD fields - Helm template fields, so there are 2 options to tweak the results if needed.
</strong>ITEMS_TO_PARSE:</strong> Indicates for which Operator the program should run. For now possible values are GIT_PG_INFO , GIT_PXC_INFO , GIT_PSMDB_INFO . In future if more operators needs to be checked, it should be very simple by adding the relevant variables in predefined file.
</strong>tag_pattern:</strong> For each CRD, tags to be filtered with a specific pattern are added here.For example all PXC DB chart tags start with pxc-db , all PSMDB chart tags start with psmdb-db . If there is a need to check release candidates or other patterns, this can be modified.