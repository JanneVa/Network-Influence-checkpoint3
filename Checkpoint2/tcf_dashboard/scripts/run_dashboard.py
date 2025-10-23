#!/usr/bin/env python3
"""
Script para ejecutar el Dashboard Estratégico de TCF
"""

import subprocess
import sys
import os

def check_requirements():
    """Verificar que los archivos necesarios estén presentes"""
    required_files = [
        "tcf_strategic_dashboard_english.py",
        "country_gdp_population.csv",
        "org_structure.csv"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("Missing files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("All required files are present")
    return True

def install_requirements():
    """Install dependencies if necessary"""
    try:
        print("Checking dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements_dashboard.txt"], 
                      check=True, capture_output=True)
        print("Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

def run_dashboard():
    """Run the Streamlit dashboard"""
    try:
        print("Starting TCF Strategic Dashboard...")
        print("The dashboard will open in your browser")
        print("URL: http://localhost:8501")
        print("\n" + "="*50)
        
        subprocess.run(["streamlit", "run", "tcf_strategic_dashboard_english.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running dashboard: {e}")
        return False
    except KeyboardInterrupt:
        print("\nDashboard closed by user")
        return True

def main():
    """Main function"""
    print("TCF Strategic Dashboard - Launcher")
    print("="*50)
    
    # Check files
    if not check_requirements():
        print("\nCannot run dashboard. Missing required files.")
        return
    
    # Install dependencies
    if not install_requirements():
        print("\nCannot install required dependencies.")
        return
    
    # Run dashboard
    print("\nStarting dashboard...")
    run_dashboard()

if __name__ == "__main__":
    main()
