"""Custom filters for rootless Docker collection."""


def _apt_arch_from_ansible(arch):
    mapping = {
        "x86_64": "amd64",
        "amd64": "amd64",
        "aarch64": "arm64",
        "arm64": "arm64",
        "armv7l": "armhf",
    }
    return mapping.get(arch, arch)


class FilterModule(object):
    """Ansible filter plugin entrypoint."""

    def filters(self):
        return {
            "rootless_docker_apt_arch": _apt_arch_from_ansible,
        }
