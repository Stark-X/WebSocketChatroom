# WebSocket

## Stack
Python + JS(Verify on Browser)

## Steps
1. Agenda and base knowledge
2. Homework (1 vs many chat room)
3. WebSocket server set up
4. Verify on Browser
5. WebSocket client set up
6. 1 vs 1 chat room implementation
7. Homework Tips

## Verification
Each members could connect to the WebSocket server I've built, and receive the messages from other members.


## Snippets
```javascript
var ws = new WebSocket("ws://xiaost-w10:8080/")
ws.onmessage = evt => {console.log(evt.data)}
ws.send('{"name": "abcd", "action": "add"}')
ws.send('{"name": "abcd", "action": "say", "message": "Hello World"}')
ws.send('{"name": "abcd", "action": "close", "message": "Bye"}')
```
