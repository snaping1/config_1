def history(shell_gui, self):
    for idx, cmd in enumerate(self.history):
        shell_gui.display_output(f"{idx + 1}: {cmd}")