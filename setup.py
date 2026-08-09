#!/usr/bin/env python
"""
Automated Setup and Run Script for eBooks Full-Stack Application
"""

import os
import sys
import subprocess

def run_cmd(command):
    print(f"\n==> Executing: {command}")
    res = subprocess.run(command, shell=True)
    if res.returncode != 0:
        print(f"[ERROR] Command failed with return code {res.returncode}")
        sys.exit(res.returncode)

def main():
    print("==================================================")
    print(" eBooks Application - Automated Setup & Launcher")
    print("==================================================")

    # Step 1: Makemigrations
    run_cmd(f"{sys.executable} manage.py makemigrations")

    # Step 2: Migrate
    run_cmd(f"{sys.executable} manage.py migrate")

    # Step 3: Seed Real Data
    run_cmd(f"{sys.executable} seed_db.py")

    print("\n[SUCCESS] Setup Completed Successfully!")
    print("[SERVER] Launching Django Development Server on http://127.0.0.1:8000/ ...\n")

    # Step 4: Runserver
    subprocess.run(f"{sys.executable} manage.py runserver 8000", shell=True)

if __name__ == '__main__':
    main()
