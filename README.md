
# File Integrity Verification using SHA-256

## About the Project
File Integrity Verification using SHA-256 is a Python-based application that detects changes in files using cryptographic hashing. It generates a reference hash for a selected file and compares it with a newly generated hash during verification.

If both hashes match, the file is considered unchanged. If the hashes differ, the application reports that the file has been modified.

## Features
- Select files using a graphical user interface.
- Generate SHA-256 reference hashes.
- Verify the integrity of unchanged files.
- Detect file modifications through hash comparison.
- Display reference and current hash values.
- Support different file types through binary file handling.

## Technologies Used
- **Python** — Core programming language
- **hashlib** — SHA-256 hash generation
- **Tkinter** — Graphical user interface
- **Visual Studio Code** — Development environment
- **Git and GitHub** — Version control and project hosting

## How It Works
1. Select a file.
2. Generate and store its reference SHA-256 hash.
3. Verify the selected file when required.
4. Generate its current hash.
5. Compare the reference and current hashes.
6. Display the verification result.

**Matching hashes:** File Integrity Verified

**Different hashes:** File Modification Detected

## How to Run
1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in Visual Studio Code.
4. Run the following command in the terminal:

   ```bash
   python file_integrity.py
   ```

5. Select a file and generate its reference hash.
6. Verify the file to check its integrity.

## Testing
The application was tested using a sample text file.

- **Test 1:** Generated a SHA-256 reference hash successfully.
- **Test 2:** Verified the file when its contents remained unchanged.
- **Test 3:** Modified the file and successfully detected the change.

## Project Report
The project report documents the problem statement, methodology, tools and technologies, results and analysis, advantages, limitations, conclusion, and future work.

## Future Enhancements
- Support verification of multiple files and folders.
- Add file change monitoring and automatic alerts.
- Maintain verification history and timestamps.
- Improve reference hash protection and security.

## Author
**Asfina Magi**

B.Tech CSE – AI & ML
