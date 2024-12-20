#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
if (args.length < 3) {
  console.log('You need 3 arguments. Error.');
  process.exit(1);
}
const fa = fs.readFileSync(args[0]);
const fb = fs.readFileSync(args[1]);
fs.writeFileSync(args[2], fa + fb);
