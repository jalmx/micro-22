_B=False
_A=None
import usocket as socket,ustruct as struct
from ubinascii import hexlify
import utime
class MQTTException(Exception):0
class MQTTClientS:
	def __init__(A,client_id,server,port=0,user=_A,password=_A,keepalive=0,ssl=_B,ssl_params={}):
		B=port
		if B==0:B=8883 if ssl else 1883
		A.client_id=client_id;A.sock=_A;A.server=server;A.port=B;A.ssl=ssl;A.ssl_params=ssl_params;A.pid=0;A.cb=_A;A.user=user;A.pswd=password;A.keepalive=keepalive;A.lw_topic=_A;A.lw_msg=_A;A.lw_qos=0;A.lw_retain=_B
	def _send_str(A,s):A.sock.write(struct.pack('!H',len(s)));A.sock.write(s)
	def _recv_len(D):
		A=0;B=0
		while 1:
			C=D.sock.read(1)[0];A|=(C&127)<<B
			if not C&128:return A
			B+=7
	def set_callback(A,f):A.cb=f
	def set_last_will(A,topic,msg,retain=_B,qos=0):B=topic;assert 0<=qos<=2;assert B;A.lw_topic=B;A.lw_msg=msg;A.lw_qos=qos;A.lw_retain=retain
	def connect(A,clean_session=True):
		A.sock=socket.socket();G=socket.getaddrinfo(A.server,A.port)[0][-1];A.sock.connect(G)
		if A.ssl:import ussl;A.sock=ussl.wrap_socket(A.sock,**A.ssl_params)
		F=bytearray(b'\x10\x00\x00\x00\x00\x00');B=bytearray(b'\x04MQTT\x04\x02\x00\x00');C=10+2+len(A.client_id);B[6]=clean_session<<1
		if A.user is not _A:C+=2+len(A.user)+2+len(A.pswd);B[6]|=192
		if A.keepalive:assert A.keepalive<65536;B[7]|=A.keepalive>>8;B[8]|=A.keepalive&255
		if A.lw_topic:C+=2+len(A.lw_topic)+2+len(A.lw_msg);B[6]|=4|(A.lw_qos&1)<<3|(A.lw_qos&2)<<3;B[6]|=A.lw_retain<<5
		E=1
		while C>127:F[E]=C&127|128;C>>=7;E+=1
		F[E]=C;A.sock.write(F,E+2);A.sock.write(B);A._send_str(A.client_id)
		if A.lw_topic:A._send_str(A.lw_topic);A._send_str(A.lw_msg)
		if A.user is not _A:A._send_str(A.user);A._send_str(A.pswd)
		D=A.sock.read(4);assert D[0]==32 and D[1]==2
		if D[3]!=0:raise MQTTException(D[3])
		return D[2]&1
	def disconnect(A):A.sock.write(b'\xe0\x00');A.sock.close()
	def ping(A):A.sock.write(b'\xc0\x00')
	def publish(A,topic,msg,retain=_B,qos=0):
		G=topic;D=qos;C=bytearray(b'0\x00\x00\x00');C[0]|=D<<1|retain;B=2+len(G)+len(msg)
		if D>0:B+=2
		assert B<2097152;E=1
		while B>127:C[E]=B&127|128;B>>=7;E+=1
		C[E]=B;A.sock.write(C,E+1);A._send_str(G)
		if D>0:A.pid+=1;H=A.pid;struct.pack_into('!H',C,0,H);A.sock.write(C,2)
		A.sock.write(msg)
		if D==1:
			while 1:
				I=A.wait_msg()
				if I==64:
					B=A.sock.read(1);assert B==b'\x02';F=A.sock.read(2);F=F[0]<<8|F[1]
					if H==F:return
		elif D==2:assert 0
	def subscribe(A,topic,qos=0):
		D=topic;assert A.cb is not _A,'Subscribe callback is not set';B=bytearray(b'\x82\x00\x00\x00');A.pid+=1;struct.pack_into('!BH',B,1,2+2+len(D)+1,A.pid);A.sock.write(B);A._send_str(D);A.sock.write(qos.to_bytes(1,'little'))
		while 1:
			E=A.wait_msg()
			if E==144:
				C=A.sock.read(4);assert C[1]==B[2]and C[2]==B[3]
				if C[3]==128:raise MQTTException(C[3])
				return
	def wait_msg(A):
		E=A.sock.read(1);A.sock.setblocking(True)
		if E is _A:return _A
		if E==b'':raise OSError(-1)
		if E==b'\xd0':B=A.sock.read(1)[0];assert B==0;return _A
		C=E[0]
		if C&240!=48:return C
		B=A._recv_len();D=A.sock.read(2);D=D[0]<<8|D[1];H=A.sock.read(D);B-=D+2
		if C&6:F=A.sock.read(2);F=F[0]<<8|F[1];B-=2
		I=A.sock.read(B);A.cb(H,I)
		if C&6==2:G=bytearray(b'@\x02\x00\x00');struct.pack_into('!H',G,2,F);A.sock.write(G)
		elif C&6==4:assert 0
	def check_msg(A):A.sock.setblocking(_B);return A.wait_msg()
class MQTTClient(MQTTClientS):
	DELAY=2;DEBUG=_B
	def delay(A,i):utime.sleep(A.DELAY)
	def log(A,in_reconnect,e):
		if A.DEBUG:
			if in_reconnect:print('mqtt reconnect: %r'%e)
			else:print('mqtt: %r'%e)
	def reconnect(A):
		B=0
		while 1:
			try:return super().connect(_B)
			except OSError as C:A.log(True,C);B+=1;A.delay(B)
	def publish(A,topic,msg,retain=_B,qos=0):
		while 1:
			try:return super().publish(topic,msg,retain,qos)
			except OSError as B:A.log(_B,B)
			A.reconnect()
	def wait_msg(A):
		while 1:
			try:return super().wait_msg()
			except OSError as B:A.log(_B,B)
			A.reconnect()