import sys,time, cgi, BaseHTTPServer
import os, linecache
from settings import server_ip, server_port, weight_output_file

servAddr=(server_ip, server_port)

class httpServHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.find('?') != -1:
			self.path, self.query_string = self.path.split('?',1)
		else:
			self.query_string = ''
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
                l=linecache.getline(weight_output_file, 1)
                
		#self.globals=dict(cgi.parse_qsl(self.query_string))
		self.stout =self.wfile
		self.wfile.write("{'wt':'%s'}" % (l))
                linecache.clearcache()
serv = BaseHTTPServer.HTTPServer(servAddr, httpServHandler)
print "Serve forever"
serv.serve_forever()