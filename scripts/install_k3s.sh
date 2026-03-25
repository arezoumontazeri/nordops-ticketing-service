#!/bin/bash

set -e

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing k3s..."
curl -sfL https://get.k3s.io | sh -

echo "Setting kubectl alias..."
echo 'alias kubectl="sudo k3s kubectl"' >> ~/.bashrc

echo "Done!"
