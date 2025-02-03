#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:00:20 2025

@author: saurabh.agarwal
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Flask App Deployed on Azure with CI/CD By Sumit🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
