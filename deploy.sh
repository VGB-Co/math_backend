#!/bin/bash

ssh -oStrictHostKeyChecking=no -i "rft-math.pem" ec2-user@ec2-18-220-101-207.us-east-2.compute.amazonaws.com "cd math_backend && git pull"