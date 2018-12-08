Writeup 10 - Crypto II
=====

Name: Kaan Ibici
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kaan Ibici

## Assignment 10 Writeup

### Part 1 (70 Pts)

Thanks to the obvious hint, I knew I had to perform an sql injection somewhere on the site. I wasn't able to find any input fields, however I noticed the URL included item?id=1 on one of the project pages. After seeing that entering different id values resulted in different products being displayed, it was clear that the URL field was an input to an sql query. I attempted to obtain all of the table records by adding OR '1'='1' to the query. Many attemps produced server errors, which to me implied that my syntax was incorrect. Eventually I realized that OR was filtered, but not or, and that since the query was probably adding single quotes around the input number, so I tried item?id=1'or'1'='1 so that the single quotes would all match up. The entire table was dumped, alloweing me to find the flag CMSC38R-{y0U-are_the_5ql_n1nja}.

### Part 2 (30 Pts)

Level 1:

The first level is pretty simple; by looking at the source for the page I could see that the input given to the search bar is placed directly into the HTML for the page, so the obvious solution is to input an js script tag with an alert, <script>alert()</script>.

Level 2:

I had to look at a couple of hints to figure this one out as I was not able to see why injecting script tags doesn't work (my knowledge of HTML is limited). Once I saw the hint that they in fact do not work, I looked up why this is the case, and found that script tags don't work when inserted into innerHTML. Fortunately the same source pointed out that onerror scripts are still executed, so I looked up onerror and found an example of onerror in an img tag. Seeing this, I tried the input <img src = 'nada' onerror = 'alert()'/> in the post box, which was successful!

Level 3:

I looked into the html for the webpage and found that clicking on the tabs calls the function chooseTab(num) with the number of the tab. I also saw that upon loading the page, the URL is parsed for whatever comes after the #, which is then passed to chooseTab(num). I looked into the chooseTab function and saw that it inserts an image tag with a src path that uses the num passed to the function, so I figured that I needed to get the chooseTab function to be called with an input that provides an invalid path and also concludes the img tag with an onerror function. To do this I replaced the number after # with nada.jpg' onerror='alert()'/>, which produced the desired error. 

Level 4:

This level took me a while, and required me to look at all of the hints (although the last one didn't really help me at all). I saw that the input to the timer is sent to startTimer(seconds), with single quotes applied around the input: onload="startTimer('{{ timer }}');". I figured that I needed to provide an input that would terminate the startTimer function and add an alert function after it. I tried inputing ');alert(), which resulted in onload="startTimer('&#39;);alert()');" and produced a syntax error. After a while I figured out that this was equivalent to onload="startTimer('');alert()');" thanks to the hint about HTML decoding, although I still have no idea why only one single quote is decoded instead of the entire input. Nevertheless, it was clear that I had to handle the syntax error produced by the unexpected '); after my alert call, which I accomplished by changing my input to ');alert(', which worked successfully. 

Level 5:

This level did not take me that long, although I'm still not completely sure how my solution worked. I saw that the signup html has the line <a href="{{ next }}">Next >></a>, so I figured I needed to find a way to provide an input for next such that the href links to a javascript program (I found out this is possible via a quick search on href tags). The only place I saw next being assigned a value is in the URL, so I tried changing the end of the URL from signup?next=confirm to signup?next=javascript:alert();. After entering the URL I then clicked on next to trigger the js function, and the alert popped up as expected. I'm not sure why this worked because I couldn't find where next=confirm is determined/parsed in the source files... I guess I should look into that.

Level 6:

From the level description it was clear that I needed to get the URL to link to an external js file that produces an alert. However I had no idea how to host a js script. I looked it up and found that dropbox is a popular solution, so I wrote the js file and uploaded it to dropbox. I saw that the js function that loads the gadget uses a regexp to disallow http and https, so I tried removing the https from the dropbox url, which did not work. By playing around with a browser search bar to find ways to modify https such that the page would still load, I realized that http doesn't have to be lowercase (duh), so I changed the https to HTTPS since the regexp is not case sensitive. I then had issues with using the wrong dropbox URL, however I eventually got it to work. The final URL I used is https://xss-game.appspot.com/level6/frame#HTTPS://dl.dropbox.com/s/ljt7vnfhu3axnhd/alert.js?dl=.

