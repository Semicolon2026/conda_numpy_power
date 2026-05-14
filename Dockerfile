FROM continuumio/miniconda3

WORKDIR /workspace

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "mlenv", "/bin/bash", "-c"]

COPY app/ ./app/
COPY data/ ./data/
COPY scripts/ ./scripts/

RUN chmod +x scripts/run.sh

CMD ["./scripts/run.sh"]
