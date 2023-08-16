#!/bin/bash

# Verifique se o usuário forneceu um argumento
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 YOUR_OPENAI_API_KEY"
    exit 1
fi

API_KEY=$1

# Check if .bashrc exists, otherwise use .bash_profile
if [ -f "$HOME/.bashrc" ]; then
    PROFILE_FILE="$HOME/.bashrc"
else
    PROFILE_FILE="$HOME/.bash_profile"
fi

# Add or Update OPENAI_API_KEY in the profile
grep -q "export OPENAI_API_KEY=" $PROFILE_FILE
if [ $? -eq 0 ]; then
    # OPENAI_API_KEY exists, update it
    sed -i "s/export OPENAI_API_KEY=.*/export OPENAI_API_KEY=$API_KEY/" $PROFILE_FILE
else
    # OPENAI_API_KEY doesn't exist, append it
    echo "export OPENAI_API_KEY=$API_KEY" >> $PROFILE_FILE
fi

echo "OPENAI_API_KEY updated in $PROFILE_FILE. You might need to restart your terminal to see the changes."
