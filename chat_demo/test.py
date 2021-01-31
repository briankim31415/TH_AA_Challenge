from server import Chat_Server
from client import run_client
import socket
import select
import socket
import select
import errno


server_chat = Chat_Server()
server_chat.main()

run_client