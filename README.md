# pubmed-fetcher
# get-papers-dist

`get-papers-dist` is a Python command-line tool designed to fetch research papers from PubMed based on user-specified queries. The program identifies papers with authors affiliated with pharmaceutical or biotech companies and outputs the results in a structured CSV format. It uses the PubMed API for fetching articles and provides flexible options for filtering and saving results.

## Table of Contents
1. [Code Organization](#code-organization)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Tools Used](#tools-used)
5. [Contributing](#contributing)

## Code Organization
The project is organized as follows:
get-papers-dist/
├── paper_fetcher/
│ ├── init.py # Package initialization
│ ├── pubmed_client.py # Handles PubMed API integration
│ ├── author_analysis.py # Filters authors based on affiliations
│ └── csv_writer.py # Writes results to CSV format
├── tests/ # Unit tests for the project
├── pyproject.toml # Poetry configuration file
├── README.md # Project documentation
└── get_papers_dist/
└── cli.py # Command-line interface implementation


Key components:
- **paper_fetcher**: Contains core modules for API handling, author filtering, and CSV writing.
- **tests**: Includes unit tests to ensure code quality.
- **pyproject.toml**: Manages dependencies and packaging using Poetry.
- **cli.py**: Implements the command-line interface.

## Installation

### Prerequisites
- Python 3.8 or higher
- Poetry (Dependency management tool)

### Steps to Install
1. Clone the repository:
2. Install dependencies using Poetry:
3. Activate the virtual environment:

## Usage

### Basic Command-Line Usage
1. Fetch papers based on a query:
2. Save results to a CSV file:
3. Enable debug mode for detailed logs:
## Tools Used

### Libraries and Frameworks:
1. **[PyMed](https://pypi.org/project/pymed/)**: For interacting with the PubMed API.
2. **[Poetry](https://python-poetry.org/)**: Dependency management and packaging.
3. **[Python Standard Library](https://docs.python.org/3/library/)**: For CSV handling, command-line arguments, etc.

### External Resources:
- Markdown formatting guide: [Markdown Cheatsheet](https://www.markdownguide.org/basic-syntax/)
- PubMed API documentation: [PubMed API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
