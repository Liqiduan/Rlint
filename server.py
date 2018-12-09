from flask import Flask,request
import subprocess, shlex
import os

app = Flask('myapp')

@app.route('/')
def hello():
    return 'Hello'

@app.route('/compile')
def compile():
    base = request.args.get('base')
    filename = request.args.get('file')

    args = shlex.split('gcc -o main ' + filename)
    s = subprocess.Popen(args, cwd=base, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out, err = s.communicate()

    return err

app.run(host='0.0.0.0')
