import numpy as np

# Load data
climate_data = np.genfromtxt('data/climate.txt', delimiter=',', skip_header=1)

# Weights
weights = np.array([0.3, 0.2, 0.5])

# Compute yields
yields = climate_data @ weights

# Combine results
climate_results = np.concatenate((climate_data, yields.reshape(15, 1)), axis=1)

# Save results
np.savetxt(
    'data/climate_results.txt',
    climate_results,
    fmt='%.2f',
    header='temperature, rainfall, humidity, yield_of_apples',
    comments=''
)

print("Done. File saved.")
