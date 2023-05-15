#!/bin/bash

source ./lib/assert.sh/assert.sh

just run

(cd /home/jgoral/Documents/projects/sample-project/; just docker-up)

echo "TEST: should launch healthy application when just docker-up command is run"

curl -s -w "\n%{http_code}" 'http://127.0.0.1:8989/actuator/health' | {
    read body
    read code

    component_status=$(jq .status <<< "$body" | tr -d '"')

    assert_eq "200" "$code" "Expected http code 200 got $code" || exit 1
    assert_eq "UP" "$component_status" "Expected component status UP got $component_status" || exit 1
}

test_result="$?"

if [ "$test_result" -eq "1" ]; then
    RED='\033[0;91m'
    NC='\033[0m'
    echo -e "${RED}TEST FAILED: should launch healthy application when just docker-up command is run${NC}"
fi

just clean

exit $test_result