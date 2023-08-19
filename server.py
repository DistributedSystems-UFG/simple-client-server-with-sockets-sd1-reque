from socket import *
from constCS import *

def handle_request(request):
    parts = request.split()
    if len(parts) != 3:
        return "Invalid request"
    
    operation = parts[0]
    num1 = int(parts[1])
    num2 = int(parts[2])

    if operation == "ADD":
        return str(num1 + num2)
    elif operation == "SUB":
        return str(num1 - num2)
    else:
        return "Unknown operation"

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Server is listening...")
(conn, addr) = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break

    request = bytes.decode(data)
    result = handle_request(request)
    conn.send(str.encode(result))

conn.close()
