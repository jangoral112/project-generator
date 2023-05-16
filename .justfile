set dotenv-load

# Run project generation
run:
    python -m project_generator

# Rune e2e test
test:
    $(pwd)/test/run.sh

# TODO use different config for location
# Clean up after run
clean:
    just -f /home/jgoral/Documents/projects/$PROJECT_NAME/.justfile clean || true
    rm -rf /home/jgoral/Documents/projects/$PROJECT_NAME