# AI Carbon Footprint Calculator

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python CLI tool for calculating carbon emissions from AI compute workloads. Help enterprises disclose AI compute carbon emissions in ESG reports, or satisfy tech enthusiasts' curiosity.

一个用于计算 AI 算力碳排放的 Python CLI 工具。帮助企业在 ESG 报告中披露 AI 算力造成的碳排放数据,或满足技术极客的好奇心。

---

## Features | 特性

- 🎯 Support 20+ mainstream GPU models (NVIDIA, AMD, Google TPU)
- 🌍 Multi-region carbon intensity data (Global, US, EU, China, etc.)
- ⚡ Consider PUE (Power Usage Effectiveness) coefficient
- 📊 Provide concrete comparisons (e.g., "equivalent to X cars driving for a year")
- 🎨 Beautiful terminal output (based on Rich library)
- 📦 Support JSON output format

---

- 🎯 支持 20+ 款主流 GPU 型号(NVIDIA、AMD、Google TPU)
- 🌍 支持多地区碳强度数据(全球、美国、欧盟、中国等)
- ⚡ 考虑 PUE(能源使用效率)系数
- 📊 提供具象化对比(如"相当于 X 辆燃油车行驶一年")
- 🎨 美观的终端输出(基于 Rich 库)
- 📦 支持 JSON 输出格式

---

## Quick Start | 快速开始

### Installation | 安装

```bash
pip install ai-carbon-footprint
```

Or using Poetry | 或使用 Poetry:

```bash
poetry add ai-carbon-footprint
```

### Basic Usage | 基础使用

```bash
# Calculate carbon emissions for 1 A100 GPU running 1000 hours
# 计算 1 个 A100 GPU 运行 1000 小时的碳排放
ai-carbon-footprint --gpu A100 --hours 1000

# Using short parameters | 使用短参数
ai-carbon-footprint -g A100 -h 1000
```

---

## Usage Guide | 使用指南

### Advanced Usage | 高级用法

```bash
# Multiple GPUs, custom PUE, specify region
# 多 GPU、自定义 PUE、指定地区
ai-carbon-footprint -g H100 -h 500 -n 8 -p 1.2 -r us -u 0.85

# JSON output | JSON 输出
ai-carbon-footprint -g A100 -h 100 --output json

# List all supported GPUs | 列出所有支持的 GPU
ai-carbon-footprint list-gpus

# List all supported regions | 列出所有支持的地区
ai-carbon-footprint list-regions
```

### Parameters | 参数说明

- `--gpu, -g`: GPU model (required) | GPU 型号(必需)
- `--hours, -h`: Runtime in hours (required) | 运行时间(小时)(必需)
- `--num-gpus, -n`: Number of GPUs (default: 1) | GPU 数量(默认: 1)
- `--pue, -p`: PUE coefficient (default: 1.58, industry average) | PUE 系数(默认: 1.58,行业平均)
- `--region, -r`: Geographic region (default: global) | 地区(默认: global)
- `--utilization, -u`: GPU utilization 0-1 (default: 1.0) | GPU 利用率 0-1(默认: 1.0)
- `--output, -o`: Output format text/json (default: text) | 输出格式 text/json(默认: text)

### Calculation Formula | 计算公式

```
1. GPU Energy (kWh) = (TDP × Hours × GPU Count × Utilization) / 1000
2. Total Energy (kWh) = GPU Energy × PUE
3. CO2 Emissions (kg) = Total Energy × Carbon Intensity
```

### Supported GPUs | 支持的 GPU

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

### Carbon Intensity Data | 碳强度数据

| Region | Carbon Intensity (kg CO2/kWh) |
|--------|--------------------------------|
| global | 0.475 |
| us | 0.386 |
| eu | 0.276 |
| china | 0.555 |
| india | 0.708 |
| uk | 0.233 |
| france | 0.056 |
| iceland | 0.010 |

---

## Project Structure | 项目结构

```
ai-carbon-footprint/
├── src/ai_carbon_footprint/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point for python -m
│   ├── cli.py               # CLI interface
│   ├── core.py              # Core calculation logic
│   ├── data.py              # GPU database and constants
│   └── comparisons.py       # Concrete comparison functionality
├── tests/                   # Test suite
│   ├── test_core.py
│   ├── test_cli.py
│   └── test_comparisons.py
├── .github/workflows/       # CI/CD configuration
├── pyproject.toml           # Poetry configuration
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

## Tech Stack | 技术栈

- **Language**: Python 3.9+
- **Package Manager**: Poetry
- **CLI Framework**: Click
- **Terminal UI**: Rich
- **Testing**: pytest, pytest-cov
- **Code Quality**: black, ruff, mypy

---

## Development | 开发

### Install Development Dependencies | 安装开发依赖

```bash
poetry install
```

### Run Tests | 运行测试

```bash
poetry run pytest --cov --cov-report=term-missing
```

### Code Quality Checks | 代码质量检查

```bash
poetry run ruff check .
poetry run black --check .
poetry run mypy src/
```

---

## Data Sources | 数据来源

- GPU TDP Data: NVIDIA, AMD, Google official specifications
- Carbon Intensity Data: IEA (International Energy Agency) annual reports
- PUE Data: Uptime Institute data center surveys

---

- GPU TDP 数据: NVIDIA、AMD、Google 官方规格
- 碳强度数据: IEA (国际能源署) 年度报告
- PUE 数据: Uptime Institute 数据中心调研

---

## Contributing | 贡献

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何为本项目做出贡献。

---

## License | 许可证

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

---

## Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com

---

**Made with ❤️ by Chance Dean**
