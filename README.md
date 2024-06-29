# PyProcData

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/romanmurzac/pyprocdata/actions/workflows/build.yml/badge.svg)](https://github.com/romanmurzac/pyprocdata/actions)
[![PyPI version](https://badge.fury.io/py/data_processor.svg)](https://badge.fury.io/py/data_processor)
[![codecov](https://codecov.io/gh/yourusername/data_processor/branch/main/graph/badge.svg?token=yourtoken)](https://codecov.io/gh/yourusername/data_processor)

## Description

PyProcData is a Python application that allows users to process data by applying transformations such as flattening nested dictionaries, unescaping HTML characters, and masking sensitive information. The processed data can be stored or provided as a downloadable file.

## Features

- **Flattening**: Convert nested dictionaries to a flat structure.
- **HTML Unescaping**: Convert HTML entities to their corresponding characters.
- **Masking**: Mask sensitive information in strings.
- **Upload and Download**: Process data from user uploads or storage and provide processed data for download.

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

### Run Test
Tests run:
```
pytest tests/  
```

Tests coverage:
```
pytest --cov=src --cov-report=term-missing
```

## Phases
Different phases of development and implementation.
Each phase will have similar processing functionalities, only the integration with the current stack will differ.

### Phase 1: *Local Development*
**Description:** Run in a Docker container and process data and store them to local disk.\
**Run:** Run on manual trigger.\
**Knowledge:** Need high technical knowledge for implementation.\
**Roadmap:** 29.06.2024 / 31.11.2024.\
**Status:** Work in progress. 5%.

### Phase 2: *PyPi Package*
**Description:** Run in a Docker container and process data and store them to local disk.\
**Run:** Run on manual trigger.\
**Knowledge:** Need high technical knowledge for implementation.\
**Roadmap** 20.07.2024 / 15.12.2024.\
**Status:** In backlog. 0%.

### Phase 3: *Public Manual UI*
**Description:** Run in a Web Application, upload input data, choose what processes to be aplied and download data.\
**Run:** Run on manual trigger.\
**Knowledge:** No technical knowledge required.\
**Roadmap:** 31.07.2024 / 31.12.2024.\
**Status:** In backlog. 0%.

### Phase 4: *Public Pipeline UI*
**Description:** Run in a Web Application, setup a source, setup a destination, create a connector based on source, desination, and processes to be applied.\
**Run:** Run on schedule or on trigger.\
**Knowledge:** Need low technical knowledge required.\
**Roadmap:** 31.08.2024 / 31.01.2025.\
**Status:** In backlog. 0%.

### Phase 5: *Private Pipeline UI*
**Description:** Run in a Private Web Application, setup a source, setup a destination, create a connector based on source, desination, and processes to be applied.\
**Run:** Run on schedule or on trigger.\
**Knowledge:** Need high technical knowledge required.\
**Roadmap:** 01.02.2025 / 30.08.2025.\
**Status:** In backlog. 0%.