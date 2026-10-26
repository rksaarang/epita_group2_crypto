# EPITA Engineering Tools TP2 — CryptoCompare Report

**Author:** Tharun Gunasekar  
**EPITA login:** `tharun.gunasekar`  
**Package:** `epita-tharun-gunasekar-crypto`  
**Version:** `0.1.0`  
**Python:** `3.14.8`

## Part 1 — Python Environment and `uv`

The project environment was synchronized successfully using `uv sync`.

The environment inspection script, `scripts/inspect_env.py`, confirmed that:

- Python version is 3.14.8.
- The Python executable is inside the project's `.venv` directory.
- `sys.prefix` differs from `sys.base_prefix`, confirming that a virtual environment is active.
- The `CRYPTOCOMPARE_API_KEY` environment variable is configured.
- Python import paths and PATH entries were inspected.

The `.env` file contains the local API credentials and is excluded from Git. `.env.template` provides a placeholder configuration for other users.

## Part 2 — REST API Integration and Configuration

The application connects to the CryptoCompare REST API to retrieve cryptocurrency market data.

The CLI successfully retrieved live data for:

- Bitcoin (BTC) in USD and EUR.
- Ethereum (ETH) in USD and EUR.
- Prices and market capitalization.

The CLI displayed a `LIVE_SUCCESS` status and a formatted terminal table.

Configuration is loaded through environment variables using `python-dotenv`. The API key is read from `CRYPTOCOMPARE_API_KEY`; the actual key is not included in this report.

## Part 3 — Dependencies and Version Control

The command `uv tree` completed successfully and resolved 16 packages.

Direct runtime dependencies:

- `python-dotenv` 1.2.4
- `requests` 2.34.2
- `rich` 15.0.0

Development dependency:

- `pytest` 9.1.1

The dependency tree also showed the required transitive dependencies, including `certifi`, `charset-normalizer`, `idna`, `urllib3`, `markdown-it-py`, and `pygments`.

The project uses `pyproject.toml` to declare its metadata and dependencies, while `uv.lock` records the resolved dependency versions.

Git ignore checks confirmed that `.env`, `.venv`, and `dist/` are ignored. This helps prevent accidental inclusion of secrets, virtual-environment files, and generated build artifacts.

## Part 4 — Build and TestPyPI Publishing

The command `uv build` completed successfully and generated both distributions:

- `dist/epita_tharun_gunasekar_crypto-0.1.0.tar.gz`
- `dist/epita_tharun_gunasekar_crypto-0.1.0-py3-none-any.whl`

The CLI was also executed successfully using:

`uv run epita-tharun-gunasekar-cli`

**TestPyPI publication status:** Pending verification. Add the successful publication details and TestPyPI package URL after the upload completes. Do not mark this step as completed until the upload is confirmed.

## Part 5 — Debugging Challenge

The debugging exercise is implemented in `scripts/debug_challenge.py`.

The parsing function converts the numeric `volume` and `weight` fields to floating-point values. This ensures that weighted calculations use numeric values rather than strings.

In Visual Studio Code, a conditional breakpoint was configured with the condition `idx == 2`. During debugging:

- The loop index was verified as `2`.
- `type(record["volume"])` returned `<class 'float'>`.
- `type(record["weight"])` returned `<class 'float'>`.
- The expression `record["volume"] * record["weight"]` evaluated to `1350.0` for the third record.
- The Call Stack was inspected to identify the active function and its caller.

After continuing execution, the script produced:

```text
Aggregate Result: {'successful_entries': 3, 'total_volume': 650.0, 'avg_volume': 216.66666666666666, 'high_impact_count': 1}
```

The result confirms that three entries have `SUCCESS` status, their total volume is `650.0`, their average volume is approximately `216.67`, and one successful entry exceeds the high-impact threshold.

## Automated Tests

The command `uv run pytest` completed successfully.

Result:

```text
3 passed in 0.06s
```

The tests cover numeric parsing, the expected aggregation result, and empty-payload handling.

## Conclusion

The project environment, live API integration, dependency resolution, automated tests, package build, and debugging exercise were verified successfully. TestPyPI publication remains to be confirmed before the report is finalized for submission.
