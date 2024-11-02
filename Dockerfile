from ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# -- Install UV:
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /SQLModelExample
ADD . /SQLModelExample
RUN uv sync --frozen
ENV PATH="/SQLModelExample/.venv/bin:$PATH"

# Run the application.
CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--host", "0.0.0.0"]
