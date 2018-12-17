var io = require('socket.io')(process.env.PORT || 3000);
const { Pool, Client } = require('pg')

console.log('Database starting...');
const pool = new Pool({
  user: 'alitid_1',
  host: 'localhost',
  database: 'alitid',
  password: 'Nomorelove12',
  port: 5432,
})

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
	
    client.query(MyQuery, (err, res) => {
	  //console.log(err, res.rows[0])
	  if(res.rows[0] != null){
		  socket.emit('Loged', res.rows[0]['id'], res.rows[0]['app']);
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
