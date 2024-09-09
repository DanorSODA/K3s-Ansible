import subprocess


def run_ansible_playbook():
    try:
        subprocess.run(
            ["ansible-playbook", "-i", "inventory", "install_k3s.yml"], check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the playbook: {e}")


if __name__ == "__main__":
    run_ansible_playbook()
