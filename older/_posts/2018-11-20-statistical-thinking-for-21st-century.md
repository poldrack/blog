---
date: '2018-11-20T10:09:00.001-08:00'
description: ''
published: true
slug: 2018-11-20-statistical-thinking-for-21st-century
tags:
- http://schemas.google.com/blogger/2008/kind#post
- legacy-blogger
time_to_read: 5
title: Statistical Thinking for the 21st Century - a new intro statistics book
---

*This was originally posted on blogger [here](http://www.russpoldrack.org/2018/11/statistical-thinking-for-21st-century.html)*.

I have published an online draft of my new introductory statistics book, titled "Statistical Thinking for the 21st Century", at <a href="http://thinkstats.org/">http://thinkstats.org</a>.&nbsp; This book was written for my&nbsp;<a href="http://psych10.github.io/">undergraduate statistics course </a>at Stanford, which I started teaching last year.&nbsp; The first time around I used Andy Field's <a href="https://uk.sagepub.com/en-gb/eur/an-adventure-in-statistics/book237529">An Adventure in Statistics</a>, which I really like but most of my students disliked because the statistical content was buried within a lot of story.&nbsp; In addition, there are a number of topics (overfitting, cross-validation, reproducibility) that I wanted to cover in the course but weren't covered deeply in the book.&nbsp; So I decided to write my own, basically transcribing my lecture slides into a set of RMarkdown notebooks and generating a book using <a href="https://bookdown.org/yihui/bookdown/">Bookdown</a>.<br /><br />There are certainly many claims in the book that are debatable, and almost certainly things that I have gotten wrong as well, given that I Am Not A Statistician.&nbsp; If you have the time and energy, I'd love to hear your thoughts/suggestions/corrections - either by emailing me, or by <a href="https://github.com/poldrack/psych10-book/issues">posting issues at the github repo.</a>&nbsp;<br /><br />I am currently looking into options for publishing this book in low-cost paper form - if you would be interested in using such a book for a course you teach, please let me know.&nbsp; Either way, the electronic version will remain freely available online.<br /><br /><br />

---

## 5 comments captured from [original post](http://www.russpoldrack.org/2018/11/statistical-thinking-for-21st-century.html) on Blogger

**Unknown said on 2018-11-20**

I teach undergrad stats tobpsych majors... Id be interested in the paper version.

**Unknown said on 2018-11-20**

Give a free copy and all Indians learn it freely.

**Opher Donchin said on 2018-11-21**

Hello Russ, this book looks really good. I have been teaching statistics to biomedical engineers out of Slinker and Glanz Primer of Applied Regression for many years now and your book has a bunch of advantages. <br />There are two things that will slow me down and I wonder if they aren't easy fixes (or things I could help with, if you're interested): (1) exercises at the end of chapters help enormously when using a textbook; I understand you may have these available from teaching the course. (2) slightly more mathematical sophistication, especially in building the relationship between the chi squared distribution and the F and t tests and for understanding the relationship between the least squared fits and the parameters estimates in a regression model. I can understand the math might make more sense as optional chapters, given the spirit of the book, but I think they're important for an audience with a little more technical background.<br />One more thing that I thought just now is that the Bayesian chapter seems to me to undersell the power of the Bayesian approach. Bayesian methods seem to me to take their power from the shift in emphasis from hypothesis testing to parameter estimation and from the flexibility in model selection that comes with an approach based in JAGS or Stan. I'm not sure how to fix this, but the current chapter seems problematic to me.<br />I solve the Bayes problem by teaching a classical course to undergraduates and a Bayesian course to graduate students. It gives me the opportunity to pretend I'm like the physicists who get to introduce modern physics by telling the students everything they learned so far is completely wrong.

**Russ Poldrack said on 2018-11-21**

Thanks Opher!  I agree that it would be nice to have more mathematical sophistication as well as exercises.  Since I haven't used the book yet in the course (will do so starting in January) I don't have a well fleshed out set of exercises, but I hope to add them in the future.  <br /><br />re: the Bayes chapter, I agree that it's limited, but that's largely due to the fact that this is meant for an audience without the level of mathematical or computational sophistication to handle working directly with something like JAGS or STAN.  I wanted to still give them a feel for the Bayesian approach, without scaring them off.  <br /><br />I can see a couple of alternatives - one would be to include some additional sections that one could unfold for greater detail (I think that's possible with Gitbooks but need to figure out details).  Another would be to have multiple versions of the book, with different degrees of mathematical detail.  Once I've taught with it this winter, I will reconsider these options and hope to get back to you at that point.  would love your input and contributions!

**Russ Poldrack said on 2018-11-21**

great, thanks Ben!

