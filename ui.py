from tkinter import Tk, Button, Listbox, END, Scrollbar, Frame
import subprocess
from commands import get_commands

class CommandUI:
    def __init__(self, master):
        self.master = master
        master.title("Bash Command Executor")

        self.frame = Frame(master)
        self.frame.pack()

        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side='right', fill='y')

        self.command_listbox = Listbox(self.frame, yscrollcommand=self.scrollbar.set)
        self.command_listbox.pack(side='left', fill='both', expand=True)
        self.scrollbar.config(command=self.command_listbox.yview)

        self.commands = get_commands()
        for command in self.commands:
            self.command_listbox.insert(END, command)

        self.execute_button = Button(master, text="Execute Command", command=self.execute_command)
        self.execute_button.pack()

    def execute_command(self):
        selected_command_index = self.command_listbox.curselection()
        if selected_command_index:
            command = self.commands[selected_command_index[0]]
            subprocess.run(command, shell=True)

def main():
    root = Tk()
    command_ui = CommandUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()