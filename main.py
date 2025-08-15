from license_guard import validate_or_exit
validate_or_exit()
import os as _o, sys as _s, json as _j, time as _t, uuid as _u, hashlib as _h
import threading as _th, asyncio as _ay
import requests as _rq
from discord import listener as _discord_listener
from src.roblox import roblox_main as _roblox_main
def _b64d(_x):  
    import base64 as _b
    return _b.b64decode(_x).decode("utf-8")
def _hw():
    _mac = _u.getnode()
    _sys_id = f"{_mac}{_o.environ.get('COMPUTERNAME','')}{_o.environ.get('USERDOMAIN','')}"
    return _h.sha256(_sys_id.encode()).hexdigest()
_SERVER = "https://serverhaha.onrender.com/verify" 
_CFG = _b64d(b'Y29uZmlnLmpzb24=')  
_K = _b64d(b'a2V5')               
_H = _b64d(b'aHd pZA=='.replace(b' ', b''))  
_STATUS = _b64d(b'c3RhdHVz')       
_OK = {_b64d(b'dmFsaWQ='), _b64d(b'T0s=')}
def _load():
    try:
        if _o.path.exists(_CFG):
            with open(_CFG, "r", encoding="utf-8") as f:
                return _j.load(f)
    except Exception:
        pass
    return {}
def _save(d):
    try:
        with open(_CFG, "w", encoding="utf-8") as f:
            _j.dump(d, f, indent=2)
    except Exception:
        pass
def _verify_or_exit():
    _cfg = _load()
    _key = _cfg.get(_K)
    _finger = _hw()
    if not _SERVER.endswith("/verify"):
        _srv = _SERVER.rstrip("/") + "/verify"
    else:
        _srv = _SERVER
    def _ask_key():
        try:
            return input("Enter your license key: ").strip()
        except EOFError:
            return ""
    if not _key:
        _key = _ask_key()
    try:
        _r = _rq.get(_srv, params={_K: _key, _H: _finger}, timeout=10)
        if _r.status_code != 200:
            print(f"❌ Error: { _r.status_code } { _r.text }")
            _s.exit(1)
        try:
            _data = _r.json()
        except Exception:
            print("❌ Invalid response from license server.")
            _s.exit(1)
        _st = str(_data.get(_STATUS, "")).lower()
        if _st not in {x.lower() for x in _OK}:
            if _st == "expired":
                print("❌ License expired. Please contact support.")
            elif _st == "hwid_mismatch":
                print("❌ HWID mismatch. Please contact support to reset your device binding.")
            else:
                print(f"❌ License invalid or error: {_data}")
            try:
                if _o.path.exists(_CFG):
                    _o.remove(_CFG)
            except Exception:
                pass
            _s.exit(1)
        _cfg[_K] = _key
        _save(_cfg)
        print("✅ License valid. Starting program...")
    except Exception as _e:
        print(f"❌ Could not contact license server: {_e}")
        _s.exit(1)
def _start_app():
    print("\033[35m" + "Roblox AutoJoiner")
    print("\033[35m" + "Version: 1.0.2")
    print("\033[35m" + "Starting in 2 seconds...")
    _t.sleep(2)
    _th.Thread(target=_roblox_main, daemon=True).start()
    _ay.run(_discord_listener())
if __name__ == "__main__":
    _verify_or_exit()
    _start_app()
