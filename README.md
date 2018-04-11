# WebSocketChatroom
This project is set up for practicing the websocket with `Tornado`.
Everyone could easily join the chatroom on bowser or other clients.

## Prerequisistes
- Python3
- [pipenv](https://github.com/pypa/pipenv)

## Usage

1. Install dependencis by `pipenv`
```
pipenv install
```
2. Start the server in the virtualenv
```
pipenv run python server.py
```
3. Use JavaScript on browser to verify
Open the browser DEV tools, use the console on it to enter below command.
```
var ws = new WebSocket("ws://localhost:8080")
ws.onmessage = evt => {console.log(evt.data)}
ws.send('{"name": "abc", "action": "add"}')
ws.send('{"action": "say", "message": "Hello world!"}')
ws.send('{"action": "close"}')
```

## Configuration
- logger settings in `config/logger.ini`
