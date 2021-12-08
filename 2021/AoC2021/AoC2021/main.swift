import Foundation

let start = mach_absolute_time()

day2_2()

let end = mach_absolute_time()

print()
print("Ran in \(Double(end - start) / Double(NSEC_PER_SEC)) seconds")
