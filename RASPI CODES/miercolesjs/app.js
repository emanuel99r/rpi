const http = require('http');

const hostname = '192.168.1.11';
const port = 8080;

const server = http.createServer((req, res) => {
	res.statuscode = 200;
	res.setHeader('Content-Type', 'text/pain');
	res.end('Hola Mundo!\n');
	});
	
server.listen(port, hostname, () => {
	console.log('Servidor corriendo en http://${hostname}:${port}/');
	});
