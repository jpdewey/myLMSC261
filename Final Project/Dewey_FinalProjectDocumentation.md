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
- I noticed that the website was super spread out, so I looked into the css file and noticed the margins were 0, so I adjusted that in the main.css file and saved the file
  - This moved everything in slightly, but upon trying to make things move in further, adjusting these bounds changed nothing.
  - I consulted Thomas, and changed everything to fall into the subclass "main" which didn't work, then tried the class "major" which added lines under all the headers, which didn't help. I gave up on Thomas at this point
  - I managed to get the page wrapped and look more professional, but lost my main header, which I found is due to not being linked as an animation in the javascript files, which I have to link. I found this by utilizing the css file, which had an important! note next to where this is function is called.
- While working on other aspects of the code, I blew time by utilizing this code in order to create a better sub heading underneath the main title of the website:
```
<section id="one" class="wrapper style1 special">
  <div class="inner">
    <header class="major">
      <h2>Arcu aliquet vel lobortis ata nisl<br />
      eget augue amet aliquet nisl cep donec</h2>
      <p>Aliquam ut ex ut augue consectetur interdum. Donec amet imperdiet eleifend<br />
      fringilla tincidunt. Nullam dui leo Aenean mi ligula, rhoncus ullamcorper.</p>
    </header>
    <ul class="icons major">
      <li><span class="icon fa-gem major style1"><span class="label">Lorem</span></span></li>
      <li><span class="icon fa-heart major style2"><span class="label">Ipsum</span></span></li>
      <li><span class="icon solid fa-code major style3"><span class="label">Dolor</span></span></li>
    </ul>
  </div>
</section>
```
I altered it to become this code to fit my needs:
```
<section id="one" class="wrapper style1 special"> <!-- Sub title code -->
  <div class="inner">
    <header class="major">
      <h2><i>Producer, Arranger, Composer, Keyboardist, Songwriter</i></h2>
    </header>
  </div>
</section>
```
- I then began the process of implementing different aspects of the html templates into my code, starting by establishing a better way of inserting my image for my "About" section, which involved copying a piece of code from the example that allowed the image to become indented:
```
<section>
<h5>Left &amp; Right</h5>
<p><span class="image left"><img src="images/pic04.jpg" alt="" /></span>Morbi mattis mi consectetur tortor elementum, varius pellentesque velit convallis. Aenean tincidunt lectus auctor mauris maximus, ac scelerisque ipsum tempor. Duis vulputate ex et ex tincidunt, quis lacinia velit aliquet. Duis non efficitur nisi, id malesuada justo. Maecenas sagittis felis ac sagittis semper. Curabitur purus leo, tempus sed finibus eget, fringilla quis risus. Maecenas et lorem quis sem varius sagittis et a est. Maecenas iaculis iaculis sem. Donec vel dolor at arcu tincidunt bibendum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce ut aliquet justo. Donec id neque ipsum. Integer eget ultricies odio. Nam vel ex a orci fringilla tincidunt. Aliquam eleifend ligula non velit accumsan cursus. Etiam ut gravida sapien. Morbi mattis mi consectetur tortor elementum, varius pellentesque velit convallis. Aenean tincidunt lectus auctor mauris maximus, ac scelerisque ipsum tempor. Duis vulputate ex et ex tincidunt, quis lacinia velit aliquet. Duis non efficitur nisi, id malesuada justo. Maecenas sagittis felis ac sagittis semper. Curabitur purus leo, tempus sed finibus eget, fringilla quis risus. Maecenas et lorem quis sem varius sagittis et a est. Maecenas iaculis iaculis sem. Donec vel dolor at arcu tincidunt bibendum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce ut aliquet justo. Donec id neque ipsum. Integer eget ultricies odio. Nam vel ex a orci fringilla tincidunt. Aliquam eleifend ligula non velit accumsan cursus. Etiam ut gravida sapien.</p>
</section>
```
The implementation:
```
<section>
  <h2>About</h2>
  <p><span class="image left"><img src="Pianoimage1.JPG" alt="" /></span>JP Dewey is a versatile producer, arranger, composer, keyboardist, and songwriter, with music spanning across a wide variety of genres and with work experience spanning across many facets of the music industry.
  Originally from the Southerntier region of upstate New York, Dewey participated in numerous regional musical festivities while in high school, including the 2018 NYSSMA All-State Conference Festival as the Jazz Ensemble's Pianist, performing with the Central Winds Jazz Orchestra, performing with the Hartwick College Jazz Ensemble, and winning "Best Musician of the Festival" awards in Oneida, NY and Fonda, NY.
  Following high school, Dewey went on to study at Berklee College of Music in Boston, MA, majoring in Contemporary Writing and Production with a minor in Writing for Television and New Media. While at Berklee, Dewey arranged for two large-scale concerts, produced and wrote with a multitude of artists across genres from pop, jazz, rock, and R&B, composed original music for picture and for release, and contributed dozens of arrangements to fellow students and organizations. Additionally, he performed in a number of difference facets, including for pop, latin pop, R&B, and neo-soul artists, singer-songwriter showcases, and musical theatre endeavors.
  While at Berklee, Dewey also began working for the company Hit Songs Deconstructed, first as an intern, and then as an analyst.
  Currently, JP Dewey is in the process of finishing his degree at Berklee, working part-time for Hit Songs Deconstructed, and freelance writing, producing, and arranging.</p>
</section>
```
- It was at this point that I realized that dividing the website into separate, scrolling pages like the template dictated would probably be easier than trying to adapt the template into one, scrolling webpage.
  - Despite this realization, I decided to continue trying to adapt the template to my vision before embarking on this extra amount of work
