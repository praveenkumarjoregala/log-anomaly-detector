import pandas as pd
from datetime import datetime

def load_logs(filepath="auth_logs.csv"):
    df = pd.read_csv(filepath)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

def detect_brute_force(df, threshold=8):
    failed = df[df["success"] == False]
    counts = failed.groupby("source_ip").size()
    flagged = []
    for ip in counts[counts >= threshold].index:
        flagged.append({"source_ip": ip, "attack_type": "Brute Force", "failed_attempts": int(counts[ip]), "severity": "HIGH"})
    return pd.DataFrame(flagged)

def detect_credential_stuffing(df, username_threshold=5):
    failed = df[df["success"] == False]
    ip_counts = failed.groupby("source_ip")["username"].nunique()
    flagged = []
    for ip in ip_counts[ip_counts >= username_threshold].index:
        flagged.append({"source_ip": ip, "attack_type": "Credential Stuffing", "unique_usernames_tried": int(ip_counts[ip]), "severity": "HIGH"})
    return pd.DataFrame(flagged)

def generate_report(bf, cs):
    print("\n===== SECURITY ANALYSIS REPORT =====")
    print(f"Generated: {datetime.now().strftime(chr(37)+chr(89)+chr(45)+chr(37)+chr(109)+chr(45)+chr(37)+chr(100))}\n")
    print(f"[!] Brute Force Attacks Detected: {len(bf)}")
    if not bf.empty: print(bf.to_string(index=False))
    print(f"\n[!] Credential Stuffing Attacks Detected: {len(cs)}")
    if not cs.empty: print(cs.to_string(index=False))
    print("\n=====================================")

if __name__ == "__main__":
    df = load_logs()
    generate_report(detect_brute_force(df), detect_credential_stuffing(df))
