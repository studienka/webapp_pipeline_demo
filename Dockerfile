# starting with a slim python base image
FROM python:3.9-slim

# setting workdir
WORKDIR /app

# installing python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source
COPY . .

# expose flask port
EXPOSE 5000

# run
CMD ["python", "app.py"] 
