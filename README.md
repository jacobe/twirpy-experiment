# twirpy-experiments

VSCode-based development workflow for Twirp (protobuf) project in Python.

## Prerequisites

1. Python 3.9 and Pipenv
2. Go (1.9)
3. VSCode

## Getting Started

1. Install the protoc generator + Twirpy plugin

   ```bash
   go install github.com/verloop/twirpy/protoc-gen-twirpy@latest
   ```

2. Install pip dependencies and activate the virtual environment

   ```bash
   pipenv install --dev
   pipenv shell
   ```

3. Start the server

   ```bash
   uvicorn server:app
   ```

4. Test it with a `curl` request

   ```bash
   curl http://localhost:8000/twirp/jacobe.twirpy_experiment.test.TestService/CreateTest \
   -H'Content-Type: application/json' \
   -d'{"test": {"name": "hello"}}'
   ```
