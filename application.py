import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
