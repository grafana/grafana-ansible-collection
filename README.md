# Ansible Collection for Grafana Cloud

[![CI Tests](https://github.com/grafana/grafana-ansible-collection/actions/workflows/ci-test.yml/badge.svg)](https://github.com/grafana/grafana-ansible-collection/actions/workflows/ci-test.yml)
[![Full Integration Test](https://github.com/grafana/grafana-ansible-collection/actions/workflows/full-integration-test.yml/badge.svg?branch=main)](https://github.com/grafana/grafana-ansible-collection/actions/workflows/full-integration-test.yml)

This collection (grafana.grafana) contains modules and plugins to assist in automating managing of resources in <b>Grafana Cloud</b> with Ansible.

- [Ansible collection Documentation](https://grafana.github.io/grafana-ansible-collection/)
- [Grafana website](https://grafana.com)
- [Grafana Cloud website](https://grafana.com/products/cloud/)

## Ansible version compatibility
The collection is tested and supported with:

* ansible >= 2.9

## Installing the collection

Before using the Grafana collection, you need to install it using the below commoand:

```shell
ansible-galaxy collection install grafana.grafana
```

You can also include it in a `requirements.yml` file and install it via ansible-galaxy collection install -r `requirements.yml`, using the format:

```yaml
---
collections:
  - name: grafana.grafana
```
A specific version of the collection can be installed by using the version keyword in the `requirements.yml` file:

```yaml
---
collections:
  - name: grafana.grafana
    version: 1.0.0
```
## Using this collection

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `grafana.grafana.cloud_stack`:
```yaml
- name: Using grafana collection
  hosts: localhost
  tasks:
    - name: Create a Grafana Cloud stack
      grafana.grafana.cloud_stack:
        name: mystack
        stack_slug: mystack
        org_slug: myorg
        cloud_api_key: "{{ cloud_api_key }}"
        region: eu
        state: present
```

or you can add full namespace and collection name in the `collections` element in your playbook
```yaml
- name: Using grafana collection
  hosts: localhost
  collection:
    - grafana.grafana
  tasks:
    - name: Create a Grafana Cloud stack
      cloud_stack:
        name: mystack
        stack_slug: mystack
        org_slug: myorg
        cloud_api_key: "{{ cloud_api_key }}"
        region: eu
        state: present
```

## Contributing
We are accepting Github pull requests and issues. There are many ways in which you can participate in the project, for example:

* Submit bugs and feature requests, and help us verify them
* Submit and review source code changes in Github pull requests
* Add new modules for more Grafana resources

## Testing and Development

If you want to develop new content for this collection or improve what is already
here, the easiest way to work on the collection is to clone it into one of the configured
[`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths),
and work on it there.

### Testing with `ansible-test`

We use `ansible-test` for sanity.

## Releasing, Versioning and Deprecation

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

We plan to regularly release new minor or bugfix versions once new features or bugfixes have been implemented.

Releasing the current major version on GitHub happens from the `main` branch by the [GitHub Release Workflow](https://github.com/grafana/grafana-ansible-collection/blob/main/.github/workflows/release.yml)
Before the [GitHub Release Workflow](https://github.com/grafana/grafana-ansible-collection/blob/main/.github/workflows/release.yml) is run, Contributors should push the new version on Ansible Galaxy Manually.

We currently are not planning any deprecations or new major releases. The current landscape includes minor version updates for Module's documentation in 1.1.1.

## Code of Conduct
This collection follows the Ansible project's [Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html). Please read and familiarize yourself with this doc

## More information

- [Maintainer guidelines](https://docs.ansible.com/ansible/devel/community/maintainers.html)
- Subscribe to the [news-for-maintainers](https://github.com/ansible-collections/news-for-maintainers) repo and track announcements there. 
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## License

GPL-3.0-or-later
