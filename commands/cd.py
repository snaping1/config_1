import os
def cd(fs, shell_gui, shell, args):
    if not args:
        shell_gui.display_output("Укажите путь.")
        return

    new_dir = args[0]
    
    while new_dir.startswith(".."):
        new_dir = new_dir[3:]
        shell.current_dir = "/".join(shell.current_dir.strip("/").split("/")[:-1])

    if not new_dir.startswith("/"):
        new_dir = "/" + new_dir

    normalized_dir = os.path.normpath(new_dir)

    try:
        result_dir = fs.change_dir(shell.current_dir, normalized_dir)
        shell.current_dir = result_dir

        current_dir_display = f"{shell.username}@shell: {shell.current_dir} $ "
        shell_gui.display_output(current_dir_display)
    except FileNotFoundError as e:
        shell_gui.display_output(e)

