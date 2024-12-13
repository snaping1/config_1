import os
def chown(fs, shell_gui, shell, args):
    if len(args) < 2:
        shell_gui.display_output("Используйте: chown <новый_владелец> <файл>")
        return
    
    new_owner, file = args[0], args[1]
    
    if not file.startswith("/"):
        file = os.path.join(shell.current_dir, file)


    file = os.path.normpath(file)
    
    try:
        fs.change_owner(file, new_owner)
    except FileNotFoundError as e:
        shell_gui.display_output(e)
