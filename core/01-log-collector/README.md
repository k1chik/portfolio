# Log Collector

This project provides a simple framework for running basic number algorithms, logging their execution, and processing the resulting logs into structured formats.

## File Overview

- **main_app.py**  
  Entry point for running the algorithms. Generates random numbers, calls various functions from `algorithms.py`, and logs all activity to a timestamped log file.

- **algorithms.py**  
  Contains several number-related functions (e.g., check if a number is even, find smallest/largest, check primality, etc.). Each function is decorated to log its calls, arguments, results, and execution time.

- **log_processor.py**  
  Parses the latest log file generated by `main_app.py`, extracts structured information from each log entry, and outputs both a `.txt` and `.json` file with the parsed data.

## How to Use

1. **Run the Algorithms and Generate Logs**

   In your terminal, execute:
`python main_app.py`

## This will

- Generate random numbers and arrays.
- Run various algorithms on them.
- Log all function calls, arguments, results, and execution times to a file named like `log_HHMMSS.log` (with the current time).

2. **Process the Log File**

After running `main_app.py`, process the latest log file by running:

"python log_processor.py"

This will:
- Find the most recent `log_*.log` file.
- Parse each log entry into structured data.
- Output two files:  
  - `<timestamp>.txt` — human-readable, pretty-printed log entries  
  - `<timestamp>.json` — structured JSON array of log entries

## Example Workflow

```sh
python [main_app.py](http://_vscodecontentref_/2)
# ...outputs to log_123456.log

python [log_processor.py](http://_vscodecontentref_/3)
# ...creates 123456.txt and 123456.json
