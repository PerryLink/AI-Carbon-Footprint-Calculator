<div align="center">

# AI-Carbon-Footprint-Calculator

**估算 AI GPU 算力工作负载二氧化碳排放的 Python CLI 工具。**

*已移植到 [dsh-budget](https://github.com/PerryLink/dsh-budget) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

`ai-carbon-footprint` 根据 GPU 型号、运行时长、GPU 数量、利用率、PUE 以及地区碳强度，估算 AI 工作负载的
能耗与二氧化碳排放，并输出具象化对比（如"相当于 X 辆燃油车行驶一年"），同时支持 JSON 输出。

## 特性

- 🎯 支持 17 款主流 GPU（NVIDIA、AMD、Google TPU）
- 🌍 8 个地区的碳强度数据（global、us、eu、china、india、uk、france、iceland）
- ⚡ 考虑 PUE（能源使用效率）系数
- 📊 提供具象化日常对比
- 🎨 基于 Rich 的终端输出，并支持 JSON 格式

## 快速开始

```bash
pip install ai-carbon-footprint

ai-carbon-footprint --gpu A100 --hours 1000
ai-carbon-footprint -g A100 -h 1000
```

## 使用方法

```bash
# 8 块 H100 GPU，自定义 PUE、地区与利用率
ai-carbon-footprint -g H100 -h 500 -n 8 -p 1.2 -r us -u 0.85

# JSON 输出
ai-carbon-footprint -g A100 -h 100 --output json

# 列出支持的 GPU 与地区
ai-carbon-footprint list-gpus
ai-carbon-footprint list-regions
```

### 参数说明

- `-g, --gpu` — GPU 型号（必需）
- `-h, --hours` — 运行时长（小时）（必需）
- `-n, --num-gpus` — GPU 数量（默认 1）
- `-p, --pue` — PUE 系数（默认 1.58）
- `-r, --region` — 地区代码（默认 `global`）
- `-u, --utilization` — GPU 利用率 0–1（默认 1.0）
- `-o, --output` — `text` 或 `json`（默认 `text`）

### 计算公式

```
GPU 能耗（kWh）   = TDP × 时长 × GPU 数量 × 利用率 / 1000
总能耗（kWh）     = GPU 能耗 × PUE
二氧化碳排放（kg）= 总能耗 × 碳强度
```

## 支持的 GPU

| 型号 | 名称 | TDP (W) | 类别 |
|------|------|---------|------|
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

## 碳强度数据

| 地区 | 碳强度 (kg CO₂/kWh) |
|------|---------------------|
| global | 0.475 |
| us | 0.386 |
| eu | 0.276 |
| china | 0.555 |
| india | 0.708 |
| uk | 0.233 |
| france | 0.056 |
| iceland | 0.010 |

## 数据来源

- GPU TDP 数据：NVIDIA、AMD、Google 官方规格
- 碳强度数据：IEA（国际能源署）年度报告
- PUE 数据：Uptime Institute 数据中心调研

## 项目结构

```
ai-carbon-footprint/
├── src/ai_carbon_footprint/
│   ├── __init__.py          # 包初始化
│   ├── __main__.py          # python -m 入口
│   ├── cli.py               # CLI 接口
│   ├── core.py              # 核心计算逻辑
│   ├── data.py              # GPU 数据库与常量
│   └── comparisons.py       # 具象化对比功能
├── tests/                   # test_core.py、test_cli.py、test_comparisons.py
├── pyproject.toml           # Poetry 配置
├── LICENSE
└── CONTRIBUTING.md
```

## 技术栈

- **语言**：Python 3.9+
- **包管理器**：Poetry
- **CLI 框架**：Click
- **终端 UI**：Rich
- **测试**：pytest、pytest-cov
- **代码质量**：black、ruff、mypy

## 开发

```bash
poetry install
poetry run pytest --cov --cov-report=term-missing
poetry run ruff check .
poetry run black --check .
poetry run mypy src/
```

## 贡献

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何为本项目做出贡献。

## 相关项目

- [dsh-budget](https://github.com/PerryLink/dsh-budget) — 本项目被移植进的 DSH 插件
- [PerryLink](https://github.com/PerryLink) — PerryLink DSH 插件家族

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
