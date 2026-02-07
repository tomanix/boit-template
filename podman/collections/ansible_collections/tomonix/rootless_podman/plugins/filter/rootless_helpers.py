"""Custom filters for rootless Podman collection."""


def _rootless_podman_supported(distribution, os_family):
    if os_family == "Debian":
        return distribution in {"Debian", "Ubuntu"}
    if os_family == "RedHat":
        return distribution in {"RedHat", "Rocky", "AlmaLinux", "CentOS", "OracleLinux"}
    return False


def _rootless_podman_packages(os_family, install_compose):
    base = []
    if os_family == "Debian":
        base = [
            "podman",
            "uidmap",
            "dbus-user-session",
            "slirp4netns",
            "fuse-overlayfs",
            "containernetworking-plugins",
        ]
    elif os_family == "RedHat":
        base = [
            "podman",
            "shadow-utils",
            "dbus-daemon",
            "slirp4netns",
            "fuse-overlayfs",
            "containernetworking-plugins",
        ]

    if install_compose:
        base.append("podman-compose")

    return base


def _rootless_podman_socket(uid):
    return f"unix:///run/user/{uid}/podman/podman.sock"


class FilterModule(object):
    """Ansible filter plugin entrypoint."""

    def filters(self):
        return {
            "rootless_podman_supported": _rootless_podman_supported,
            "rootless_podman_packages": _rootless_podman_packages,
            "rootless_podman_socket": _rootless_podman_socket,
        }
