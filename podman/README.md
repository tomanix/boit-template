# `tomonix.rootless_podman`

Projet Ansible pour installer Podman rootless + podman-compose en mode rootless sur Debian, Ubuntu et systèmes RedHat, avec un compte de service `svc_podman`.

## Structure

- `ansible.cfg`
- `inventories/production/hosts.yml`
- `inventories/production/group_vars/all.yml`
- `playbooks/install_rootless_podman.yml`
- `collections/ansible_collections/tomonix/rootless_podman/*`

## Exécution

```bash
cd podman
ANSIBLE_LOCAL_TEMP=/tmp ANSIBLE_REMOTE_TEMP=/tmp \
ansible-playbook playbooks/install_rootless_podman.yml
```

## Rôles inclus

- `podman_repo`: prépare cache/repo selon OS
- `podman_rootless`: installe Podman rootless, `podman-compose`, configure `svc_podman`
- `container_policy`: interdit Docker côté root (service + CLI) et réserve Podman au seul compte `svc_podman`

## Variables principales

Variables globales par défaut dans `inventories/production/group_vars/all.yml`.
