import numpy as np
import matplotlib.pyplot as plt

# Calculate weight loss progression over 4 months (120 days)
days = np.arange(0, 121, 1)
daily_weight_loss = 23 / 120  # Pounds lost per day
weight_progression = 198 - daily_weight_loss * days

# Plot the weight loss progression
plt.figure(figsize=(10, 6))
plt.plot(days, weight_progression, label='Weight Progression')
plt.title('Projected Weight Loss Over 4 Months')
plt.xlabel('Days')
plt.ylabel('Weight (lbs)')
plt.axhline(y=175, color='r', linestyle='--', label='Target Weight (175 lbs)')
plt.legend()
plt.grid(True)
plt.show()
