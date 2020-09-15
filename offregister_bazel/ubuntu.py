from fabric.api import sudo
from fabric.contrib.files import append
from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.fs import cmd_avail


def install_bazel(from_ppa=True):
    if not from_ppa:
        raise NotImplementedError()
    elif cmd_avail("bazel"):
        return

    fname = "/etc/apt/sources.list.d/bazel.list"
    sudo("touch {}".format(fname))
    append(
        filename=fname,
        text="deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8",
        use_sudo=True,
    )
    sudo("curl https://bazel.build/bazel-release.pub.gpg | apt-key add -")
    apt_depends("openjdk-8-jdk", "bazel")
