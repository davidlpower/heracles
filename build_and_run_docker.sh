#!/bin/bash

echo "== Remove Image =="
docker rm --force heracles

echo "== Build Image =="
docker build --tag heracles:1.0 .

echo "== Run Container =="
docker run --name heracles heracles:1.0