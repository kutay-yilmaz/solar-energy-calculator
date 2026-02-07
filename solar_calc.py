# Solar Energy Yield Calculator
# Developer: Kutay Yilmaz
# Description: Calculates daily, monthly, and yearly energy output of a PV system based on inputs.

def calculate_yield():
    print("--- SOLAR PV YIELD CALCULATOR ---")
    print("Welcome! Let's calculate your energy production.\n")

    try:
        # User Inputs
        panel_power = float(input("Enter single panel power (Watts) [e.g., 450]: "))
        panel_count = int(input("Enter number of panels [e.g., 20]: "))
        sun_hours = float(input("Enter average daily peak sun hours (h) [e.g., 5.5 for Mersin]: "))
        
        # System Efficiency (Performance Ratio)
        # Standard loss due to cables, dust, temperature is usually around 14-20%.
        # We assume a Performance Ratio (PR) of 80% (0.80).
        pr = 0.80 

        # Calculations
        total_capacity_kw = (panel_power * panel_count) / 1000  # kWp
        daily_generation = total_capacity_kw * sun_hours * pr   # kWh
        monthly_generation = daily_generation * 30              # kWh
        yearly_generation = daily_generation * 365              # kWh

        # Results Output
        print("\n--- CALCULATION RESULTS ---")
        print(f"Total System Size: {total_capacity_kw:.2f} kWp")
        print(f"Daily Production : {daily_generation:.2f} kWh")
        print(f"Monthly Production: {monthly_generation:.2f} kWh")
        print(f"Yearly Production : {yearly_generation:.2f} kWh")
        print("---------------------------")
        print("Note: Calculation assumes a standard Performance Ratio (PR) of 80%.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

# Run the function
if __name__ == "__main__":
    calculate_yield()
