
# Introduction

In the operator development process, Kubernetes manifests are developed first and then translated into Helm charts. This approach introduces the possibility of omitting fields due to manual errors. If any fields were historically omitted, they will continue to be absent.

This program scans both the Custom Resource Definition (CRD) and the templates in the Helm chart for the corresponding Custom Resource. If any fields that should be present in the Helm chart are missing, they will be highlighted.

This ensures that no fields from the CRD are missed in the Helm templates.

# How it works

"The program retrieves the latest tag for both the CRD and the Helm chart template for the database. The latest tag is determined based on semantic versioning.

The program parses the CRD object (OpenAPI V3 Schema) and lists all the possible fields from the CRD. Meanwhile, the template related to the respective Custom Resource is scanned.

If there are any fields that need to be omitted during the process, they can be configured as described in the sections below."


# All the possible configurations

All the configurable sections are present [here](https://github.com/cshiv/chart-check/blob/2ca719b5f999592d8cb99071709adbc12fc29a6e/src/predefined.py#L1).
Some important configurations are 

<strong>IGNORE_CRD_PATH:</strong> There are several fields managed by the operators that users cannot control. Without this configuration, the script will highlight these fields as missing from the Helm chart. This is predominantly a one-time activity, and to simplify the process, it accepts regular expressions, so it’s not necessary to specify every single field. However, if any new fields are added to the CRD that cannot be managed by the user, they must be added here.

<strong>ADD_HELM_PATH:</strong> Very similar to IGNORE_CRD_PATH and probably this will never be used, but I wanted to keep this buffer in case we find something in future. IGNORE_CRD_PATH excludes things from CRD fields, ADD_HELM_PATH adds fields in Helm template fields. Missing fields is calculated by CRD fields - Helm template fields, so there are 2 options to tweak the results if needed.

<strong>ITEMS_TO_PARSE:</strong> Indicates for which Operator the program should run. For now possible values are GIT_PG_INFO , GIT_PXC_INFO , GIT_PSMDB_INFO . In future if more operators needs to be checked, it should be very simple by adding the relevant variables in predefined file.

<strong>tag_pattern:</strong> For each CRD, tags to be filtered with a specific pattern are added here.For example all PXC DB chart tags start with pxc-db , all PSMDB chart tags start with psmdb-db . If there is a need to check release candidates or other patterns, this can be modified.