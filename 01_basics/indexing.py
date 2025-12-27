HospitalData = [
    "|HR=120/80mg|BT=37C|Sugar=95mg|",
    "|HR=140/90mg|BT=38C|Sugar=110mg|",
    "|HR=110/70mg|BT=36C|Sugar=85mg|",
    "|HR=160/100mg|BT=39C|Sugar=140mg|",
    "|HR=130/85mg|BT=37C|Sugar=100mg|"
]

patient_no = 1

for data in HospitalData:
    code = data.split("|")

    heart_rate = code[1].replace("HR=", "").replace("mg", "")
    Body_Temp  = code[2].replace("BT=", "").replace("C", "")
    Sugar      = code[3].replace("Sugar=", "").replace("mg", "")
    
    sugar_mg = int(Sugar)
    sugar_mol = sugar_mg / (180 * 1000)          
    sugar_mol_rounded = round(sugar_mol, 6)      

    print("╔════════════════════════════════╗")
    print(f"║        Patient {patient_no:<6}          ║")
    print("╠════════════════════════════════╣")
    print(f"║ Heart Rate : {heart_rate:<10}        ║")
    print(f"║ Body Temp  : {Body_Temp} °C        ║")
    print(f"║ Sugar      : {Sugar} mg : {sugar_mol_rounded} mol ║")
    print("╚════════════════════════════════╝\n")

    patient_no += 1
