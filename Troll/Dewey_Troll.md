# Troll Documentation file

Upon my Github stalking journey, I began by finding two projects that were related to my final project:
- The first one, [this website development](https://github.com/Bookshlf-in/Website) looked interesting but had nothing happening in over 23 days when I first looked
- The second one, [this website development](https://github.com/moinworld/wtm-website) also looked interesting but had nothing happening in over 5 years, so naturally I couldn't use this one either
Despite these discouragements, I still read their opening markdown files, and found their projects quite interesting.
- The first one was a way of book sharing called bookshlf, developed by a team of college students to create an easier way of lending textbooks to one another. This was an open project, and anyone could hop on the team by joining the slack and cloning the repository
- The second one was a simple website development run by "Women Techmakers Hamburg" which seemed super cool, but unfortunately was rather old


I then explored the github "explore" feature, which had me stumble across [this app development](https://github.com/asteroid-team/asteroid) that I decided to stalk, despite it having nothing to do with my final project.

## Discovery
- The [project](https://github.com/asteroid-team/asteroid), known as "Asteroid" is a "PyTorch-based audio source separation toolkit for researchers," allowing "fast experimentation on common datasets," which is a bunch of words for something that processes wav files, analyzes them, and creates summaries for analysis of these waveforms.
  - To be completely honest, I don't fully understand all of the aspects of this program, it's a bit beyond the scope of my understanding, but it seems really cool and is audio related!
- Despite not fully understanding the program, the collaboration and communication via Github was quite interesting to witness. At this time, they were in the middle of developing a Voice Activity Detector, which was finalized on Thanksgiving day. This addition was done on a branch that was merged with the master. Since it was a brand new piece of code, there were no issues
- Additional collaborations, communications, and troubleshooting were found in the recent pull requests, where users and administrators were testing to make tests faster, and fixing issues such as "the issue regarding X-UMX when receiving a mono audio as the input."
  - Coding issues such as this mono audio issue is reported by having users create a pull request and either fixing the issue themselves in the python source code, or by reporting it via opening an issue and having someone else edit the source code for the issue. This is all outlined in the initial markdown file. There is also a slack channel that can be joined for asking questions/suggesting new features.
- Another interesting code change I found interesting was how new features were added, specifically regarding the new VAD that was added over Thanksgiving. (For the most part, this application is finalized, so updates to the code are sometimes months apart, but I was lucky enough to stalk during an updating time.)
  - The process of adding a new feature required code to be tested first in the testing portion of the repository, followed by an update in the "egs" portion of the repository, which is where the "recipes" exist. (This is a portion of the code that I do not fully understand, as it has to do with the application of Asteroid), followed by being fully implemented in the "asteroid" portion of the repository, which is where users can find the application.
  - Additionally, it should be noted that Asteroid is not an application for the casual user. Asteroid must be downloaded via Terminal through a step-by-step process outlined in the repository, and run using a python shell.
- Finally, I found the changes in the branch development to be rather interesting, with branches open both for testing new features and fixing old issues. Each branch had a clearly defined role, and it seems that some of this behind-the-scenes discussion of the code occurs via the slack channel (which I did not join)

## Final Thoughts
- I found the way that collaborators communicated via pull requests and opening issues through github to be very cool, especially since this project is incredibly open-sourced, allowing anyone to collaborate and contribute via pull requests.
- I also found the whole concept of an open-source project to be very cool, allowing many different contributors and collaborators to be part of the project. This project has 44 contributors and is used by 45 people, which was very cool.
- Finally, this code is PYTHON which is very exciting, since we learned this in class! 
