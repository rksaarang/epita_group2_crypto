# CryptoCompare - EPITA Engineering Tools TP2

**Author:** Tharun Gunasekar  
**EPITA login:** `tharun.gunasekar`  
**Python version:** 3.14+

## Overview

CryptoCompare is a Python command-line application that retrieves live cryptocurrency market data from the CryptoCompare REST API.

The application retrieves Bitcoin (BTC) and Ethereum (ETH) prices in USD and EUR and displays the results, including market capitalization, in a formatted terminal table.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- A valid CryptoCompare API key

## Setup

Open a terminal in the project root and synchronize the project environment:

```powershell
uv sync
```

Create your local environment file from the template:

```powershell
Copy-Item .env.template .env
```

Edit `.env` and replace the placeholder with your own API key:

```dotenv
APP_ENV=development
DEBUG=True
CRYPTOCOMPARE_API_KEY=your_actual_api_key_here
```

Never commit or share your `.env` file.

## Run the application

Display live cryptocurrency prices:

```powershell
uv run epita-tharun-gunasekar-cli
```

Run the environment inspection script:

```powershell
uv run python .\scripts\inspect_env.py
```

Run the debugging challenge:

```powershell
uv run python .\scripts\debug_challenge.py
```

## Build the package

```powershell
uv build
```

The wheel and source distribution are generated in the `dist/` directory.

## Project structure

```text
.
├── .env.template
├── .gitignore
├── .python-version
├── README.md
├── REPORT.md
├── pyproject.toml
├── uv.lock
├── scripts/
│   ├── inspect_env.py
│   └── debug_challenge.py
└── src/
    └── epita_tharun_gunasekar_crypto/
        ├── __init__.py
        ├── config.py
        ├── client.py
        └── cli.py
```

## Security

API credentials are loaded from local environment configuration. The `.env` file, virtual environment, build artifacts, and Python caches are excluded from Git where configured.

## Assignment report

See [REPORT.md](REPORT.md) for the environment analysis, API integration, dependency management, build and publishing steps, and debugging exercise results.
