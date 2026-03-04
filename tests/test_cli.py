"""Tests for CLI interface."""

from click.testing import CliRunner
from ai_carbon_footprint.cli import main


def test_cli_basic():
    """Test basic CLI invocation."""
    runner = CliRunner()
    result = runner.invoke(main, ["--gpu", "A100", "--hours", "1000"])

    assert result.exit_code == 0
    assert "NVIDIA A100" in result.output
    assert "碳排放" in result.output


def test_cli_json_output():
    """Test JSON output format."""
    runner = CliRunner()
    result = runner.invoke(main, ["--gpu", "A100", "--hours", "100", "--output", "json"])

    assert result.exit_code == 0
    assert "gpu_name" in result.output
    assert "co2_kg" in result.output


def test_cli_all_parameters():
    """Test CLI with all parameters."""
    runner = CliRunner()
    result = runner.invoke(main, [
        "--gpu", "H100",
        "--hours", "500",
        "--num-gpus", "8",
        "--pue", "1.2",
        "--region", "us",
        "--utilization", "0.85"
    ])

    assert result.exit_code == 0
    assert "H100" in result.output


def test_cli_list_gpus():
    """Test list-gpus subcommand."""
    runner = CliRunner()
    result = runner.invoke(main, ["list-gpus"])

    assert result.exit_code == 0
    assert "A100" in result.output
    assert "H100" in result.output


def test_cli_list_regions():
    """Test list-regions subcommand."""
    runner = CliRunner()
    result = runner.invoke(main, ["list-regions"])

    assert result.exit_code == 0
    assert "global" in result.output
    assert "us" in result.output


def test_cli_invalid_gpu():
    """Test error handling for invalid GPU."""
    runner = CliRunner()
    result = runner.invoke(main, ["--gpu", "INVALID", "--hours", "100"])

    assert result.exit_code != 0
    assert "错误" in result.output or "Unknown GPU" in result.output


def test_cli_missing_arguments():
    """Test CLI with missing required arguments."""
    runner = CliRunner()
    result = runner.invoke(main, [])

    # Should show help when no arguments provided
    assert "Usage:" in result.output or "Calculate carbon" in result.output
