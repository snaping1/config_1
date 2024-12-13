import argparse
from shell_gui import ShellGUI 

def main():
    parser = argparse.ArgumentParser(description="Shell Emulator GUI")
    parser.add_argument('--username', required=True, help='Имя пользователя для приглашения в командной строке')
    parser.add_argument('--fs', required=True, help='Путь к tar-архиву виртуальной файловой системы')
    parser.add_argument('--log', required=True, help='Путь к CSV файлу для логирования')
    parser.add_argument('--config', required=False, help='Путь к стартовому скрипту')

    args = parser.parse_args()

    shell_gui = ShellGUI(args.username, args.fs, args.log, args.config)
    if args.config:
        with open(args.config, 'r') as script:
            for line in script:
                shell_gui.command_entry.insert(len(f"{shell_gui.shell.username}@shell: {shell_gui.shell.current_dir} $ "), line.strip())
                shell_gui.execute_command()
    shell_gui.run()

if __name__ == "__main__":
    main()
