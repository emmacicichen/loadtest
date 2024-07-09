## Start a fake server with json-server for testing

- json-server.py
    - doc: https://pypi.org/project/json-server-py/
- Install json-server
- Create a random json, such as test.json
- Start the json-server
  - <code>json-server test.json -b :3030</code>
    ```angular2html
    ====================
    Local:	http://localhost:3030
    Remote:	http://172.17.244.137:3030
    ---
    Local:	http://[::1]:3030
    ====================
    ```
- Uses the url above for testing