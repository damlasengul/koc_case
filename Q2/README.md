# Loan-Approval-Prediction Flask Application

This repository contains a Flask application that serves a machine learning model prediction service to predict whether the applicant should receive a loan or not, Dockerized for easy deployment.

### Prerequisites

- Docker installed on your machine.

### Project Structure
project-root/
│
├── app/
│ ├── __init__.py
│ ├── final_model.pkl
│ └── requirements.txt
│
├── Dockerfile
└── README.md


### Usage

1. **Build Docker Image:**

   Navigate to the project root directory where `Dockerfile` is located and run:

   ```bash
   docker build -t your-app-name .

2. **Run Docker Container:**
    
    Once the image is built, you can run the Docker container:

    docker run -p 5001:5001 your-app-name

    Replace 5001:5001 with the appropriate port mapping if you have adjusted it in __init__.py
s
3. **Access Application:**

    By default, you can access the application at http://localhost:5001.
