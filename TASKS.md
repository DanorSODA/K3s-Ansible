# Project Tasks

## Completed Tasks

1. **K3s Master and Agent Roles:**

   - Created separate Ansible roles for setting up K3s master and agent nodes.
   - Added offline support by including binaries and airgap images in the role's files directories.
   - Set up tasks to copy the binaries and airgap images, and to install K3s on master and agent nodes.
   - Included dynamic configuration for the agent nodes to connect to the master using the master IP and token.

2. **Ansible Playbook:**

   - Developed an Ansible playbook (install_k3s.yml) to orchestrate the installation of K3s on master and agent nodes.
   - Configured the playbook to dynamically retrieve the master IP and token for agents to join the cluster.

3. **Python Script:**

   - Created a Python script (run_ansible_playbook.py) to automate the execution of the Ansible playbook.
   - Added basic logging for monitoring the playbook execution.

4. **Inventory Setup:**
   - Set up the inventory file to define master and agent node IP addresses.
