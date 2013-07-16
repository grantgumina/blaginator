##Epic Fail##
**Posted Sun, 14 Jul 2013 08:21:00**

Last week I had an epic fail. No really - it was a very, *very* epic fail. The startup my good friend and co-founder [Luke Walsh](http://lukewal.sh) and I have been working on, [Outfitly](http://outfitly.com) launched. Within hours, the response was overwhelmingly negative and besides that - we were hacked. As I said, it was a big epic fail.

In retrospect, the epic fail really could've been prevented. In fact, just about everything that contributed to the fail's epicness was an issue Luke and I knew many startups suffer from (mostly from reading [Hacker News](http://news.ycombinator.com)), but we simply didn't have the life experiences necessary to see those issues manifest themselves in our own product. Here's where we screwed up:

###Homepage Fail###
This is probably one of the more embarrassing fails of our launch. Simply put, our homepage sucked. It consisted of a logo, a signup (and separate login) form, and a beta "sticker" in the top right corner. There was no information about Outfitly, what it did, how to use it, or anything other than what I mentioned above. For me, someone who takes pride in my design and UX work, this was incredibly embarrassing when the blinders were pulled off and I realized what I had created.

Luke and I had been working on Outfitly part time since the beginning of summer. It was the first time either of us had written anything in Backbone.js, and the entire time we worked on it we suffered from critical architectural issues created as we made very common rookie mistakes (primarily zombie views). Instead of doing the right thing and doing a re-write, we continued to push on hacking our way out of any issue that came up - vowing we would do a re-write after launch. Obviously, this caused our issues to exponentially grow as one hack created five more as soon as it was implemented.

Honestly, that kind of shoddy work isn't something we'd do in our academic work but we were so blinded by meeting an arbitrary deadline we had created we compromised and put out really sub-par work. The big take away here is to never lose sight of the bigger picture no matter how much pressure you're under.

###Security Fail###
I'm not necessarily as embarrased by this simply because we did specifically say Outfitly was a *beta*, but it's still pretty embarrassing. Outfitly was susceptible to what's called a Cross Site Scripting attack. Basically users were able to upload a comment that was Javascript and that Javascript would actually be rendered in the browser. Someone attacked the site and all of our users were Rick Rolled. Talk about a blow to the ego. Ouch.

Once again, this wouldn't have been an issue if Luke or I had been thinking about the longterm, bigger picture. Had we been in this mindset, we would've done a proper risk assessment and most likely wouldn't have run into a critical bug hours after launch.

###Moving Forward###
Once we were hacked and saw all the Rick Rolling, porn uploading, and other nasty trolling that was going on in Outfitly, we had to take it offline. However, we're not done just yet. We still think there's many new and interesting opportunities for a social shopping service, so we're still working on Outfitly. Importantly though, we are challenging some of the assumptions we initially made and are planning on doing a very targeted release so we can make intelligent decisions as we move forward.