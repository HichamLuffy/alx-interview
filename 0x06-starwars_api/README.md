

# Star Wars Characters Script

This script fetches and prints the names of all characters in a specified Star Wars movie using the Star Wars API. The movie is identified by its ID passed as a positional argument.

## Prerequisites

- Node.js installed on your machine [official Node.js website](https://nodejs.org/) .
- `request` module installed in your Node.js environment.
```sh
   npm install request
   ```


## Usage

1. **Make the script executable:**
   ```sh
   chmod +x 0-starwars_characters.js
   ```

2. **Run the script with the movie ID as an argument:**
   ```sh
   ./0-starwars_characters.js <Movie ID>
   ```

   Example:
   ```sh
   ./0-starwars_characters.js 3
   ```

   This will print the names of all characters in the movie with ID 3, "Return of the Jedi".

## Script Explanation

The script `0-starwars_characters.js` performs the following steps:

1. **Import the Request Module:**
   ```javascript
   const request = require('request');
   ```
   This imports the `request` module, which is used to make HTTP requests.

2. **Check Command-Line Arguments:**
   ```javascript
   if (process.argv.length !== 3) {
     console.log('Usage: ./0-starwars_characters.js <Movie ID>');
     process.exit(1);
   }
   ```
   This checks if exactly one positional argument (the movie ID) is provided. If not, it prints the usage message and exits.

3. **Build the API URL:**
   ```javascript
   const movieId = process.argv[2];
   const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
   ```
   Constructs the URL to fetch data for the specified movie using the provided movie ID.

4. **Make the API Request to Fetch Movie Data:**
   ```javascript
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
   ```
   Makes an HTTP GET request to the Star Wars API to fetch data for the specified movie. If successful, it parses the response to extract the list of character URLs.

5. **Fetch and Print Character Names:**
   ```javascript
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
   ```
   For each character URL, it makes an HTTP GET request to fetch the character data. If successful, it parses the response to extract and print the character's name.

## Example Output

When running `./0-starwars_characters.js 3`, the output will be:
```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```
