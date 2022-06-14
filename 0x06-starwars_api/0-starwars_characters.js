#!/usr/bin/node

// Print all characters from a Star Wars movie fetched from an API
// Movie ID required as a command line argument

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    const characterNames = characters.map(
      (charactersUrl) => new Promise((resolve, reject) => {
        request(charactersUrl, (error, response, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      }));
    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  }
});
