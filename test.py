import time
import random

# 2**46  random numbers yieled 1 year.

# 2**46/2**256 = 2**-210%

total_numbers = 2**(int(input(f'Total Numbers: 2**')));
time_before = time.time()

# a guess of how many random numbers I can generate a second
counter = 0
while True:
    # Generate a random number
    random_number = random.random()
    
    # Increment counter
    counter += 1
    
    # Check if 1 second has elapsed
    time_after = time.time()
    elapsed_time = time_after - time_before
    if elapsed_time >= 1:
        # Calculate and print the rate
        rate = counter / elapsed_time
        print(f"Random numbers generated per second: {rate:.2f}")
        break

rate_per_second = rate

time_seconds = total_numbers / rate_per_second

# Convert time to years for better readability
time_years = time_seconds / (365.25 * 24 * 60 * 60)

print(f"It will take approximately {time_seconds:.2f} seconds or {time_years:.2f} years to generate {total_numbers} random numbers.")
