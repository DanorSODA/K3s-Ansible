import subprocess
import logging

# Configure logging to display informational messages
logging.basicConfig(level=logging.INFO)


# Function to run the Ansible playbook
# -------------------------------------
# This function runs the Ansible playbook using the 'subprocess.run' method. It calls the
# 'ansible-playbook' command with the inventory and playbook file (install_k3s.yml).
# If the playbook runs successfully, it logs an informational message.
# If the playbook fails (raises CalledProcessError), it logs an error and raises the exception again.
def run_ansible_playbook():
    try:
        # Log the start of the Ansible playbook execution
        logging.info("Running Ansible playbook...")

        # Run the Ansible playbook using the 'ansible-playbook' command
        # The '-i' option specifies the inventory file, and 'install_k3s.yml' is the playbook to run.
        subprocess.run(
            ["ansible-playbook", "-i", "inventory", "install_k3s.yml"], check=True
        )

        # Log the successful execution of the playbook
        logging.info("Playbook executed successfully.")

    # Handle any errors that occur during the playbook execution
    # -----------------------------------------------------------
    # If 'subprocess.run' encounters an error (non-zero exit code), it raises a CalledProcessError.
    # This block catches the error, logs it, and re-raises the exception for further handling (if needed).
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the playbook: {e}")
        raise


# Main script execution block
if __name__ == "__main__":
    run_ansible_playbook()
