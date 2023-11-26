# QR Code Registration System

This repository implements a QR Code-based registration system, comprising two components: a web application for registration using Flask and a GUI interface built with Python and Qt5.

## Overview

The system leverages QR codes for efficient registration, offering a web-based platform for user registration and a desktop GUI interface for quick access to registered information.

## Components

### 1. Web Application (Registration)

- **Features:**
  - User-friendly registration form.
  - Dynamic QR code generation for each registration.
  - Data validation for accurate information.

- **Getting Started:**
  1. Clone the repository.
  ```bash
  git clone https://github.com/hima890/QrcodeSystem_IEEE.git
  ```

  2. Install dependencies.
  ```bash
  pip install -r requirements.txt
  ```

  3. Run the Flask web application.
  ```bash
  python run_server.py
  ```
  Open your browser and go to [http://localhost:5000](http://localhost:5000) to access the registration page.

### 2. GUI Interface (Python with Qt5)

- **Features:**
  - Simple interface for scanning QR codes.
  - Instant retrieval of registered information.
  - Intuitive design for ease of use.

- **Getting Started:**
  1. Clone the repository.
  ```bash
  git clone https://github.com/hima890/QrcodeSystem_IEEE.git
  cd QrcodeSystem_IEEE/gui-interface
  ```

  2. Install dependencies.
  ```bash
  pip install -r requirements.txt
  ```

  3. Run the Python script for the GUI.
  ```bash
  python gui.py
  ```

## Customization

Feel free to customize both the web application and the GUI interface based on your specific requirements. Modify the UI, add features, or integrate additional functionalities as needed.

## Contributing

Contributions are welcome! If you encounter issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy coding and QR code registration!
