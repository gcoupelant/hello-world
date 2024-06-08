# Hello World

## Docker

The `Dockerfile.all-in-one` is self contained and will create the pipenv virtual environment.

The `Dockerfile` is a stripped version where it expects a `.venv` directory to exists in the build context. Note that this virtual environment MUST NOT use symlink (using `PIPENV_VIRTUALENV_COPIES`), else it will not work.

To ensure the `.venv` directory is created in the project directory, ensure you have the `PIPENV_VENV_IN_PROJECT` environment variable set to "1".

## GitHub Actions

The configured GitHub Actions will build the dependencies in a Ubuntu runner, run the program using `pipenv run` and upload the virtual environment artifacts.

After these steps, it will also build a Docker image by providing the previously built virtual environment and run the program using a container this time.
