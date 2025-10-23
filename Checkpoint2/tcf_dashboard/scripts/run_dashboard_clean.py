#!/usr/bin/env python3
"""
TCF Strategic Dashboard Runner
Professional version without emojis
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    return True

def check_required_files():
    """Check if required files exist"""
    required_files = [
        '../src/tcf_strategic_dashboard.py',
        '../data/country_gdp_population.csv',
        '../data/org_structure.csv'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("Error: Required files not found:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    return True

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-r', '../requirements.txt'
        ])
        print("Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

def run_dashboard():
    """Run the Streamlit dashboard"""
    print("Starting TCF Strategic Dashboard...")
    print("Dashboard will be available at: http://localhost:8501")
    print("Press Ctrl+C to stop the dashboard")
    
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 
            '../src/tcf_strategic_dashboard.py', 
            '--server.port', '8501'
        ])
    except KeyboardInterrupt:
        print("\nDashboard stopped by user")
    except Exception as e:
        print(f"Error running dashboard: {e}")

def main():
    """Main function"""
    print("TCF Strategic Dashboard Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check required files
    if not check_required_files():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Run dashboard
    run_dashboard()

if __name__ == "__main__":
    main()
