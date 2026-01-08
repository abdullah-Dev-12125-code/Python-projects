resp = "name == steams ;; age == 27 ;; score == 88 ;; country == pak"

pairs = resp.split(";;")
clean_data = {}

for p in pairs:
    key, val = p.split("==")
    key = key.strip()
    val = val.strip()
  
    if val.isdigit():
        val = int(val)
    else:
        pass

    clean_data[key] = val

print(clean_data)



