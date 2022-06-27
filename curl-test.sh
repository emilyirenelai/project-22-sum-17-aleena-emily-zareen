#!/bin/bash
curl -X POST http://178.128.229.22:5000/api/timeline_post -d 'name=emily&email=emilyirenelai@gmail.com&content=test'
curl http://127.0.0.1:5000/api/timeline_post
