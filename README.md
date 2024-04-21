# TimeKeeper App

TimeKeeper App is a simple and intuitive time tracking tool designed to help individuals monitor their work hours. Built using Python and Tkinter for a graphical user interface, this desktop application allows users to clock in and out with a click of a button, keep a log of all activities, and display the total worked time dynamically. This Readme provides an overview of the application features, installation steps, and how to get started.

## Features

- **Clock In/Out**: Users can start or end their work sessions using dedicated buttons, making it easy to track work hours accurately.
- **Worked Time Display**: Displays the total amount of time worked during the current session and updates in real-time.
- **Log History**: View a detailed log of all clock in and clock out times.
- **Persistent Logs**: Work sessions are logged in a text file, allowing users to review their previous sessions anytime.
- **Dynamic UI Updates**: The background color of the app changes depending on the user's status (clocked in or out), providing a visual indicator of the current state.

## Installation

To run the TimeKeeper App, you'll need Python installed on your computer. The app is developed with Python 3.8 or later. Follow these steps to set up the app:

1. **Clone the Repository or Download the Source Code**:
   - If you have git installed, you can clone the repository using:
     ```
     git clone https://github.com/LiberlandHacker/TimeKeeperApp.git
     ```
   - Alternatively, download the source code as a zip file and extract it.

2. **Install Python**:
   - If you do not have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

3. **Navigate to the App Directory**:
   - Open a terminal or command prompt and navigate to the directory where you have the TimeKeeper App source code.

4. **Run the Application**:
   - Execute the following command in the terminal:
     ```
     python timekeeper_app.py
     ```

## Usage

Once the application starts, you will see a simple window with the following components:

- **Clock In Button**: Click to start recording your work time.
- **Clock Out Button**: Click to stop recording your work time.
- **Show Logs Button**: Displays all past entries from your work log.
- **Text Area**: Displays the log history or the total worked time dynamically.

**Note**: The log file (`punch_log.txt`) will be created in the same directory as the application if it does not already exist. This file contains all clock-in and clock-out actions.

## Contributions

Contributions to the TimeKeeper App are welcome. If you have suggestions for improvements or bug fixes, please feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.

## Contact

For support or to contact the developer, please email support@example.com.

---
Enjoy tracking your time with the TimeKeeper App, designed to make work hour monitoring straightforward and hassle-free!
