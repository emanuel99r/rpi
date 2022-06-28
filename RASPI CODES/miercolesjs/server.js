//snfiffer 
const dgram = require("dgram");
const server1 = dgram.createSocket("udp4");
var mensaje;
server1.on("error", err => {
  console.log(`server error:\n${err.stack}`);
  server.close();
});
var sniffer ;

server1.on("listening",()=>{
    const address= server1.address();
});
server1.bind(41500,"192.168.1.11");
//web server 
const express = require('express');
const socketIO = require('socket.io');
const http = require('http');

const path = require('path');

const app = express();
var contador=0;
let server = http.createServer(app);


const port = process.env.PORT || 8080;
app.use(express.static(path.join(__dirname,"../public")));
//app.use(express.static(publicPath));
//IO = this is a backend comunication 
let io = socketIO(server);

io.on('connection',(client)=>{
console.log('usuario conectado');

    client.on('disconnect',()=>{
        console.log('usuario desconectado');
    });

    //escuchar cliente(grados)
    client.on('enviarGrados',(mensaje)=>{
        console.log('Grados motor1: ',mensaje[0]);
        console.log('Grados motor2: ',mensaje[1]);
        console.log('Grados motor3: ',mensaje[2]);
        console.log('Grados motor4: ',mensaje[3]);
        console.log('Grados motor5: ',mensaje[4]);
        console.log('Grados motor6: ',mensaje[5]);
    });

        //escuchar cliente(home)
    client.on('posicionHome',(home)=>{
        console.log('llegando a home')
	var five = require("johnny-five");
	var Raspi = require("raspi-io").RaspiIO;
	var board = new five.Board({
  	io: new Raspi()
	});

	board.on("ready", function() {
  	var led = new five.Led("3");
  	led.blink();
	});
    })    

        //prueba de segundero
    client.on('prueba',(prueba)=>{
        contador=contador+1
        setInterval(function(){
            client.emit('verif',contador + prueba)
        },1000);
    });

        //enviar al cliente
    server1.on("message",(msg,rinfo)=>{
        sniffer=msg.toString("utf8");
        client.emit('enviarMensaje',sniffer);
        });
    
});

app.get("/", (req, res) => {
    res.sendfile("index.html");
  });



server.listen(port, (err) => {

    if (err) throw new Error(err);

    console.log(`Servidor corriendo en puerto ${ port }`);

});