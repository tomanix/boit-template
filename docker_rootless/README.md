# ansible_rootless

Projet Ansible pour installer Docker et Docker Compose en mode rootless sur Debian/Ubuntu,
avec compte de service dédié et politique de blocage d'usage Docker côté root.

## Structure

- `playbooks/install_rootless_docker.yml`: playbook principal
- `inventories/production/hosts.yml`: inventaire exemple
- `inventories/production/group_vars/all.yml`: variables globales
- `collections/ansible_collections/tomonix/rootless_docker`: collection locale

## Variables principales

- `docker_rootless_service_user`: compte de service Docker rootless
- `docker_rootless_state`: `started` ou `stopped`
- `docker_rootless_install_compose_plugin`: installe `docker compose`
- `docker_rootless_disable_system_service`: masque `docker.service`/`docker.socket`
- `docker_policy_enforce_root_cli_block`: active le blocage shell de la CLI Docker pour root

## Exécution

```bash
cd /data/Developpement/ansible_rootless
ansible-playbook playbooks/install_rootless_docker.yml
```

## Notes de sécurité

- Le daemon Docker système est masqué pour forcer le mode rootless.
- Un blocage shell est ajouté pour empêcher l'utilisation directe de `docker` par root.
- Root conserve des privilèges système intrinsèques; ce contrôle vise la politique opérationnelle.
