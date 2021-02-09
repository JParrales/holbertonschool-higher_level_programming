#!/usr/bin/node

const API_URL = 'https://swapi-api.hbtn.io/api/';
const FILMS_URL = 'films/:id';
require('request').get(`${API_URL}${FILMS_URL.replace(':id', process.argv[2])}`, function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
