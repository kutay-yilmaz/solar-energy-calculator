import numpy as np
import matplotlib.pyplot as plt
# SOLAR PANEL EFFICIENCY & SHADING ANALYSIS
def run_efficiency_study():
    # 1. PARAMETERS
    standard_eff = 0.20 # 20% Efficiency
    temp_coeff = -0.004 # -0.4% loss per degree Celsius
    ambient_temps = np.linspace(15, 55, 100) # From 15C to 55C
    shading_factors = [0, 0.1, 0.3, 0.5] # 0% to 50% shading
    # 2. CALCULATION
    plt.figure(figsize=(10, 6))
    for shade in shading_factors:
        # P_out = P_STC * (1 - shade) * (1 + coeff * (T_cell - 25))
        efficiency = standard_eff * (1 - shade) * (1 + temp_coeff * (ambient_temps - 25))
        plt.plot(ambient_temps, efficiency * 100, label=f'Shading: {shade*100}%')
    # 3. PLOTTING
    plt.title('Solar Panel Efficiency vs Temperature & Shading')
    plt.xlabel('Ambient Temperature (Celsius)')
    plt.ylabel('System Efficiency (%)')
    plt.axvline(x=25, color='gray', linestyle='--', label='STC Temp (25C)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    print("Efficiency analysis generated.")
if __name__ == "__main__":
    run_efficiency_study()
