#!/usr/bin/node

const sw_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(sw_url, function (err, res, body) {
	body = JSON.parse(body);
	console.log(body.title);
});
