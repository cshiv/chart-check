# IGNORE_CRD_PATH indicates the fields which needs to be ignored when the parsing is done.
# Fields which are handled by the operator or the fields which users cannot control are added here.
# This is also a field for temporarily disabling a field for matching.
# This is a list of key-value pairs. Key is the name of the CRD derived from the crd.yaml file, i.e metadata.name,
# ensure the CRD name in the crd.yaml file and here matches otherwise the fields might be missed from parsing
# Fields are regular expression, so if you want to skip all the fields starting from spec.users, just add spec.users.* here

IGNORE_CRD_PATH = {
    "perconaservermongodbs.psmdb.percona.com": [
        "spec.users.roles.*"
    ],
    "perconapgclusters.pgv2.percona.com": [

    ],
    "perconaxtradbclusters.pxc.percona.com": [

    ]
}

# ADD_HELM_PATH indicates extra paths which need to be added while parsing the template.
# Program parses the template and populates all the keys present with the full path.
# For exceptions or any temporary workarounds, it might be needed to ignore some paths which are present in the CRD,
# but not present in the template. Either field IGNORE_CRD_PATH can be used or this variable can be used to get the 
# expected output. 
ADD_HELM_PATH = {
    "PerconaServerMongoDB": [
        # "root.patha.subpathb"        
    ],
    "PerconaPGCluster": [

    ],
    "PerconaXtraDBCluster": [

    ]
}
# Git information
# 
# Variable GIT_<DATABASE>_INFO contains following values
# crd_repo: Repo from where the crd.yaml file is present
# template_file: Location of template file for the custom resource with respect to helm template repo
# tag_pattern: Pattern of tags used in the helm charts repo , for example PXC DB chart uses the format pxc-db-X.Y.Z
#              Pattern will have the character set for comparison with regular expression
# cr_name: Custom Resource name used in the template of a chart. This is used for exceptions when needed
GIT_PXC_INFO={
    "crd_repo": "percona/percona-xtradb-cluster-operator",
    "template_file": "charts/pxc-db/templates/cluster.yaml",
    "tag_pattern": "pxc-db",
    "cr_name": "PerconaXtraDBCluster"                 
}
GIT_PSMDB_INFO={
    "crd_repo":"percona/percona-server-mongodb-operator",
    "template_file": "charts/psmdb-db/templates/cluster.yaml",
    "tag_pattern": "psmdb-db",
    "cr_name": "PerconaServerMongoDB"
}
GIT_PG_INFO={
    "crd_repo":"percona/percona-postgresql-operator",
    "template_file": "charts/pg-db/templates/cluster.yaml",
    "tag_pattern": "pg-db",
    "cr_name": "PerconaPGCluster"
}
GIT_REPO_CRD_PATH="deploy/crd.yaml"
GIT_RAW_URL="https://raw.githubusercontent.com/"
GIT_API_URL="https://api.github.com"
GIT_HELM_REPO="percona/percona-helm-charts"     


# Flow Control
# Populate any one of the GIT_PXC_INFO,GIT_PSMDB_INFO,GIT_PG_INFO to kick start the process
# Only the fields enabled in ITEMS_TO_PARSE will be considered for comparison between crd and helm template
ITEMS_TO_PARSE = [GIT_PXC_INFO]   

# Github Token for the API requests
TOKEN = ""