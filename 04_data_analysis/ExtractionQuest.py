# ------------------------
# Task 1: Parse Encrypted ID
# ------------------------
encrypted_id = "USR-2026-11-PAK-98342-XY"

region = encrypted_id[0:3]
year = encrypted_id[4:8]
month = encrypted_id[9:11]
country = encrypted_id[12:15]
serial = encrypted_id[-8:-3]
random = encrypted_id[22:25]

print("Region:", region)
print("Year:", year)
print("Month:", month)
print("Country:", country)
print("Serial:", serial)
print("Random:", random)

# Validate year
int_year = int(year)
if 2020 <= int_year <= 2025:
    print("This is valid:", int_year)
else:
    print("This is not valid!!")

# ------------------------
# Task 2: Parse Log Entry
# ------------------------
log = 'IP:192.168.1.22 [STATUS=404] ENDPOINT="/api/v1/users" TIME=0.452s'

# Extract IP
ip = log[log.index(":")+1 : log.index(" ")]
# Extract status code
status = log[log.index("=")+1 : log.index("]", log.index("="))]
# Extract endpoint
endpoint = log.split('ENDPOINT="')[1].split('"')[0]
# Extract response time
time = float(log.split("TIME=")[1].replace("s", ""))

print("\nIP Address:", ip)
print("Status Code:", status)
print("Endpoint:", endpoint)
print("Response Time:", time, "seconds")

# Check if status code indicates error
if int(status) >= 400:
    print("FALSE: Status code indicates an error.")
else:
    print("Status code is OK.")

# ------------------------
# Task 3: Parse Raw Sensor Data
# ------------------------
raw = "Age: 21 yrs,height: 5.8ft,weight = 65kg,Tempreature = 39.9C,humidity = 85%"
clean = raw.replace(" ", "").lower()

age = int(clean[clean.index("age:")+4 : clean.index("yrs")])
height = float(clean[clean.index("height:")+7 : clean.index("ft")])
weight = int(clean[clean.index("weight=")+7 : clean.index("kg")])
temp = float(clean[clean.index("tempreature=")+12 : clean.index("c")])
humidity = int(clean[clean.index("humidity=")+9 : clean.index("%")])

print(f"""
Age: {age}
Height: {height} ft
Weight: {weight} kg
Temperature: {temp} C
Humidity: {humidity} %
""")
