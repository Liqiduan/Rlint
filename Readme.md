## What is this?
- A simple server handle RESTful like compile request
- A simple implement clinet to raise a compile request

## Why this
When you want to get the result of build in cross platform develope enviromen, like edit in *windows* using SourceInsight and compile in *Linux*).
This is a most simply way to do that.

## Using with source insight
- Install flask in your compile server and for sure run the server:
```bash
python server.py
```
- Create an SourceInsight command to request an buile:
```
Run: C:\Python27\python.exe compile.py %r
Parse pattern: ^[a-zA-Z].*\/\([a−zA−Z].*\):\([0-9][0-9]*\).*
```
