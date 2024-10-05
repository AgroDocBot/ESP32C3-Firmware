import socket
from movement import move_forward, move_backward, turn_left, turn_right, go_forward, go_backward, go_left, go_right, stop

# Start the HTTP server
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Server listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        print('Request:', request)

        # Routing
        if b'/move/forward' in request:
            move_forward()
            response = 'HTTP/1.1 200 OK\n\nMoving Forward!'
        elif b'/move/backward' in request:
            move_backward()
            response = 'HTTP/1.1 200 OK\n\nMoving Backward!'
        elif b'/move/left' in request:
            turn_left()
            response = 'HTTP/1.1 200 OK\n\nTurning Left!'
        elif b'/move/right' in request:
            turn_right()
            response = 'HTTP/1.1 200 OK\n\nTurning Right!'
        elif b'/go/forward' in request:
            go_forward()
            response = 'HTTP/1.1 200 OK\n\nGoing Forward!'
        elif b'/go/backward' in request:
            go_backward()
            response = 'HTTP/1.1 200 OK\n\nGoing Backward!'
        elif b'/go/left' in request:
            go_left()
            response = 'HTTP/1.1 200 OK\n\nGoing Left!'
        elif b'/go/right' in request:
            go_right()
            response = 'HTTP/1.1 200 OK\n\nGoing Right!'
        elif b'/stop' in request:
            stop()
            response = 'HTTP/1.1 200 OK\n\nStopped!'
        elif b'/check' in request:
            response = 'HTTP/1.1 200 OK\n\nOK!'
        else:
            response = 'HTTP/1.1 404 Not Found\n\nCommand not found.'

        cl.send(response)
        cl.close()
