# IGNORE_CRD_PATH indicates the fields which needs to be ignored when the parsing is done.
# Fields which are handled by the operator or the fields which users cannot control are added here.
# This is also a field for temporarily disabling a field for matching.
# This is a list of key-value pairs. Key is the name of the CRD derived from the crd.yaml file, i.e metadata.name,
# ensure the CRD name in the crd.yaml file and here matches otherwise the fields might be missed from parsing
# Fields are regular expression, so if you want to skip all the fields starting from spec.users, just add spec.users.* here

IGNORE_CRD_PATH = {
    "perconaservermongodbs.psmdb.percona.com": [
        "spec.backup.containerSecurityContext.*",
        "spec.backup.podSecurityContext.*",
        "spec.initContainerSecurityContext.*",
        "spec.pmm.containerSecurityContext.*",
        "spec.replsets.affinity.advanced.*",
        "spec.replsets.arbiter.affinity.advanced.*",
        "spec.replsets.arbiter.sidecar.*",
        "spec.replsets.arbiter.topologySpreadConstraints.*",
        "spec.replsets.containerSecurityContext.*",
        "spec.replsets.livenessProbe.*",
        "spec.replsets.nonvoting.affinity.advanced.*",
        "spec.replsets.nonvoting.containerSecurityContext.*",
        "spec.replsets.nonvoting.livenessProbe.*",
        "spec.replsets.nonvoting.podSecurityContext.*",
        "spec.replsets.nonvoting.readinessProbe.*",
        "spec.replsets.nonvoting.sidecar*",
        "spec.replsets.nonvoting.topologySpreadConstraints.*",
        "spec.replsets.podSecurityContext.*",
        "spec.replsets.readinessProbe.*",
        "spec.replsets.sidecar*",
        "spec.replsets.topologySpreadConstraints.*",
        "spec.sharding.configsvrReplSet.affinity.advanced.*",
        "spec.sharding.configsvrReplSet.arbiter.affinity.advanced.*",
        "spec.sharding.configsvrReplSet.arbiter.sidecar.*",
        "spec.sharding.configsvrReplSet.arbiter.topologySpreadConstraints.*",
        "spec.sharding.configsvrReplSet.containerSecurityContext.*",
        "spec.sharding.configsvrReplSet.livenessProbe.*",
        "spec.sharding.configsvrReplSet.nonvoting.affinity.advanced.*",
        "spec.sharding.configsvrReplSet.nonvoting.containerSecurityContext.*",
        "spec.sharding.configsvrReplSet.nonvoting.livenessProbe.*",
        "spec.sharding.configsvrReplSet.nonvoting.podSecurityContext.*",
        "spec.sharding.configsvrReplSet.nonvoting.readinessProbe.*",
        "spec.sharding.configsvrReplSet.nonvoting.sidecar*",
        "spec.sharding.configsvrReplSet.nonvoting.topologySpreadConstraints.*",
        "spec.sharding.configsvrReplSet.podSecurityContext.*",
        "spec.sharding.configsvrReplSet.readinessProbe.*",
        "spec.sharding.configsvrReplSet.sidecar*",
        "spec.sharding.configsvrReplSet.topologySpreadConstraints.*",
        "spec.sharding.mongos.affinity.advanced.*",
        "spec.sharding.mongos.containerSecurityContext.*",
        "spec.sharding.mongos.livenessProbe.*",
        "spec.sharding.mongos.podSecurityContext.*",
        "spec.sharding.mongos.readinessProbe.*",
        "spec.sharding.mongos.sidecar*",
        "spec.sharding.mongos.topologySpreadConstraints.*"
    ],
    "perconapgclusters.pgv2.percona.com": [
        "spec.backups.pgbackrest.jobs.affinity.*",
        "spec.backups.pgbackrest.jobs.securityContext.*",
        "spec.backups.pgbackrest.repoHost.affinity.*",
        "spec.backups.pgbackrest.repoHost.securityContext.*",
        "spec.backups.pgbackrest.repoHost.topologySpreadConstraints.*",
        "spec.backups.pgbackrest.restore.affinity.*",
        "spec.dataSource.pgbackrest.affinity.*",
        "spec.dataSource.postgresCluster.affinity.*",
        "spec.instances.affinity.*",
        "spec.instances.initContainers.*",
        "spec.instances.securityContext.*",
        "spec.instances.sidecars.env.*",
        "spec.instances.sidecars.envFrom*",
        "spec.instances.sidecars.lifecycle.*",
        "spec.instances.sidecars.livenessProbe.*",
        "spec.instances.sidecars.readinessProbe.*",
        "spec.instances.sidecars.securityContext.*",
        "spec.instances.sidecars.startupProbe.*",
        "spec.pmm.containerSecurityContext.*",
        "spec.proxy.pgBouncer.affinity.*",
        "spec.proxy.pgBouncer.config.files.*",
        "spec.proxy.pgBouncer.securityContext.*",
        "spec.proxy.pgBouncer.sidecars.env.*",
        "spec.proxy.pgBouncer.sidecars.lifecycle.*",
        "spec.proxy.pgBouncer.sidecars.livenessProbe.*",
        "spec.proxy.pgBouncer.sidecars.readinessProbe.*",
        "spec.proxy.pgBouncer.sidecars.securityContext.*",
        "spec.proxy.pgBouncer.sidecars.startupProbe.*",
        "spec.proxy.pgBouncer.topologySpreadConstraints.*",
        "spec.dataSource.pgbackrest.configuration.configMap.*",
        "spec.backups.pgbackrest.configuration.configMap.*",
        "spec.backups.pgbackrest.configuration.downwardAPI.*",
        "spec.backups.pgbackrest.configuration.secret.*",
        "spec.proxy.pgBouncer.sidecars.*",
        "spec.instances.topologySpreadConstraints.*",
        "spec.instances.topologySpreadConstraints.*",
        "spec.dataSource.pgbackrest.configuration.downwardAPI.*",
        "spec.dataSource.pgbackrest.configuration.secret.*"
    ],

    "perconaxtradbclusters.pxc.percona.com": [
        ".*.containerSecurityContext.*",
        ".*.podSecurityContext.*",
        ".*.readinessProbes.*",
        ".*.livenessProbes.*",
        ".*.securityContext.*",
        ".*.livenessProbe.*",
        ".*.affinity.advanced.*",
        ".*.topologySpreadConstraints.*",
        "spec.haproxy.imagePullSecrets.name",
        "spec.haproxy.lifecycle.*",  
        "spec.haproxy.sidecar*",  
        "spec.proxysql.lifecycle.*",    
        "spec.pxc.lifecycle.*", 
        "spec.pxc.sidecar*",
        "spec.proxysql.sidecar.*"            
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
# crd_branch: Name of the branch from where CRD file needs to be picked. If left empty, latest tag will be taken
# template_file: Location of template file for the custom resource with respect to helm template repo
# template_branch: Name of the branch from where template of the helm chart needs to be taken, If left empty, latest tag will be taken
# tag_pattern: Pattern of tags used in the helm charts repo , for example PXC DB chart uses the format pxc-db-X.Y.Z
#              Pattern will have the character set for comparison with regular expression
# cr_name: Custom Resource name used in the template of a chart. This is used for exceptions when needed
GIT_PXC_INFO={
    "crd_repo": "percona/percona-xtradb-cluster-operator",
    "crd_branch": "",
    "template_file": "charts/pxc-db/templates/cluster.yaml",
    "template_branch": "",
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