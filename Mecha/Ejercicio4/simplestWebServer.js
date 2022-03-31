const http = require('http');
const os = require('os')

http.createServer((req, res) => {

    

    res.end();
}).listen(3000);


console.log("Here is something vv \n")

console.log(__filename);

console.log("There is ^^^^");




console.log('serving since '+Date.now());