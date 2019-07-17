# Content Collector

The Ansible content collector is an Ansible playbook designed to assist in the creation of an Ansible collection and migrate content from an Ansible distribution into that collection.

For an overview of Ansible collections, see the Ansible documentation. https://docs.ansible.com/

## Getting started

#### Clone this repo

```
git clone https://github.com/ansible/content_collector.git
```

#### The content collector requires an Ansible distribution from which content will be mirgated.

```
cd content_collector
wget https://releases.ansible.com/ansible/ansible-latest.tar.gz
tar -xvf ansible-latest.tar.gz
```

#### Update the `site.yaml` with the desired collection details:

The following are required:

- `ansible_source_directory`: The location of the Ansible distribution from which content will be migrated (e.g. `./ansible-2.8.2`)
- `destination_directory`: The destination directory in which the collection will be built. (e.g. `~/my_ansible_collection`)
- `collection_namespace`: The collection namespace. (e.g. `contoso`)
- `collection_name`: The name of the collection. (e.g. `myos`)
- `source_sub_directory`: The source directory within `modules` and `module_utils` from which content will be migrated. (e.g. `/network/myos`)

The following are optional and only used for the galaxy.yml file:

- `collection_description`: A description of the collection
- `collection_version`: The version of the collection (default=1.0.0)
- `collection_readme`: The readme file for the collection (default='README.md')
- `collection_authors`: A list of collection authors (default=[])
- `collection_dependencies`: A dictionary of collection dependencies (default={})
- `collection_license`: A list of licenses for the collection (default=[])
- `collection_tags`: A list of tags for the collection (default=[])
- `collection_repository`: The collection URL (default='')
- `collection_documentation`: The collection documentation URL (default='')
- `collection_homepage`: The colection homepage URL (default='')
- `collection_issues`: The collection issues URL (default='')

Details for the galaxy metadata fields can be found here: https://galaxy.ansible.com/docs/contributing/creating_collections.html#collection-metadata

#### Run the Ansible playbook:

```
ansible-playbook site.yaml
```

#### Update the `galaxy.yml`

A `galaxy.yml` file was generated in the root of the collection directory.  Update as needed.

## Details

1) Modules, module_utils, docs and test will be migrated into the collection.
2) Plugins will need to be manually migrated.
3) Testing is limited to `ImportError` detection by running each module.


## Example resulting collection structure

```
my_ansible_collection
└── contoso
    └── myos
        ├── docs
        ├── playbooks
        ├── plugins
        │   ├── action
        │   ├── filter
        │   ├── inventory
        │   ├── modules
        │   │   ├── __init__.py
        │   │   ├── myos_module1.py
        │   │   ├── myos_module2.py
        │   │   └── myos_module3.py
        │   └── module_utils
        │       └── network
        │           └── myos
        │               ├── __init__.py
        │               └── myos.py
        └── roles
```
