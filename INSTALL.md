# K3s Offline Installation with Ansible - Installation Guide

## Step-by-Step Installation Instructions

Follow this guide to install and set up the K3s cluster using the provided Ansible playbook, which supports an offline installation for both master and agent nodes.

1. **Clone the Project**

Begin by cloning the project repository from your version control system.

```sh
git clone https://github.com/DanorSODA/K3s-Ansible
cd K3s-Ansible
```

2. **Place K3s Binaries in the Correct Directory**

Once you have downloaded the binaries (as mention in the README.md file), place them in the appropriate directories:

- Master Node Setup:
  - Place the k3s binary and k3s-airgap-images-amd64.tar file in the roles/k3s_master/files/ directory.

```sh
cp /path/to/k3s roles/k3s_master/files/
cp /path/to/k3s-airgap-images-amd64.tar roles/k3s_master/files/
```

- Agent Nodes Setup:
  - Place the k3s binary and k3s-airgap-images-amd64.tar file in the roles/k3s_agent/files/ directory.

```sh
cp /path/to/k3s roles/k3s_agent/files/
cp /path/to/k3s-airgap-images-amd64.tar roles/k3s_agent/files/
```

3. **Configure the Inventory File**

The inventory file (inventory) specifies the master and agent nodes' IP addresses.
Open the inventory file and modify it to match your environment by replacing <Master_Node_IP>, <Agent_Node1_IP>, and <Agent_Node2_IP> with the actual IP addresses of your nodes.

4. **Set Up SSH Access**

Ensure that you have passwordless SSH access set up between your control machine and the target nodes (master and agents).
This is required for Ansible to be able to connect and execute tasks on the remote nodes.

5. **Run the Ansible Playbook**

With everything configured, you're ready to run the playbook and install K3s on the nodes.

A Python script (run_ansible_playbook.py) is provided to simplify the process.
You can run the playbook by executing this script:

```sh
python3 run_ansible_playbook.py
```
