# LessSpam
*A global spam number reporting and searching system, to avoid malicious attackers!*

![Logo](https://www.lessspamwith.tech/static/images/logo.png)

## Inspiration ❄️❄️
Each year, tens of millions of Americans receive spam calls. A lot of money is lost to these scammers, and personally, as people who are educated to be safe online, these spam callers are becoming more and more lifelike. 5 years ago, these voices sounded like those of robots, but nowadays, it sounds like an actual human being is talking to you. According to statistics collected by many colleges, approximately 46% of the calls a person receives daily is a spam call. This inspired us to create an application that could possibly end or at least minimize the amount of money lost yearly by these scammers, by providing a global database of spam numbers. We'll talk more about this below ⬇

## What it does ☃️☃️
The user begins by texting the phone number (+1 580 681 1131) with the spam number they want to report. If it's a valid number, it then gets stored in our Firebase Database, and each time that number is reported, the "# of Reports" count increases by one. If a user reports a new number, that appears in our table as well. Eventually, anyone who thinks a number might be a spam number can just verify it by reporting it to our database. And if tons of other people also reported the same number, then it's probably spam! (What are the chances that a real person called thousands of phone numbers and also made them think they are a scam?)

## How we built it 🌲🌲
Languages:
 - HTML (Designing the structure of the website)
 - CSS (Styling the website)
 - JavaScript (Searching phone numbers on the website)
 - Python (What Flask runs on ⬇)
    - Flask (Runs Flask and the Twilio SMS webhook)

Tools:
 - Google Cloud Firebase (What Firestore runs on ⬇ )
    - Cloud Firestore (Storing Data like Phone Numbers)
 - Twilio (Sending and receiving SMS Messages)
 - Domain.com (For our domain: [lessspamwith.tech](http://www.lessspamwith.tech/))


## Challenges we ran into 🧥🧥
We had a hard time connecting our domain with Replit, because there were a bunch of configuration issues that took a while to solve. This included some advanced setup with DNS Records and Nameservers. However, with patience, we were successfully able to identify this issue, and solve it!

Another challenge that we ran into was the search bar on our site: we had many issues with it. Some of these issues include not being able to type in it, the site refreshing on entering (which clears the search), and more! Eventually, we needed to change various things like the input type, action, submission trigger, and more, and we're glad to say we got it all working!

## Accomplishments that we're proud of 📱📱
Overall, we were really proud of how the website ended up turning out. We are honestly proud of the fact that we made a complete and working winter-themed application connecting online security with the world. We designed the entire website from scratch (instead of using a website template), and designed the logo & banner too. Aditionally, learning tons of new tools like Firebase and Twilio was a great experience, and we really enjoyed this project. 

## What we learned 🔋🔋
We were mostly new to using Firebase and Firestore in our application, and especially it's usage in both Python *and* JavaScript. Additionally, we were unfamiliar with Twilio as a whole, but were super interested in it and learned how to create complex reply chains and other cool Twilio features. Finally, we were mostly new to live updates and single-page sites, as although we had made websites before, a new page for search results just didn't feel right. This forced us to learn complicated JavaScript to let us find search queries and update the data live.

## What's next for Less Spam 📞📞
We want to help people stay safer online. We hope to build some sort of a defense mechanism for users to only enter a phone number once, in order to ensure that the number of reports stays valid (meaning one specific number can only report a specific spam number once, and there is a cooldown per-user for reporting any spam numbers). Additionally, we hope to improve our visual aesthetic in the future, and hopefully add more content/functionality to our site, such as the ability to submit records through a website instead of only through SMS.
