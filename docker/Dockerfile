FROM python:3.13

RUN pip install uv

COPY pyproject.toml uv.lock ./
COPY src/ src/

RUN uv sync

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
