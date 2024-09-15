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



















