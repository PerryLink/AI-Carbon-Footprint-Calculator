<div align="center">

# AI-Carbon-Footprint-Calculator
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/ai-carbon-footprint-calculator)

**A Python CLI tool for estimating CO₂ emissions from AI GPU compute workloads.**

*Ported into [dsh-budget](https://github.com/PerryLink/dsh-budget) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

`ai-carbon-footprint` estimates the energy use and CO₂ emissions of an AI workload from the GPU model,
runtime hours, GPU count, utilization, PUE, and regional carbon intensity. It also prints concrete
comparisons (e.g. "equivalent to X cars driving for a year") and supports JSON output.

## Features

- 🎯 17 mainstream GPUs (NVIDIA, AMD, Google TPU)
- 🌍 8 regional carbon-intensity values (global, us, eu, china, india, uk, france, iceland)
- ⚡ PUE (Power Usage Effectiveness) coefficient
- 📊 Concrete everyday comparisons
- 🎨 Rich terminal output, plus JSON format

## Quick start

```bash
pip install ai-carbon-footprint

ai-carbon-footprint --gpu A100 --hours 1000
ai-carbon-footprint -g A100 -h 1000
```

## Usage

```bash
# 8 H100 GPUs, custom PUE, region, and utilization
ai-carbon-footprint -g H100 -h 500 -n 8 -p 1.2 -r us -u 0.85

# JSON output
ai-carbon-footprint -g A100 -h 100 --output json

# List supported GPUs and regions
ai-carbon-footprint list-gpus
ai-carbon-footprint list-regions
```

### Options

- `-g, --gpu` — GPU model (required)
- `-h, --hours` — runtime in hours (required)
- `-n, --num-gpus` — GPU count (default 1)
- `-p, --pue` — PUE coefficient (default 1.58)
- `-r, --region` — region code (default `global`)
- `-u, --utilization` — GPU utilization 0–1 (default 1.0)
- `-o, --output` — `text` or `json` (default `text`)

### Calculation

```
GPU energy (kWh)    = TDP × hours × GPU count × utilization / 1000
Total energy (kWh)  = GPU energy × PUE
CO₂ emissions (kg)  = Total energy × carbon intensity
```

## Supported GPUs

| Model | Name | TDP (W) | Category |
|-------|------|---------|----------|
| A100 | NVIDIA A100 | 400 | datacenter |
| A100-80GB | NVIDIA A100 80GB | 400 | datacenter |
| H100 | NVIDIA H100 | 700 | datacenter |
| H100-80GB | NVIDIA H100 80GB | 700 | datacenter |
| V100 | NVIDIA V100 | 300 | datacenter |
| A40 | NVIDIA A40 | 300 | datacenter |
| A30 | NVIDIA A30 | 165 | datacenter |
| A10 | NVIDIA A10 | 150 | datacenter |
| RTX-4090 | NVIDIA RTX 4090 | 450 | consumer |
| RTX-4080 | NVIDIA RTX 4080 | 320 | consumer |
| RTX-3090 | NVIDIA RTX 3090 | 350 | consumer |
| RTX-3080 | NVIDIA RTX 3080 | 320 | consumer |
| MI250X | AMD MI250X | 560 | datacenter |
| MI210 | AMD MI210 | 300 | datacenter |
| MI100 | AMD MI100 | 300 | datacenter |
| TPU-v4 | Google TPU v4 | 450 | tpu |
| TPU-v3 | Google TPU v3 | 450 | tpu |

## Carbon intensity data

| Region | Carbon intensity (kg CO₂/kWh) |
|--------|--------------------------------|
| global | 0.475 |
| us | 0.386 |
| eu | 0.276 |
| china | 0.555 |
| india | 0.708 |
| uk | 0.233 |
| france | 0.056 |
| iceland | 0.010 |

## Data sources

- GPU TDP data: NVIDIA, AMD, Google official specifications
- Carbon intensity data: IEA (International Energy Agency) annual reports
- PUE data: Uptime Institute data-center surveys

## Project structure

```
ai-carbon-footprint/
├── src/ai_carbon_footprint/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # python -m entry point
│   ├── cli.py               # CLI interface
│   ├── core.py              # Core calculation logic
│   ├── data.py              # GPU database and constants
│   └── comparisons.py       # Concrete comparison functionality
├── tests/                   # test_core.py, test_cli.py, test_comparisons.py
├── pyproject.toml           # Poetry configuration
├── LICENSE
└── CONTRIBUTING.md
```

## Tech stack

- **Language**: Python 3.9+
- **Package manager**: Poetry
- **CLI framework**: Click
- **Terminal UI**: Rich
- **Testing**: pytest, pytest-cov
- **Code quality**: black, ruff, mypy

## Development

```bash
poetry install
poetry run pytest --cov --cov-report=term-missing
poetry run ruff check .
poetry run black --check .
poetry run mypy src/
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.

## Related

- [dsh-budget](https://github.com/PerryLink/dsh-budget) — the DSH plugin this project was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH Plugin Family

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
