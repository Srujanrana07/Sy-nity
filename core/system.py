import platform
import psutil

class SystemChecker:
    def check(self):
        system_info = {
            "os": platform.system(),
            "cpu_percent": psutil.cpu_percent(),
            "ram_percent": psutil.virtual_memory().percent,
        }

        # Pass criteria (example logic)
        system_ok = (
            system_info["cpu_percent"] < 90 and
            system_info["ram_percent"] < 90
        )

        system_info["system_ok"] = system_ok
        return system_info
