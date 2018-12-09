from flask import Flask,request
import subprocess, shlex
import os
import json

def command_cmp(a, b):
    return cmp(a['file'], b['file'])

def search_command(database, fname):
    l = len(database)

    if (l == 1):
        if (cmp(database[0]['file'], fname) == 0):
                return database[0]['command']
        else:
            return None

    if (cmp(database[l/2]['file'], fname) == 0):
        return database[l/2]['command']
    elif (cmp(database[l/2]['file'], fname) > 0):
        return search_command(database[l/2:], fname)
    else :
        return search_command(database[:l/2], fname)

def do_compile(base, fname, real_path):
    path = os.path.join(base, 'compile_commands.json')
    with open(path, 'r') as f:
        database = json.load(f)

    database.sort(command_cmp)
    command = search_command(database, os.path.join(base, fname))

    args = shlex.split(command)
    args = args[:-1]

    base, fname = os.path.split(real_path)
    args.append(fname)

    s = subprocess.Popen(args, cwd=base, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out, err = s.communicate()
    return err

app = Flask('myapp')
@app.route('/')
def hello():
    return 'Hello'

@app.route('/compile', methods=['POST', 'GET'])
def compile():
    if request.method == 'POST':
        base = request.form['base']
        fdata = request.form['file']
        fname_with_path = request.form['fname']

        basepath = os.path.dirname(__file__)
        fname = os.path.split(fname_with_path)[1]
        upload_path = os.path.join(basepath, "tmp/", fname)

        with open(upload_path, 'wb') as f:
            f.write(fdata)

        r = do_compile(base, fname_with_path, upload_path)
        return r
    elif request.method == 'GET':
        return 'Ready for compile'
    else :
        return 'Impossible'

app.run(host='0.0.0.0')
