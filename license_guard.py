import os
import json
import base64
import requests
_B64 = b'aHR0cHM6Ly9zZXJ2ZXJoYWhhLm9ucmVuZGVyLmNvbS92ZXJpZnk='
_URL = base64.b64decode(_B64).decode()
CONFIG_DIR = os.path.join(os.getenv('PROGRAMDATA') or os.getcwd(), 'KhalidAutoJoiner')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')
def _get_saved_key():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
            return data.get("license_key")
        except Exception:
            return None
    return None
def _save_key(key):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"license_key": key}, f)
def _check(key):
    try:
        import platform, hashlib
        hwid = hashlib.sha256(platform.node().encode()).hexdigest()
        r = requests.get(_URL, params={"key": key, "hwid": hwid}, timeout=10)
        if r.status_code == 200:
            result = r.json()
            status = result.get("status", "error")
            if status == "valid":
                return True, "✅ License valid."
            elif status == "expired":
                return False, "❌ License expired."
            elif status == "hwid_mismatch":
                return False, "❌ HWID mismatch."
            elif status == "invalid":
                return False, "❌ License invalid."
            else:
                return False, f"❌ Unknown status: {status}"
        return False, "❌ Server error."
    except Exception as e:
        return False, f"⚠️ Error contacting server: {e}"
def validate_or_exit():
    key = _get_saved_key()
    while True:
        if key:
            print(f"Using saved license key: {key}")
        else:
            key = input("Enter your license key: ").strip()
        status, message = _check(key)
        print(message)
        if status:
            _save_key(key)
            print("✅ License saved locally.")
            return
        else:
            print("❌ License invalid. Please try again.")
            key = None
