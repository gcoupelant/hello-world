FROM python:3.12-slim

# Copy the virtual env from the context (must be created outside of the docker builder)
COPY .venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home worker
USER worker
WORKDIR /home/worker

# Install application into container
COPY . /home/worker

# Run the application
ENTRYPOINT ["python", "./main.py"]
