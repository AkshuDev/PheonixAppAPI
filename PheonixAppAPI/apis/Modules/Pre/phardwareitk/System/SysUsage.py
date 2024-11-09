import psutil
from typing import *

import os

from psutil import *
import subprocess
import platform
import socket

SYSTEM = platform.system().lower()

class CPU:
    @staticmethod
    def CpuUsage(interval:Union[None, float]=1.0) -> float:
        """This function calculates the CPU usage via the given interval and returns the CPU usage.

        Args:
            interval (Union[None, float], optional): Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.

        Returns:
            float: The Cpu usage.
        """
        return psutil.cpu_percent(interval, False)
    
    @staticmethod
    def CpuUsageDetails():
        """This function returns the following details about the CPU usage ->

        user: This represents the time spent by normal processes executing in the user mode.
        system: This represents the time spent by processes executing in the kernel mode.
        idle: This represents the time when the system is idle.
        nice: This represents the time spent by priority processes executing in the user mode.
        iowait: This represents the time spent waiting for I/O to complete.
        irq: This represents the time spent for servicing hardware interrupts.
        softirq: This represents the time spent for servicing software interrupts.
        steal: Represents the time spent by other operating systems running in a virtualized environment
        guest: This represents the time spent running a virtual CPU for guest operating systems under the control of the Linux kernel.

        WINDOWS ONLY:
        interrupt: This represents the time spent for servicing hardware interrupts.
        dpc: This represents the time spent servicing deferred procedure calls (DPCs).

        Returns:
            Any: Return type -> psutil._ps[Your OS].scputimes
        """
        return psutil.cpu_times(False)
    
    @staticmethod
    def CpuUsageTimesDetails(interval:Union[float, None]=1.0):
        """Same as CpuUsage but returns like CpuUsageDetails.

        Args:
            interval (Union[None, float], optional): Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.

        Returns:
            Any: Return Type -> psutil._ps[Your OS].scputimes.
        """
        return psutil.cpu_times_percent(interval, False)
    
    @staticmethod
    def CpuCount(logical:bool=False) -> int:
        """Returns the number of Cpu Cores in System.

        Args:
            logical (bool, optional): If set to true returned value will be [Number of Physical Cores + Hyper Threading]. Defaults to False.

        Returns:
            int: The number of Cpu Physical Cores [+ Hyper Threading if [logical] is True].
        """
        return psutil.cpu_count(logical)
    
    @staticmethod
    def CpuStats():
        """Returns detailed CPU statistics such as context switches, interrupts, and soft interrupts.

        Returns:
            Any: Object containing detailed statistics about the CPU.
        """
        return psutil.cpu_stats()

    @staticmethod
    def CpuFreq():
        """Returns the current frequency of the CPU, in MHz.

        Returns:
            Any: A scpufreq object that contains the current frequency of the CPU.
        """
        return psutil.cpu_freq()

    @staticmethod
    def CpuFreqPerCore() -> list:
        """Returns the current frequency per CPU core, in MHz.

        Returns:
            list: A list of scpufreq objects, one per CPU core.
        """
        return psutil.cpu_freq(True)

    @staticmethod
    def CpuLoadAvg() -> list:
        """Returns the 1, 5, and 15 minute load averages for the CPU system.

        Returns:
            list: list of 3 floats representing the load averages over 1, 5, and 15 minutes.
        """
        return psutil.getloadavg()

    @staticmethod
    def CpuAffinity(pid: int = None) -> Union[list, None]:
        """Returns a list of CPU cores the given process (or current process if no PID is specified) is allowed to run on.

        Args:
            pid (int, optional): The process ID. If None, the current process is used. Defaults to None.

        Returns:
            Union[list, None]: A list of CPU cores the process is allowed to use, or None if the process is not found.
        """
        if pid:
            p = psutil.Process(pid)
            return p.cpu_affinity()
        return psutil.Process().cpu_affinity()

    @staticmethod
    def CpuTimesPerCore() -> list:
        """Returns the CPU times per core in the system.

        Returns:
            list: A list of scputimes objects per CPU core.
        """
        return psutil.cpu_times(percpu=True)

    @staticmethod
    def CpuUsagePerCore(interval: Union[None, float] = 1.0) -> list:
        """Returns the CPU usage per core over the given interval.

        Args:
            interval (Union[None, float], optional): Interval for calculating the usage. Defaults to 1.0.

        Returns:
            list: list of CPU usage percentages per core.
        """
        return psutil.cpu_percent(interval=interval, percpu=True)
    
    if LINUX:
        @staticmethod
        def CpuWaitTime() -> float:
            """Returns the CPU I/O wait time percentage.

            Returns:
                float: The percentage of time the CPU spends waiting for I/O to complete.
            """
            return psutil.cpu_times().iowait

        @staticmethod
        def CpuSteal() -> float:
            """Returns the percentage of time the CPU is stolen by other operating systems (in virtualized environments).

            Returns:
                float: The percentage of time the CPU is stolen.
            """
            return psutil.cpu_times().steal

