#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, body) => {
  console.log(err || body);
});
