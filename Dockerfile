FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .



CMD bash -c "python code/extract.py && \
             python code/extract_abs.py && \
             python code/keyword_cloud.py && \
             python code/num_fig.py && \
             python code/links.py"