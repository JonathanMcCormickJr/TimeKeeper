import tkinter as tk
from datetime import datetime, timedelta

class TimeKeeperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TimeKeeper App")

        self.total_worked_time = timedelta(0)
        self.last_clock_in_time = None
        self.is_clocked_in = False

        # Status border frame
        self.status_frame = tk.Frame(self.root, bg="#7F0000", bd=10)  # Initial color red for clocked out
        self.status_frame.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)

        self.frame = tk.Frame(self.status_frame)
        self.frame.pack(pady=20, padx=20)

        self.clock_in_button = tk.Button(self.frame, text="Clock In", command=self.clock_in)
        self.clock_in_button.pack(fill=tk.BOTH, expand=True)

        self.clock_out_button = tk.Button(self.frame, text="Clock Out", command=self.clock_out)
        self.clock_out_button.pack(fill=tk.BOTH, expand=True, pady=5)

        self.show_logs_button = tk.Button(self.frame, text="Show Logs", command=self.show_logs)
        self.show_logs_button.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(self.frame, height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.total_time_label = tk.Label(self.frame, text="Total Worked Time: 00:00:00")
        self.total_time_label.pack(pady=5)

        self.load_logs()
        self.update_clock()

    def update_status_frame(self):
        color = "green" if self.is_clocked_in else "#7F0000"
        self.status_frame.config(bg=color)

    def load_logs(self):
        try:
            with open("punch_log.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    action, time_str = line.strip().split(": ", 1)
                    time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                    if action == "Clocked In":
                        self.last_clock_in_time = time
                        self.is_clocked_in = True
                    elif action == "Clocked Out":
                        if self.last_clock_in_time:
                            self.total_worked_time += (time - self.last_clock_in_time)
                            self.last_clock_in_time = None
                        self.is_clocked_in = False
        except FileNotFoundError:
            pass
        self.update_status_frame()

    def update_clock(self):
        if self.is_clocked_in and self.last_clock_in_time:
            elapsed = datetime.now() - self.last_clock_in_time
            current_total = self.total_worked_time + elapsed
            hours, remainder = divmod(current_total.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            formatted_time = f'{hours:02}:{minutes:02}:{seconds:02}'
            self.total_time_label.config(text=f"Total Worked Time: {formatted_time}")
        self.root.after(1000, self.update_clock)

    def clock_in(self):
        current_time = datetime.now()
        self.last_clock_in_time = current_time
        self.is_clocked_in = True
        self.update_status_frame()
        self.log_text.insert(tk.END, f"Clocked In: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.write_to_log(f"Clocked In: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def clock_out(self):
        current_time = datetime.now()
        if self.is_clocked_in and self.last_clock_in_time:
            elapsed = current_time - self.last_clock_in_time
            self.total_worked_time += elapsed
            self.last_clock_in_time = None
            self.is_clocked_in = False
        self.update_status_frame()
        self.log_text.insert(tk.END, f"Clocked Out: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.write_to_log(f"Clocked Out: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def show_logs(self):
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, "Punch History:\n")
        try:
            with open("punch_log.txt", "r") as file:
                lines = file.readlines()
                self.log_text.insert(tk.END, ''.join(lines))
        except FileNotFoundError:
            self.log_text.insert(tk.END, "Log file not found. No history available.\n")

    def write_to_log(self, message):
        with open("punch_log.txt", "a") as file:
            file.write(f"{message}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeKeeperApp(root)
    root.mainloop()
