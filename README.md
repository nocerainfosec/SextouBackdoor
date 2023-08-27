# SextouBackdoor

SextouBackdoor is a cross-platform, educational offensive tool written in Python 3. This tool includes both the listener and client components for establishing a remote connection and executing commands on a target machine. Please note that this tool is intended for educational use only. 🛠️🔒

## Features

- Remote command execution on the target machine.
- Cross-platform compatibility (Python 3).
- Minimal setup required.
- Educational tool only. 📘🎓

## Disclaimer

This tool is provided for educational purposes only. Misuse of this tool on unauthorized systems is illegal. The developer is not responsible for any illegal activities performed using this tool. 🚫🕊️

## Usage

### Listener

1. Clone the repository:

   ```bash
   git clone https://github.com/nocerainfosec/SextouBackdoor.git
   cd SextouBackdoor
   ```

2. Run the listener script:

   ```bash
   python listener.py
   ```

3. Follow the on-screen instructions and enter your educational use oath.

4. The listener will wait for incoming connections from the client.

### Client

1. Clone the repository:

   ```bash
   git clone https://github.com/nocerainfosec/SextouBackdoor.git
   cd SextouBackdoor
   ```

2. Edit the `client.py` script to set the appropriate `host` and `port` values to match the listener's IP address and port. Change the following line in `client.py`:

   ```python
   host = "127.0.0.1"
   ```

   Replace `"127.0.0.1"` with the IP address of the machine running the listener.

3. Run the client script:

   ```bash
   python client.py
   ```

4. The client will establish a connection with the listener. You can now input commands on the listener's side to be executed on the client's machine.

## Creating Standalone Executables with PyInstaller

You can create standalone executables for different operating systems using PyInstaller:

- **Windows:**

   Open a Command Prompt and navigate to the directory where your `listener.py` and `client.py` scripts are located.

   ```bash
   pyinstaller --onefile --noconsole listener.py
   pyinstaller --onefile --noconsole client.py
   ```

- **macOS:**

   Open the Terminal and navigate to the directory where your `listener.py` and `client.py` scripts are located.

   ```bash
   pyinstaller --onefile --noconsole listener.py
   pyinstaller --onefile --noconsole client.py
   ```

- **Linux:**

   Open a terminal window and navigate to the directory where your `listener.py` and `client.py` scripts are located.

   ```bash
   pyinstaller --onefile --noconsole listener.py
   pyinstaller --onefile --noconsole client.py
   ```

The standalone executables will be generated in the `dist` directory within the project folder.

## Requirements

- Python 3.x
- PyInstaller (for creating standalone executables)

## Legal Notice

This tool is intended to be used for educational purposes only. It is the user's responsibility to ensure that their usage complies with all applicable laws and regulations. The developer disclaims any responsibility for any misuse or damage caused by this tool. 📜⚖️

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
