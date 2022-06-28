from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import time
import socketio

app = Flask(__name__)
app.config['SECRET KEY']='secret'
socketio= SocketIO(app)

@app.route('/',methods=['POST','GET'])
def index():
   return render_template('index2.html')
     
@socketio.on('message_1')
def another_event_1(data):
    print('LOS DATOS SON', data)
    emit('message_1',data,broadcast=True)

@socketio.on('message_2')
def another_event_2(data):
    print('LOS DATOS SON', data)
    emit('message_2',data,broadcast=True)

@socketio.on('message_3')
def another_event_3(data):
    print('LOS DATOS SON', data)
    emit('message_3',data,broadcast=True)

@socketio.on('message_4')
def another_event_4(data):
    print('LOS DATOS SON', data)
    emit('message_4',data,broadcast=True)

@socketio.on('message_5')
def another_event_5(data):
    print('LOS DATOS SON', data)
    emit('message_5',data,broadcast=True)

@socketio.on('message_6')
def another_event_6(data):
    print('LOS DATOS SON', data)
    emit('message_6',data,broadcast=True)

@socketio.on('lim_1_inf')
def li1(data):
    print('LOS DATOS SON', data)
    emit('lim_1_inf',data,broadcast=True) 
@socketio.on('lim_1_sup')
def ls1(data):
    print('LOS DATOS SON', data)
    emit('lim_1_sup',data,broadcast=True)  

@socketio.on('lim_2_inf')
def li2(data):
    print('LOS DATOS SON', data)
    emit('lim_2_inf',data,broadcast=True) 
@socketio.on('lim_2_sup')
def ls2(data):
    print('LOS DATOS SON', data)
    emit('lim_2_sup',data,broadcast=True)             

@socketio.on('lim_3_inf')
def li3(data):
    print('LOS DATOS SON', data)
    emit('lim_3_inf',data,broadcast=True) 
@socketio.on('lim_3_sup')
def ls3(data):
    print('LOS DATOS SON', data)
    emit('lim_3_sup',data,broadcast=True) 

@socketio.on('lim_4_inf')
def li4(data):
    print('LOS DATOS SON', data)
    emit('lim_4_inf',data,broadcast=True) 
@socketio.on('lim_4_sup')
def ls4(data):
    print('LOS DATOS SON', data)
    emit('lim_4_sup',data,broadcast=True)  

@socketio.on('lim_5_inf')
def li5(data):
    print('LOS DATOS SON', data)
    emit('lim_5_inf',data,broadcast=True) 
@socketio.on('lim_5_sup')
def ls5(data):
    print('LOS DATOS SON', data)
    emit('lim_5_sup',data,broadcast=True)             

@socketio.on('lim_6_inf')
def li6(data):
    print('LOS DATOS SON', data)
    emit('lim_6_inf',data,broadcast=True) 
@socketio.on('lim_6_sup')
def ls6(data):
    print('LOS DATOS SON', data)
    emit('lim_6_sup',data,broadcast=True)

@socketio.on('outRange')
def outrange():
    emit('outRange',broadcast=True)

@socketio.on('typeError')
def typeerror():
    emit('typeError',broadcast=True)

@socketio.on('enviarGrados')       
def grados(msg):
    print('el mensaje es', msg)
    emit('grados',msg,broadcast=True)

@socketio.on('posicionHome')       
def home():
    print('llegando a home')
    emit('home','home',broadcast=True)

if __name__=='__main__':
    socketio.run(app,host='192.168.100.10' ,port=10000)

    