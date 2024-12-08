FROM python:3.11

WORKDIR /prj

COPY . /prj

RUN python -m venv /venv

RUN /venv/bin/pip install -r requirements.txt

ENV PATH="/venv/bin:$PATH"

EXPOSE 8000:8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]