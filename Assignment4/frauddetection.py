from datetime import datetime, timedelta
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
                if email != prev_email and (t - prev_time) <= timedelta(hours=24):
                    frauds.append(
                        f"{order['id']} - Matches previous order {prev_id} (different email, same address)"
                    )
                    break  

        
        address_map.setdefault(addr_norm, []).append((order["id"], email, t))

    return frauds

orders = [
    {"id": "ORD001", "email": "john@email.com", "address": "123 Main Street, Apt 4B, NYC", "timestamp": "2025-10-23 10:00"},
    {"id": "ORD002", "email": "jane@email.com", "address": "456 Oak Ave, Boston", "timestamp": "2025-10-23 10:15"},
    {"id": "ORD003", "email": "bob@email.com", "address": "123 Main St, Apartment 4B, NYC", "timestamp": "2025-10-23 10:30"},
    {"id": "ORD004", "email": "alice@email.com", "address": "789 Pine Road, Seattle", "timestamp": "2025-10-23 11:00"},
    {"id": "ORD005", "email": "charlie@email.com", "address": "123 Main Street Apt 4-B New York City", "timestamp": "2025-10-23 12:00"},
]

fraud_list = detect_fraud(orders)

print("FRAUD ALERT:")
for f in fraud_list:
    print(f)