class Battery:
    @staticmethod
    def BatteryStatus() -> str:
        """Returns the status of the battery (e.g., 'charging', 'discharging', 'full', or 'not present').

        Returns:
            str: The battery status.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return "Battery not present"
        return battery.power_plugged and "Charging" or "Discharging" if battery.percent < 100 else "Full"

    @staticmethod
    def BatteryPercentage() -> float:
        """Returns the current battery percentage.

        Returns:
            float: The battery percentage.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return -1.0  # Battery not present
        return battery.percent

    @staticmethod
    def BatteryTimeLeft() -> str:
        """Returns the estimated time left on the battery in minutes. If plugged in, returns 'Charging'.

        Returns:
            str: Time left + Time Period (Minutes/Hours/Seconds/Days/Months/Years/Centuries), or 'Charging' if plugged in.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return "Battery not present"
        if battery.power_plugged:
            return "Charging"
        if battery.secsleft != psutil.POWER_TIME_UNKNOWN and battery.secsleft != 4294967295:
            mins = battery.secsleft / 60
            if mins > 60:
                hours = mins / 60
                if hours > 24:
                    days = hours / 24
                    if days > 31:
                        months = days / 31
                        if months > 12:
                            years = months / 12
                            if years > 100:
                                century = years / 100
                                return str(century) + " Centuries"
                            else:
                                return str(years) + " Years"
                        return str(months) + " Months"
                    else:
                        return str(days) + " Days"
                else:
                    return str(hours) + " Hours"
            else:
                return str(mins) + " Minutes"

        else: return "-1.0" + " Unknown Duration"

    @staticmethod
    def BatteryPlugged() -> bool:
        """Returns True if the battery is currently plugged in (charging), otherwise False.

        Returns:
            bool: True if the battery is plugged in, else False.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return False  # No battery present
        return battery.power_plugged

    @staticmethod
    def BatterySecsLeft() -> Union[int, None]:
        """Returns the remaining seconds of battery life. Returns None if the time left is unknown.

        Returns:
            Union[int, None]: Remaining time in seconds or None if unknown.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return None  # No battery present
        return battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNKNOWN and battery.secsleft != 4294967295 else None

    @staticmethod
    def BatteryPluggedTime() -> float:
        """Returns the time in seconds that the battery has been plugged in.

        Returns:
            float: The time in seconds the battery has been plugged in.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return -1.0  # Battery not present
        try:
            return battery.plugged_time if battery.plugged_time != psutil.POWER_TIME_UNKNOWN else -10.0
        except AttributeError:
            return -11.0

    @staticmethod
    def BatteryIsCharging() -> bool:
        """Returns True if the battery is currently charging, False otherwise.

        Returns:
            bool: True if the battery is charging, False otherwise.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return False  # No battery present
        return battery.power_plugged

    @staticmethod
    def BatteryTimeToFullCharge() -> Union[str, float]:
        """Returns the estimated time in minutes for the battery to be fully charged. Returns 'Charging' if plugged in.

        Returns:
            Union[str, float]: Time to full charge in minutes or 'Charging' if plugged in.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return "Battery not present"
        if battery.power_plugged:
            return "Charging"
        return battery.secsleft / 60 if battery.secsleft != psutil.POWER_TIME_UNKNOWN else -1.0

    @staticmethod
    def BatteryDetails() -> Union[str, dict]:
        """Returns detailed information about the battery, including percent, time left, and charging status.

        Returns:
            Union[str, dict]: A dictionary with detailed battery information or 'Battery not present'.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return "Battery not present"
        return {
            "Percent": battery.percent,
            "Time Left": battery.secsleft / 60 if battery.secsleft != psutil.POWER_TIME_UNKNOWN else "Unknown",
            "Charging": battery.power_plugged
        }

    @staticmethod
    def BatteryStatusDetails() -> Union[str, dict]:
        """Returns detailed battery status information, including charging status and percent.

        Returns:
            Union[str, dict]: A dictionary with battery status details or 'Battery not present'.
        """
        battery = psutil.sensors_battery()
        if battery is None:
            return "Battery not present"
        return {
            "Status": battery.power_plugged and "Charging" or "Discharging",
            "Percent": battery.percent,
            "Time Left": battery.secsleft / 60 if battery.secsleft != psutil.POWER_TIME_UNKNOWN else "Unknown"
        }

    @staticmethod
    def BatteryType() -> str:
        """Returns the battery type (e.g., 'Li-ion', 'NiMH', etc.) if available.

        Returns:
            str: The battery type or 'Unknown' if the information is unavailable.
        """
        # Note: This may not be available on all systems.
        try:
            battery = psutil.sensors_battery()
            if battery is None:
                return "Battery not present"
            # Some systems might provide battery type info in different ways, and this can be platform-dependent
            # In many cases, this info is not directly available through psutil.
            return "Li-ion"  # Placeholder, may need custom detection
        except Exception as e:
            return "Unknown"  # Return 'Unknown' if unable to get battery type

#Linux Only
class Temperature:
        """Linux Only"""
        @staticmethod
        def CpuTemp() -> float:
            """Returns the current temperature of the CPU in Celsius.
            
            Returns:
                float: The current CPU temperature in Celsius.
            """
            sensors = psutil.sensors_temperature()
            return sensors.get('cpu_thermal', [])[0].current if 'cpu_thermal' in sensors else -1.0
        
        @staticmethod
        def GpuTemp() -> float:
            """Returns the current temperature of the GPU in Celsius.
            
            Returns:
                float: The current GPU temperature in Celsius.
            """
            sensors = psutil.sensors_temperatures()
            return sensors.get('gpu', [])[0].current if 'gpu' in sensors else -1.0

        @staticmethod
        def TempSensors() -> dict:
            """Returns a dictionary of available temperature sensors and their values.
            
            Returns:
                dict: A dictionary where keys are sensor names, and values are lists of sensor readings.
            """
            return psutil.sensors_temperatures()

        @staticmethod
        def TempMax() -> float:
            """Returns the maximum temperature of the CPU in Celsius.
            
            Returns:
                float: The maximum CPU temperature.
            """
            sensors = psutil.sensors_temperatures()
            return max([sensor.current for sensor in sensors.get('cpu_thermal', [])]) if 'cpu_thermal' in sensors else -1.0

        @staticmethod
        def TempMin() -> float:
            """Returns the minimum temperature of the CPU in Celsius.
            
            Returns:
                float: The minimum CPU temperature.
            """
            sensors = psutil.sensors_temperatures()
            return min([sensor.current for sensor in sensors.get('cpu_thermal', [])]) if 'cpu_thermal' in sensors else -1.0

        @staticmethod
        def TempAveraged() -> float:
            """Returns the average temperature of the CPU in Celsius.
            
            Returns:
                float: The average CPU temperature.
            """
            sensors = psutil.sensors_temperatures()
            temperatures = [sensor.current for sensor in sensors.get('cpu_thermal', [])] if 'cpu_thermal' in sensors else []
            return sum(temperatures) / len(temperatures) if temperatures else -1.0

        @staticmethod
        def CpuTempPerCore() -> list:
            """Returns the temperature of each CPU core in Celsius.
            
            Returns:
                list: A list of CPU temperatures for each core.
            """
            sensors = psutil.sensors_temperatures()
            return [sensor.current for sensor in sensors.get('cpu_thermal', [])] if 'cpu_thermal' in sensors else []

        @staticmethod
        def GpuTempPerCore() -> list:
            """Returns the temperature of each GPU core in Celsius.
            
            Returns:
                list: A list of GPU temperatures for each core.
            """
            sensors = psutil.sensors_temperatures()
            return [sensor.current for sensor in sensors.get('gpu', [])] if 'gpu' in sensors else []

        @staticmethod
        def TempCritical() -> float:
            """Returns the critical temperature threshold for the CPU in Celsius.
            
            Returns:
                float: The critical temperature threshold.
            """
            sensors = psutil.sensors_temperatures()
            return max([sensor.critical for sensor in sensors.get('cpu_thermal', [])]) if 'cpu_thermal' in sensors else -1.0

        @staticmethod
        def TempWarning() -> float:
            """Returns the warning temperature threshold for the CPU in Celsius.
            
            Returns:
                float: The warning temperature threshold.
            """
            sensors = psutil.sensors_temperatures()
            return max([sensor.warning for sensor in sensors.get('cpu_thermal', [])]) if 'cpu_thermal' in sensors else -1.0

        @staticmethod
        def TempStatus() -> dict:
            """Returns a dictionary of temperature status (e.g., current, critical, warning) for each sensor.
            
            Returns:
                dict: A dictionary with temperature status.
            """
            sensors = psutil.sensors_temperatures()
            return {sensor: {'current': s.current, 'critical': s.critical, 'warning': s.warning} for sensor, s in sensors.items()}

        @staticmethod
        def GpuTempStatus() -> dict:
            """Returns the temperature status for the GPU.
            
            Returns:
                dict: A dictionary with GPU temperature status.
            """
            sensors = psutil.sensors_temperatures()
            return {'gpu': {'current': sensors.get('gpu', [])[0].current, 'critical': sensors.get('gpu', [])[0].critical}} if 'gpu' in sensors else {}

        @staticmethod
        def CpuTempStatus() -> dict:
            """Returns the temperature status for the CPU.
            
            Returns:
                dict: A dictionary with CPU temperature status.
            """
            sensors = psutil.sensors_temperatures()
            return {'cpu': {'current': sensors.get('cpu_thermal', [])[0].current, 'critical': sensors.get('cpu_thermal', [])[0].critical}} if 'cpu_thermal' in sensors else {}

        @staticmethod
        def MaxTempThreshold() -> float:
            """Returns the maximum temperature threshold for all sensors.
            
            Returns:
                float: The maximum temperature threshold across all sensors.
            """
            sensors = psutil.sensors_temperatures()
            all_temps = [sensor.critical for sensor in sensors.get('cpu_thermal', [])] if 'cpu_thermal' in sensors else []
            return max(all_temps) if all_temps else -1.0

        @staticmethod
        def MinTempThreshold() -> float:
            """Returns the minimum temperature threshold for all sensors.
            
            Returns:
                float: The minimum temperature threshold across all sensors.
            """
            sensors = psutil.sensors_temperatures()
            all_temps = [sensor.warning for sensor in sensors.get('cpu_thermal', [])] if 'cpu_thermal' in sensors else []
            return min(all_temps) if all_temps else -1.0

        @staticmethod
        def TemperatureTrends() -> dict:
            """Returns the temperature trends (current, max, min) for each sensor.
            
            Returns:
                dict: A dictionary with temperature trends for each sensor.
            """
            sensors = psutil.sensors_temperatures()
            trends = {}
            for sensor_name, sensor_list in sensors.items():
                trends[sensor_name] = {
                    'current': max([s.current for s in sensor_list]),
                    'max': max([s.max for s in sensor_list]),
                    'min': min([s.min for s in sensor_list]),
                }
            return trends

        @staticmethod
        def TempInFahrenheit() -> dict:
            """Returns all temperature readings in Fahrenheit.
            
            Returns:
                dict: A dictionary with temperature readings in Fahrenheit.
            """
            sensors = psutil.sensors_temperatures()
            return {sensor: {'current': (s.current * 9 / 5) + 32} for sensor, s in sensors.items()}

        @staticmethod
        def TempInKelvin() -> dict:
            """Returns all temperature readings in Kelvin.
            
            Returns:
                dict: A dictionary with temperature readings in Kelvin.
            """
            sensors = psutil.sensors_temperatures()
            return {sensor: {'current': s.current + 273.15} for sensor, s in sensors.items()}

        @staticmethod
        def TempForProcesses(pid: int) -> dict:
            """Returns the temperature readings for processes, if available.
            
            Args:
                pid (int): The process ID.
            
            Returns:
                dict: A dictionary with temperature readings for the given process.
            """
            sensors = psutil.sensors_temperatures()
            return {pid: {'current': sensors.get('cpu_thermal', [])[0].current}} if 'cpu_thermal' in sensors else {}

class Disk:
    @staticmethod
    def DiskUsage(path: str = '/') -> dict:
        """
        Returns the disk usage (free, used, total, percent).
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_usage(path)._asdict()
            except Exception as e:
                print(f"Error fetching disk usage: {e}")
                return {}
        return {}

    @staticmethod
    def DiskPartitions() -> list:
        """
        Returns a list of partitions on the system.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_partitions()
            except Exception as e:
                print(f"Error fetching partitions: {e}")
                return []
        return []

    @staticmethod
    def DiskFree(path: str = '/') -> float:
        """
        Returns the free space of a partition in bytes.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_usage(path).free
            except Exception as e:
                print(f"Error fetching free space: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def DiskUsed(path: str = '/') -> float:
        """
        Returns the used space of a partition in bytes.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_usage(path).used
            except Exception as e:
                print(f"Error fetching used space: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def DiskTotal(path: str = '/') -> float:
        """
        Returns the total space of a partition in bytes.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_usage(path).total
            except Exception as e:
                print(f"Error fetching total space: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def DiskReadBytes() -> int:
        """
        Returns the total number of bytes read from all disks.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_io_counters().read_bytes
            except Exception as e:
                print(f"Error fetching read bytes: {e}")
                return 0
        return 0

    @staticmethod
    def DiskWriteBytes() -> int:
        """
        Returns the total number of bytes written to all disks.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_io_counters().write_bytes
            except Exception as e:
                print(f"Error fetching write bytes: {e}")
                return 0
        return 0

    @staticmethod
    def DiskReads() -> int:
        """
        Returns the total number of read operations performed on all disks.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_io_counters().read_count
            except Exception as e:
                print(f"Error fetching read count: {e}")
                return 0
        return 0

    @staticmethod
    def DiskWrites() -> int:
        """
        Returns the total number of write operations performed on all disks.
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_io_counters().write_count
            except Exception as e:
                print(f"Error fetching write count: {e}")
                return 0
        return 0

    @staticmethod
    def DiskReadTime() -> int:
        """
        Returns the total time spent reading from the disk (in milliseconds).
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_io_counters().read_time
            except Exception as e:
                print(f"Error fetching read time: {e}")
                return 0
        return 0

    @staticmethod
    def DiskWriteTime() -> int:
        """
        Returns the total time spent writing to the disk (in milliseconds).
        Works cross-platform (Linux, Windows, macOS)
        """
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.disk_io_counters().write_time
            except Exception as e:
                print(f"Error fetching write time: {e}")
                return 0
        return 0

    @staticmethod
    def DiskIOMerges() -> int:
        """
        Returns the total number of merged I/O operations.
        Works on Linux (Not available on Windows/macOS)
        """
        if SYSTEM == 'linux':
            try:
                return psutil.disk_io_counters().merged_read_count + psutil.disk_io_counters().merged_write_count
            except Exception as e:
                print(f"Error fetching I/O merges: {e}")
                return 0
        return 0

    @staticmethod
    def DiskQueueDepth() -> int:
        """
        Returns the current disk I/O queue depth.
        Works on Linux (Not available on Windows/macOS)
        """
        if SYSTEM == 'linux':
            try:
                return psutil.disk_io_counters().queue
            except Exception as e:
                print(f"Error fetching disk queue depth: {e}")
                return 0
        return 0

    @staticmethod
    def DiskHealth(device: str) -> dict:
        """
        Returns the SMART health status of a disk.
        Works on Linux (using smartmontools), Windows (using OpenHardwareMonitor), macOS (via system commands)
        """
        if SYSTEM == 'linux':
            try:
                result = subprocess.check_output(["smartctl", "-H", device])
                return result.decode()
            except subprocess.CalledProcessError as e:
                print(f"Error fetching SMART data for {device}: {e}")
                return {}

        elif SYSTEM == 'windows':
            try:
                result = subprocess.check_output(["OpenHardwareMonitorCLI", "get", "disk", device])
                return result.decode()
            except subprocess.CalledProcessError as e:
                print(f"Error fetching SMART data for {device}: {e}")
                return {}

        elif SYSTEM == 'darwin':
            try:
                result = subprocess.check_output(["diskutil", "info", device])
                return result.decode()
            except subprocess.CalledProcessError as e:
                print(f"Error fetching SMART data for {device}: {e}")
                return {}

        return {}

    @staticmethod
    def DiskTemp(device: str) -> float:
        """
        Returns the temperature of the disk (if supported).
        Works on Linux (using smartmontools), Windows (using OpenHardwareMonitor), macOS (via system commands)
        """
        if SYSTEM == 'linux':
            try:
                result = subprocess.check_output(["smartctl", "-A", device])
                for line in result.decode().splitlines():
                    if "Temperature_Celsius" in line:
                        return float(line.split()[-1])
            except subprocess.CalledProcessError as e:
                print(f"Error fetching temperature for {device}: {e}")
                return -1.0

        elif SYSTEM == 'windows':
            try:
                result = subprocess.check_output(["OpenHardwareMonitorCLI", "get", "temperature", device])
                return float(result.decode())
            except subprocess.CalledProcessError as e:
                print(f"Error fetching temperature for {device}: {e}")
                return -1.0

        elif SYSTEM == 'darwin':
            try:
                result = subprocess.check_output(["sysctl", "-a"])
                return -1.0  # Modify to extract disk temperature on macOS if needed
            except subprocess.CalledProcessError as e:
                print(f"Error fetching temperature for {device}: {e}")
                return -1.0

        return -1.0

class Memory:
    # RAM Functions

    @staticmethod
    def RAMInfo() -> dict:
        """Returns overall system RAM information (total, available, used, percent)."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory()._asdict()
            except Exception as e:
                print(f"Error fetching RAM info: {e}")
                return {}
        return {}

    @staticmethod
    def RAMTotal() -> float:
        """Returns total RAM in bytes."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().total
            except Exception as e:
                print(f"Error fetching total RAM: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMAvailable() -> float:
        """Returns available RAM in bytes."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().available
            except Exception as e:
                print(f"Error fetching available RAM: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMUsed() -> float:
        """Returns used RAM in bytes."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().used
            except Exception as e:
                print(f"Error fetching used RAM: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMPercent() -> float:
        """Returns percentage of RAM used."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().percent
            except Exception as e:
                print(f"Error fetching RAM percent: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMActive() -> float:
        """Returns active RAM in bytes (used for active processes)."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().active
            except Exception as e:
                print(f"Error fetching active RAM: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMBuffered() -> float:
        """Returns buffered RAM in bytes (used for temporary caching)."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().buffers
            except Exception as e:
                print(f"Error fetching buffered RAM: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMShared() -> float:
        """Returns shared RAM in bytes (used by multiple processes)."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().shared
            except Exception as e:
                print(f"Error fetching shared RAM: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMSlab() -> float:
        """Returns slab memory in bytes (kernel memory used to cache objects)."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().slab
            except Exception as e:
                print(f"Error fetching slab memory: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMFree() -> float:
        """Returns free RAM in bytes."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().free
            except Exception as e:
                print(f"Error fetching free RAM: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMUsedByProcesses() -> list:
        """Returns memory used by processes in a list of dictionaries."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return [{"pid": p.info["pid"], "memory": p.info["memory_info"].rss} for p in psutil.process_iter(['pid', 'memory_info'])]
            except Exception as e:
                print(f"Error fetching used RAM by processes: {e}")
                return []
        return []

    @staticmethod
    def RAMSwapTotal() -> float:
        """Returns total swap memory used for RAM overflow (if applicable)."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.swap_memory().total
            except Exception as e:
                print(f"Error fetching swap total memory: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMSwapUsed() -> float:
        """Returns used swap memory in bytes."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.swap_memory().used
            except Exception as e:
                print(f"Error fetching swap used memory: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMSwapFree() -> float:
        """Returns free swap memory in bytes."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.swap_memory().free
            except Exception as e:
                print(f"Error fetching swap free memory: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMSwapPercent() -> float:
        """Returns swap memory usage percentage."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.swap_memory().percent
            except Exception as e:
                print(f"Error fetching swap percent memory: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMSwapInUse() -> bool:
        """Returns True if swap memory is in use, otherwise False."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.swap_memory().used > 0
            except Exception as e:
                print(f"Error checking if swap is in use: {e}")
                return False
        return False

    @staticmethod
    def RAMBufferInfo() -> dict:
        """Returns detailed memory buffer information."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory()._asdict()
            except Exception as e:
                print(f"Error fetching buffer info: {e}")
                return {}
        return {}

    @staticmethod
    def RAMPhysicalMemory() -> float:
        """Returns total physical memory (RAM) in bytes."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                return psutil.virtual_memory().total
            except Exception as e:
                print(f"Error fetching physical memory: {e}")
                return 0.0
        return 0.0

    @staticmethod
    def RAMActiveProcessMemory(pid: int) -> float:
        """Returns memory used by a specific process (pid)."""
        if SYSTEM in ['linux', 'windows', 'darwin']:
            try:
                process = psutil.Process(pid)
                return process.memory_info().rss
            except Exception as e:
                print(f"Error fetching memory for process {pid}: {e}")
                return 0.0
        return 0.0

#Linux Only
class Fan:
        """Linux Only"""
        @staticmethod
        def FansInfo() -> dict:
            """Returns detailed information about all fans, including fan ID and speed (RPM)."""
            fans = psutil.sensors_fans()
            if fans:
                return fans
            return {}

        @staticmethod
        def FansCount() -> int:
            """Returns the number of fans in the system."""
            fans = psutil.sensors_fans()
            if fans:
                return len(fans)
            return 0

        @staticmethod
        def FanSpeed(fan_id: int) -> Union[int, None]:
            """Returns the speed of a specific fan by fan ID (RPM)."""
            fans = psutil.sensors_fans()
            if fans and fan_id in fans:
                return fans[fan_id][0]  # Return the speed (RPM) of the specified fan
            return None

        @staticmethod
        def AllFanSpeeds() -> dict:
            """Returns a dictionary of fan speeds (RPM) for all fans."""
            fans = psutil.sensors_fans()
            if fans:
                return {fan_id: fan[0] for fan_id, fan in fans.items()}
            return {}

        @staticmethod
        def FanInfoById(fan_id: int) -> Union[dict, None]:
            """Returns detailed information about a specific fan (by fan ID)."""
            fans = psutil.sensors_fans()
            if fans and fan_id in fans:
                return {"fan_id": fan_id, "speed_rpm": fans[fan_id][0]}  # Fan ID and speed in RPM
            return None

class Network:
    # 1. Get network interfaces (Linux, Windows)
    @staticmethod
    def Interfaces() -> Union[dict[str, dict], str]:
        """Returns a dictionary of network interfaces, their addresses, and stats. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return psutil.net_if_addrs()
        except Exception as e:
            return f"Error: Unable to fetch interfaces - {str(e)}"

    # 2. Get network interface stats (Linux, Windows)
    @staticmethod
    def InterfaceStats() -> Union[dict[str, dict], str]:
        """Returns the stats (bytes, packets, errors, drops, etc.) for each network interface. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return psutil.net_if_stats()
        except Exception as e:
            return f"Error: Unable to fetch interface stats - {str(e)}"

    # 3. Get network connections (Linux, Windows)
    @staticmethod
    def NetworkConnections(kind: str = 'inet') -> Union[list, str]:
        """Returns a list of network connections of the specified type (TCP, UDP, etc.). (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return psutil.net_connections(kind=kind)
        except Exception as e:
            return f"Error: Unable to fetch network connections - {str(e)}"

    # 4. Get network statistics (Linux, Windows)
    @staticmethod
    def NetworkStats() -> Union[dict[str, Union[int, float]], str]:
        """Returns global network statistics like bytes sent, received, errors, etc. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return psutil.net_io_counters(pernic=False)._asdict()
        except Exception as e:
            return f"Error: Unable to fetch network stats - {str(e)}"

    # 5. Get per-interface network statistics (Linux, Windows)
    @staticmethod
    def InterfaceNetworkStats(interface: str) -> Union[dict, str]:
        """Returns per-interface network stats (bytes sent, received, etc.). (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return psutil.net_io_counters(pernic=True).get(interface, {})
        except Exception as e:
            return f"Error: Unable to fetch network stats for {interface} - {str(e)}"

    # 6. Get the default gateway (Linux, Windows)
    @staticmethod
    def DefaultGateway() -> Union[dict[str, str], str]:
        """Returns the default gateway for the system. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            gateways = psutil.net_if_addrs()
            return gateways.get('default', {})
        except Exception as e:
            return f"Error: Unable to fetch default gateway - {str(e)}"

    # 7. Get the DNS configuration (Linux, Windows)
    @staticmethod
    def DNSConfig() -> Union[dict[str, list], str]:
        """Returns DNS configuration for the system (DNS servers). (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            dns_info = psutil.net_if_addrs()
            return dns_info.get('dns', {})
        except Exception as e:
            return f"Error: Unable to fetch DNS configuration - {str(e)}"

    # 8. Get the IP address for a given interface (Linux, Windows)
    @staticmethod
    def IPAddress(interface: str) -> Union[str, str]:
        """Returns the IP address of a given interface. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            addrs = psutil.net_if_addrs().get(interface, [])
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    return addr.address
            return "Error: No IPv4 address found for this interface."
        except Exception as e:
            return f"Error: Unable to fetch IP address for {interface} - {str(e)}"

    # 9. Get MAC address for a given interface (Linux, Windows)
    @staticmethod
    def MACAddress(interface: str) -> Union[str, str]:
        """Returns the MAC address of a given interface. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            addrs = psutil.net_if_addrs().get(interface, [])
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    return addr.address
            return "Error: No MAC address found for this interface."
        except Exception as e:
            return f"Error: Unable to fetch MAC address for {interface} - {str(e)}"

    # 10. Get the hostname of the machine (Linux, Windows)
    @staticmethod
    def Hostname() -> Union[str, str]:
        """Returns the hostname of the machine. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return socket.gethostname()
        except Exception as e:
            return f"Error: Unable to fetch hostname - {str(e)}"

    # 11. Get the fully qualified domain name (FQDN) (Linux, Windows)
    @staticmethod
    def FQDN() -> Union[str, str]:
        """Returns the fully qualified domain name (FQDN) of the machine. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return socket.getfqdn()
        except Exception as e:
            return f"Error: Unable to fetch FQDN - {str(e)}"

    # 12. Get the IP address of the current machine (Linux, Windows)
    @staticmethod
    def LocalIPAddress() -> Union[str, str]:
        """Returns the local IP address of the machine. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            hostname = socket.gethostname()
            return socket.gethostbyname(hostname)
        except Exception as e:
            return f"Error: Unable to fetch local IP address - {str(e)}"

    # 13. Get current network interface state (Linux, Windows)
    @staticmethod
    def InterfaceState(interface: str) -> Union[str, str]:
        """Returns the current state (UP/DOWN) of the network interface. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            stats = psutil.net_if_stats().get(interface)
            if stats:
                return "UP" if stats.isup else "DOWN"
            return f"Error: Interface {interface} not found."
        except Exception as e:
            return f"Error: Unable to fetch interface state for {interface} - {str(e)}"

    # 14. Check if a network interface is up (Linux, Windows)
    @staticmethod
    def IsInterfaceUp(interface: str) -> Union[bool, str]:
        """Returns True if the network interface is up, False otherwise. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            stats = psutil.net_if_stats().get(interface)
            return stats.isup if stats else f"Error: Interface {interface} not found."
        except Exception as e:
            return f"Error: Unable to check if interface {interface} is up - {str(e)}"

    # 15. Get network connection by PID (Linux, Windows)
    @staticmethod
    def NetworkConnectionsByPID(pid: int) -> Union[list, str]:
        """Returns network connections by the process ID (PID). (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return psutil.net_connections(kind='inet', pid=pid)
        except Exception as e:
            return f"Error: Unable to fetch network connections for PID {pid} - {str(e)}"

    # 16. Get the local ports in use (Linux, Windows)
    @staticmethod
    def LocalPortsInUse() -> Union[list, str]:
        """Returns a list of local ports in use. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            connections = psutil.net_connections(kind='inet')
            return [conn.laddr.port for conn in connections]
        except Exception as e:
            return f"Error: Unable to fetch local ports - {str(e)}"

    # 17. Get the external IP address (Linux, Windows)
    @staticmethod
    def ExternalIPAddress() -> Union[str, str]:
        """Returns the external IP address of the system (if available)."""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            import requests
            response = requests.get("https://api.ipify.org")
            return response.text
        except Exception as e:
            return f"Error: Unable to fetch external IP address - {str(e)}"

    # 18. Get network interface type (Linux, Windows)
    @staticmethod
    def InterfaceType(interface: str) -> Union[str, str]:
        """Returns the type of a network interface (e.g., ethernet, wifi). (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            addrs = psutil.net_if_addrs().get(interface, [])
            if addrs:
                return addrs[0].family.name
            return f"Error: Interface {interface} not found."
        except Exception as e:
            return f"Error: Unable to fetch interface type for {interface} - {str(e)}"

    # 19. Get network connection status (Linux, Windows)
    @staticmethod
    def ConnectionStatus(connection) -> Union[str, str]:
        """Returns the status of a network connection (ESTABLISHED, LISTEN, etc.). (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            return connection.status
        except Exception as e:
            return f"Error: Unable to fetch connection status - {str(e)}"

    # 20. Get the netmask of an interface (Linux, Windows)
    @staticmethod
    def Netmask(interface: str) -> Union[str, str]:
        """Returns the netmask of the given network interface. (Linux, Windows only)"""
        if SYSTEM not in ['linux', 'windows']:
            return "Error: This function is only supported on Linux and Windows."
        try:
            addrs = psutil.net_if_addrs().get(interface, [])
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    return addr.netmask
            return f"Error: No netmask found for {interface}."
        except Exception as e:
            return f"Error: Unable to fetch netmask for {interface} - {str(e)}"

class System(CPU, Battery, Temperature, Disk, Memory, Fan, Network):
    #CPU
    @classmethod
    def CpuUsage(cls, interval: Union[None, float] = 1.0) -> float:
        """This function calculates the CPU usage via the given interval and returns the CPU usage.

        Args:
            interval (Union[None, float], optional): Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.

        Returns:
            float: The Cpu usage.
        """
        return super().CpuUsage(interval)

    @classmethod
    def CpuUsageDetails(cls):
        """This function returns the following details about the CPU usage ->

        user: This represents the time spent by normal processes executing in the user mode.
        system: This represents the time spent by processes executing in the kernel mode.
        idle: This represents the time when the system is idle.
        nice: This represents the time spent by priority processes executing in the user mode.
        iowait: This represents the time spent waiting for I/O to complete.
        irq: This represents the time spent for servicing hardware interrupts.
        softirq: This represents the time spent for servicing software interrupts.
        steal: Represents the time spent by other operating systems running in a virtualized environment
        guest: This represents the time spent running a virtual CPU for guest operating systems under the control of the Linux kernel.

        WINDOWS ONLY:
        interrupt: This represents the time spent for servicing hardware interrupts.
        dpc: This represents the time spent servicing deferred procedure calls (DPCs).

        Returns:
            Any: Return type -> psutil._ps[Your OS].scputimes
        """
        return super().CpuUsageDetails()

    @classmethod
    def CpuUsageTimesDetails(cls, interval: Union[float, None] = 1.0):
        """Same as CpuUsage but returns like CpuUsageDetails.

        Args:
            interval (Union[None, float], optional): Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.

        Returns:
            Any: Return Type -> psutil._ps[Your OS].scputimes.
        """
        return super().CpuUsageTimesDetails(interval)

    @classmethod
    def CpuCount(cls, logical: bool = False) -> int:
        """Returns the number of Cpu Cores in System.

        Args:
            logical (bool, optional): If set to true returned value will be [Number of Physical Cores + Hyper Threading]. Defaults to False.

        Returns:
            int: The number of Cpu Physical Cores [+ Hyper Threading if [logical] is True].
        """
        return super().CpuCount(logical)

    @classmethod
    def CpuStats(cls):
        """Returns detailed CPU statistics such as context switches, interrupts, and soft interrupts.

        Returns:
            Any: Object containing detailed statistics about the CPU.
        """
        return super().CpuStats()

    @classmethod
    def CpuFreq(cls):
        """Returns the current frequency of the CPU, in MHz.

        Returns:
            Any: A scpufreq object that contains the current frequency of the CPU.
        """
        return super().CpuFreq()

    @classmethod
    def CpuFreqPerCore(cls) -> list:
        """Returns the current frequency per CPU core, in MHz.

        Returns:
            list: A list of scpufreq objects, one per CPU core.
        """
        return super().CpuFreqPerCore()

    @classmethod
    def CpuLoadAvg(cls) -> list:
        """Returns the 1, 5, and 15 minute load averages for the CPU system.

        Returns:
            list: list of 3 floats representing the load averages over 1, 5, and 15 minutes.
        """
        return super().CpuLoadAvg()

    @classmethod
    def CpuAffinity(cls, pid: int = None) -> Union[list, None]:
        """Returns a list of CPU cores the given process (or current process if no PID is specified) is allowed to run on.

        Args:
            pid (int, optional): The process ID. If None, the current process is used. Defaults to None.

        Returns:
            Union[list, None]: A list of CPU cores the process is allowed to use, or None if the process is not found.
        """
        return super().CpuAffinity(pid)

    @classmethod
    def CpuTimesPerCore(cls) -> list:
        """Returns the CPU times per core in the system.

        Returns:
            list: A list of scputimes objects per CPU core.
        """
        return super().CpuTimesPerCore()

    @classmethod
    def CpuUsagePerCore(cls, interval: Union[None, float] = 1.0) -> list:
        """Returns the CPU usage per core over the given interval.

        Args:
            interval (Union[None, float], optional): Interval for calculating the usage. Defaults to 1.0.

        Returns:
            list: list of CPU usage percentages per core.
        """
        return super().CpuUsagePerCore(interval)

    if LINUX:
        @classmethod
        def CpuWaitTime(cls) -> float:
            """Returns the CPU I/O wait time percentage.

            Returns:
                float: The percentage of time the CPU spends waiting for I/O to complete.
            """
            return super().CpuWaitTime()

        @classmethod
        def CpuSteal(cls) -> float:
            """Returns the percentage of time the CPU is stolen by other operating systems (in virtualized environments).

            Returns:
                float: The percentage of time the CPU is stolen.
            """
            return super().CpuSteal()
    
    #Battery
    @classmethod
    def SystemBatteryStatus(cls) -> str:
        """Returns the battery status using the Battery class."""
        return super().BatteryStatus()

    @classmethod
    def SystemBatteryPercentage(cls) -> float:
        """Returns the battery percentage using the Battery class."""
        return super().BatteryPercentage()

    @classmethod
    def SystemBatteryTimeLeft(cls) -> str:
        """Returns the estimated time left on the battery using the Battery class.
        
        Returns:
            str: Time left + Time Period (Minutes/Hours/Seconds/Days/Months/Years/Centuries), or 'Charging' if plugged in."""
        return super().BatteryTimeLeft()

    @classmethod
    def SystemBatteryPlugged(cls) -> bool:
        """Returns whether the battery is plugged in (charging) using the Battery class."""
        return super().BatteryPlugged()

    @classmethod
    def SystemBatterySecsLeft(cls) -> Union[int, None]:
        """Returns the remaining battery life in seconds using the Battery class."""
        return super().BatterySecsLeft()

    @classmethod
    def SystemBatteryPluggedTime(cls) -> float:
        """Returns the time the battery has been plugged in using the Battery class."""
        return super().BatteryPluggedTime()

    @classmethod
    def SystemBatteryIsCharging(cls) -> bool:
        """Returns whether the battery is charging using the Battery class."""
        return super().BatteryIsCharging()

    @classmethod
    def SystemBatteryTimeToFullCharge(cls) -> Union[str, float]:
        """Returns the estimated time to full charge using the Battery class."""
        return super().BatteryTimeToFullCharge()

    @classmethod
    def SystemBatteryDetails(cls) -> Union[str, dict]:
        """Returns detailed battery information using the Battery class."""
        return super().BatteryDetails()

    @classmethod
    def SystemBatteryStatusDetails(cls) -> Union[str, dict]:
        """Returns detailed battery status information using the Battery class."""
        return super().BatteryStatusDetails()

    @classmethod
    def SystemBatteryType(cls) -> str:
        """Returns the battery type using the Battery class."""
        return super().BatteryType()
    
    #Temperature
    if LINUX:
        @classmethod
        def CpuTemp(cls) -> float:
            """Returns the current temperature of the CPU in Celsius."""
            return super().CpuTemp()

        @classmethod
        def GpuTemp(cls) -> float:
            """Returns the current temperature of the GPU in Celsius."""
            return super().GpuTemp()

        @classmethod
        def TempSensors(cls) -> dict:
            """Returns a dictionary of available temperature sensors and their values."""
            return super().TempSensors()

        @classmethod
        def TempMax(cls) -> float:
            """Returns the maximum temperature of the CPU in Celsius."""
            return super().TempMax()

        @classmethod
        def TempMin(cls) -> float:
            """Returns the minimum temperature of the CPU in Celsius."""
            return super().TempMin()

        @classmethod
        def TempAveraged(cls) -> float:
            """Returns the average temperature of the CPU in Celsius."""
            return super().TempAveraged()

        @classmethod
        def CpuTempPerCore(cls) -> list:
            """Returns the temperature of each CPU core in Celsius."""
            return super().CpuTempPerCore()

        @classmethod
        def GpuTempPerCore(cls) -> list:
            """Returns the temperature of each GPU core in Celsius."""
            return super().GpuTempPerCore()

        @classmethod
        def TempCritical(cls) -> float:
            """Returns the critical temperature threshold for the CPU in Celsius."""
            return super().TempCritical()

        @classmethod
        def TempWarning(cls) -> float:
            """Returns the warning temperature threshold for the CPU in Celsius."""
            return super().TempWarning()

        @classmethod
        def TempStatus(cls) -> dict:
            """Returns a dictionary of temperature status for each sensor."""
            return super().TempStatus()

        @classmethod
        def GpuTempStatus(cls) -> dict:
            """Returns the temperature status for the GPU."""
            return super().GpuTempStatus()

        @classmethod
        def CpuTempStatus(cls) -> dict:
            """Returns the temperature status for the CPU."""
            return super().CpuTempStatus()

        @classmethod
        def MaxTempThreshold(cls) -> float:
            """Returns the maximum temperature threshold for all sensors."""
            return super().MaxTempThreshold()

        @classmethod
        def MinTempThreshold(cls) -> float:
            """Returns the minimum temperature threshold for all sensors."""
            return super().MinTempThreshold()

        @classmethod
        def TemperatureTrends(cls) -> dict:
            """Returns the temperature trends (current, max, min) for each sensor."""
            return super().TemperatureTrends()

        @classmethod
        def TempInFahrenheit(cls) -> dict:
            """Returns all temperature readings in Fahrenheit."""
            return super().TempInFahrenheit()

        @classmethod
        def TempInKelvin(cls) -> dict:
            """Returns all temperature readings in Kelvin."""
            return super().TempInKelvin()

        @classmethod
        def TempForProcesses(cls, pid: int) -> dict:
            """Returns the temperature readings for processes, if available."""
            return super().TempForProcesses(pid)
    
    #Disk
    @classmethod
    def DiskUsage(cls, path: str = '/') -> dict:
        """
        Returns the disk usage (free, used, total, percent).
        Delegates to the Disk class methods.
        """
        return super().DiskUsage(path)

    @classmethod
    def DiskPartitions(cls) -> list:
        """
        Returns a list of partitions on the system.
        Delegates to the Disk class methods.
        """
        return super().DiskPartitions()

    @classmethod
    def DiskFree(cls, path: str = '/') -> float:
        """
        Returns the free space of a partition in bytes.
        Delegates to the Disk class methods.
        """
        return super().DiskFree(path)

    @classmethod
    def DiskUsed(cls, path: str = '/') -> float:
        """
        Returns the used space of a partition in bytes.
        Delegates to the Disk class methods.
        """
        return super().DiskUsed(path)

    @classmethod
    def DiskTotal(cls, path: str = '/') -> float:
        """
        Returns the total space of a partition in bytes.
        Delegates to the Disk class methods.
        """
        return super().DiskTotal(path)

    @classmethod
    def DiskReadBytes(cls) -> int:
        """
        Returns the total number of bytes read from all disks.
        Delegates to the Disk class methods.
        """
        return super().DiskReadBytes()

    @classmethod
    def DiskWriteBytes(cls) -> int:
        """
        Returns the total number of bytes written to all disks.
        Delegates to the Disk class methods.
        """
        return super().DiskWriteBytes()

    @classmethod
    def DiskReads(cls) -> int:
        """
        Returns the total number of read operations performed on all disks.
        Delegates to the Disk class methods.
        """
        return super().DiskReads()

    @classmethod
    def DiskWrites(cls) -> int:
        """
        Returns the total number of write operations performed on all disks.
        Delegates to the Disk class methods.
        """
        return super().DiskWrites()

    @classmethod
    def DiskReadTime(cls) -> int:
        """
        Returns the total time spent reading from the disk (in milliseconds).
        Delegates to the Disk class methods.
        """
        return super().DiskReadTime()

    @classmethod
    def DiskWriteTime(cls) -> int:
        """
        Returns the total time spent writing to the disk (in milliseconds).
        Delegates to the Disk class methods.
        """
        return super().DiskWriteTime()

    @classmethod
    def DiskIOMerges(cls) -> int:
        """
        Returns the total number of merged I/O operations.
        Delegates to the Disk class methods (Linux only).
        """
        return super().DiskIOMerges()

    @classmethod
    def DiskQueueDepth(cls) -> int:
        """
        Returns the current disk I/O queue depth.
        Delegates to the Disk class methods (Linux only).
        """
        return super().DiskQueueDepth()

    @classmethod
    def DiskHealth(cls, device: str) -> dict:
        """
        Returns the SMART health status of a disk.
        Delegates to the Disk class methods.
        """
        return super().DiskHealth(device)

    @classmethod
    def DiskTemp(cls, device: str) -> float:
        """
        Returns the temperature of the disk (if supported).
        Delegates to the Disk class methods.
        """
        return super().DiskTemp(device)
    
    #Memory
    @classmethod
    def RAMInfo(cls) -> dict:
        """Returns overall system RAM information (total, available, used, percent)."""
        return super().RAMInfo()

    @classmethod
    def RAMTotal(cls) -> float:
        """Returns total RAM in bytes."""
        return super().RAMTotal()

    @classmethod
    def RAMAvailable(cls) -> float:
        """Returns available RAM in bytes."""
        return super().RAMAvailable()

    @classmethod
    def RAMUsed(cls) -> float:
        """Returns used RAM in bytes."""
        return super().RAMUsed()

    @classmethod
    def RAMPercent(cls) -> float:
        """Returns percentage of RAM used."""
        return super().RAMPercent()

    @classmethod
    def RAMActive(cls) -> float:
        """Returns active RAM in bytes (used for active processes)."""
        return super().RAMActive()

    @classmethod
    def RAMBuffered(cls) -> float:
        """Returns buffered RAM in bytes (used for temporary caching)."""
        return super().RAMBuffered()

    @classmethod
    def RAMShared(cls) -> float:
        """Returns shared RAM in bytes (used by multiple processes)."""
        return super().RAMShared()

    @classmethod
    def RAMSlab(cls) -> float:
        """Returns slab memory in bytes (kernel memory used to cache objects)."""
        return super().RAMSlab()

    @classmethod
    def RAMFree(cls) -> float:
        """Returns free RAM in bytes."""
        return super().RAMFree()

    @classmethod
    def RAMUsedByProcesses(cls) -> list:
        """Returns memory used by processes in a list of dictionaries."""
        return super().RAMUsedByProcesses()

    @classmethod
    def RAMSwapTotal(cls) -> float:
        """Returns total swap memory used for RAM overflow (if applicable)."""
        return super().RAMSwapTotal()

    @classmethod
    def RAMSwapUsed(cls) -> float:
        """Returns used swap memory in bytes."""
        return super().RAMSwapUsed()

    @classmethod
    def RAMSwapFree(cls) -> float:
        """Returns free swap memory in bytes."""
        return super().RAMSwapFree()

    @classmethod
    def RAMSwapPercent(cls) -> float:
        """Returns swap memory usage percentage."""
        return super().RAMSwapPercent()

    @classmethod
    def RAMSwapInUse(cls) -> bool:
        """Returns True if swap memory is in use, otherwise False."""
        return super().RAMSwapInUse()

    @classmethod
    def RAMBufferInfo(cls) -> dict:
        """Returns detailed memory buffer information."""
        return super().RAMBufferInfo()

    @classmethod
    def RAMPhysicalMemory(cls) -> float:
        """Returns total physical memory (RAM) in bytes."""
        return super().RAMPhysicalMemory()

    @classmethod
    def RAMActiveProcessMemory(cls, pid: int) -> float:
        """Returns memory used by a specific process (pid)."""
        return super().RAMActiveProcessMemory(pid)
    
    #Fans
    if LINUX:
        @classmethod
        def SystemFansInfo(cls) -> dict:
            """Returns detailed information about all fans, including fan ID and speed (RPM)."""
            return super().FansInfo()

        @classmethod
        def SystemFansCount(cls) -> int:
            """Returns the number of fans in the system."""
            return super().FansCount()

        @classmethod
        def SystemFanSpeed(cls, fan_id: int) -> Union[int, None]:
            """Returns the speed of a specific fan by fan ID (RPM)."""
            return super().FanSpeed(fan_id)

        @classmethod
        def SystemAllFanSpeeds(cls) -> dict:
            """Returns a dictionary of fan speeds (RPM) for all fans."""
            return super().AllFanSpeeds()

        @classmethod
        def SystemFanInfoById(cls, fan_id: int) -> Union[dict, None]:
            """Returns detailed information about a specific fan (by fan ID)."""
            return super().FanInfoById(fan_id)
    
    #Network
    
    # 1. Get network interfaces (Linux, Windows)
    @classmethod
    def Interfaces(cls) -> Union[dict[str, dict], str]:
        """Returns a dictionary of network interfaces, their addresses, and stats. (Linux, Windows only)"""
        return super().Interfaces()

    # 2. Get network interface stats (Linux, Windows)
    @classmethod
    def InterfaceStats(cls) -> Union[dict[str, dict], str]:
        """Returns the stats (bytes, packets, errors, drops, etc.) for each network interface. (Linux, Windows only)"""
        return super().InterfaceStats()

    # 3. Get network connections (Linux, Windows)
    @classmethod
    def NetworkConnections(cls, kind: str = 'inet') -> Union[list, str]:
        """Returns a list of network connections of the specified type (TCP, UDP, etc.). (Linux, Windows only)"""
        return super().NetworkConnections(kind)

    # 4. Get network statistics (Linux, Windows)
    @classmethod
    def NetworkStats(cls) -> Union[dict[str, Union[int, float]], str]:
        """Returns global network statistics like bytes sent, received, errors, etc. (Linux, Windows only)"""
        return super().NetworkStats()

    # 5. Get per-interface network statistics (Linux, Windows)
    @classmethod
    def InterfaceNetworkStats(cls, interface: str) -> Union[dict, str]:
        """Returns per-interface network stats (bytes sent, received, etc.). (Linux, Windows only)"""
        return super().InterfaceNetworkStats(interface)

    # 6. Get the default gateway (Linux, Windows)
    @classmethod
    def DefaultGateway(cls) -> Union[dict[str, str], str]:
        """Returns the default gateway for the system. (Linux, Windows only)"""
        return super().DefaultGateway()

    # 7. Get the DNS configuration (Linux, Windows)
    @classmethod
    def DNSConfig(cls) -> Union[dict[str, list], str]:
        """Returns DNS configuration for the system (DNS servers). (Linux, Windows only)"""
        return super().DNSConfig()

    # 8. Get the IP address for a given interface (Linux, Windows)
    @classmethod
    def IPAddress(cls, interface: str) -> Union[str, str]:
        """Returns the IP address of a given interface. (Linux, Windows only)"""
        return super().IPAddress(interface)

    # 9. Get MAC address for a given interface (Linux, Windows)
    @classmethod
    def MACAddress(cls, interface: str) -> Union[str, str]:
        """Returns the MAC address of a given interface. (Linux, Windows only)"""
        return super().MACAddress(interface)

    # 10. Get the hostname of the machine (Linux, Windows)
    @classmethod
    def Hostname(cls) -> Union[str, str]:
        """Returns the hostname of the machine. (Linux, Windows only)"""
        return super().Hostname()

    # 11. Get the fully qualified domain name (FQDN) (Linux, Windows)
    @classmethod
    def FQDN(cls) -> Union[str, str]:
        """Returns the fully qualified domain name (FQDN) of the machine. (Linux, Windows only)"""
        return super().FQDN()

    # 12. Get the IP address of the current machine (Linux, Windows)
    @classmethod
    def LocalIPAddress(cls) -> Union[str, str]:
        """Returns the local IP address of the machine. (Linux, Windows only)"""
        return super().LocalIPAddress()

    # 13. Get current network interface state (Linux, Windows)
    @classmethod
    def InterfaceState(cls, interface: str) -> Union[str, str]:
        """Returns the current state (UP/DOWN) of the network interface. (Linux, Windows only)"""
        return super().InterfaceState(interface)

    # 14. Check if a network interface is up (Linux, Windows)
    @classmethod
    def IsInterfaceUp(cls, interface: str) -> Union[bool, str]:
        """Returns True if the network interface is up, False otherwise. (Linux, Windows only)"""
        return super().IsInterfaceUp(interface)

    # 15. Get network connection by PID (Linux, Windows)
    @classmethod
    def NetworkConnectionsByPID(cls, pid: int) -> Union[list, str]:
        """Returns network connections by the process ID (PID). (Linux, Windows only)"""
        return super().NetworkConnectionsByPID(pid)

    # 16. Get the local ports in use (Linux, Windows)
    @classmethod
    def LocalPortsInUse(cls) -> Union[list, str]:
        """Returns a list of local ports in use. (Linux, Windows only)"""
        return super().LocalPortsInUse()

    # 17. Get the external IP address (Linux, Windows)
    @classmethod
    def ExternalIPAddress(cls) -> Union[str, str]:
        """Returns the external IP address of the system (if available)."""
        return super().ExternalIPAddress()

    # 18. Get network interface type (Linux, Windows)
    @classmethod
    def InterfaceType(cls, interface: str) -> Union[str, str]:
        """Returns the type of a network interface (e.g., ethernet, wifi). (Linux, Windows only)"""
        return super().InterfaceType(interface)

    # 19. Get network connection status (Linux, Windows)
    @classmethod
    def ConnectionStatus(cls, connection) -> Union[str, str]:
        """Returns the status of a network connection (ESTABLISHED, LISTEN, etc.). (Linux, Windows only)"""
        return super().ConnectionStatus(connection)

    # 20. Get the netmask of an interface (Linux, Windows)
    @classmethod
    def Netmask(cls, interface: str) -> Union[str, str]:
        """Returns the netmask of the given network interface. (Linux, Windows only)"""
        return super().Netmask(interface)