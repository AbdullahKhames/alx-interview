#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api/';
const URL = BASE_URL + 'films/' + process.argv[2];

request.get(URL).on('response', function (response) {
  let responseData = '';

  response.on('data', (chunk) => {
    responseData += chunk;
  });

  response.on('end', () => {
    const obj = JSON.parse(responseData);
    const ACTOR_URLS = obj.characters;

    const getActorName = (ACTOR_URL) => {
      return new Promise((resolve, reject) => {
        request.get(ACTOR_URL).on('response', (resp) => {
          let respData = '';

          resp.on('data', (chunk) => {
            respData += chunk;
          });

          resp.on('end', () => {
            resolve(JSON.parse(respData).name);
          });
        });
      });
    };

    const promises = ACTOR_URLS.map((ACTOR_URL) => getActorName(ACTOR_URL));

    Promise.all(promises)
      .then((actorNames) => {
        actorNames.forEach((name) => console.log(name));
      })
      .catch((error) => {
        console.error('Error fetching actor names:', error);
      });
  });
});
