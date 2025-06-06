import platform
import time
import subprocess

def get_uptime_linux():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_sec = int(float(f.readline().split()[0]))
        return uptime_sec
    except Exception as e:
        print(f"Error getting uptime on Linux: {e}")
        return None

def get_uptime_windows():
    try:
        import ctypes
        uptime_ms = ctypes.windll.kernel32.GetTickCount64()
        uptime_sec = int(uptime_ms / 1000)
        return uptime_sec
    except Exception as e:
        print(f"Error getting uptime on Windows: {e}")
        return None

def get_uptime_macos():
    try:
        result = subprocess.run(
            ['sysctl', '-n', 'kern.boottime'],
            capture_output=True, text=True, check=True
        )
        output = result.stdout
        boot_time_str = output.strip().split('=')[1].split(',')[0].strip()
        boot_time = int(boot_time_str)
        uptime_sec = int(time.time() - boot_time)
        return uptime_sec
    except Exception as e:
        print(f"Error getting uptime on macOS: {e}")
        return None

def get_system_uptime():
    system = platform.system()
    if system == "Linux":
        return get_uptime_linux()
    elif system == "Windows":
        return get_uptime_windows()
    elif system == "Darwin":
        return get_uptime_macos()
    else:
        print(f"Platform {system} not supported for uptime check.")
        return None

def print_uptime():
    uptime_sec = get_system_uptime()
    if uptime_sec is not None:
        hours = uptime_sec // 3600
        minutes = (uptime_sec % 3600) // 60
        seconds = uptime_sec % 60
        print(f"System Uptime: {hours} hours, {minutes} minutes, {seconds} seconds")
    else:
        print("Could not determine system uptime.")

if __name__ == "__main__":
    print_uptime()
