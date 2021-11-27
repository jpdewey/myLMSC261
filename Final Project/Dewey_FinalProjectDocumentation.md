# Final Project Documentation

## Some Sources
- [How To Build A Website by W3](https://www.w3schools.com/howto/howto_website.asp)

## Process
### Steps
#### Code Creation
- First, I established an html file called index.html, and began to create an outline of my html code
  - This involved beginning with the standard
  ``` <!DOCTYPE html>
  <html lang="en">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, intial-scale=1">
  ```
  - This final line of code was from the "How To Build A Website by W3" source from [here](https://www.w3schools.com/howto/howto_website.asp), in order to allow the website to translate to multiple devices and still look good
- Next I began to establish my basic body of the site, in order to have a website that can be hosted, before the it looks good through a css file. This process is being done prior to establishing and linking a css file since my goal from Rachael is to have an ugly site that can be hosted by Monday, November 29th, then to make that site pretty.
  - I linked the css file that I plan on using, but didn't call to the css file at all during the basic construction of the website
- I then tested how the site was working and looked by opening the .html file on my computer in my browser, to great success!
    The basic code:
    ```
    <!DOCTYPE html>
    <html lang="en">
    <header>
    <meta charset="UTF-8">
    <title>JP Dewey</title>
    <meta name="viewport" content="width=device-width, intial-scale=1">
    <link rel="stylesheet" href="main.css">
    </header>
    <div>
      <body>
        <h1>
          JP Dewey Music
        </h1>
        <h3>
          <i>Producer, Arranger, Composer, Keyboardist, Songwriter</i>
        </h3>
        <h2>Home</h3>
        <br>
        <img src="Pianoimage1.JPG">
    </div>
      <br>
    <p>
      <div>
        <h2>About</h2>
          <br>
          JP Dewey is a versatile producer, arranger, composer, keyboardist, and songwriter, with music spanning across a wide variety of genres and with work experience spanning across many facets of the music industry. Finish this portion of the website at a later point.
      </div>
      <br>
      <div>
        <h2>Music</h2>
          <br>
          This is where some 30 second demos of music will go (these cuts in my music still need to occur)
          <br>
      <div>
        <h2>Performance</h2>
          <br>
          This is where some embedded videos of performance will go
      </div>
      <br>
      <div>
        <h2>Resumé</h2>
          <br>
          This is where both a well-laid out visual representation of my resumé will go, as well as a link to a .pdf of my resumé
      </div>
      <br>
      <div>
        <h2>Contact</h2>
          <br>
          JP Dewey can be reached at the following sources:
          <ul>
            <li>jpdeweymusic@gmail.com</li>
            <li>@jpdeweymusic</li><!-- embed a small instagram icon before @ symbol -->
          </ul>
          <br>
            Or, reach out here!
          <br>
            This is where the contact form will be inserted
      </div>
        <br>

    </p>
    </body>
    </html>
    ```
    This looked boring, but without any glitches or issues
- The next step is to add some more content, and then begin the process and investigation of hosting the website
- Regarding the css template I downloaded, code for the form, buttons, and formatting is available in provided html files, as well as the css file, so I may utilize some of this, stay tuned!
- I began to more deeply investigate the css file in order to create more interesting connections, since the mere css connection dictated at the top of the html file was not enough
- While viewing the css file, I became confused about some aspects of the code, such as:
```
#banner {
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  -moz-flex-direction: column;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
  -moz-justify-content: center;
  -webkit-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  cursor: default;
  height: 100vh;
  min-height: 35em;
  overflow: hidden;
  position: relative;
  text-align: center;
}

```
  - Additionally, I tried using the .align-center to center some of my text like this:
  ```
  <h1 class=".align-center">
    JP Dewey Music
  </h1 class=".align-center">
  <h3 class=".align-center">
    <i>Producer, Arranger, Composer, Keyboardist, Songwriter</i>
  </h3 class=".align-center">
  <h2 class=".align-center">Home</h3 class=".align-center">
  <br>
  <img src="Pianoimage1.JPG">
</div>
<br>
  ```
  But this didn't work the way I had intended, prompting me to investigate the sample website provided in the css template, and utilizing the code from that index.html file, I tried connecting it into my own website.

  I first copied this code for the beginning header feature:
  ```
  <head>
  	<title>Spectral by HTML5 UP</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
  	<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
  </head>

  ```
I then took out some of the redundant code, including the link to the main.css file, the ``` <meta name="viewport">``` section, and the ``` <meta charset="utf-8" /> ``` since these were pieces of code that I already had
- Then I tested this to see if it worked similar to the sample Website
- I then realized I had merely copied the main head, not the header I was attempting to, so I copied a different set of code:
```
<header id="header" class="alt">
  <h1><a href="index.html">Spectral</a></h1>
  <nav id="nav">
    <ul>
      <li class="special">
        <a href="#menu" class="menuToggle"><span>Menu</span></a>
        <div id="menu">
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="generic.html">Generic</a></li>
            <li><a href="elements.html">Elements</a></li>
            <li><a href="#">Sign Up</a></li>
            <li><a href="#">Log In</a></li>
          </ul>
        </div>
      </li>
    </ul>
  </nav>
</header>
```
I then tweaked some of these elements in order to relate it to my own Website
This ended up creating a side menu function that I hadn't intended on incorporating, and left the rest of the html file I had created as ugly as it was previously. I decided to read the entire reference html file before continuing to modify my code.
#### Hosting
- During the process of creating my code, I had to figure out how to get the website hosted outside of github (it wasn't already on github, but the only process I am familiar with is github). As per Rachael's instructions, I went about figuring out how to host with an ugly html file
- I utilized my roommate Thomas to figure this section out, with a conversation looking something like this:
  "Thomas, where did you host your website for Rachael's class?" "Well, I actually hosted it on github during her class, but I ended up hosting it on this server called Digital Ocean" 
