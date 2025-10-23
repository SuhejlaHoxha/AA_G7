import re

def normalize_address(address):
    address = address.lower()
    address = re.sub(r'[^\w\s]', '', address) 
    address = re.sub(r'\s+', ' ', address).strip()

    replacements = {
        "street": "st",
        "road": "rd",
        "avenue": "ave",
        "apartment": "apt",
        "suite": "apt",
        "new york city": "nyc",
        "ny": "nyc"
    }
    for k, v in replacements.items():
        address = address.replace(k, v)
    return address
