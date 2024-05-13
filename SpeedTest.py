import speedtest
import tkinter as tk
from tkinter import ttk

class InternetSpeedTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")
        self.root.geometry("300x200")

        # Create a frame for the speed test results
        self.speed_test_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.speed_test_frame.pack(fill="both", expand=True)

        # Create a label to display the speed test results
        self.speed_label = ttk.Label(self.speed_test_frame, text="Performing speed test...", font=("Helvetica", 14))
        self.speed_label.pack(pady=20)

        # Create a button to run the speed test
        self.run_button = ttk.Button(self.speed_test_frame, text="Run Speed Test", command=self.update_speed_label)
        self.run_button.pack(pady=10)

    def internet_speed_test(self):
        # Create speedtest object
        st = speedtest.Speedtest()
        
        # Perform speed test
        st.get_best_server()
        download_speed = st.download() / 1_000_000   # Convert to Mbps
        upload_speed = st.upload() / 1_000_000       # Convert to Mbps
        
        return download_speed, upload_speed

    def update_speed_label(self):
        download_speed, upload_speed = self.internet_speed_test()
        self.speed_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    root = tk.Tk()
    gui = InternetSpeedTestGUI(root)
    root.mainloop()