const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Failed to fetch movie data. Status Code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.log(`Failed to fetch character data. Status Code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
