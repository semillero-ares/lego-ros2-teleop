# LEGO NXT Brick Setup with WSL2

## What We've Learned

1. Windows shows Bluetooth devices as COM ports (COM3-COM13) when they use the Serial Port Profile
2. The NXT brick uses Bluetooth Serial Port Profile (SPP), unlike modern devices (headphones, keyboards) which use different profiles
3. We'll need to bridge Windows COM ports to WSL2 using `socat`

## Next Steps

When you get the NXT brick:

1. Pair the NXT brick with Windows
2. Check which COM port it's assigned:
   ```powershell
   Get-CimInstance -ClassName Win32_SerialPort | Select-Object Name, DeviceID
   ```

3. Create the bridge (replace X with COM port number minus 1):
   ```bash
   sudo socat -d -d pty,raw,echo=0 /dev/ttySX
   ```

4. Test the connection using Python and the `pyserial` library

## Project Goals

- Connect to NXT brick from WSL2 through Windows Bluetooth
- Implement ROS2 teleop control
- Create a user interface for robot control

---

# MkDocs Reference

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
