from socket import *
from constCS import *

def send_request(s, request):
    s.send(str.encode(request))
    data = s.recv(1024)
    return bytes.decode(data)

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    operation = input("Enter operation (ADD/SUB/MULT/DIV): ")
    if operation == "exit":
        break

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    request = f"{operation} {num1} {num2}"
    result = send_request(s, request)
    print("Result:", result)

s.close()
