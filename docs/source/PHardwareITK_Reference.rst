Documentation Contents
======================

.. contents::
   :local:
   :depth: 1

Overview
--------

This document provides an overview of the project's features.

Features
--------

The project includes the following components:

+--------------------+--------------------------------------------------+----------+
| **Feature**                    | **Description**                                 |
+====================+==================================================+==========+
| Extensions                     | This section includes information on supported  |
|                                | extensions and their usage.                     |
+--------------------+--------------------------------------------------+----------+
| GUI (Graphical User Interface) | Details on the graphical user interface, design |
|                                | elements, and user interaction.                 |
+--------------------+--------------------------------------------------+----------+
| CLI (Command Line Interface)   | Information on command-line tools, available    |
|                                | commands, and usage examples.                   |
+--------------------+--------------------------------------------------+----------+
| CLI (Command Line Interface)   | Information on command-line tools, available    |
|                                | commands, and usage examples.                   |
+--------------------+--------------------------------------------------+----------+
| CLI (Command Line Interface)   | Information on command-line tools, available    |
|                                | commands, and usage examples.                   |
+--------------------+--------------------------------------------------+----------+
| CLI (Command Line Interface)   | Information on command-line tools, available    |
|                                | commands, and usage examples.                   |
+--------------------+--------------------------------------------------+----------+
| CLI (Command Line Interface)   | Information on command-line tools, available    |
|                                | commands, and usage examples.                   |
+--------------------+--------------------------------------------------+----------+

PHardwareITK
------------

**Description:**

The `PHardwareITK` library provides a comprehensive toolkit for interacting with hardware components and functionalities. It offers functionalities for various hardware-related tasks, including:

* Error handling and system management
* File system operations
* Graphical User Interface (GUI) development
* Hardware control and interaction (details to be filled based on available functionalities)
* Module management and control
* Low-level programming aspects (details to be filled based on available functionalities)

Files
-----

**Description**: The files directly available in the phardwareitk module.

LIB
---

**Internal Paths:**

The `phardwareitk.LIB` module establishes various file paths within the library structure. These paths are used to access sub-modules and functionalities.

**Classes:**

**1. Paths:**

This class provides pre-defined paths to various directories and files within the `PHardwareITK` library. It avoids the need for manually constructing paths throughout the codebase.

**Example:**

    .. code-block:: python

      import phardwareitk.LIB as phLIB
   
      # Access the path to the ErrorSystem directory
      error_system_path = phLIB.Paths.ErrorSystem
   
      print(error_system_path)  # Output: /path/to/phardwareitk/ErrorSystem

Dependenicies
-------------

**All requirement modules:**
The `phardwareitk.Dependencies` module allows users to download any required module that is used in Phardwareitk as per their need.

**Classes:**

**1. Requirements:**

This class is the one and only main class of this file.

**Functions:**

**1. Modules:**

This function is the main function of this class.


Parameters:

1. mode [Union[str, None, list]] -> This argument allows the program to understand the specified mode. modes ->
                
   str: Returns the string representation of the required modules seperated via ' '.
                   
   list: Returns the list representation of the required modules.
                   
   None: Downloads all the required modules.


Returns:

Union[str, list, None] -> Return is based on parameter


**Example:**

   .. code-block:: python

      import phardwareitk.Dependencies as pHD

      # Call the function and download all modules
      pHD.Requirements.Modules() # 'mode' has the default value as None

System
------

