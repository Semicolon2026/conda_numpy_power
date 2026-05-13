FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "testenv", "/bin/bash", "-c"]

COPY app.py .

CMD ["conda", "run", "--no-capture-output", "-n", "testenv", "python", "app.py"]
