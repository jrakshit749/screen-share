from vidstream import ScreenShareClient
import threading

#specify public ip address in the paramenter to connect over the internet 
#here the local ip addr. is used since since I'm connecting it one only one computer 
#NOT a real case scenario

sender = ScreenShareClient('127.0.0.1', 9999) 
t = threading.Thread(target = sender.start_stream)
#sender.start_stream()

t.start()

while input("") != 'STOP':
	continue

sender.stop_stream()