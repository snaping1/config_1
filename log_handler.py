import csv
from datetime import datetime

class LogHandler:
    def __init__(self, log_path, username):
        self.log_path = log_path
        self.username = username
    
    def log(self, command):
        with open(self.log_path, 'a', newline='') as log_file:
            writer = csv.writer(log_file)
            writer.writerow([self.username, datetime.now(), command])
