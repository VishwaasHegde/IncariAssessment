FROM ollama/ollama

COPY run-ollama.sh /app/run-ollama.sh

WORKDIR /app

RUN chmod +x run-ollama.sh \
    && ./run-ollama.sh

EXPOSE 11434