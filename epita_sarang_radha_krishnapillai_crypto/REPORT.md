# TP2 Report — Python Environments and Packaging

**Student:** R K Sarang  
**Group:** Group 2 — Crypto Assets  
**API:** CryptoCompare  
**Project:** `epita_sarang_radha_krishnapillai_crypto`

---

## 1. Python Environment Management

### 1.1 Comparing Python Environments

The `scripts/inspect_env.py` script displays the active Python executable, Python version, virtual environment prefix, base prefix, and import search paths.

The commands used were:

```powershell
python scripts/inspect_env.py
uv run python scripts/inspect_env.py
```

The observed Python executable was:

```text
C:\Users\Sarang\Documents\epita_sarang_radha_krishnapillai_crypto\.venv\Scripts\python.exe
```

Python version:

```text
3.14.8
```

Virtual environment prefix (`sys.prefix`):

```text
C:\Users\Sarang\Documents\epita_sarang_radha_krishnapillai_crypto\.venv
```

Base prefix (`sys.base_prefix`):

```text
C:\Users\Sarang\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none
```

The script reported:

```text
Is in Virtual Environment?
True
```

**Observation:** The Python executable and virtual environment prefix point to the project's `.venv` directory. The base prefix points to the Python installation managed by `uv`. This indicates that the commands shown were using the project's virtual environment.

### 1.2 Purpose of uv

`uv` is used to manage Python dependencies and project environments. It can create virtual environments, install packages, resolve dependencies, maintain a lockfile, run Python scripts, and build distributable packages.

Using `uv run` helps ensure that commands execute using the project's configured environment and dependencies.

### 1.3 Purpose of .gitignore

The `.gitignore` file excludes generated files and sensitive configuration from Git. The project ignores the virtual environment, `.env`, Python cache files, build artifacts, and package metadata.

This helps keep the repository cleaner and prevents private API credentials from being accidentally committed.

---

## 2. Live API Integration and Secret Hygiene

### 2.1 Environment Configuration

The project uses `python-dotenv` to load configuration from an `.env` file. The `.env.template` file provides example settings without containing the real API key.

Example template:

```dotenv
APP_ENV=development
DEBUG=True
CRYPTOCOMPARE_API_KEY=your_dummy_api_key_here
```

The actual API key is stored in the private `.env` file and is not included in this report.

### 2.2 CryptoCompare API Integration

The project uses the `requests` library to retrieve cryptocurrency prices from CryptoCompare.

The endpoint used is:

```text
https://min-api.cryptocompare.com/data/pricemultifull
```

The request retrieves BTC and ETH prices in USD and EUR. The API key is supplied through the authorization header, and the response is checked before its JSON data is returned.

The CLI displays the results using the `rich` library.

### 2.3 Live API Test

The application successfully retrieved cryptocurrency prices from the live API and displayed BTC and ETH prices in USD and EUR.

A previous test run displayed the following sample values:

```text
BTC USD: 80384.7
BTC EUR: 71854.9
ETH USD: 2329.22
ETH EUR: 2082.13
```

These values are from a previous run and are not current prices. Cryptocurrency prices change over time.

### 2.4 Security Considerations

**1. Protecting credentials**

Storing API keys in environment variables rather than directly in source code reduces the risk of exposing credentials when code is shared or published.

**2. Separating configuration**

Environment variables allow different API keys and settings to be used in different environments without modifying application source code.

### 2.5 Git Security Verification

The command used to check whether `.env` is ignored was:

```powershell
git check-ignore .env
```

Output:

```text
.env
```

This confirms that `.env` matches a Git ignore rule.

The command:

```powershell
git ls-files .env .env.template
```

returned:

```text
.env.template
```

This confirms that `.env.template` is tracked by Git, while `.env` is not listed as a tracked file by this command.

The `git status --short` output showed:

```text
?? scripts/REPORT.md
```

At the time of this check, the report file was untracked. The status output should be checked again before committing the completed report.

---

## 3. Dependency Management and Reproducibility

### 3.1 Project Dependencies

The project uses the following direct dependencies:

| Package | Purpose |
|---|---|
| `python-dotenv` | Loads configuration from `.env` |
| `requests` | Sends HTTP requests to CryptoCompare |
| `rich` | Formats CLI output |

The project also has `pytest` as a development dependency for testing.

The package requirements shown in `pyproject.toml` are:

```toml
dependencies = [
    "python-dotenv>=1.2.4",
    "requests>=2.34.2",
    "rich>=15.0.0",
]

[dependency-groups]
dev = [
    "pytest>=9.1.1",
]
```

### 3.2 Dependency Tree

The command:

```powershell
uv tree
```

reported 16 resolved packages.

```text
epita-sarang-radha-krishnapillai-crypto v0.1.0
├── python-dotenv v1.2.4
├── requests v2.34.2
│   ├── certifi v2026.10.23
│   ├── charset-normalizer v3.5.2
│   ├── idna v3.20
│   └── urllib3 v2.8.0
├── rich v15.0.0
│   ├── markdown-it-py v4.2.0
│   │   └── mdurl v0.1.2
│   ├── pygments v2.21.0
└── pytest v9.1.1 (group: dev)
    ├── colorama v0.4.6
    ├── iniconfig v2.3.1
    ├── packaging v26.3
    ├── pluggy v1.7.0
    └── pygments v2.21.0
```

