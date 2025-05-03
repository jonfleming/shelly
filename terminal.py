import subprocess
from commands import get_commands
import questionary

def main():
    commands = get_commands()
    command = questionary.select(
        "Choose a command to execute:",
        choices=commands
    ).ask()
    if command:
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()