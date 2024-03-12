function manageMovies(commandsArr) {
  let movies = [];

  for (let command of commandsArr) {
    let splitCommand = command.split(" ");

    if (command.includes("addMovie")) {
      let movieName = splitCommand.slice(1).join(" ");
      movies.push({
        name: movieName,
      });
    } else if (command.includes("directedBy")) {
      let [movieName, director] = command.split(" directedBy ");
      for (let movie of movies) {
        if (movie["name"] === movieName) {
          movie["director"] = director;
        }
      }
    } else if (command.includes("onDate")) {
      let [movieName, date] = command.split(" onDate ");
      for (let movie of movies) {
        if (movie["name"] === movieName) {
          movie["date"] = date;
        }
      }
    }
  }

  for (let movie of movies) {
    if (movie["name"] && movie["director"] && movie["date"]) {
      console.log(JSON.stringify(movie));
    }
  }
}

manageMovies([
  "addMovie The Avengers",
  "addMovie Superman",
  "The Avengers directedBy Anthony Russo",
  "The Avengers onDate 30.07.2010",
  "Captain America onDate 30.07.2010",
  "Captain America directedBy Joe Russo",
]);
