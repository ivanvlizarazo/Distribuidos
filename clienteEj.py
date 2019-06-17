import socket
import threading
import sys
import pickle

class Cliente():
	def __init__(self, host="localhost", port=4000, name='Anon'):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))
		self.name = str(name)

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		while True:
			msg = input(self.name + '->')
			if msg != 'salir':
				self.send_msg('\n' + self.name + ': '+ msg)
			else:
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))


c = Cliente("10.253.23.221", 4000, input("Nombre de usuario: "))