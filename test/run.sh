#!/bin/bash

echo "Running tests"

if ./test/test.sh; then
    echo Tests run succeeded
else
    echo Tests run failed
fi
