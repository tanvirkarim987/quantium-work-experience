#!/bin/bash

# 1. Activate the virtual environment
# Since you are using global/user python on your Mac, we skip 'source venv/bin/activate'
# but in a standard CI environment, you would include it here.

# 2. Execute the test suite
# We use 'python3 -m pytest' to ensure it uses the correct path we found earlier
python3 -m pytest test_app.py

# 3. Handle the Exit Codes
# $? is a special variable in bash that holds the exit status of the last command.
# Pytest returns 0 if tests pass and non-zero if they fail.
if [ $? -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi