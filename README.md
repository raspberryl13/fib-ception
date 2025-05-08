# Fib-ception: The Most Painfully Recursive Fibonacci Generator 🤯
### The Mad Scientist's Fibonacci Nightmare

Welcome to **Fib-ception**, the unhinged, recursion-fueled nightmare that calculates Fibonacci numbers in the *least efficient* way possible. Why settle for a simple `def fib(n)` when you can have Python compile C++ code to generate Python scripts, rewriting files with multilingual greetings, ASCII art, and chaos-mode JSON/blockchain hashes? Crafted with maniacal pride in Lowell, Massachusetts, this mad scientist experiment channels *sláinte* (Irish), *sousdey* (Khmer), *síu sām* (Cantonese), and *konnichiwa* (Japanese) to terrify recursion amateurs. Buckle up for computational chaos!

*"Madness! Madness! THIS ... IS ... RECURSION!"* — Unknown Programmer

## What’s This Madness?

Fib-ception is a Python → C++ → Python pipeline designed to make recursion haters weep:
- **`fib_ception.py`**: The mastermind Python script that:
  1. Prompts for chaos mode (`Y/y/N/n`) and sequence length (1–11).
  2. Generates a C++ program (`generate_fib.cpp`) to calculate Fibonacci numbers recursively.
  3. Compiles it with `g++`/`clang++`.
  4. Runs it to spawn `fibonacci.py`, printing each Fibonacci number with `pyfiglet` ASCII art and a random greeting in English, Irish, Khmer, Cantonese, Spanish, or Japanese.
  5. Repeats for each step, with chaos mode adding JSON serialization and mock blockchain hashes for maximum pain.
- **`generate_fib.cpp`**: C++ code that computes Fibonacci numbers (no memoization, pure torture) and writes `fibonacci.py`.
- **`fibonacci.py`**: The generated Python script, flaunting “FIB” ASCII art and taunting greetings like “*Sláinte* to the Spiral!”

This is recursion on steroids, optimized for SSD safety but not for your sanity. Born in Lowell, MA, where the Merrimack River inspires such unhinged brilliance.

## Why So Painful?

Because regular recursion is for amateurs, and we’re here to cackle in the lab. Fib-ception could’ve been a one-liner, but we chose a multilingual, file-writing, chaos-mode monstrosity to prove recursion can be *painfully* beautiful. Tested on macOS, Ubuntu, and RHEL 9, with Windows support (WSL/MinGW) in progress.

## How to Embrace the Nightmare

### Prerequisites
- **Python 3.x**: Your mad scientist toolkit.
- **g++** (Linux, WSL) or **clang++** (macOS): For compiling C++ chaos.
- **pyfiglet**: For glorious ASCII art (`pip install pyfiglet`). Falls back to `===== FIB =====` if missing.
- **Platforms**:
  - **macOS**: Tested with Homebrew Python 3.13 and `clang++`.
  - **Ubuntu**: Tested with `g++` for smoother compilation.
  - **RHEL 9**: Tested post-ESXi migration, enterprise-grade chaos.
  - **Windows**: WSL/MinGW recommended (untested, proceed with caution).

### Setup
1. **Clone the Repo** (post-unflag):
   ```bash
   git clone https://github.com/raspberryl13/fib-ception.git
   cd fib-ception
   ```

2. **Set Up Virtual Environment** (recommended):
   ```bash
   python3 -m venv fib-ception-venv
   source fib-ception-venv/bin/activate  # macOS/Linux
   fib-ception-venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   - **macOS**:
     ```bash
     brew install gcc
     /opt/homebrew/bin/pip3.13 install pyfiglet
     ```
   - **Ubuntu**:
     ```bash
     sudo apt update
     sudo apt install g++ python3-pip
     pip install pyfiglet
     ```
   - **RHEL 9**:
     ```bash
     sudo dnf install gcc-c++ python3-pip -y
     pip install pyfiglet
     ```
   - **Windows (WSL)**:
     ```bash
     sudo apt update
     sudo apt install g++ python3-pip
     pip install pyfiglet
     ```

4. **Run the Chaos**:
   ```bash
   python3 fib_ception.py
   ```
   - **Prompt 1**: Enter `Y/y` for chaos mode (JSON, blockchain) or `N/n` for normal mode.
   - **Prompt 2**: Enter an integer (1–11) for sequence length.
   - Watch the Fibonacci madness unfold with ASCII art and multilingual greetings.

### Example Output (Chaos Mode, n=5)
```
Welcome to Fib-ception: Unhinged Fibonacci Chaos!
Enable chaos mode (JSON, blockchain)? (Y/y/N/n): Y
Enter Fibonacci sequence length (1–11): 5
Launching Fib-ception for n=5, chaos mode: True... Buckle up for the spiral!
Generating for n=1, fib_n=1
Step 1/5:
   _____ ___ ____
  |  ___|_ _| __ )
  | |_   | ||  _ \
  |  _|  | || |_) |
  |_|   |___|____/
Fibonacci 1: 1
Sláinte to the Spiral! | SLAWN-chuh | Irish Fibonacci cheer
Chaos Hash: b236758845...

Generating for n=2, fib_n=1
Step 2/5:
   _____ ___ ____
  |  ___|_ _| __ )
  | |_   | ||  _ \
  |  _|  | || |_) |
  |_|   |___|____/
Fibonacci 2: 1
Síu sām 螺旋! | SYOO SUM SAI GAI | Cantonese Fibonacci spiral
Chaos Hash: 19852a523d...
...
```

## Notes
- **Unicode**: Supports Khmer (វង់), Cantonese (螺旋), Japanese (螺旋). Use a UTF-8 terminal. Windows CMD may choke on non-ASCII.
- **SSD Safety**: Capped at `n=11`, uses temp files, and buffers writes. No drive meltdowns.
- **Chaos Mode**: Adds JSON writes and mock blockchain hashes for extra inefficiency. Enable with `Y/y`.
- **Threading**: Planned for Ubuntu/Windows testing to ensure stability (macOS threading pending).
- **Windows**: WSL/MinGW setup in progress. Feedback welcome!

## Contributing
Got a crazier way to compute Fibonacci? Add a new language, amplify the chaos, or test on Windows. Open a PR and join the mad scientist lab!

*"Madness! Madness! THIS ... IS ... RECURSION!"* — Unknown Programmer

## License
MIT License—fork, modify, and spread the recursion nightmares!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Made with 💥 in Lowell, Massachusetts.
