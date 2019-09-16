#!/bin/bash -v
pip3 install -r requirements.txt -t ./site-packages
zip -r src.zip *
