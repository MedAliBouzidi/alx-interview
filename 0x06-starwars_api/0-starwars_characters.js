#!/usr/bin/node
const request = require("request");

if (process.argv.length !== 3) {
  console.log("Usage: ./0-starwars_characters.js <filmId>");
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
