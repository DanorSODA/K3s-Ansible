# K3s Offline Installation with Ansible

## Project Overview

This project provides an automated way to install K3s (a lightweight Kubernetes distribution) on both master and agent nodes using Ansible, without needing an internet connection. It achieves this by copying pre-downloaded K3s binaries and airgap images to the target nodes.

The installation process is completely offline, which is ideal for airgapped environments or locations with limited internet access.

### Key Features

- **Offline installation**: K3s is installed using pre-downloaded binaries and images.
- **Master and Agent setup**: The project supports the installation of both K3s master and agent nodes.
- **Ansible roles**: The roles for master and agent nodes are separated to allow easy management and scalability.
- **Python script for execution**: A Python script is provided to run the Ansible playbook for setting up the cluster.

## Project Structure

```plaintext
.
├── inventory               # Ansible inventory file containing master and agent nodes
├── install_k3s.yml         # Ansible playbook that orchestrates the master and agent setup
├── roles
│   ├── k3s_master          # Role for installing K3s master node
│   │   ├── files           # Directory where K3s binaries should be placed
│   │   └── tasks
│   │       └── main.yml    # Tasks for setting up K3s master node
│   └── k3s_agent           # Role for installing K3s agent nodes
│       ├── files           # Directory where K3s binaries should be placed
│       └── tasks
│           └── main.yml    # Tasks for setting up K3s agent nodes
├── run_ansible_playbook.py # Python script to run the Ansible playbook
├── README.md               # This File
├── INSTALL.md              # Install Guide of the project
├── TASKS.md                # Project Tasks completed successfully
├── Contributors.md         # Describe the contributors of the project.
```

## Requirements

Before running this project, ensure that you have the following requirements met:

1. **Ansible**

Ensure that Ansible is installed on the control machine (the machine from which you will run the playbook). To install Ansible, run:

```sh
sudo apt update
sudo apt install ansible -y
```

2. **K3s Binaries**
   Since the instal lation is done offline, you need to manually download the following K3s files: - K3s binary (k3s) - Airgap images (k3s-airgap-images-amd64.tar)
   You can download these from the K3s release page: https://github.com/k3s-io/k3s/releases
