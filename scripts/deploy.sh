#!/bin/bash
set -e

cd ~/nordops-ticketing-service

git pull origin main

kubectl set image deployment/ticketing-app \
  ticketing-app=arezoumontazeri/nordops-ticketing:latest \
  -n ticketing

kubectl rollout status deployment/ticketing-app -n ticketing
