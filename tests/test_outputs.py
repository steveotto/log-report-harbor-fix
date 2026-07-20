import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report():
    assert REPORT_PATH.is_file(), "Expected /app/report.json to exist"

    try:
        with REPORT_PATH.open(encoding="utf-8") as report_file:
            report = json.load(report_file)
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc

    assert isinstance(report, dict), "The report must be a JSON object"
    return report


def test_total_requests():
    report = load_report()

    assert type(report.get("total_requests")) is int
    assert report["total_requests"] == 6


def test_unique_ips():
    report = load_report()

    assert type(report.get("unique_ips")) is int
    assert report["unique_ips"] == 3


def test_top_path():
    report = load_report()

    assert type(report.get("top_path")) is str
    assert report["top_path"] == "/index.html"


def test_exact_schema():
    report = load_report()

    assert set(report.keys()) == EXPECTED_KEYS
