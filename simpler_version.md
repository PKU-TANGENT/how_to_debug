# Simpler Version of How to Debug
Suppose that you are connecting to a server via host machine. This tutorial should be transferable for local debugging.

Suppose that you have `conda` installed on server.
1. install debugpy using pip
```bash
pip install debugpy
```
2. install vscode on host
    - install ssh extension and connect to host
3. install vscode python extension on server
4. create a launch.json, add the following to configurations.
```json
{
  "name": "Python: Attach",
  "type": "python",
  "request": "attach",
  "connect": {
    "host": "127.0.0.1",
    "port": 5678
  }
}
```
Suppose that you have a script like this:
```bash
#!/bin/bash
python args_test.py \
    "This is arg 1" \
    "This is arg 2"
```
5. convert the script and use debugpy
```bash
#!/bin/bash
python -m debugpy --listen 127.0.0.1:5678 --wait-for-client args_test.py \
  "This is arg 1" \
    "This is arg 2"
```
6. run the script
```bash
bash test.sh
```
7. navigate to the vscode debug panel, select `Python: Attach` and run
8. test that debugging is working properly