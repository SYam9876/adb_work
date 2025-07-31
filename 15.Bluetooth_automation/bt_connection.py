import re
import subprocess
from datetime import datetime

# File paths
LOG_FILE = "logcat_log.txt"
BT_DUMPSYS_FILE = "dumpsy_log.txt"
DEVICE_NAME = "OnePlus Nord Buds 3"
MAC_PREFIX = "08:12:87"

# Regex for MAC
MAC_REGEX = r"([0-9A-F]{2}[:-]){5}([0-9A-F]{2})"

# LMP to Bluetooth version map
LMP_MAP = {
    0: "1.0b", 1: "1.1", 2: "1.2", 3: "2.0 + EDR", 4: "2.1 + EDR",
    5: "3.0 + HS", 6: "4.0", 7: "4.1", 8: "4.2", 9: "5.0",
    10: "5.1", 11: "5.2", 12: "5.3", 13: "5.4"
}

def get_android_version():
    try:
        output = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"], text=True)
        return output.strip()
    except:
        return "Unknown"

def parse_datetime(date_str):
    try:
        full_date_str = f"2025-{date_str}"
        return datetime.strptime(full_date_str, "%Y-%m-%d %H:%M:%S.%f")
    except:
        return None

def fmt(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S.%f") if dt else "Unknown"

def extract_timestamps(lines, pattern, mac=None):
    timestamps = []
    for line in lines:
        if pattern in line and (mac is None or mac.lower() in line.lower()):
            match = re.match(r"(\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)", line)
            if match:
                timestamps.append(match.group(1))
    return timestamps

def extract_best_detection_time(lines, acl_time):
    detection_times = []
    for line in lines:
        if "BluetoothDeviceInfo" in line and DEVICE_NAME in line:
            match = re.match(r"(\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)", line)
            if match:
                t = parse_datetime(match.group(1))
                if t:
                    detection_times.append(t)
    if acl_time:
        detection_times = [t for t in detection_times if t <= acl_time]
    return max(detection_times) if detection_times else None

def extract_mac_address(lines):
    for line in lines:
        if DEVICE_NAME in line:
            macs = re.findall(MAC_REGEX, line, re.IGNORECASE)
            for mac in macs:
                return mac[0] + mac[1]
    return None

def extract_bt_version_and_mac_from_dumpsys(file_path, target_mac_prefix):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(rf"\[({re.escape(target_mac_prefix)}.*?)\]\n(.*?)(?=\n\[|\Z)", re.DOTALL)
    match = pattern.search(content)
    if not match:
        return None, "Unknown", None

    mac = match.group(1).strip()
    block = match.group(2)

    lmp_match = re.search(r"LmpVer\s*=\s*(\d+)", block)
    lmp_version = int(lmp_match.group(1)) if lmp_match else None
    bt_version = LMP_MAP.get(lmp_version, f"Unknown (LMP {lmp_version})" if lmp_version is not None else "Unknown")

    return mac, bt_version, lmp_version

def main():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logcat_lines = f.readlines()
    except FileNotFoundError:
        print(f"[ERROR] Log file '{LOG_FILE}' not found.")
        return

    try:
        with open(BT_DUMPSYS_FILE, "r", encoding="utf-8") as f:
            dumpsys_lines = f.readlines()
    except FileNotFoundError:
        dumpsys_lines = []

    mac_address = extract_mac_address(logcat_lines) or "Unknown"
    android_version = get_android_version()

    bt_version = "Unknown"
    lmp_version = None

    # Try to extract BT version and MAC from dumpsys-style file if available
    if dumpsys_lines:
        full_mac, bt_version, lmp_version = extract_bt_version_and_mac_from_dumpsys(BT_DUMPSYS_FILE, MAC_PREFIX)
        if full_mac:
            mac_address = full_mac

    acl_timestamps = extract_timestamps(logcat_lines, "ACTION_ACL_CONNECTED", mac=mac_address)
    a2dp_timestamps = extract_timestamps(logcat_lines, "A2DP", mac=mac_address)

    acl_time = parse_datetime(acl_timestamps[0]) if acl_timestamps else None
    a2dp_time = parse_datetime(a2dp_timestamps[0]) if a2dp_timestamps else None
    detection_time = extract_best_detection_time(logcat_lines, acl_time)

    connection_time = None
    if acl_time and a2dp_time:
        connection_time = (a2dp_time - acl_time).total_seconds()

    print("\n===== Bluetooth Connection Report =====\n")
    print(f"Device Name         : K S SYAMKRISHNA's {DEVICE_NAME}")
    print(f"MAC Address         : {mac_address}")
    print(f"Bluetooth Version   : {bt_version}")
    print(f"Android Version     : {android_version}")
    print(f"First Detected At   : {fmt(detection_time)}")
    print(f"ACL Connected At    : {fmt(acl_time)}")
    print(f"A2DP Connected At   : {fmt(a2dp_time)}")

    if connection_time is not None:
        print(f"\nConnection Time      : {connection_time:.2f} seconds")
    else:
        print(f"\nConnection Time      : Could not calculate (incomplete data)")

    print("\n======================================\n")

if __name__ == "__main__":
    main()
