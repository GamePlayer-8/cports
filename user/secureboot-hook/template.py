pkgname = "secureboot-hook"
pkgver = "1.0"
pkgrel = 0
archs = [
    "aarch64",
    "arm64",
    "!armhf",
    "armv7",
    "i386",
    "loongarch64",
    "ppc64",
    "!ppc64le",
    "powerpc",
    "riscv*",
    "!s390x",
    "x86_64",
]
depends = [
    "base-kernel",
    "gsed",
    "initramfs-tools",
    "sbctl",
    "systemd-boot-ukify",
]
pkgdesc = "Kernel hook for generating signed UEFI Unified Kernel Image"
license = "MIT"
url = "https://github.com/chimera-linux/cports"
options = ["etcfiles"]


def install(self):
    self.install_file(
        self.files_path / "secureboot.conf",
        "etc/default/",
        mode=0o644,
        name="secureboot",
    )

    self.install_file(
        self.files_path / "sbctl.conf.in", "usr/share/secureboot/", mode=0o644
    )

    self.install_file(
        self.files_path / "secureboot.hook",
        "usr/lib/kernel.d/",
        mode=0o755,
        name="90-secureboot-uki.sh",
    )


def post_install(self):
    self.install_license(self.files_path / "LICENSE-MIT")
