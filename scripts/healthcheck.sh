#!/bin/bash
- name: Health check (retry)
  run: |
    for i in {1..10}; do
      if curl -f http://localhost/health; then
        echo "App is healthy!"
        exit 0
      fi
      echo "Waiting for app..."
      sleep 15
    done
    exit 1