The direct dependencies are declared by the project. Transitive dependencies are installed because other packages require them. For example, `requests` depends on `urllib3`, `certifi`, `charset-normalizer`, and `idna`.

`pytest` is listed under the development dependency group.

### 3.3 Purpose of uv.lock

The `pyproject.toml` file declares project metadata and dependency requirements. The `uv.lock` file records resolved dependency versions and package information.

The lockfile helps make installations reproducible across different environments. Package hashes, including SHA-256 hashes, can be used to verify the integrity of downloaded distributions.

### 3.4 Version Constraints

Semantic versioning uses three main components:

- **Major:** Incompatible changes.
- **Minor:** Backward-compatible features.
- **Patch:** Backward-compatible fixes.

The lab's example constraints illustrate different ways to restrict dependency versions:

| Constraint | Meaning |
|---|---|
| `^2.31.0` | Compatible versions from 2.31.0 up to, but not including, 3.0.0 |
| `~=2.2.1` | Compatible versions from 2.2.1 up to, but not including, 2.3.0 |
| `==13.7.1` | Exactly version 13.7.1 |

Under the caret constraint `^2.31.0`, version `3.0.0` is excluded because it changes the major version.

These are examples of version-constraint notation from the lab, not the exact constraints currently declared in this project's `pyproject.toml`.

---

## 4. CLI, Package Build, and TestPyPI

### 4.1 CLI Entry Point

The project defines the following command-line entry point:

```toml
[project.scripts]
epita-sarang-cli = "epita_sarang_radha_krishnapillai_crypto.cli:main"
```

This maps the `epita-sarang-cli` command to the `main` function in the package's `cli.py` module.

The CLI retrieves cryptocurrency prices and displays them in a formatted terminal interface.

### 4.2 Building the Package

The package was built using:

```powershell
uv build
```

The build succeeded and generated two distribution files:

```text
dist/epita_sarang_radha_krishnapillai_crypto-0.1.0.tar.gz
dist/epita_sarang_radha_krishnapillai_crypto-0.1.0-py3-none-any.whl
```

The `.whl` file is a wheel distribution, while the `.tar.gz` file is a source distribution.

### 4.3 Publishing to TestPyPI

The package was successfully uploaded to TestPyPI using `uv publish`.

The upload endpoint was:

```text
https://test.pypi.org/legacy/
```

The published package page is:

https://test.pypi.org/project/epita-sarang-radha-krishnapillai-crypto/

The published version is `0.1.0`.

TestPyPI is a test environment for Python package distribution. It allows developers to test publishing and installation workflows before using the production Python Package Index.

The publishing token is not included in this report.

### 4.4 Testing the Installed Package

After publication, the package was installed and run from a separate temporary directory. The CLI successfully retrieved and displayed BTC and ETH prices in USD and EUR.

This test helped verify that the packaged application could run outside its original development directory.

---

## 5. Debugging Challenge

### 5.1 Initial Problem

The debugging challenge involved processing records containing `volume` and `weight` values. These values were initially represented as strings, even though the program needed to perform numerical calculations.

Using strings where numeric values are expected can lead to type errors or incorrect calculations.

### 5.2 Debugging Process

The script `scripts/debug_challenge.py` was inspected using the VS Code debugger.

The debugging process involved:

1. Setting a breakpoint.
2. Inspecting the input record and its field types.
3. Stepping through `compute_weighted_metric`.
4. Examining the call stack to understand the sequence of function calls.
5. Identifying the need to convert string values into numeric values before performing arithmetic.

### 5.3 Fix Implemented

The parsing logic was updated to convert the `volume` and `weight` values to floating-point numbers.

The essential conversion is:

```python
volume = float(record["volume"])
weight = float(record["weight"])
```

This ensures that the values are numeric before calculations are performed.

### 5.4 Validation Results

The command:

```powershell
uv run python scripts/debug_challenge.py
```

produced:

```text
Aggregate Result: {'successful_entries': 3, 'total_volume': 650.0, 'avg_volume': 216.66666666666666, 'high_impact_count': 1}
```

The result is consistent with the three successful records:

- Total volume: `120 + 450 + 80 = 650`
- Average volume: `650 / 3 = 216.66666666666666`
- High-impact count: `1`, because only the weighted metric `450 × 3 = 1350` exceeds the threshold of `500`.

The debugging exercise demonstrated how breakpoints, variable inspection, and call-stack analysis can be used to identify and fix runtime type problems without relying only on temporary print statements.

---

## 6. Conclusion

This project demonstrates the use of `uv` for Python environment and dependency management, integration with a live CryptoCompare API, secure handling of API credentials, dependency locking, package building, and publication to TestPyPI.

The project uses `requests` for API communication, `python-dotenv` for configuration, and `rich` for the CLI interface. The package was built successfully, and its published version was tested independently of the original development directory.

The debugging challenge also demonstrated the importance of validating data types and using an interactive debugger to identify and fix errors.

Overall, the lab provided practical experience with Python packaging, environment isolation, dependency management, API integration, secret hygiene, and systematic debugging.