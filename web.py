from http.server import HTTPServer, BaseHTTPRequestHandler
content ="""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>TCP/IP Protocol List</title>
</head>
<body>
  <h1>TCP/IP Layers and Protocols</h1>

  <ol>
    <li>
      <strong>Application Layer</strong>
      <ul>
        <li>HTTP / HTTPS</li>
        <li>FTP</li>
        <li>SMTP</li>
        <li>DNS</li>
        <li>DHCP</li>
      </ul>
    </li>

    <li>
      <strong>Transport Layer</strong>
      <ul>
        <li>TCP</li>
        <li>UDP</li>
      </ul>
    </li>

    <li>
      <strong>Internet Layer</strong>
      <ul>
        <li>IP (IPv4 / IPv6)</li>
        <li>ICMP</li>
        <li>IGMP</li>
      </ul>
    </li>

    <li>
      <strong>Network Access Layer</strong>
      <ul>
        <li>Ethernet</li>
        <li>Wi-Fi (IEEE 802.11)</li>
        <li>ARP</li>
      </ul>
    </li>
  </ol>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()