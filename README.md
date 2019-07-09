# Content Collector

The Ansible content collector is an Ansible playbook designed to assist in the creation of an Ansible collection and migrate content from an Ansible distribution into that collection.

For an overview of Ansible collections, see the Ansible documentation. https://docs.ansible.com/

## Getting started

Clone this repo

```
git clone https://github.com/ansible/content_collector.git
```

The content collector requires an Ansible distribution from which content will be mirgated.

```
cd content_collector
wget https://releases.ansible.com/ansible/ansible-latest.tar.gz
tar -xvf ansible-latest.tar.gz
```

Update the `site.yml` with the desired collection details:

- `ansible_source_directory`: The location of the Ansible distribution from which content will be migrated (e.g. `./ansible-2.8.2`)
- `destination_directory`: The destination directory in which the collection will be built. (e.g. `~/my_ansible_collection`)
- `collection_organization`: The collection organization. (e.g. `contoso`)
- `collection_name`: The name of the collection. (e.g. `myos`)
- `source_sub_directory`: The source directory within `modules` and `module_utils` from which content will be migrated. (e.g. `/network/myos`)

Run the Ansible playbook:

```
ansible-playbook site.yaml
```

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
        │   │   ├── myos_func1.py
        │   │   ├── myos_func2.py
        │   │   └── myos_func3.py
        │   └── module_utils
        │       └── network
        │           └── myos
        │               ├── __init__.py
        │               └── myos.py
        └── roles
```
