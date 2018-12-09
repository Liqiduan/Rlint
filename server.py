from flask import Flask,request
import subprocess, shlex
import os

app = Flask('myapp')

def do_compile(filename):
    args = shlex.split('gcc -o /tmp/main ' + filename)
    s = subprocess.Popen(args, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out, err = s.communicate()
    return err

@app.route('/')
def hello():
    return 'Hello'

@app.route('/compile', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        base = request.args.get('base')
        fdata = request.form['file']
        fname = request.form['fname']

        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, "tmp/", fname)

        with open(upload_path, 'wb') as f:
            f.write(fdata)

        r = do_compile(upload_path)
        return r
    elif request.method == 'GET':
        return 'Ready for compile'
    else :
        return 'Impossible'

app.run(host='0.0.0.0')
