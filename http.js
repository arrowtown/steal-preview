const express = require('express')
const app = express()
const port = 23333
const { exec } = require("child_process");
var url = require('url');

app.get('/', (req, res) => {
  res.send('Hello World');
});

app.get('/v', (req, res) => {
  console.log(req.ip,req.path,req.url);
  var q = url.parse(req.url, true).query;
  var name = q.a;
  if(!name){
    res.send("Hello World"); //write a response to the client
  }else {
    console.log(name);
    exec("scrapy runspider ./avSpider.py -a name="+name+" --nolog 2>&1", (error, stdout, stderr) => {
        res.send(stdout); //write a response to the client
    });
  }
})

app.listen(port, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }

  console.log(`server is listening on ${port}`)
})
