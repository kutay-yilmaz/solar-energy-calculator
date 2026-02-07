import numpy as np
import matplotlib.pyplot as plt
# SOLAR TRACKER VS FIXED PANEL ANALYSIS
def run_tracking_comparison():
    # 1. PARAMETERS
    hours = np.linspace(6, 18, 100) # From 6 AM to 6 PM
    # Incident angle for fixed panel (Cosine loss)
    # At noon (12:00), angle is 0 (max power)
    angles = (hours - 12) * 15 # 15 degrees per hour
    fixed_output = np.cos(np.radians(angles))
    # Tracker keeps the angle at 0 all day
    tracker_output = np.ones(len(hours)) * 0.95 # 5% loss for motor energy
    # 2. PLOTTING
    plt.figure(figsize=(10, 5))
    plt.plot(hours, fixed_output, label='Fixed Panel (Static)', color='blue')
    plt.plot(hours, tracker_output, label='Single-Axis Tracker', color='green', linestyle='--')
    plt.fill_between(hours, fixed_output, tracker_output, color='yellow', alpha=0.2, label='Energy Gain')
    # 3. RESULTS
    plt.title('Energy Generation: Fixed vs. Tracking System')
    plt.xlabel('Hour of Day')
    plt.ylabel('Normalized Power Output')
    plt.xticks(np.arange(6, 19, 1))
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    print("Tracking comparison analysis complete.")
if __name__ == "__main__":
    run_tracking_comparison()
