#!/bin/bash

root_directory="$1"
project_name="$2"

just -f "$root_directory"/"$project_name"/.justfile clean || true
rm -rf "$root_directory"/"$project_name"