import json
from datetime import datetime
import os
#import 'global pattern matching'
import glob    

def get_latest_log_file():
    log_files = glob.glob("log_*.log")
    if not log_files:
        raise FileNotFoundError("No log_*.log files found.")
    return max(log_files, key=os.path.getctime)
 



def parse_line(line):
    #splitting line (max 3 splits)
    parts = line.strip().split(" - ", 3)
    
    #skip malformed lines
    if len(parts) < 4:
        return None

    try:
        #parsing timestamps
        dt = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S,%f")
        
        #extracting date and time format
        day = dt.strftime("%Y-%m-%d")
        time = dt.strftime("%H:%M:%S.%f")[:-3]  
    except ValueError:
        return None

    #return structured log entry
    return {
        "day": day,                    #date 
        "time": time,                  #time 
        "source": parts[1],            #source component
        "level": parts[2],             #log level 
        "message": parts[3]            #actual log message
    }

def main():
    #list to store parsed log entries
    log_file = get_latest_log_file()
    timestamp_str = log_file[len("log_") : -len(".log")]
    
    TXT_OUTPUT = f"{timestamp_str}.txt"
    JSON_OUTPUT = f"{timestamp_str}.json"
    
    
    parsed_entries = []

    #read log file and parsing each line
    with open(log_file, "r") as infile:
        for line in infile:
            parsed = parse_line(line)
            if parsed:
                parsed_entries.append(parsed)


    #parsed entries to text file
    with open(TXT_OUTPUT, "a") as txt_out:
    
        for entry in parsed_entries:
            txt_out.write(json.dumps(entry, indent=2) + "\n")
            txt_out.write("__________\n")

    #parsed entries to JSON file
    with open(JSON_OUTPUT, "a") as json_out:
        json.dump(parsed_entries, json_out, indent=2)

    #messages in terminal
    print(f"\n{TXT_OUTPUT} created")
    print(f"{JSON_OUTPUT} created\n")

if __name__ == "__main__":
    main()
