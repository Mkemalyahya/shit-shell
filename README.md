# Shit Shell — Lightweight Python CLI Shell for Terminal Tasks
[https://github.com/Mkemalyahya/shit-shell/releases](https://github.com/Mkemalyahya/shit-shell/releases)

[![Releases](https://img.shields.io/badge/Releases-%20Download-blue?logo=github&style=for-the-badge)](https://github.com/Mkemalyahya/shit-shell/releases)

🖥️ 🐍 🐚 Simple. Small. Scriptable.

Short description
- Simple and lightweight CLI written in Python.
- A tiny shell-like tool for quick commands, task scripts, and automation.
- Built to run on POSIX-like systems and Windows with Python installed.

Hero image
![Terminal](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=1200&q=60)

About this repo
- Repo: shit-shell
- Topics: cli, command-line, command-line-tool, os, python, shell, shit, subprocess, sys, terminal
- License: MIT (see LICENSE file)

Key features
- Minimal core. The tool stays small and focused.
- Command runner. Spawn shell commands and capture output.
- Pipeline helpers. Connect Python code with subprocess streams.
- Built-in shortcuts. Map short commands for quick tasks.
- Portable. Pure Python, no native extensions.

Why use Shit Shell
- You need a tiny helper for scripted terminal work.
- You want a readable Python codebase to extend.
- You prefer a small dependency footprint.
- You want a fast loop for prototyping shell helpers.

Quick links
- Releases and download: https://github.com/Mkemalyahya/shit-shell/releases
- Use the releases page to get packaged versions and binary assets.

Download and run (releases)
- Visit the releases page and download the asset that matches your platform.
- The releases page contains packaged files. Download the file named like:
  - shit-shell.py
  - shit-shell-<version>.tar.gz
  - shit-shell-<version>-win.exe
- After download, run the main script or binary:
  - Python source: python3 shit-shell.py
  - Archive: tar xzf shit-shell-<version>.tar.gz && cd shit-shell-<version> && python3 setup.py install
  - Windows exe: double-click or run from cmd

Install from releases (example)
1. Go to releases: https://github.com/Mkemalyahya/shit-shell/releases
2. Download the asset for your OS.
3. If you downloaded a .py file:
   - chmod +x shit-shell.py
   - ./shit-shell.py
   - or python3 shit-shell.py
4. If you downloaded a binary for Windows:
   - Run the exe from Explorer or cmd.

Install via pip (if packaged)
- If a wheel or sdist appears in releases, you can install:
  - pip install shit-shell-<version>-py3-none-any.whl
  - pip install shit-shell-<version>.tar.gz

Usage overview
- Launch the shell interface:
  - python3 shit-shell.py
- Run a single command:
  - python3 shit-shell.py --run "ls -la /tmp"
- Use as a module in Python scripts:
  - from shit_shell import runner
  - out = runner.run("echo hello")
  - print(out)

Common commands and flags
- --run "<cmd>" : Run a single shell command and print output.
- --script <file> : Execute a local script file with shit-shell helpers.
- --interactive : Open the interactive prompt.
- --version : Print version.
- --help : Print help and command list.

Examples

Basic command
- Run a list command and view output:
  - python3 shit-shell.py --run "ls -la"

Use pipeline helper
- Run a command and pass output to Python filter:
  - python3 -c "from shit_shell import runner, utils; print(utils.filter_lines(runner.run('ps aux'), lambda l: 'python' in l))"

Script file example (myscript.sh or myscript.py)
- Create myscript.py:
  - from shit_shell import runner
  - out = runner.run("date")
  - print("Now:", out)
- Execute:
  - python3 shit-shell.py --script myscript.py

Scripting tips
- Use runner.run() for simple commands.
- Use runner.spawn() for long-running processes.
- Use utils.parse_args() for consistent argument handling.
- Log outputs to files when you automate critical tasks.

Configuration
- Config lives in ~/.shit-shell/config.yml by default.
- You can override config path with SHIT_SHELL_CONFIG env var.
- Example config options:
  - prompt: "shit> "
  - history: true
  - history_file: "~/.shit-shell_history"
  - shortcuts:
      s: "systemctl status"
      g: "git status"

Extending the shell
- The codebase separates runner, utils, and core command handlers.
- Add a command handler:
  - Create a file in commands/ with a register() function.
  - Update commands/__init__.py to import the module.
  - The shell auto-detects handlers on start.
- Use the small API:
  - register_command(name, func, help="")

Development
- Clone the repo:
  - git clone https://github.com/Mkemalyahya/shit-shell.git
  - cd shit-shell
- Create a venv:
  - python3 -m venv .venv
  - source .venv/bin/activate
  - pip install -r requirements.txt
- Run tests:
  - pytest

Code layout (high level)
- shit_shell/
  - runner.py      # subprocess helpers
  - core.py        # REPL loop and command dispatch
  - utils.py       # small helpers and parsers
  - commands/      # extra commands and plugins
- scripts/
  - bench.py       # small benchmarks
- tests/
  - test_runner.py
- setup.py
- README.md

Security and sandboxing
- The tool spawns shell commands using subprocess.
- Avoid running untrusted scripts with elevated privileges.
- Prefer explicit command lists for automation.

Examples for automation
- Use shit-shell in cron jobs:
  - /usr/bin/python3 /opt/shit-shell/shit-shell.py --run "backup.sh"
- Use within CI to perform small tasks:
  - python3 shit-shell.py --run "python manage.py migrate"

Changelog and releases
- See releases for stable builds, changelogs, and release assets:
  - https://github.com/Mkemalyahya/shit-shell/releases
- Each release contains a short changelog and downloadable files.
- Download the asset that matches your platform and follow the run instructions above.

Badges and status
- Build and coverage badges can appear here when CI runs.
- Use the releases badge at the top to point users to binaries.

Contributing
- Open an issue for proposals and bug reports.
- Send pull requests for features and fixes.
- Follow the code style in the repo. Keep helpers small and focused.
- Run tests before opening a PR.

Style and guidelines
- Keep functions small and testable.
- Prefer explicit return values.
- Keep dependencies minimal.

Testing
- Tests use pytest.
- Run: pytest -q
- Add unit tests for new helpers.

License
- This project uses the MIT License. See the LICENSE file.

Contact and maintainers
- Maintainer: Mkemalyahya (see GitHub profile)
- Use issues for bug reports and feature requests.

Related projects and links
- Python subprocess docs: https://docs.python.org/3/library/subprocess.html
- Shell helpers and patterns: https://github.com/awesome-cli

Screenshots and visuals
- Example interactive prompt
  ![Prompt](https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=60)

- Example pipeline flow
  ![Pipeline](https://images.unsplash.com/photo-1517433456452-f9633a875f6f?auto=format&fit=crop&w=1200&q=60)

Keywords (SEO)
- cli, command-line, command-line-tool, os, python, shell, shit, subprocess, sys, terminal

License and copyright
- MIT License. See LICENSE file for full text.