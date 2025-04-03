#!/bin/bash

# Deploy/update stack
aws cloudformation deploy \
    --template-file ec2_setup.yaml \
    --stack-name docker-host-stack \
    --parameter-overrides KeyPairName=20058324_key_pair

# Get new IP
NEW_IP=$(aws cloudformation describe-stacks --stack-name docker-host-stack --query "Stacks[0].Outputs[?OutputKey=='InstancePublicIP'].OutputValue" --output text)

# Update inventory.ini automatically
cat > inventory.ini <<EOL
[servers]
docker_host ansible_host=$NEW_IP ansible_user=ec2-user ansible_ssh_private_key_file=./20058324_key_pair.pem

[servers:vars]
ansible_python_interpreter=/usr/bin/python3.8
EOL

# Run Ansible
ansible-playbook -i inventory.ini docker_setup.yml
ansible-playbook -i inventory.ini deploy_container.yml