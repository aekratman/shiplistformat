Written with the help of chatGPT to figure out more basics of Python, week of 5/10/24. 

This program takes a .txt file of Million Year Picnic's comic shiplist and formats it in proper HTML to be uploaded to [Million Year Picnic's site,]([url](https://www.themillionyearpicnic.com/)) on which I am an intern.

Holds the following functions of note:
<li>**editor**, which finds the title line and modifies it to include the proper formatting.</li>
<li>**random_add**, which inserts the HTML that I use for featured comics on six random comic titles.</li>
<li>n**ext_wednesday**, which determines the closest Wednesday (AKA: when the comics come out) and formats the title to include it.</li>
<li>**runFile**, which takes the given .txt file, runs all of the above programs on it, and spits out a newly-formatted text file along with the randomly selected titles so I can add their features easily.</li>

This was mainly an exercise to get used to modifying Python-- again, I used chatGPT as a guiding hand-- and trying to get used to actually pushing things to Github. Overall, it's going to make my job much easier every week, so I am quite pleased!

In the future, I am going to add some parts to **editor** so it will also format the comic shortages and delays.

Cheers!
