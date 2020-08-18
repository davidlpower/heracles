#!/bin/bash

# Be sure to fail fast
set -e

# Run Linting
echo -e "\033[32m==\e[0m Linting - Start \033[32m==\e[0m"
flake8
echo -e "\033[32m==\e[0m Linting - End \033[32m==\e[0m"

# Run Tests
echo -e "\033[32m==\e[0m Tests - Start \033[32m==\e[0m"
python -m unittest -v tests/testMoneyFormat.py
echo -e "\033[32m==\e[0m Tests - End \033[32m==\e[0m"
