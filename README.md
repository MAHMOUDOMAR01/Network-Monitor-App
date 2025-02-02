# Network Monitor App

## Description
This is a simple GUI-based Network Monitoring application built using Python and Tkinter. It tracks and displays the upload and download speeds in real-time and plots them on a graph using Matplotlib.

## Features
- Displays real-time upload and download speeds.
- Provides a graphical representation of network speed over time.
- Uses `psutil` for network data monitoring.
- Multithreading ensures smooth GUI updates.
- Simple and user-friendly interface.

## Technologies Used
- Python
- Tkinter (for GUI)
- psutil (for network monitoring)
- Matplotlib (for plotting graphs)
- Threading (for real-time data processing)

## Installation
1. Install Python (3.x recommended) if not already installed.
2. Install the required dependencies using pip:
   ```sh
   pip install psutil matplotlib
   ```
3. Clone or download the project files.
4. Run the script:
   ```sh
   python network_monitor.py
   ```

## How to Use
1. Run the script to launch the application.
2. The upload and download speeds will be displayed in real-time.
3. A graph will visualize the speed variations over time.
4. Close the application when finished.

## Files and Structure
```
network_monitor.py  # Main application file
README.md           # Documentation
```

## Future Enhancements
- Add an option to export network speed data to a CSV file.
- Improve graph visualization with dynamic scaling.
- Implement additional network statistics.

## Disclaimer
This application is for educational and monitoring purposes only. It should not be used for critical network performance assessments.

