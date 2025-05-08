#!/usr/bin/env python3
import os
import subprocess
import random
import tempfile
import json
import hashlib
import time

# Multilingual Fibonacci-themed greetings
greetings = [
    "Sláinte to the Spiral! | SLAWN-chuh | Irish Fibonacci cheer",
    "Sousdey វង់! | SOOS-day VONG | Khmer Fibonacci spiral",
    "Síu sām 螺旋! | SYOO SUM SAI GAI | Cantonese Fibonacci spiral",
    "¡Hola, Espiral! | OH-lah es-pee-RAL | Spanish Fibonacci spiral",
    "こんにちは、螺旋！ | KON-NEE-chee-wah RAH-sen | Japanese Fibonacci spiral"
]

# Mock blockchain for chaos mode
blockchain = []

# C++ code template
cpp_template = """
#include <fstream>
#include <string>

unsigned long long fib(int n) {{
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}}

int main() {{
    std::ofstream out("{temp_file}");
    if (!out) return 1;
    out << "#!/usr/bin/env python3\\n";
    out << "try:\\n";
    out << "    from pyfiglet import Figlet\\n";
    out << "    f = Figlet(font='standard')\\n";
    out << "    print(f.renderText('FIB'))\\n";
    out << "except ImportError:\\n";
    out << "    print('===== FIB =====')\\n";
    out << "print('Fibonacci {n}: ' + str({fib_n}))\\n";
    out << "print(\\\"{greeting}\\\")\\n";
    out.close();
    {chaos_code}
    return 0;
}}
"""

def get_user_input():
    # Prompt for chaos mode
    while True:
        chaos_input = input("Enable chaos mode (JSON, blockchain)? (Y/y/N/n): ").strip().lower()
        if chaos_input in ['y', 'n']:
            unhinged = chaos_input == 'y'
            break
        print("Invalid input! Please enter Y, y, N, or n.")
    
    # Prompt for sequence length
    while True:
        try:
            n = int(input("Enter Fibonacci sequence length (1–11): ").strip())
            if 1 <= n <= 11:
                break
            print("Invalid input! Please enter an integer between 1 and 11.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    return n, unhinged

def run_fib_ception(n, unhinged):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
        temp_file_path = temp_file.name

    for i in range(1, n+1):
        random.seed(time.time())  # Reseed for varied greetings
        fib_n = fib(i)
        greeting = random.choice(greetings)
        chaos_code = ""
        if unhinged:
            json_data = {"n": i, "fib": fib_n, "timestamp": time.time()}
            with open("fib.json", "w") as jf:
                json.dump(json_data, jf)
            blockchain.append(hashlib.sha256(str(json_data).encode()).hexdigest())
            chaos_code = """
                std::ofstream json_out("fib.json", std::ios::app);
                json_out << "\\n";
                json_out.close();
            """
        cpp_code = cpp_template.format(
            n=i,
            fib_n=fib_n,
            greeting=greeting.replace('"', '\\"').replace('\n', '\\n'),
            temp_file=temp_file_path.replace('\\', '/'),
            chaos_code=chaos_code
        )
        print(f"Generating for n={i}, fib_n={fib_n}")
        with open("generate_fib.cpp", "w") as cpp_file:
            cpp_file.write(cpp_code)
        try:
            subprocess.run(["g++", "generate_fib.cpp", "-o", "generate_fib"], check=True, capture_output=True, text=True)
            subprocess.run(["./generate_fib"], check=True, capture_output=True, text=True)
            result = subprocess.run(["python3", temp_file_path], check=True, capture_output=True, text=True)
            print(f"\nStep {i}/{n}:\n{result.stdout.strip()}")
            if unhinged:
                print(f"Chaos Hash: {blockchain[-1][:10]}...")
        except subprocess.CalledProcessError as e:
            print(f"Failed at n={i}: {e.stderr}")
            return
    os.remove(temp_file_path)
    if unhinged and os.path.exists("fib.json"):
        os.remove("fib.json")

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print("Welcome to Fib-ception: Unhinged Fibonacci Chaos!")
    n, unhinged = get_user_input()
    print(f"Launching Fib-ception for n={n}, chaos mode: {unhinged}... Buckle up for the spiral!")
    run_fib_ception(n, unhinged)