
const {readFile, writeFile} = require('fs').promises
const http = require('http');


const path = require('path');

let base = path.basename(__filename)
let appPath = '/' + base

const get_request = async(path) =>{
     try{
           const data = await readFile(path, 'utf-8')
           return data
         
     }catch(err){
          console.log(err)
          res.writeHead(400, {'Content-Type': 'text/plain'});
          return;
     }
    
}


const record_status = async (status, method) =>{
     try{
          const data = await readFile("./history.txt", 'utf-8')

          await writeFile("./history.txt", data + `\nMethod: ${method}, Status: ${status}`, {flag : 'a'})
     }catch(err){

          console.log(err)

     }
}

http.createServer((req, res) => {
     
     if(!(req.url === appPath)){

          if(req.method === "GET"){

               get_request("."+req.url)
                .then(resolve =>{
                     res.writeHead(200, {'Content-Type': 'text/plain'});
                     res.end(resolve)
                });
               
          }else{
               console.log("Method not Handle");
               res.writeHead(405, {'Content-Type': 'text/plain'});
          }

     }else{
          res.writeHead(403, {'Content-Type': 'text/plain'});          
     }
     

     record_status(res.statusCode, req.method);

    
     
}).listen(3000);

console.log('serving since '+Date.now());
