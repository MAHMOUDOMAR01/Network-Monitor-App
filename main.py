import tkinter as tk
from tkinter import ttk
import psutil
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NetworkMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Monitor")
        self.root.geometry("600x400")
        
        # Labels to display network information
        self.upload_speed_label = ttk.Label(self.root, text="Upload Speed: 0 KB/s", font=("Arial", 14))
        self.upload_speed_label.pack(pady=10)
        
        self.download_speed_label = ttk.Label(self.root, text="Download Speed: 0 KB/s", font=("Arial", 14))
        self.download_speed_label.pack(pady=10)
        
        # Graph Area
        self.figure, self.ax = plt.subplots(figsize=(5, 3))
        self.ax.set_title("Network Speed Over Time")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Speed (KB/s)")
        
        self.graph_canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.graph_canvas.get_tk_widget().pack(pady=10)
        
        # Data storage for graph plotting
        self.times = []
        self.upload_speeds = []
        self.download_speeds = []
        
        # Start the network monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitor_network)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def monitor_network(self):
        previous_sent = psutil.net_io_counters().bytes_sent
        previous_recv = psutil.net_io_counters().bytes_recv
        start_time = time.time()
        
        while True:
            # Get the current sent and received bytes
            current_sent = psutil.net_io_counters().bytes_sent
            current_recv = psutil.net_io_counters().bytes_recv
            
            # Calculate upload and download speed
            upload_speed = (current_sent - previous_sent) / 1024  # KB/s
            download_speed = (current_recv - previous_recv) / 1024  # KB/s
            
            # Update the labels with new data
            self.upload_speed_label.config(text=f"Upload Speed: {upload_speed:.2f} KB/s")
            self.download_speed_label.config(text=f"Download Speed: {download_speed:.2f} KB/s")
            
            # Append the data to the lists for graphing
            current_time = time.time() - start_time
            self.times.append(current_time)
            self.upload_speeds.append(upload_speed)
            self.download_speeds.append(download_speed)
            
            # Update graph
            self.ax.clear()
            self.ax.plot(self.times, self.upload_speeds, label="Upload Speed", color="blue")
            self.ax.plot(self.times, self.download_speeds, label="Download Speed", color="green")
            self.ax.set_title("Network Speed Over Time")
            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Speed (KB/s)")
            self.ax.legend()
            
            self.graph_canvas.draw()

            # Update previous values
            previous_sent = current_sent
            previous_recv = current_recv
            
            # Refresh every second
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMonitorApp(root)
    root.mainloop()
