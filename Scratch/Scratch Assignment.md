# Scratch Documentation

### Scratch game: Musical Fun!
- This week I created a scratch game that allowed the user to play sounds from four different instruments by clicking on each instrument sprite, as well as hear the sounds all together by clicking on the speaker sprite in the middle of the scratch environment. Additionally, when each sprite is clicked, the background changes and the sprite moves (except for the middle sprite, which just changes the background and plays the music of the other four sprites).
- I accomplished this by creating variables for each sprite, to represent when the music is playing. When the sprite is clicked, the variable changes from 0 to 1, which determines what the sprite does using a conditional if/then/else statement. Each sprite has a script with an if/then/else code set, allowing music to play, the sprite to turn, and the background to change when the sprite is clicked, and allowing the default settings to remain the same when the sprite is not clicked or when the music is done playing from the sprite. I also made sure that the sounds were unique by utilizing samples from Splice, and uploading them in as new sounds in each sprite. I then edited the sounds to somewhat fit together, maintaining the same bpm and key throughout the samples.
- I struggled to get the backgrounds to revert back to the original when the music was done playing, and I overcame this by experimenting with different code combinations within the if/then/else statements. I found a solution when I used two similar if/then/else statements, but performing the opposite function (one statement for when the variable = 1 and one for when the variable = 0). I also had to make sure the variables were set back to 0 at the end of the program in order for everything to return back to the starting position.
- I did not use any code from others, I spent a lot of time playing around with different scratch code to become as familiar as possible with both the scratch interface and the logic behind each block. 