import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_normal_logs(num_entries=2000):
    logs = []
    base_time = datetime.now() - timedelta(hours=10)
    for _ in range(num_entries):
        base_time += timedelta(seconds=random.randint(1, 30))
        logs.append({
            "timestamp": base_time.strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": fake.ipv4(),
            "username": fake.user_name(),
            "success": random.choices(["True", "False"], weights=[85, 15])[0]
        })
    return logs

def inject_brute_force(logs):
    attack_ip = "192.168.1.199"
    attack_time = datetime.now() - timedelta(hours=2)
    for i in range(50):
        attack_time += timedelta(seconds=random.randint(1, 5))
        logs.append({
            "timestamp": attack_time.strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": attack_ip,
            "username": "admin",
            "success": "False"
        })
    return logs

def inject_credential_stuffing(logs):
    attack_ip = "10.0.0.88"
    attack_time = datetime.now() - timedelta(hours=1)
    usernames = [fake.user_name() for _ in range(40)]
    for username in usernames:
        attack_time += timedelta(seconds=random.randint(2, 8))
        logs.append({
            "timestamp": attack_time.strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": attack_ip,
            "username": username,
            "success": "False"
        })
    return logs

def save_logs(logs, filename="auth_logs.csv"):
    random.shuffle(logs)
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "source_ip", "username", "success"])
        writer.writeheader()
        writer.writerows(logs)
    print(f"Saved {len(logs)} log entries to {filename}")

if __name__ == "__main__":
    logs = generate_normal_logs()
    logs = inject_brute_force(logs)
    logs = inject_credential_stuffing(logs)
    save_logs(logs)