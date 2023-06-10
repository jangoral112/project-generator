set dotenv-load

# Run project generation
run:
    python -m project_generator generate

# Rune e2e test
test:
    $(pwd)/test/run.sh

# Clean up after run
clean:
    python -m project_generator clean