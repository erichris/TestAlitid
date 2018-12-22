var io = require('socket.io')(process.env.PORT || 26495);
const { Pool, Client } = require('pg')

console.log('Database starting...');


const pool = new Pool({
  user: 'alitid_1',
  host: 'localhost',
  database: 'alitid',
  password: 'Nomorelove12',
  port: 5432,
})

/*
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'Playeras',
  password: 'Nomorelove12',
  port: 5432,
})
*/
pool.query('SELECT NOW()', (err, res) => {
  //console.log(err, res)
  pool.end()
})


const client = new Client({
  user: 'alitid_1',
  host: 'localhost',
  database: 'alitid',
  password: 'Nomorelove12',
  port: 5432,
})

/*
const client = new Client({
  user: 'postgres',
  host: 'localhost',
  database: 'Playeras',
  password: 'Nomorelove12',
  port: 5432,
})
*/

client.connect()

console.log('Database started');




console.log('Server starting');
io.on('connection', function(socket){
  console.log('client connected');

  //socket.emit('login', 'Par1', 'Par2');

  socket.on('Login', function(user, pass, deviceID){
    console.log("OnMessage");
    socket.emit('test', 'MyNick', 'Msg to the client');
    
	var MyQuery = 'SELECT id, app FROM public."Login_planescape" WHERE "ID1" = '; 
	MyQuery += "'" + user + "'";
	MyQuery += ' AND "ID2" = ';
	MyQuery += "'" + pass + "'"
	MyQuery += ';';
	console.log(MyQuery);
	
	var DeviceQuery = 'SELECT "ID_Movil1" FROM public."Login_planescape" WHERE "ID1" = ';
	DeviceQuery += "'" + user + "'";
	DeviceQuery += ' AND "ID2" = ';
	DeviceQuery += "'" + pass + "'"
	DeviceQuery += ';';
	console.log(DeviceQuery);
	
	var UpdateDevice = 'UPDATE public."Login_planescape" SET "ID_Movil1" = ' ;
	UpdateDevice += "'" + deviceID + "'";
	UpdateDevice += ' WHERE "ID1" = ';
	UpdateDevice += "'" + user + "'";
	UpdateDevice += ';';
	console.log(UpdateDevice);
	
    client.query(MyQuery, (err, res) => {
	  //console.log(err, res.rows[0])
	  if(res.rows[0] != null){
		  client.query(DeviceQuery, (errd, resd) => {
			  console.log(deviceID)
			  console.log(resd.rows[0]['ID_Movil1'])
			  if(resd.rows[0]['ID_Movil1'] == "" || resd.rows[0]['ID_Movil1'] == deviceID){
				  
				  
				  
				  socket.emit('Loged', res.rows[0]['id'], res.rows[0]['app']);
				  client.query(UpdateDevice, (erru, resu) => {
					  console.log(resu + " " + erru);
					  client.query('COMMIT');
					  console.log("end");
				  })
			  }else{
				  socket.emit('NotLoged', "Este codigo ya fue usado");
			  }
			  //client.end()
			  return res;
		  })
		  
		  console.log(MyQuery);
		  
		  //socket.emit('Loged', res.rows[0]['id'], res.rows[0]['app']);
	  }else{
		  socket.emit('NotLoged', "Usuario o Contraseña incorrectos");
	  }
      //client.end()
      return res;
    })
    
  });

/*
  socket.on('loggin', function(param1, param2){
    console.log("Try Login Pass");
    
    client.query('SELECT entrada FROM comidas WHERE db_id = 1;', (err, res) => {
      console.log(err, res.rows[0]['entrada'])
      client.end()
      return res;
    })
  });
*/

});
