
const {readFile, writeFile} = require('fs').promises
const fs = require('fs')
const res = require('express/lib/response');
const http = require('http');


http.
    createServer((req, res)=>{

        const fileStream = fs.createReadStream(`./history.txt`, 'utf-8' );
        fileStream.on('open', ()=>{
            fileStream.pipe(res)
        })
        ;

        fileStream.on('error', (err)=>{
            console.log(err);
        });

    }).listen(3000);


