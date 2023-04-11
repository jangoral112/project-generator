# Run project generation
run:
    python -m project_generator

# TODO use different config for location
# Clean up after run
clean:
    just -f /home/jgoral/Documents/projects/sample-project/.justfile clean || true
    rm -rf /home/jgoral/Documents/projects/sample-project