#!/usr/bin/node

const swUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(swUrl, function (err, res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
