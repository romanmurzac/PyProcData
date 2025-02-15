# PyProcData

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/romanmurzac/pyprocdata/actions/workflows/build.yml/badge.svg)](https://github.com/romanmurzac/pyprocdata/actions)
[![PyPI version](https://badge.fury.io/py/data_processor.svg)](https://badge.fury.io/py/data_processor)
[![codecov](https://codecov.io/gh/romanmurzac/data_processor/branch/main/graph/badge.svg?token=yourtoken)](https://codecov.io/gh/romanmurzac/data_processor)

## Description

PyProcData is a Python application that allows users to process data by applying transformations such as flattening nested dictionaries, unescaping HTML characters, and masking sensitive information. The processed data can be stored or provided as a downloadable file.

## Features

- **Flattening**: Convert nested dictionaries to a flat structure.
- **HTML Unescaping**: Convert HTML entities to their corresponding characters.
- **Masking**: Mask sensitive information in strings.
- **Process**: Process data from user uploads or storage and provide processed data for download.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites

- Python 3.11 or higher

### Install
Clone the repository:
```
git clone https://github.com/romanmurzac/PyProcData.git
```
### Create virtual environment
Create virtual environment and activate it:
```
python3 -m venv venv
souce venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

### Run Test
Tests run:
```
pytest tests/  
```

Tests coverage:
```
pytest --cov=src --cov-report=term-missing
```

## Usage

## Configuration

## Testing

## Contributing

## License

## Contact