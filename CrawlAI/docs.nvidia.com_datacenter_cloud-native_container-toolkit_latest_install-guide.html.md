[Skip to main content](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#main-content)
Back to top `Ctrl`+`K`
[ ![NVIDIA Container Toolkit - Home](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg) ![NVIDIA Container Toolkit - Home](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) NVIDIA Container Toolkit ](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
Search `Ctrl`+`K`
Light Dark System Settings
Search `Ctrl`+`K`
[ ![NVIDIA Container Toolkit - Home](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg) ![NVIDIA Container Toolkit - Home](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) NVIDIA Container Toolkit ](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
Light Dark System Settings
Table of Contents
NVIDIA Container Toolkit
  * [Overview](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
  * [Installing the Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
  * [Running a Sample Workload](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html)
  * [Platform support](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html)
  * [Troubleshooting](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/troubleshooting.html)
  * [Release Notes](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/release-notes.html)


Advanced Configuration
  * [Architecture Overview](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/arch-overview.html)
  * [Container Device Interface](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)
  * [Specialized Configurations with Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html)


1.17.5
[1.17.5](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.5install-guide.html)[1.17.4](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.4install-guide.html)[1.17.3](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.3install-guide.html)[1.17.2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.2install-guide.html)[1.17.1](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.1install-guide.html)[1.17.0](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.0install-guide.html)[1.16.2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.16.2install-guide.html)[1.16.1](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.16.1install-guide.html)[1.16.0](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.16.0install-guide.html)
  * [NVIDIA Docs Hub](https://docs.nvidia.com)
  * [Cloud Native Technologies](https://docs.nvidia.com/datacenter/cloud-native)
  * [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
  * Installing the NVIDIA Container Toolkit


# Installing the NVIDIA Container Toolkit[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit "Permalink to this headline")
## Installation[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation "Permalink to this headline")
### Prerequisites[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#prerequisites "Permalink to this headline")
  1. Read [this section](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) about platform support.
  2. Install the NVIDIA GPU driver for your Linux distribution. NVIDIA recommends installing the driver by using the package manager for your distribution. For information about installing the driver with a package manager, refer to the [_NVIDIA Driver Installation Quickstart Guide_](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html). Alternatively, you can install the driver by [downloading](https://www.nvidia.com/en-us/drivers/) a `.run` installer.


### With `apt`: Ubuntu, Debian[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian "Permalink to this headline")
Note
These instructions [should work](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) for any Debian-derived distribution.
  1. Configure the production repository:
```
$ curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
 && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

```
Copy to clipboard
Optionally, configure the repository to use experimental packages:
```
$ sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list

```
Copy to clipboard
  2. Update the packages list from the repository:
```
$ sudo apt-get update

```
Copy to clipboard
  3. Install the NVIDIA Container Toolkit packages:
```
$ sudo apt-get install -y nvidia-container-toolkit

```
Copy to clipboard


### With `dnf`: RHEL/CentOS, Fedora, Amazon Linux[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-dnf-rhel-centos-fedora-amazon-linux "Permalink to this headline")
Note
These instructions [should work](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) for many RPM-based distributions.
  1. Configure the production repository:
```
$ curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
 sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo

```
Copy to clipboard
Optionally, configure the repository to use experimental packages:
```
$ sudo dnf-config-manager --enable nvidia-container-toolkit-experimental

```
Copy to clipboard
  2. Install the NVIDIA Container Toolkit packages:
```
$ sudo dnf install -y nvidia-container-toolkit

```
Copy to clipboard


### With `zypper`: OpenSUSE, SLE[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-zypper-opensuse-sle "Permalink to this headline")
  1. Configure the production repository:
```
$ sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo

```
Copy to clipboard
Optionally, configure the repository to use experimental packages:
```
$ sudo zypper modifyrepo --enable nvidia-container-toolkit-experimental

```
Copy to clipboard
  2. Install the NVIDIA Container Toolkit packages:
```
$ sudo zypper --gpg-auto-import-keys install -y nvidia-container-toolkit

```
Copy to clipboard


## Configuration[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuration "Permalink to this headline")
### Prerequisites[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#id1 "Permalink to this headline")
  * You installed a supported container engine (Docker, Containerd, CRI-O, Podman).
  * You installed the NVIDIA Container Toolkit.


### Configuring Docker[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker "Permalink to this headline")
  1. Configure the container runtime by using the `nvidia-ctk` command:
```
$ sudo nvidia-ctk runtime configure --runtime=docker

```
Copy to clipboard
The `nvidia-ctk` command modifies the `/etc/docker/daemon.json` file on the host. The file is updated so that Docker can use the NVIDIA Container Runtime.
  2. Restart the Docker daemon:
```
$ sudo systemctl restart docker

```
Copy to clipboard


#### Rootless mode[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode "Permalink to this headline")
To configure the container runtime for Docker running in [Rootless mode](https://docs.docker.com/engine/security/rootless/), follow these steps:
  1. Configure the container runtime by using the `nvidia-ctk` command:
```
$ nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json

```
Copy to clipboard
  2. Restart the Rootless Docker daemon:
```
$ systemctl --user restart docker

```
Copy to clipboard
  3. Configure `/etc/nvidia-container-runtime/config.toml` by using the `sudo nvidia-ctk` command:
```
$ sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place

```
Copy to clipboard


### Configuring containerd (for Kubernetes)[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-containerd-for-kubernetes "Permalink to this headline")
  1. Configure the container runtime by using the `nvidia-ctk` command:
```
$ sudo nvidia-ctk runtime configure --runtime=containerd

```
Copy to clipboard
The `nvidia-ctk` command modifies the `/etc/containerd/config.toml` file on the host. The file is updated so that containerd can use the NVIDIA Container Runtime.
  2. Restart containerd:
```
$ sudo systemctl restart containerd

```
Copy to clipboard


### Configuring containerd (for nerdctl)[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-containerd-for-nerdctl "Permalink to this headline")
No additional configuration is needed. You can just run `nerdctl run --gpus=all`, with root or without root. You do not need to run the `nvidia-ctk` command mentioned above for Kubernetes.
See also the [nerdctl documentation](https://github.com/containerd/nerdctl/blob/main/docs/gpu.md).
### Configuring CRI-O[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-cri-o "Permalink to this headline")
  1. Configure the container runtime by using the `nvidia-ctk` command:
```
$ sudo nvidia-ctk runtime configure --runtime=crio

```
Copy to clipboard
The `nvidia-ctk` command modifies the `/etc/crio/crio.conf` file on the host. The file is updated so that CRI-O can use the NVIDIA Container Runtime.
  2. Restart the CRI-O daemon:
```
$ sudo systemctl restart crio

```
Copy to clipboard


### Configuring Podman[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-podman "Permalink to this headline")
For Podman, NVIDIA recommends using [CDI](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html) for accessing NVIDIA devices in containers.
## Next Steps[#](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#next-steps "Permalink to this headline")
  * [Running a Sample Workload](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html)


[ previous Overview ](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html "previous page") [ next Running a Sample Workload ](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html "next page")
On this page 
  * [Installation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation)
    * [Prerequisites](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#prerequisites)
    * [With `apt`: Ubuntu, Debian](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian)
    * [With `dnf`: RHEL/CentOS, Fedora, Amazon Linux](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-dnf-rhel-centos-fedora-amazon-linux)
    * [With `zypper`: OpenSUSE, SLE](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-zypper-opensuse-sle)
  * [Configuration](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuration)
    * [Prerequisites](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#id1)
    * [Configuring Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker)
      * [Rootless mode](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode)
    * [Configuring containerd (for Kubernetes)](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-containerd-for-kubernetes)
    * [Configuring containerd (for nerdctl)](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-containerd-for-nerdctl)
    * [Configuring CRI-O](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-cri-o)
    * [Configuring Podman](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-podman)
  * [Next Steps](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#next-steps)


[ ![NVIDIA](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg) ![NVIDIA](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg) ](https://www.nvidia.com)
[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Manage My Privacy](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Do Not Sell or Share My Data](https://www.nvidia.com/en-us/preferences/start/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)
Copyright © 2020-2025, NVIDIA Corporation. 
