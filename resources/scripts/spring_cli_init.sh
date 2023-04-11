#!/bin/bash

function kebab_case_to_camel_case() {
    local kebab_case_string="$1"
    local camel_case_string=$(sed -r 's/(^|-)(\w)/\U\2/g' <<<"$kebab_case_string")
    echo "$camel_case_string"
}

main_projects_directory="$1"
project_name="$2"
application_name=$(kebab_case_to_camel_case "$project_name")Application

cd "$main_projects_directory"

spring init --build gradle --type gradle-project --dependencies web,actuator,data-jpa,mysql,jdbc,lombok --package-name com.jan --name "$application_name" --language java "$project_name"