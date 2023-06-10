period = int(input())
doctors = 7
untreated = 0
treated = 0
counter = 0

for n in range(0, period):
    patients = int(input())
    counter += 1
    if counter % 3 == 0 and untreated > treated:
        doctors += 1
    if patients <= doctors:
        treated += patients
    elif patients > doctors:
        treated += doctors
        untreated += abs(patients-doctors)


print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