This module is one ofthe biggest in the entire PHardwareITK, as it contains over 200 functions over multiple platforms, so we will just look at the classes and some example, look at [https://github.com/AkshuDev/PHardwareITK] Test folder for more examples.

**Files:**

**1. SysUsage**

This file has 200+ functions for monitoring the system usage, **NOTE: Some functions are OS-exclusive due to Python limitations.**


**Classes:**


**1. CPU**

This class handles all CPU related montitoring.

   .. code-block:: python

      import phardwareitk.System.SysUsage as pHSU

      # Get some data
      print(pHSU.CPU.GetUsage()) # Result in float

      # Check github for more details


**2. Battery**

This class handles all Battery related montitoring.

   .. code-block:: python

      import phardwareitk.System.SysUsage as pHSU

      # Get some data
      print(pHSU.Battery.BatteryStatus()) # Result in string

      # Check github for more details


**3. Temperature**

This class handles all Temperature related montitoring. LINUX ONLY.

   .. code-block:: python

      import phardwareitk.System.SysUsage as pHSU

      # Get some data
      print(pHSU.Temperature.CpuTemp()) # Result in float

      # Check github for more details


**4. Disk**

This class handles all Disk related montitoring.

   .. code-block:: python

      import phardwareitk.System.SysUsage as pHSU

      # Get some data
      print(pHSU.Disk.DiskUsage()) # Result in dict

      # Check github for more details


**5. Memory**

This class handles all Memory related montitoring.

   .. code-block:: python

      import phardwareitk.System.SysUsage as pHSU

      # Get some data
      print(pHSU.Memory.RAMInfo()) # Result in dict

      # Check github for more details


**6. Fan**

This class handles all Fan related montitoring. LINUX ONLY

   .. code-block:: python

      import phardwareitk.System.SysUsage as pHSU

      # Get some data
      print(pHSU.Fan.FansInfo()) # Result in dict

      # Check github for more details


**7. Network**

This class handles all Network related montitoring.

   .. code-block:: python

      import phardwareitk.System.SysUsage as pHSU

      # Get some data
      print(pHSU.Network.Interfaces()) # Result in Union[dict[str, dict], str]

      # Check github for more details


**8. System**

This class is a bundle for all functions. Not supported functions of other OS are not shown, so Dont Worry! Same with Classes!

   .. code-block:: python

      # This is the SysUsage Test file from github!
      from phardwareitk.System import SysUsage
      
      #Note: Some funcs not included as they are not supported by our testing OS. Testing OS -> Windows 11
      # If you like please test them, and give response to our github
      
      # CPU Section
      print("Logical CPU Count: ", SysUsage.System.CpuCount(True))
      print("Physical CPU Count: ", SysUsage.System.CpuCount(False))
      
      print("CPU Usage: ", SysUsage.System.CpuUsage())
      print("CPU Usage Details: ", SysUsage.System.CpuUsageDetails())
      print("CPU Usage Times Details: ", SysUsage.System.CpuUsageTimesDetails())
      
      print("CPU Stats: ", SysUsage.System.CpuStats())
      print("CPU Frequency: ", SysUsage.System.CpuFreq())
      print("CPU Frequency Per Core: ", SysUsage.System.CpuFreqPerCore())
      print("CPU Load Average (1, 5, 15 minutes): ", SysUsage.System.CpuLoadAvg())
      print("CPU Affinity (current process): ", SysUsage.System.CpuAffinity())
      print("CPU Times Per Core: ", SysUsage.System.CpuTimesPerCore())
      print("CPU Usage Per Core: ", SysUsage.System.CpuUsagePerCore())
      
      # Battery Section
      print("Battery Status: ", SysUsage.System.SystemBatteryStatus())
      print("Battery Percentage: ", SysUsage.System.SystemBatteryPercentage())
      print("Battery Time Left: ", SysUsage.System.SystemBatteryTimeLeft())
      print("Battery Plugged: ", SysUsage.System.SystemBatteryPlugged())
      print("Battery Seconds Left: ", SysUsage.System.SystemBatterySecsLeft())
      print("Battery Plugged Time: ", SysUsage.System.SystemBatteryPluggedTime())
      print("Battery Is Charging: ", SysUsage.System.SystemBatteryIsCharging())
      print("Battery Time to Full Charge: ", SysUsage.System.SystemBatteryTimeToFullCharge())
      print("Battery Details: ", SysUsage.System.SystemBatteryDetails())
      print("Battery Status Details: ", SysUsage.System.SystemBatteryStatusDetails())
      print("Battery Type: ", SysUsage.System.SystemBatteryType())
      
      # Disk Section
      print("Disk Usage (/): ", SysUsage.System.DiskUsage('/'))
      print("Disk Partitions: ", SysUsage.System.DiskPartitions())
      print("Disk Free Space (/): ", SysUsage.System.DiskFree('/'))
      print("Disk Used Space (/): ", SysUsage.System.DiskUsed('/'))
      print("Disk Total Space (/): ", SysUsage.System.DiskTotal('/'))
      print("Disk Read Bytes: ", SysUsage.System.DiskReadBytes())
      print("Disk Write Bytes: ", SysUsage.System.DiskWriteBytes())
      print("Disk Reads: ", SysUsage.System.DiskReads())
      print("Disk Writes: ", SysUsage.System.DiskWrites())
      print("Disk Read Time: ", SysUsage.System.DiskReadTime())
      print("Disk Write Time: ", SysUsage.System.DiskWriteTime())
      print("Disk I/O Merges: ", SysUsage.System.DiskIOMerges())
      print("Disk Queue Depth: ", SysUsage.System.DiskQueueDepth())
      
      # Memory Section
      print("RAM Info: ", SysUsage.System.RAMInfo())
      print("Total RAM: ", SysUsage.System.RAMTotal())
      print("Available RAM: ", SysUsage.System.RAMAvailable())
      print("Used RAM: ", SysUsage.System.RAMUsed())
      print("RAM Usage Percentage: ", SysUsage.System.RAMPercent())
      print("Active RAM: ", SysUsage.System.RAMActive())
      print("Buffered RAM: ", SysUsage.System.RAMBuffered())
      print("Shared RAM: ", SysUsage.System.RAMShared())
      print("Slab Memory: ", SysUsage.System.RAMSlab())
      print("Free RAM: ", SysUsage.System.RAMFree())
      
      print("RAM Used By Processes: ", SysUsage.System.RAMUsedByProcesses())
      print("RAM Swap Total: ", SysUsage.System.RAMSwapTotal())
      print("RAM Swap Used: ", SysUsage.System.RAMSwapUsed())
      print("RAM Swap Free: ", SysUsage.System.RAMSwapFree())
      print("RAM Swap Percentage: ", SysUsage.System.RAMSwapPercent())
      print("RAM Swap In Use: ", SysUsage.System.RAMSwapInUse())
      print("RAM Buffer Info: ", SysUsage.System.RAMBufferInfo())
      print("Total Physical RAM: ", SysUsage.System.RAMPhysicalMemory())
      
      # Replace '1234' with your actual process ID if needed
      print("RAM Used by Process 1234: ", SysUsage.System.RAMActiveProcessMemory(1234))
      
      # Network Section
      print("Network Interfaces: ", SysUsage.System.Interfaces())
      print("Network Interface Stats: ", SysUsage.System.InterfaceStats())
      
      print("Network Connections (inet): ", SysUsage.System.NetworkConnections('inet'))
      print("Network Stats: ", SysUsage.System.NetworkStats())
      
      # Replace 'eth0' with your actual interface name (e.g., 'wlan0', 'en0', etc.)
      print("Interface Network Stats (eth0): ", SysUsage.System.InterfaceNetworkStats('eth0'))
      
      print("Default Gateway: ", SysUsage.System.DefaultGateway())
      print("DNS Config: ", SysUsage.System.DNSConfig())
      
      # Replace 'eth0' with your actual interface name
      print("IP Address of eth0: ", SysUsage.System.IPAddress('eth0'))
      print("MAC Address of eth0: ", SysUsage.System.MACAddress('eth0'))
      
      print("Hostname: ", SysUsage.System.Hostname())
      print("FQDN: ", SysUsage.System.FQDN())
      print("Local IP Address: ", SysUsage.System.LocalIPAddress())
      
      # Replace 'eth0' with your actual interface name
      print("Interface State (eth0): ", SysUsage.System.InterfaceState('eth0'))
      print("Is Interface Up (eth0): ", SysUsage.System.IsInterfaceUp('eth0'))
      
      # Replace '1234' with your actual process ID
      print("Network Connections by PID (1234): ", SysUsage.System.NetworkConnectionsByPID(1234))
      
      print("Local Ports In Use: ", SysUsage.System.LocalPortsInUse())
      print("External IP Address: ", SysUsage.System.ExternalIPAddress())
      
      # Replace 'eth0' with your actual interface name
      print("Interface Type (eth0): ", SysUsage.System.InterfaceType('eth0'))
      
      # Replace 'psutil.sconn' with an actual connection object if you have one
      print("Connection Status: ", SysUsage.System.ConnectionStatus(None))  # Requires a valid connection object
      
      # Replace 'eth0' with your actual interface name
      print("Netmask of eth0: ", SysUsage.System.Netmask('eth0'))
