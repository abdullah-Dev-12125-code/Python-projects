
cnic = ["35202-1234567-1","444-abc-222","42501-4455667-3","invalid","61101-8877665-2"]

cnic_valid = []
cnic_karachi = []
cnic_invalids = []

def extracting_valid_cnic():
    for extract in cnic:
        length = len(extract)
        if length >= 15:
            cnic_valid.append(extract)

extracting_valid_cnic()

print("All valid CNIC-S",cnic_valid)

def karchi_extract_cnic():
    for karachi in cnic:
        if karachi[0:5] == '42501':
            cnic_karachi.append(karachi)
karchi_extract_cnic()
print("ALl CNIC'S from karachi",cnic_karachi)

def karachi_invalid_cnic():
    for extract in cnic:
        length = len(extract)
        if length < 15 or extract == 'invalid':
            cnic_invalids.append(extract)

karachi_invalid_cnic()


print("All invalid CNIC'S",cnic_invalids)