# Contributing to AI Carbon Footprint Calculator

Thank you for your interest in contributing to the AI Carbon Footprint Calculator project!

感谢您对 AI Carbon Footprint Calculator 项目的关注!

---

## Project Status | 项目状态

This is currently a personal project maintained by Chance Dean ([@PerryLink](https://github.com/PerryLink)). While contributions are welcome, please note that this is an individual effort and response times may vary.

这是一个由 Chance Dean ([@PerryLink](https://github.com/PerryLink)) 个人维护的项目。虽然欢迎贡献,但请注意这是个人项目,响应时间可能会有所不同。

---

## How to Report Issues | 如何报告问题

If you encounter a bug or have a feature request, please:

如果您遇到错误或有功能请求,请:

1. **Check existing issues** to avoid duplicates | **检查现有问题**以避免重复
2. **Create a new issue** with a clear title and description | **创建新问题**并提供清晰的标题和描述
3. **Include the following information** | **包含以下信息**:
   - Python version | Python 版本
   - Operating system | 操作系统
   - Steps to reproduce the issue | 重现问题的步骤
   - Expected behavior | 期望的行为
   - Actual behavior | 实际的行为
   - Error messages or logs (if applicable) | 错误信息或日志(如果适用)

---

## Development Environment Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.9 or higher | Python 3.9 或更高版本
- Poetry (recommended) or pip | Poetry(推荐)或 pip
- Git

### Setup Steps | 搭建步骤

1. **Fork and clone the repository** | **Fork 并克隆仓库**

```bash
git clone https://github.com/PerryLink/ai-carbon-footprint.git
cd ai-carbon-footprint
```

2. **Install dependencies** | **安装依赖**

Using Poetry (recommended) | 使用 Poetry(推荐):
```bash
poetry install
```

Or using pip | 或使用 pip:
```bash
pip install -e .
pip install pytest pytest-cov black ruff mypy
```

3. **Verify installation** | **验证安装**

```bash
# Run tests | 运行测试
poetry run pytest

# Or with pip | 或使用 pip
pytest
```

---

## Code Standards | 代码规范

This project follows **PEP 8** style guidelines with the following tools:

本项目遵循 **PEP 8** 代码规范,使用以下工具:

### Code Formatting | 代码格式化

- **Black**: Code formatter with 100 character line length
- **Black**: 代码格式化工具,行长度为 100 字符

```bash
poetry run black src/ tests/
```

### Linting | 代码检查

- **Ruff**: Fast Python linter
- **Ruff**: 快速的 Python 代码检查工具

```bash
poetry run ruff check .
```

### Type Checking | 类型检查

- **Mypy**: Static type checker
- **Mypy**: 静态类型检查工具

```bash
poetry run mypy src/
```

### Testing | 测试

- Write tests for all new features and bug fixes | 为所有新功能和错误修复编写测试
- Maintain test coverage above 85% | 保持测试覆盖率在 85% 以上
- Run tests before submitting PR | 提交 PR 前运行测试

```bash
poetry run pytest --cov --cov-report=term-missing
```

---

## Pull Request Process | 提交 Pull Request 流程

1. **Create a feature branch** | **创建功能分支**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** | **进行修改**
   - Write clean, readable code | 编写清晰、可读的代码
   - Follow PEP 8 guidelines | 遵循 PEP 8 规范
   - Add tests for new functionality | 为新功能添加测试
   - Update documentation if needed | 如需要更新文档

3. **Run quality checks** | **运行质量检查**

```bash
# Format code | 格式化代码
poetry run black src/ tests/

# Check linting | 检查代码
poetry run ruff check .

# Type checking | 类型检查
poetry run mypy src/

# Run tests | 运行测试
poetry run pytest --cov
```

4. **Commit your changes** | **提交更改**

Use clear, descriptive commit messages:
使用清晰、描述性的提交信息:

```bash
git add .
git commit -m "Add feature: description of your changes"
```

5. **Push to your fork** | **推送到您的 fork**

```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request** | **创建 Pull Request**
   - Go to the original repository | 前往原始仓库
   - Click "New Pull Request" | 点击 "New Pull Request"
   - Select your feature branch | 选择您的功能分支
   - Fill in the PR template with: | 填写 PR 模板,包含:
     - Description of changes | 更改描述
     - Related issue number (if applicable) | 相关问题编号(如果适用)
     - Testing performed | 执行的测试
     - Screenshots (if UI changes) | 截图(如果有 UI 更改)

---

## Code Review Process | 代码审查流程

- The maintainer will review your PR as soon as possible | 维护者会尽快审查您的 PR
- Address any feedback or requested changes | 处理任何反馈或请求的更改
- Once approved, your PR will be merged | 一旦批准,您的 PR 将被合并

---

## Adding New GPU Models | 添加新 GPU 型号

To add support for a new GPU model:

要添加对新 GPU 型号的支持:

1. Update `src/ai_carbon_footprint/data.py` with GPU specifications
2. Add the GPU to the README.md supported GPU table
3. Add tests in `tests/test_core.py`
4. Provide official documentation links for TDP values

---

## Questions? | 有问题?

If you have questions about contributing, feel free to:

如果您对贡献有疑问,请随时:

- Open an issue for discussion | 开启一个问题进行讨论
- Contact the maintainer: novelnexusai@outlook.com | 联系维护者: novelnexusai@outlook.com

---

## License | 许可证

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0.

通过为本项目做出贡献,您同意您的贡献将根据 Apache License 2.0 许可。

---

**Thank you for contributing! | 感谢您的贡献!**
