# ML Inference Service

This is a **FastAPI-based ML inference service** containerized with Docker, deployed on Kubernetes, and automated using a CI/CD pipeline via GitHub Actions.

---

## 1. Local Deployment

```bash
# Clone the repository
git clone https://github.com/BogaMeghanaNetha/ml-inference-service.git
cd ml-inference-service

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app locally
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Build the Docker image
docker build -t meghananetha/ml-inference-service .

# Run the container
docker run -d -p 8000:8000 meghananetha/ml-inference-service

# View logs
docker logs <container_id>

# Test API endpoint
curl http://localhost:8000/predict

docker tag meghananetha/ml-inference-service meghananetha/ml-inference-service:latest
docker push meghananetha/ml-inference-service:latest

# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml    # For autoscaling (optional)

# Check deployment status
kubectl get pods
kubectl get svc

# Apply Ingress (if configured)
kubectl apply -f k8s/ingress.yaml

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

