<div align="center">

# AI-Carbon-Footprint-Calculator

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

### Supported GPUs

A100, A100-80GB, H100, H100-80GB, V100, A40, A30, A10, RTX 4090, RTX 4080, RTX 3090, RTX 3080,
MI250X, MI210, MI100, TPU v4, TPU v3.

## Development

```bash
poetry install
poetry run pytest --cov --cov-report=term-missing
poetry run ruff check .
poetry run black --check .
```

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
