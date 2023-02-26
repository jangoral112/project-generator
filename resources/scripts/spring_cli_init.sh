#!/bin/bash

spring init --build gradle --type gradle-project --dependencies web,actuator --package-name com.jan --name $1 --language java $1