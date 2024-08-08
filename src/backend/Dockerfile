FROM python:3.9-slim AS base
WORKDIR /app

# ---- Dependencies ----
FROM base AS dependencies
RUN pip3 config set global.no-cache-dir true
ADD requirements.txt .
RUN pip3 install -r requirements.txt

# ---- Copy Files/Build ----
FROM dependencies AS build
WORKDIR /app
COPY . .

# --- Release ----
FROM build AS release
WORKDIR /app
EXPOSE 8025

CMD ["uvicorn", "incariengine:app", "--host", "0.0.0.0", "--port", "8025"]






