hr_dataset_generator/
│
├── generate_dataset.py          # Main entry point
├── config.py                    # Company settings
├── generators/
│   ├── employees.py
│   ├── departments.py
│   ├── salary.py
│   ├── attendance.py
│   ├── leave.py
│   ├── performance.py
│   ├── holidays.py
│   └── errors.py
│
├── utils/
│   ├── helpers.py
│   └── faker_utils.py
│
└── output/

### 1. Running the Interactive Container
You must use the -it flags with docker run:

-i (interactive): Keeps STDIN open so you can type commands. 
-t (tty): Allocates a pseudo-terminal for proper formatting and signal handling (like Ctrl+C). 
```
docker build -t my-python-cli .
docker run -it --rm my-python-cli
```
Once inside, you have a full shell where you can run python, pip, or any installed CLI tool live. 


### 2. Run Docker with a Volume Mount
Use the `-v` (or `--mount`) flag to link your host's `output` folder to the container's `/data/output` folder. 

**Linux/macOS:**
```bash
docker run -it --rm -v $(pwd)/output:/data/output my-python-cli
```
**Windows (PowerShell):**
```powershell
docker run -it --rm -v ${PWD}/output:/data/output my-python-cli
```
**How it works:**

* `$(pwd)/output` (Host): Creates/uses an `output` folder in your current host directory.
* `/data/output` (Container): The path your Python script writes to.
* Result: As soon as `pd.ExcelWriter` finishes, the file appears instantly in your host's `output` folder. 