#!/bin/bash
python -m debugpy --listen 127.0.0.1:5678 --wait-for-client args_test.py \
  "This is arg 1" \
    "This is arg 2"