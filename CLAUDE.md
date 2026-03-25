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

## Python Environment Best Practices

This project uses `uv` with a `.venv` at `GOLDEN/.venv`. Follow these conventions:

### Preferred: use `uv run` for scripts
```bash
uv run python scripts/my_script.py
uv run python -m pytest
```
This always uses the correct interpreter regardless of shell state.

### Terminal auto-activation (IntelliJ + zsh)
`~/.zshrc` contains a `_auto_venv` hook that:
- Auto-activates `.venv` when you `cd` into `GOLDEN/` (or any subdirectory with a `.venv`)
- Auto-deactivates when you leave
- Runs on shell init — so IntelliJ terminals opening in this project directory activate immediately

The hook is registered via `chpwd_functions+=(_auto_venv)` and also called at shell startup.

### `python` alias
`alias python=python3` is set in `~/.zshrc` — macOS does not ship a bare `python` binary.

### Never rely on system Python
Always use `uv run <cmd>` or activate the venv. Do not use `/usr/bin/python` or `/usr/local/bin/python3` directly.

## Structure

This project is in early development. Source code should be placed under a package directory matching the project name (`978_11_crispai_rsa06` or a chosen package name), with `pyproject.toml` at the root.
