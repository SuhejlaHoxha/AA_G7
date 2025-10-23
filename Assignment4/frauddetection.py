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


def detect_fraud(orders):
    address_map = {}
    frauds = []

    for order in orders:
        addr_norm = normalize_address(order["address"])
        t = datetime.strptime(order["timestamp"], "%Y-%m-%d %H:%M")
        email = order["email"]

        if addr_norm in address_map:
            for prev in address_map[addr_norm]:
                prev_id, prev_email, prev_time = prev
