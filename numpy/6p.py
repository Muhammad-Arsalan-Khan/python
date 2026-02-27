# handeling missing data/values
import numpy as np
arr = np.array([1, 2, np.nan, 4, 5])
print("Original array with NaN:", arr)
print("Is NaN:", np.isnan(arr))  # Check for NaN values
print("Mean ignoring NaN:", np.nanmean(arr))  # Calculate mean while ignoring NaN values
print("Replace NaN with mean:", np.where(np.isnan(arr), np.nanmean(arr), arr))  # Replace NaN with mean value
print("Replace NaN with 0:", np.nan_to_num(arr))  # Replace NaN with 0
print("Replace NaN with 7:", np.nan_to_num(arr, nan=7))  # Replace NaN with 7
print("--------------------------------")
print(np.nan == np.nan) # NaN is not equal to itself
print(np.isnan(np.nan)) # Check if NaN is NaN (True)
print(np.isnan(5)) # Check if 5 is NaN (False)

# infinity
arr_inf = np.array([1, 2, np.inf, 4, 5, -np.inf])
print("Original array with Inf:", arr_inf)
print("Is Inf:", np.isinf(arr_inf))  # Check for Inf values
print("Replace Inf with 0:", np.where(np.isinf(arr_inf), 0, arr_inf))  # Replace Inf with 0
print("Replace Inf with 999:", np.where(np.isinf(arr_inf), 999, arr_inf))  # Replace Inf with 999
print("Replace Inf with 999:", np.where(np.isinf(arr_inf), np.nanmean(arr), arr_inf))  # Replace Inf with 999
print("repplace -Inf with 7:", np.where(arr_inf == -np.inf, 7, arr_inf))  # Replace -Inf with 7
print("replace Inf with 10:", np.where(arr_inf == np.inf, 10, arr_inf))  # Replace Inf with 10

print("repplace -Inf with 12:", np.nan_to_num(arr_inf, neginf=12, posinf=15))  # Replace -Inf with 12

print("repplace -Inf with 12:", np.nan_to_num(arr_inf, neginf=12))  # Replace -Inf with 12, 
print("replace Inf with 15:", np.nan_to_num(arr_inf ,posinf=15))  # Replace Inf with 15
# agar hum sirf pos ya sirf neg ko replace karnay gay tu like hum postive ko replace tu positive tu replace ho jaye ga or negivate main min floate value replace ho jaye ga -1.79769313e+308 or agar sirv neg ko replace kare gay tu max float value replace ho jaye ga 1.79769313e+308
print("--------------------------------")   
