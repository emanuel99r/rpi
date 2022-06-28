const express = require('express');
const socketIO = require('socket.io');

const path = require('path');

const app = express();
var contTabla=0;


const port = process.env.PORT || 8080;
app.use(express.static(path.join(__dirname,"../public")));

const server = app.listen(port, (err) => {
    if (err) throw new Error(err);
    console.log(`Servidor corriendo en puerto ${ port }`);
});


const io = socketIO(server);

io.on('connection',client=>{

console.log('usuario conectado');

    client.on('disconnect',()=>{
        console.log('usuario desconectado');
    });
    client.on('stop',()=>{
        console.log('stop')
        client.broadcast.emit('stop')
    });
    client.on('accionar',mensaje=>{
        console.log('Grados motor1: ',mensaje[0]);
        console.log('Grados motor2: ',mensaje[1]);
        console.log('Grados motor3: ',mensaje[2]);
        console.log('Grados motor4: ',mensaje[3]);
        console.log('Grados motor5: ',mensaje[4]);
        console.log('Grados motor6: ',mensaje[5]);
        client.broadcast.emit('accionar',mensaje)
    });
    client.on('accionarg',mensajeg=>{
        
        client.broadcast.emit('accionarg',mensajeg)
    });
    client.on('accionar_ik',accionar_ik=>{
        console.log('px: ',accionar_ik[0]);
        console.log('py: ',accionar_ik[1]);
        console.log('pz: ',accionar_ik[2]);
        console.log('ox: ',accionar_ik[3]);
        console.log('oy: ',accionar_ik[4]);
        console.log('oz: ',accionar_ik[5]);
        console.log('ow: ',accionar_ik[6]);
        client.broadcast.emit('accionar_ik',accionar_ik)
    });
    client.on('inRange',()=>{
        client.broadcast.emit('inRange')
    });
    client.on('arregloTabla',arregloTabla=>{
        contTabla=contTabla+1
        arrYInd=[arregloTabla[0],arregloTabla[1],arregloTabla[2],arregloTabla[3],arregloTabla[4],arregloTabla[5],contTabla]
        client.broadcast.emit('arregloTabla',arrYInd)
    });

    client.on('limpiar',()=>{
        contTabla=0
        console.log('limpiar')
        io.sockets.emit('limpiar')
    });
    client.on('contador1',cont1=>{
        client.broadcast.emit('contador1',cont1)
    });
    client.on('contador2',cont2=>{
        client.broadcast.emit('contador2',cont2)
    });
    client.on('contador3',cont3=>{
        client.broadcast.emit('contador3',cont3)
    });
    client.on('contador4',cont4=>{
        client.broadcast.emit('contador4',cont4)
    });
    client.on('contador5',cont5=>{
        client.broadcast.emit('contador5',cont5)
    });
    client.on('contador6',cont6=>{
        client.broadcast.emit('contador6',cont6)
    });
    client.on('limites',lim=>{
        client.broadcast.emit('limites',lim)
    });

    client.on('typeError',()=>{
        client.broadcast.emit('typeError')
        console.log('accionando')


    });
    client.on('pos1',pos1=>{
        client.broadcast.emit('pos1',pos1)
    });
    client.on('pos2',pos2=>{
        client.broadcast.emit('pos2',pos2)
    });
    client.on('pos3',pos3=>{
        client.broadcast.emit('pos3',pos3)
    });
    client.on('pos4',pos4=>{
        client.broadcast.emit('pos4',pos4)
    });
    client.on('pos5',pos5=>{
        client.broadcast.emit('pos5',pos5)
    });
    client.on('pos6',pos6=>{
        client.broadcast.emit('pos6',pos6)
    });
    client.on('deshabilitar',()=>{
        client.broadcast.emit('deshabilitar')
    });
    client.on('habilitar',()=>{
        client.broadcast.emit('habilitar')
    });
    client.on('colision',()=>{
        client.broadcast.emit('colision')
    });
    client.on('errorik',()=>{
        client.broadcast.emit('errorik')
    });
    client.on('MovEjecutado',()=>{
        client.broadcast.emit('MovEjecutado')
    });
    client.on('MovEjecutadoik',()=>{
        client.broadcast.emit('MovEjecutadoik')
    });
    client.on('ArmJointValues',arm_joint_values=>{
        //console.log(joint_values)
        client.broadcast.emit('ArmJointValues',arm_joint_values)
    });
    client.on('ArmJointNames',arm_joint_names=>{
        //console.log(joint_values)
        client.broadcast.emit('ArmJointNames',arm_joint_names)
    });
    client.on('GripperJointValues',gripper_joint_values=>{
        //console.log(gripper_joint_values)
        client.broadcast.emit('GripperJointValues',gripper_joint_values)
    });
    client.on('GripperJointNames',gripper_joint_names=>{
        //console.log(gripper_joint_names)
        client.broadcast.emit('GripperJointNames',gripper_joint_names)
    });
    client.on('JointValuesf',joint_valuesf=>{
        //console.log(joint_values)
        client.broadcast.emit('JointValuesf',joint_valuesf)
    });
    client.on('JointNamesf',joint_namesf=>{
        //console.log(joint_values)
        client.broadcast.emit('JointNamesf',joint_namesf)
    });
    client.on('pose',pose=>{
        //console.log(joint_values)
        client.broadcast.emit('pose',pose)
    });
    client.on('posef',posef=>{
        //console.log(joint_values)
        client.broadcast.emit('posef',posef)
    });
    client.on('gira_base',()=>{
        console.log("gira_base")
        client.broadcast.emit('gira_base')
    });
    client.on('stop_base',()=>{
        console.log("stop_base")
        client.broadcast.emit('stop_base')
    });
    client.on('arm_bounds',arm_bounds=>{
        
        client.broadcast.emit('arm_bounds',arm_bounds)
    });
    client.on('gripper_bounds',gripper_bounds=>{
        //console.log(gripper_bounds)
        client.broadcast.emit('gripper_bounds',gripper_bounds)
    });
    client.on('len',len=>{
        
        client.broadcast.emit('len',len)
    });
    client.on('leng',leng=>{
        //console.log(leng)
        client.broadcast.emit('leng',leng)
    });
    client.on('actualizar',()=>{
        console.log("actualizar")
        client.broadcast.emit('actualizar')
    });
    client.on('PGroups',p_groups=>{
        //console.log(p_groups)
        client.broadcast.emit('PGroups',p_groups)
    });
    client.on('hola',hola=>{
        console.log(hola)
        
    });
});

