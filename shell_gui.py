import tkinter as tk
from tkinter import scrolledtext
from emulator import ShellEmulator
import os


class ShellGUI:
    def __init__(self, username, tar_path, log_path, script_path=None):
        self.shell = ShellEmulator(username, tar_path, log_path)

        self.root = tk.Tk()
        self.root.title(f"{self.shell.username}@shell")
        
        self.root.configure(bg="#2e2e2e")
        self.root.geometry("600x400")

        self.font = ('Monaco', 12)

        self.output_display = scrolledtext.ScrolledText(
            self.root, width=80, height=20, wrap=tk.WORD, state=tk.DISABLED, bg="#1e1e1e", fg="#ffffff", font=self.font
        )
        self.output_display.grid(row=0, column=0, padx=10, pady=10)

        self.command_entry = tk.Entry(
            self.root, font=self.font, bg="#1e1e1e", fg="#ffffff", insertbackground="white", width=80
        )
        self.command_entry.bind("<Return>", self.on_command_entered)
        self.command_entry.bind("<Key>", self.prevent_prompt_edit)
        self.command_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.update_prompt()

    def on_command_entered(self, event):
        """Handler for pressing Enter key"""
        command = self.command_entry.get().strip()

        if command.startswith(self.prompt):
            command = command[len(self.prompt):].strip()

        self.output_display.config(state=tk.NORMAL)
        self.output_display.insert(tk.END, f"$ {command}\n")
        self.output_display.config(state=tk.DISABLED)

        self.execute_command(command)

    def execute_command(self, command):
        """Execute the entered command"""
        if command:
            self.shell.execute_command(command, self)

        self.command_entry.delete(0, tk.END)
        self.update_prompt()

    def update_prompt(self):
        """Update the prompt text in the command entry"""
        self.prompt = f"{self.shell.username}@shell: {self.shell.current_dir} $ "
        self.command_entry.delete(0, tk.END)
        self.command_entry.insert(0, self.prompt)
        self.command_entry.icursor(len(self.prompt))

    def prevent_prompt_edit(self, event):
        """Prevent the user from editing the prompt"""
        prompt_length = len(self.prompt)
        cursor_position = self.command_entry.index(tk.INSERT)

        if cursor_position < prompt_length or (
            event.keysym in ("BackSpace", "Delete") and cursor_position <= prompt_length
        ):
            return "break"

    def truncate_path(self, path, max_length=30):
        """Truncate the directory path if it exceeds a certain length"""
        if len(path) > max_length:
            path_parts = path.split(os.sep)
            truncated = os.sep.join(path_parts[-2:])  
            return f".../{truncated}"
        return path

    def display_output(self, *output):
        output = " ".join(output)
        """Display the result of a command in the output window"""
        self.output_display.config(state=tk.NORMAL)
        self.output_display.insert(tk.END, f"{output}\n")
        self.output_display.config(state=tk.DISABLED)
        self.output_display.yview(tk.END)

    def run(self):
        """Start the GUI event loop"""
        self.root.mainloop()