- After a bit of difficulty, I managed to fix the fancy parts of the cover page by realizing my javascript links were referencing the wrong location, so upon re-linking it to the right location, I had homepage success!!
- I then created three new html files for each page: about.html, resume.html, and contact.html. I copied the main code wrappers from the index.html file, and then utilized the other page html files from the template for the different formatting based on the page. This allowed the pages to have a different feel from the main homepage. I then copied all of the necessary body information into each respective html page file, and linked the files to the main index.html file through the menu command in the header, which looks like this:
```
<header id="header" class="alt">
  <h1><a href="index.html">JP Dewey Music</a></h1>
  <nav id="nav">
    <ul>
      <li class="special">
        <a href="#menu" class="menuToggle"><span>Menu</span></a>
        <div id="menu">
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="resume.html">Resumé</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
      </li>
    </ul>
  </nav>
</header>
```
- I then worked out different bugs by comparing code between the example html files and the html files for each page. An example of this would be making sure the border worked across all pages, which I fixed by deleting the class section of the header function in the above code
-

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
- I chose to launch as a Devian OS
- I then routed the hostname to the IP of the server space I bought in San Francisco
- I then followed [this instructional guide](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-debian-8?utm_source=Customerio&utm_medium=Email_Internal&utm_campaign=Email_DebianDistroNginxWelcome&mkt_tok=MTEzLURUTi0yNjYAAAGBDgiCwyP5XtBB4IpIPZLTUy70XEC5jOhbaUnTotpD9gCoNRymxz-0KoX5ym_4rdq4x_YHEnwR9COrd6RufiqvD2WO12XUZumofuniYPSWvQ) for how to configure and set up the server, utilizing bash to create remote connections to the server that I had established and routed in Digital Ocean and namecheap. I then followed those instructions, establishing SSH keys, root passwords, and the linux system with a user
- In the future, I would like to implement further security measures as outlined [here](https://www.digitalocean.com/community/tutorials/recommended-security-measures-to-protect-your-servers?mkt_tok=MTEzLURUTi0yNjYAAAGBDgiCw3dqEcjsyf5rqTq4QvPJNsw9Xr-bz8lyhc_usVWzLpkPc8jkhcULggQK0qWeFwX9HCVfQXXp7Bm_llrWfO2s64_4vkXPEwiEuy9n5g&utm_campaign=Email_DebianDistroNginxWelcome&utm_medium=Email_Internal&utm_source=Customerio)
- I then worked towards installing Nginx on the server, using [this](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-debian-8?utm_source=Customerio&utm_medium=Email_Internal&utm_campaign=Email_DebianDistroNginxWelcome&mkt_tok=MTEzLURUTi0yNjYAAAGBDgiCxMdWtf7whsaUMNxsn5g7CoIXoZROoh6DbMOPRh63tKGyhneOY_0lbNsMfztoBMKbh_ItGudwUSv9yMhzbaqjTHl6_Zei1aW-HgJLww) guide
- Through this, I installed Nginx on the server through sudo commands within the user I had established on the server (not through the root user)
- After installing the Nginx server, I began the process of uploading my website files to the server
- The following sources were referenced for how to get the html files to upload to the nginx server:
  - [This source](https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/)
  - [Plus this source](https://futurestud.io/tutorials/nginx-how-to-serve-a-static-html-page)
  - [And this source](https://www.nginx.com/resources/wiki/modules/upload/)
  - [And this source](https://www.nginx.com/resources/wiki/start/)
  - [And this source](https://www.nginx.com/resources/wiki/start/topics/examples/full/)
  None of these sources ended up helping me find the code, with all of them resulting in error messages due to trying to use a different coding language that was provided in bash
- The source that ended up helping was Thomas, who gave me this code for uploading files into nginx:
```
scp -r /Users/josephdewey/Final\ Project root@<ip address>:/var/www/html
```
- I tested this - it failed. The nginx confirmation message is gone, and there is nothing on the server. Even though there is nothing on the server, everything looks correctly from the terminal
- I fixed it through Digital Ocean, the name for the domain was incorrect, so I fixed this to say "jpdeweymusic.com" instead of "www.jpdeweymusic.com" which is what it thought was the domain name
- This rendered success, but none of the attached files were present on the internet, only the raw html file
  I realized this could be due to the attached files being located in a separate folder on the server, so I decided to upload all of the files that are necessary for linking individually, and to take down the folder that was separate from the index.html file
  I also decided that I would finish this portion of the website after the css coding was done, since I had successfully hosted the Website!
- Upon trying to upload an updated version with the css file, the website was still not linking to the css. I tried re-uploading, triple checking the file path, double checking the configuration of the server, and making small insignificant tweaks to the file path to make sure it reflected the server
  - I then decided to consult Rachel in an office hour to double check and have a fresh set of eyes look at my code. She suggested changing one of the file names to not include any symbols
    - This unfortunately did not work. So, I decided to eliminate the amount of folders present.
    - I started by moving all of the main files (the css files and the js files) into the same folder as the html files, so that there is not file path when referencing the files. I then went into each file and made sure that the "routing" was correct.
    - I then deleted aspects of the template that were unnecessary and would take up excessive space, possibly inhibiting the efficiency of the server (these included readme files, example html files, etc.)
    - I then went through and changed the paths of all of the images in the css file, since they were now in a new place
    - I verified that I had done these steps correctly by checking with the locally opened html file and making sure all the previous aspects from the css files were present
    - I then deleted all the files on my server and re-uploaded them
- This worked!!! (sorta) The css files and js files were connected to the html file, so it displays correctly, but this led me to the conclusion that storing things in folders and then trying to reference those folders on a Debian server may not be 100% efficient or effective, since the images that I kept two layers of folders deeper than the other files were not appearing.
- Since I was finally able to get a slightly more decent looking website hosted, I decided to finish up my css coding, then delete the images from the server and re-upload everything directly into the main html folder that is used for the Website
