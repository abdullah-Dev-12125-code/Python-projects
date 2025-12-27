Account_information = [
    "NYC1045689",
    "LON2034581",
    "DEL9081723",
    "PAR5647382",
    "TOK7788991",
    "KHI5566778"
]

region_code = []
Branch_code = []
Customer_Number = []

def Region_Extraction():
    for Rcode in Account_information:
        region_code.append(Rcode[:3])

def Branch_code_extraction():
    for Bcode in Account_information:
        Branch_code.append(Bcode[3:5])

def Custmer_number_extraction():
    for CNcode in Account_information:
        Customer_Number.append(CNcode[5:])


Region_Extraction()
Branch_code_extraction()
Custmer_number_extraction()

print(region_code)
print(Branch_code)
print(Customer_Number,"\n")

for NYC in Account_information:
    if NYC[:3] == 'NYC':
        print("All  acounts from NewYork |",NYC)

for Branch in Account_information:
    if Branch[3:5] == '10':
        print("All accounts in branch 10 |",Branch)