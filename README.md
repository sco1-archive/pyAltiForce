# pyAltiForce
Python Parsing for AltiForce GoPro Backpack CSVs

The CSV file is processed and a plot of time vs. total acceleration is displayed.

## Usage
Calling `pyAltiForce` from the command line with no arguments opens a file selection GUI for the user to select a single CSV file to process and display.

Calling `pyAltiForce` with the optional `-f` or `--file` flag will allow the user to specify a single CSV file to process.

Examples Include:

    python pyAltiForce -f './Data/GOPR0024.CSV'
    python pyAltiForce --file 'C:/My Data/GOPR0024.CSV'