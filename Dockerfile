# use oficial lightweight python image
FROM python:3.12-slim

# working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy application code
COPY app/ ./app

# expose port 8000 (unicorn default)
EXPOSE 8000 

# run the application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--workers", "1"]