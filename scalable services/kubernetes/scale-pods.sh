#!/bin/bash

# Define the deployment name and the desired number of replicas
DEPLOYMENT_NAME="user-service"
NAMESPACE="default"  # Specify the namespace if different
DESIRED_REPLICAS=3    # Change to your desired replica count

# Loop to scale the pods every 2 minutes
while true
do
  echo "Scaling deployment '$DEPLOYMENT_NAME' to $DESIRED_REPLICAS replicas..."
  
  # Scale the deployment
  kubectl scale deployment "$DEPLOYMENT_NAME" --replicas=$DESIRED_REPLICAS -n $NAMESPACE

  # Wait for 2 minutes (120 seconds)
  sleep 120
done
