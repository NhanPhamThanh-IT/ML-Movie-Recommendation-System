<div align="center">

# ML-Movie-Recommendation-System

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/recommendations-100%2B-orange.svg" alt="Recommendations">
  <img src="https://img.shields.io/badge/fun-100%25-ff69b4.svg" alt="Fun">
</p>
</div>

<div align="justify">

## 🎬 Welcome to the ML Movie Recommendation System!

Ever wish Netflix knew you better? Tired of your friends recommending movies that make you question your friendship? Fear not! This project is here to save your movie nights (and possibly your friendships).

### What is this?

An ML-powered, content-based movie recommendation system that uses science (and a dash of movie magic) to suggest films you'll actually want to watch. No more "Sharknado" unless you _really_ like sharks and tornadoes.

### How does it work?

1. **Data Collection**: We use a dataset of movies with genres, keywords, taglines, cast, and directors. Yes, even the director matters (looking at you, Michael Bay fans).
2. **Preprocessing**: We combine all the juicy details into one big text blob. Null values? We eat those for breakfast.
3. **Feature Extraction**: TF-IDF Vectorizer turns movie info into numbers. Because computers love numbers more than popcorn.
4. **Similarity Calculation**: Cosine similarity finds movies that are basically siblings separated at birth.
5. **User Input**: You tell us your favorite movie. We find the closest match (even if you spell "Inception" as "Insheption").
6. **Recommendation**: We serve up 30 movies you might love. Or at least not hate.

### How to use

1. Clone this repo (because you have excellent taste).
2. Run `script.py` in the `scripts/` folder. Python required. Popcorn optional.
3. Enter your favorite movie when prompted. (Try not to troll the system. Or do. We dare you.)
4. Get a list of movies to watch next. Impress your friends. Or confuse them.

### Requirements

- Python 3.x
- pandas, numpy, scikit-learn, difflib
- A sense of humor

### Data

The magic happens with `data/movies.csv`. It's packed with blockbusters, flops, and everything in between. (No judgment.)

### Project Structure

- `scripts/script.py`: The brains of the operation.
- `data/movies.csv`: The movie buffet.
- `docs/`: For those who like to read before watching.
- `notebook.ipynb`: For the data science wizards.

### Contributing

Pull requests welcome! Add your favorite movie, improve recommendations, or just fix typos. Bonus points for adding more puns.

### License

MIT. Because sharing is caring.

## Frequently Asked Questions (FAQ)

**Q: Will this recommend me movies I actually like?**  
A: If you like movies, yes. If you only watch documentaries about grass growing, results may vary.

**Q: Can I use this to settle movie night arguments?**  
A: Absolutely. Just blame the algorithm if someone hates the pick.

**Q: What if I type "Shrek" 100 times?**  
A: You’ll get a lot of recommendations. Some may even be ogre-rated.

**Q: Does it work for TV shows?**  
A: Nope. This is strictly for movies. TV shows are a whole different drama.

**Q: Can I add my own movies?**  
A: Yes! Fork, add, and pull request. The more, the merrier (and weirder).

## Troubleshooting

- If you get an error, try turning your computer off and on again. (Just kidding, but it works surprisingly often.)
- Make sure your Python packages are installed. If not, run:
  ```powershell
  pip install pandas numpy scikit-learn
  ```
- If you get weird recommendations, remember: the system is only as good as the data. Or maybe you just have unique taste.

## Fun Facts

- The system uses **cosine similarity**. Not to be confused with cosine pizza, which is also delicious.
- The dataset includes blockbusters, cult classics, and movies you’ve never heard of. (Looking at you, "Attack of the Killer Tomatoes".)
- Typing "Batman" will probably give you more Batmen than you can handle.
- The code is commented so well, even your grandma could understand it. (Assuming she’s into machine learning.)

## Pro Tips

- For best results, use your favorite movie as input. For wild results, use your least favorite.
- If you get a recommendation for "Cats" (2019), consider it a sign to go outside.
- Share your results on social media and tag your friends. Bonus points for movie puns.

## Meme Zone

![Movie Meme](https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif)

## Did You Know?

- The algorithm once recommended "The Godfather" and "Minions" in the same list. True story.
- If you run the script at midnight, you might get a horror movie. Spooky!
- The system has a secret love for Nicolas Cage movies. Try it and see.
- Typing "Matrix" may cause you to question reality. Red pill or blue pill?

## User Stories

- "I used this to pick a movie for my first date. We're now married!" — Happy User
- "The recommendations were so good, my popcorn burned because I couldn't leave the screen." — Snack Enthusiast
- "I asked for a comedy and got a drama. Turns out, it was a tragicomedy. 10/10." — Risk Taker

## Movie Night Survival Guide

- **Snacks:** Essential. The system runs faster if you have popcorn nearby (not scientifically proven, but worth a try).
- **Friends:** Optional, but recommended for maximum fun. If your friends disagree with the recommendations, remind them that robots are impartial.
- **Blanket:** For emotional support during plot twists.
- **Remote Control:** For skipping the credits, unless you’re a true fan.

## Easter Eggs

- Try entering "Titanic" and see if you get a recommendation for "Ice Age". Coincidence? Maybe.
- Type "The Room" for a truly unique experience. You’re tearing me apart, algorithm!
- Enter "Star Wars" and count how many times the word "star" appears in your recommendations.

## Advanced Usage

- Want to recommend movies to your pet? Just enter their favorite movie ("Air Bud" is a good start).
- Use the system to settle bets. Winner gets to pick the next movie, loser brings snacks.
- Challenge: Find the most obscure movie in the dataset and watch it. Report back with your sanity level.

## Community Challenges

- **The Genre Gauntlet:** Watch one movie from every genre recommended. Bonus points for surviving horror.
- **Director’s Cut:** Only watch movies by the same director for a week. Warning: May cause sudden appreciation for directorial quirks.
- **Cast Party:** Pick a favorite actor and watch every recommended movie they appear in. Prepare for emotional rollercoasters.

## Future Plans

- Add support for user ratings (so you can finally give "Cats" the score it deserves).
- Integrate with streaming APIs (Netflix, call us!).
- Add a "Surprise Me!" button for the truly adventurous.
- Make the recommendations even funnier. Because why not?

## Credits

- Created by NhanPhamThanh-IT and contributors.
- Inspired by every movie night that ended in chaos.
- Special thanks to Python, pandas, numpy, scikit-learn, and caffeine.

## Contact

Questions, suggestions, or movie memes? Open an issue or send a carrier pigeon.

## Feedback

We love feedback! If the system made you laugh, cry, or question your life choices, let us know. If it recommended "Sharknado" five times, we apologize (sort of).

## Inspirational Quotes

> "With great recommendations comes great responsibility." — Not Spider-Man

## Hall of Fame

- Most recommended movie: [Your guess here!]
- Least recommended movie: "Sharknado 5: Global Swarming" (Sorry, not sorry.)
- Most creative user input: "I want a movie that makes me laugh, cry, and question reality."

## Final Words

If you read this far, you deserve a movie marathon. Enjoy! 🍕🎥
And remember: In a world full of choices, let the algorithm be your guide.

</div>
