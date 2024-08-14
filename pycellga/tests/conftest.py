# cga/tests/conftest.py
import sys
import os

# Calculate the project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../'))  # Adjusted path

# Print the calculated project root directory for debugging
print("Calculated project root:", project_root)

# Add the project root directory to the Python path
sys.path.insert(0, project_root)

# Print the Python path for debugging
print("PYTHONPATH:", sys.path)
