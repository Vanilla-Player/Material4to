
const {readFile, writeFile, writeFileSync} = require('fs')
const http = require('http');
const path = require('path');

let base = path.basename(__filename)
let appPath = '/' + base



http.createServer((req, res) => {
     
     if(!(req.url === appPath)){

          if(req.method === "GET"){
               try{
                         readFile("."+req.url,'utf8', (err,data)=>{
                              if(err){res.writeHead(400, {'Content-Type': 'text/plain'}); return;}
                                   res.writeHead(200, {'Content-Type': 'text/plain'});
                                   res.end(data);
                              })     
               }catch(error){
                         console.log("Error")
                         res.end(err);
                    }
          }else{
               console.log("Method not Handle");
               res.writeHead(405, {'Content-Type': 'text/plain'});
          }

     }else{
          res.writeHead(403, {'Content-Type': 'text/plain'});          
     }
     
     readFile("./history.txt", 'utf-8', (err, data)=>{
          if (err){
               console.log("Not created")
               writeFileSync("./history.txt", "No matter what's here");
               
          }

          const oldData = data;

          writeFile("./history.txt", oldData + `\nMethod: ${req.method}, Status: ${res.statusCode}`, (err, data)=>{
               if(err) throw err;
               console.log("I'm Data " + data);
          });
     })

    
     
}).listen(3000);

console.log('serving since '+Date.now());
