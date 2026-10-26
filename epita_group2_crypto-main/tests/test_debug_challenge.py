import sys
from pathlib import Path

# Make the assignment script importable for pytest.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from debug_challenge import (
    aggregate_telemetry,
    parse_api_record,
)


def test_parse_api_record_converts_numbers():
    record = parse_api_record("REC_001,service_alpha,120,SUCCESS,2")

    assert record["volume"] == 120.0
    assert record["weight"] == 2.0
    assert isinstance(record["volume"], float)
    assert isinstance(record["weight"], float)


def test_aggregate_telemetry_expected_result():
    payload = [
        "REC_001,service_alpha,120,SUCCESS,2",
        "REC_002,service_beta,0,FAILURE,1",
        "REC_003,service_gamma,450,SUCCESS,3",
        "REC_004,service_delta,80,SUCCESS,1",
        "REC_005,service_epsilon,1500,PENDING,4",
    ]

    result = aggregate_telemetry(payload)

    assert result["successful_entries"] == 3
    assert result["total_volume"] == 650.0
    assert result["avg_volume"] == 650.0 / 3
    assert result["high_impact_count"] == 1


def test_aggregate_telemetry_empty_payload():
    result = aggregate_telemetry([])

    assert result["successful_entries"] == 0
    assert result["total_volume"] == 0.0
    assert result["avg_volume"] == 0.0
    assert result["high_impact_count"] == 0
