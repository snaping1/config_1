import os
def ls(fs, shell_gui, current_dir, args):
    show_owners = "".join(args)
    try:
        files = fs.list_dir(current_dir)
        
        if not files:
            shell_gui.display_output("Директория пуста.")
            return

        if show_owners == "-l":
            shell_gui.display_output("FileName Owner")
        
        for file in files:
            full_path = os.path.normpath(os.path.join(current_dir, file))
            
            if show_owners == "-l":
                shell_gui.display_output(file, fs.get_owner(full_path))
            else:
                shell_gui.display_output(file)
            
    
    except FileNotFoundError:
        shell_gui.display_output(f"Ошибка: Директория '{current_dir}' не найдена.")
    except NotADirectoryError:
        shell_gui.display_output(f"Ошибка: '{current_dir}' не является директорией.")
    except Exception as e:
        shell_gui.display_output(f"Ошибка: {e}")
