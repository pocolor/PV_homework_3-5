#!/usr/bin/env bash

MAIN_PYTHON_SCRIPT='main.py'
RUN_SHELL_SCRIPT='run.bash'

for (( i = 1; i <= 45; i++ )); do
	project_dir=$( printf 'statement_%02d' "$i" )
	mkdir -p "$project_dir"
	[[ -f "$MAIN_PYTHON_SCRIPT" ]] && cp "$MAIN_PYTHON_SCRIPT" "$project_dir/$MAIN_PYTHON_SCRIPT"
	[[ -f "$RUN_SHELL_SCRIPT" ]] && cp "$RUN_SHELL_SCRIPT" "$project_dir/$RUN_SHELL_SCRIPT"

	project_venv="$project_dir/.venv"
	[[ -d "$project_venv" ]] || python3 -m venv "$project_venv"
done
