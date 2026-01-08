data = "BP:120/80 HR=72% Temp=38.9C Sugar -155mg chol=190mg LDL=110mg HDL=45mg"

# Blood Pressure
bp = data[data.index("BP:")+3 : data.index("HR")].strip()
systolic, diastolic = [int(x) for x in bp.split("/")]

# Heart Rate
hr = int(data[data.index("HR=")+3 : data.index("%")])

# Temperature
temp = float(data[data.index("Temp=")+5 : data.index("C")])

# Sugar
sugar = int(data[data.index("Sugar -")+7 : data.index("mg")])
sugar_mm = round((sugar / 180.18) * 1000, 3)

# Cholesterol
chol_str = float(data[data.index("chol=")+5 : data.index("mg", data.index("chol="))])
chol_mm = round((chol_str / 180.18) * 1000, 3)

# LDL
ldl = float(data[data.index("LDL=")+4 : data.index("mg", data.index("LDL="))])
ldl_mm = round((ldl / 180.18) * 1000, 3)

# HDL
hdl = float(data[data.index("HDL=")+4 : data.index("mg", data.index("HDL="))])
hdl_mm = round((hdl / 180.18) * 1000, 3)

# Output
print("Systolic:", systolic, "Diastolic:", diastolic, "Heart rate:", hr, "Body Temperature:", temp, "Sugar Level:", sugar + sugar_mm)
print("Cholesterol:", chol_str + chol_mm, "LDL:", ldl_mm, "HDL:", hdl_mm)
