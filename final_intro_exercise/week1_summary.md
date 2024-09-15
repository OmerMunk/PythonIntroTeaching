# Final exercise

## introduction
- you will make an advanced Terrorist Threat Intelligence System that can:
  - analyze multiple data sources (intercepted communications, intelligence reports, field operations)
  - predict and prevent terrorist attacks.

## tech overview:
- multiple files where it makes sense
- packages
- modules
- all python concepts we have learned (classes, inheritence, abstract methods, class methods, decorators, data pipelines and more)


## project structure:
`
terror_pipline/
│
├── data/
│   ├── intercepted_communications.txt
│   ├── intelligence_reports.txt
│   └── field_operations.csv
│
├── analysis/
│   ├── __init__.py
│   ├── base.py
│   ├── communication.py
│   ├── intelligence.py
│   └── operations.py
│
├── tools/
│   ├── __init__.py
│   ├── helpers.py
│   └── utils.py
│
├── main.py
└── tester.py
`

## Files and responsibilites:
- data/: contains input data files
  - intercepted_communications.txt: Intercepted communications data in plain text.
  - intelligence_reports.txt: Intelligence reports data in plain text.
  - field_operations.csv: Field operations data in CSV format.


- analysis/: contains analysis files
  - base.py: Defines abstract base classes and common functionality.
  - communication.py: Manages the analysis of intercepted communications.
  - intelligence.py: Handles the analysis of intelligence reports.
  - operations.py: Manages the analysis and execution of field operations.


- tools/: contains tools files
  - intercepted_communications.txt: Intercepted communications data in plain text.
  - intelligence_reports.txt: Intelligence reports data in plain text.
  - utils.py: Contains utility functions for reading/writing files, logging, and other helper methods.

main.py: The main entry point for running the system.


## tech requirements
- `AnalysisUnit` is an abstract base class with `analyze` abstract method
- `CommunicationAnalysis`, `IntelligenceReportAnalysis`, and `FieldOperationsAnalysis` inherit from `IntelligenceAnalysisUnit`.
- `IntelligenceAnalysisUnit` inherits from both `AnalysisUnit` and `Loggable`.



# Terrorist Threat Data Pipeline

## Project Overview

The **Terrorist Threat Data Pipeline** project aims to build a data pipeline that processes and analyzes multiple data sources, such as intercepted communications, intelligence reports, and field operations data, to predict and prevent terrorist attacks. This project will involve reading data from various files, performing data transformations, aggregations, and generating reports that help in decision-making.

## Final Required Result

By the end of this project, you should have a fully functional data pipeline that:
1. **Processes intercepted communication data** to extract useful metrics.
2. **Analyzes intelligence reports** to identify urgent actions or suspicious activities.
3. **Aggregates field operations data** to summarize and report key findings.
4. **Generates logs** and **outputs results** in a format suitable for further analysis by intelligence teams.

You should make use of Python's advanced features, such as:
- Data processing and transformation using `map`, `filter`, `reduce`, `zip`, and `groupby`.
- Decorators to enhance function behavior.
- Magic methods (`__eq__`, `__str__`, `__repr__`).
- Abstract classes, properties, and class methods for code organization and reusability.
- File handling for reading input data and writing outputs.



## Function Requirements


#### `class AnalysisUnit(ABC)`

- An abstract base class that defines the `analyze` method, which should be implemented by all derived classes.

#### `class IntelligenceAnalysisUnit(AnalysisUnit, Loggable)`

- Inherit from both `AnalysisUnit` and `Loggable`.
- Use `@property` and `@property.setter` to manage the `name` attribute.
- Implement magic methods `__eq__`, `__str__`, and `__repr__` to provide custom comparison, string representation, and debug information.


#### `clean_data(data)`

- **Purpose**: Cleans and transforms raw data into a usable format.
- **Logic**: 
  - Use list comprehensions and `map` to apply transformations to the data.
  - Use `filter` to remove rows with invalid or missing data (e.g., rows without a date or necessary fields).

#### `aggregate_operations(data)`

- **Purpose**: Groups operations data by date and counts the number of operations per day.
- **Logic**:
  - Use `groupby` to group data by the 'Date' field.
  - Use a combination of `map` and `reduce` to aggregate counts for each group.

#### `calculate_communication_metrics(lines)`

- **Purpose**: Calculates metrics from intercepted communication data.
- **Logic**:
  - Use `map` to compute the number of words in each line.
  - Use `reduce` to compute the total number of words and the average number of words per line.


#### `log_decorator(func)`

- **Purpose**: A decorator to log the execution of any function it wraps.
- **Logic**:
  - Use `*args` and `**kwargs` to accept any number of arguments and keyword arguments for the wrapped function.
  - Log the name of the function that was executed.

#### `class CommunicationAnalysis(IntelligenceAnalysisUnit)`

- **Methods**:
  - `__init__(self, name)`: Initialize with a name.
  - `analyze(self)`: Analyze intercepted communication data.
    - **Logic**:
      - Use `calculate_communication_metrics` from `data_processing.py` to get metrics.
      - Log the results using the `log` method.
  - `_load_data(self)`: Loads communication data from the text file.
    - **Logic**:
      - Use file handling methods to read data.


#### `class IntelligenceReportAnalysis(IntelligenceAnalysisUnit)`

- **Methods**:
  - `__init__(self, name)`: Initialize with a name.
  - `analyze(self)`: Analyze intelligence reports to find urgent messages.
    - **Logic**:
      - Use `filter` to identify lines containing the keyword "urgent".
      - Log the results using the `log` method.
  - `_load_data(self)`: Loads intelligence report data from the text file.
    - **Logic**:
      - Use file handling methods to read data.


#### `class FieldOperationsAnalysis(IntelligenceAnalysisUnit)`

- **Methods**:
  - `__init__(self, name)`: Initialize with a name.
  - `analyze(self)`: Analyze field operations data to generate aggregated statistics.
    - **Logic**:
      - Use `clean_data` and `aggregate_operations` from `data_processing.py`.
      - Log the results using the `log` method.
  - `_load_data(self)`: Loads field operations data from the CSV file.
    - **Logic**:
      - Use file handling methods to read and parse CSV data.


#### `read_file(file_path)`

- **Purpose**: Reads the contents of a file given its path.
- **Logic**:
  - Use Python's built-in file handling (`open`) to read the file.

#### `write_to_file(file_path, content)`

- **Purpose**: Writes content to a file given its path.
- **Logic**:
  - Use Python's built-in file handling (`open` with write mode) to write data.

## Final Instructions

1. Implement the methods in the appropriate files.
2. Make sure to use Python's advanced features (`map`, `filter`, `reduce`, `zip`, `groupby`, decorators, and magic methods) as described.
3. Run `tester.py` to validate the correctness of your implementation.
4. Ensure that your final pipeline processes all the data correctly and outputs the required results.

Good luck!





















