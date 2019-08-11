from ssl import SSLSocket,SSLContext,CERT_REQUIRED
import socket

def main():
	ip = 'github.com'
	ssl_domains = []
	#context = ssl.create_default_context()
	context = SSLContext()
	context.verify_mode = CERT_REQUIRED
	context.check_hostname = False
	context.load_verify_locations("./cacert.pem")
	conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=ip)
	conn.connect((ip, 443))
	cert = conn.getpeercert()
	tlen = len(cert['subject'])
	ssl_domains.append(cert['subject'][tlen-1][0][1])
	if cert['subjectAltName']:
		tmp_domains = cert['subjectAltName']
		for item in tmp_domains:
			if item[1] not in ssl_domains:	
				ssl_domains.append(item[1])

	print(ssl_domains)


if __name__ == "__main__":
	main()