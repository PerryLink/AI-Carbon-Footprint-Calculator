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

### 支持的 GPU

A100、A100-80GB、H100、H100-80GB、V100、A40、A30、A10、RTX 4090、RTX 4080、RTX 3090、RTX 3080、
MI250X、MI210、MI100、TPU v4、TPU v3。

## 开发

```bash
poetry install
poetry run pytest --cov --cov-report=term-missing
poetry run ruff check .
poetry run black --check .
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
