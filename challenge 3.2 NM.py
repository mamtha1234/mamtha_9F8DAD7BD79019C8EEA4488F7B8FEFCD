def cgpa_to_percentage(cgpa):
  percentage = (cgpa - 0.5) * 10
  return percentage

try:
  cgpa = float(input("Enter your CGPA: "))
  if cgpa < 0 or cgpa > 10:
      print("CGPA should be between 0 and 10")
  else:
      percentage = cgpa_to_percentage(cgpa)
      print(f"Percentage: {percentage}%")
except ValueError:
  print("Invalid input. Please enter a valid CGPA (numeric value).")