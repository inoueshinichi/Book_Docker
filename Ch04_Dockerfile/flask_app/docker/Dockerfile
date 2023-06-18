# Flask server demonstoration

# Python3.9.17 base
From python:3.9.17-slim

Label author="inoue.shinichi.1800@gmail.com"

# Flask 2.3.2 (Python >= 3.8)
RUN pip install flask==2.3.2

# User & Current Workspace
USER root
WORKDIR /

# Copy source code
RUN touch flask_server.py
COPY ./flask_server.py /flask_server.py

# Environment variables
ENV PORT 80

# Run flask server
CMD ["python", "-u", "/flask_server.py"]

