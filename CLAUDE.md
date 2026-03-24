# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Python 3.13+ project managed with `uv`.

## Commands

```bash
# Install dependencies
uv sync

# Run the project
uv run <script>

# Add a dependency
uv add <package>

# Run a Python file or module
uv run python -m <module>
```

## Structure

This project is in early development. Source code should be placed under a package directory matching the project name (`978_10_crispai_rsa06` or a chosen package name), with `pyproject.toml` at the root.
