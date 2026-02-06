# tomonix.rootless_docker

Collection Ansible pour installer Docker et Docker Compose en mode rootless sur Debian/Ubuntu.

## Roles

- `tomonix.rootless_docker.docker_repo`
- `tomonix.rootless_docker.docker_rootless`
- `tomonix.rootless_docker.docker_policy`

## Playbook example (collection)

```yaml
- hosts: docker_rootless_hosts
  become: true
  roles:
    - role: tomonix.rootless_docker.docker_repo
    - role: tomonix.rootless_docker.docker_rootless
    - role: tomonix.rootless_docker.docker_policy
```

## Run

```bash
ANSIBLE_LOCAL_TEMP=/tmp ANSIBLE_REMOTE_TEMP=/tmp \
ansible-playbook collections/ansible_collections/tomonix/rootless_docker/playbooks/install_rootless_docker.yml
```
