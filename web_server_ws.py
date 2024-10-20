from microdot_asyncio import Microdot, Response
from microdot_asyncio_websocket import with_websocket
import uasyncio as asyncio
from movement import move_forward, move_backward, turn_left, turn_right, go_forward, go_backward, go_left, go_right, go_right_wide, go_left_wide, stop
import ujson

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/ws')
@with_websocket
async def control_robot(request, ws):
    while True:
        action = await ws.receive()
        print(f"Received message: {action}")
        
        data = ujson.loads(action)
        msg = data.get('action')
            
        if msg == 'move_forward':
            move_forward()
        elif msg == 'move_backward':
            move_backward()
        elif msg == 'turn_left':
            turn_left()
        elif msg == 'turn_right':
            turn_right()
        elif msg == 'go_forward':
            go_forward()
        elif msg == 'go_backward':
            go_backward()
        elif msg == 'go_left':
            go_left()
        elif msg == 'go_right':
            go_right()
        elif msg == 'go_left_wide':
            go_left_wide()
        elif msg == 'go_right_wide':
            go_right_wide()
        elif msg == 'stop':
            stop()
        elif msg == 'check':
            await ws.send("OK")
        await ws.send("Command Executed " + msg)

async def start_server_ws():
    app.run(port=81)


