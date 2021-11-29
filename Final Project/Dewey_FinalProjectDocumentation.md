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
- While reading the html file example, I noticed that the class "inner" and applied that to parts of my code that I wanted to be in the center of the page after the code ``` class=".aligncenter" ``` didn't work.
- I then realized what the example html file was referencing within the css file, recalling from class how the ``` <div>``` code separates things for the css file, and realized I needed to use the same syntax as the example html file in order to properly call the css file. Therefore, I copied this code:
  ```
  <section id="banner">
    <div class="inner">
      <h2>Spectral</h2>
      ```
      And added the necessary endings and changed "Spectral" to "JP Dewey Music" and checked to see if this replicated the example website, which it did! (to an extent, still not as fancy)
        - This is a large breakthrough, as I now know how to properly link to the more complex css file using code examples from the example html file. This feels like cheating, so I will ask Rachel about whether this is cheating or not.
- After this breakthrough, I decided to fill in the rest of the information before carrying on with the css file, figuring that it would be easier to format after everything had been filled out.
- I then inserted a table using this code from the elements.html file that was included, modifying the table slightly to fit my needs:
```
<section>
  <h4>Table</h4>
  <h5>Default</h5>
  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Item One</td>
          <td>Ante turpis integer aliquet porttitor.</td>
          <td>29.99</td>
        </tr>
        <tr>
          <td>Item Two</td>
          <td>Vis ac commodo adipiscing arcu aliquet.</td>
          <td>19.99</td>
        </tr>
        <tr>
          <td>Item Three</td>
          <td> Morbi faucibus arcu accumsan lorem.</td>
          <td>29.99</td>
        </tr>
        <tr>
          <td>Item Four</td>
          <td>Vitae integer tempus condimentum.</td>
          <td>19.99</td>
        </tr>
        <tr>
          <td>Item Five</td>
          <td>Ante turpis integer aliquet porttitor.</td>
          <td>29.99</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td colspan="2"></td>
          <td>100.00</td>
        </tr>
      </tfoot>
    </table>
  </div>
```
I made changes so that the initial table looked like this:
```
<div>
  <h2>Resumé</h2>
    <br>
    <section>
      <h4>Resumé</h4>
      <h5>Professional</h5>
      <div class="table-wrapper">
        <table> <!-- Table 1, Professional work experience -->
          <thead>
            <tr>
              <th>Name</th>
              <th>Description</th>
              <th>Dates</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Junior Analyst at Hit Songs Deconstructed</td>
              <td>Analyzed, drafted, and proofed data on Top 10 Hot 100 music; effectively utilizing database resources</td>
              <td>Nov 2021 - Present</td>
            </tr>
            <tr>
              <td>Admissions Student Recruiter and Tour Guide at Berklee College of Music</td>
              <td>Engaged with prospective students and parents to encourage them to apply and enroll in the College</td>
              <td>May 2021 - Present</td>
            </tr>
            <tr>
              <td>WTD Studios Scheduling Assistand at Berklee College of Music</td>
              <td> Engaged with the student body to successfully grant access to on campus studios through online reservation system</td>
              <td>May 2021 - Present</td>
            </tr>
            <tr>
              <td>Music Analysis Intern at Hit Songs Deconstructed</td>
              <td>Analyzed, drafted, and proofed data and reports on Top 10 Hot 100 pop music; effectively utilizing database resources; successfully reserached for opportunities to grow the company's reach and influence in the music industry</td>
              <td>May 2021 - Aug 2021</td>
            </tr>
          </tbody>
        </table>
```
- I then repeated this for all sections of the resumé that I wanted to include on the website 


#### Hosting
- During the process of creating my code, I had to figure out how to get the website hosted outside of github (it wasn't already on github, but the only process I am familiar with is github). As per Rachael's instructions, I went about figuring out how to host with an ugly html file
- I utilized my roommate Thomas to figure this section out, with a conversation looking something like this:
  "Thomas, where did you host your website for Rachael's class?" "Well, I actually hosted it on github during her class, but I ended up hosting it on this server called Digital Ocean"
Upon investigating Digital Ocean, a source that Thomas appreciates, I realized that I would also need to register my domain name with a common domain registrar.
I then googled domain registrars, finding register.com, google, and namecheap.com (the one that Thomas uses). Based solely on price, Google costs $7/year, namecheap is $5.98, and register.com is $5 for the first year, but suspiciously doesn't give an easy way to find the cost.
  Since Thomas trusts namecheap, and I don't need a service to host the website if I use Digital Ocean, I decided to continue with namecheap and Digital Ocean. Additionally, this allows me to bounce issues and ideas back and forth with Thomas in perpetuity.
- I successfully registered a domain with the name jpdeweymusic.com with namecheap. I then registered for Digital Ocean, and just need to deploy the website via digital ocean, and hosting should be all set.
  I did run into some confusion, since it says that in order to deploy your website, I need to choose whether to deploy as a wordpress server, magneto server, cPanel server, Ghost server, Ubuntu server, or the source code on another app platform. This will require further research to ensure I do not mess anything up in this process.
- After sending the DNS to Digital ocean from namecheap, I decided to consult my trusty resource and roommate, Thomas, for more information regarding the next hosting steps.
  This discussion resulted in him realizing that Digital Ocean is different than it was when he did it, prompting me to have to do individual research. He recommended launching as an "Ubuntu server," since that utilizes the same operating system as the os his website runs on, Divian.
