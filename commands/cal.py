import calendar
import datetime

def cal(shell_gui, args):
    if len(args) == 0:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        display_month(shell_gui, year, month)
    elif args[0] == "-3":
        now = datetime.datetime.now()
        
        previous_month = (now.month - 1) if now.month > 1 else 12
        previous_year = now.year if now.month > 1 else now.year - 1
        next_month = (now.month + 1) if now.month < 12 else 1
        next_year = now.year if now.month < 12 else now.year + 1

        display_months_in_row(shell_gui, previous_year, previous_month, now.year, now.month, next_year, next_month)
    elif len(args) == 1:
        year = int(args[0])
        display_year(shell_gui, year)
    elif len(args) == 2:
        month = int(args[0])
        year = int(args[1])
        display_month(shell_gui, year, month)
    else:
        shell_gui.display_output("Неверное количество аргументов. Используйте: cal [-3 | месяц год | год].")

def display_months_in_row(shell_gui, prev_year, prev_month, curr_year, curr_month, next_year, next_month):
    cal = calendar.TextCalendar()

    prev_month_str = cal.formatmonth(prev_year, prev_month)
    curr_month_str = cal.formatmonth(curr_year, curr_month)
    next_month_str = cal.formatmonth(next_year, next_month)

    prev_month_lines = prev_month_str.splitlines()
    curr_month_lines = curr_month_str.splitlines()
    next_month_lines = next_month_str.splitlines()

    max_lines = max(len(prev_month_lines), len(curr_month_lines), len(next_month_lines))

    for i in range(max_lines):
        prev_line = prev_month_lines[i] if i < len(prev_month_lines) else ""
        curr_line = curr_month_lines[i] if i < len(curr_month_lines) else ""
        next_line = next_month_lines[i] if i < len(next_month_lines) else ""

        output = (prev_line.ljust(25) + 
                  curr_line.ljust(25) + 
                  next_line.ljust(25))  
        shell_gui.display_output(output)


def display_month(shell_gui, year, month):
    cal_text = calendar.month(year, month)
    shell_gui.display_output(cal_text)

def display_year(shell_gui, year):
    shell_gui.display_output(f"{year}".center(28))
    for month in range(1, 13):
        cal_text = calendar.month(year, month)
        shell_gui.display_output(cal_text+"\n\n")
