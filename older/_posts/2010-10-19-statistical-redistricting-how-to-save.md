---
date: '2010-10-19T07:24:00.000-07:00'
description: ''
published: true
slug: 2010-10-19-statistical-redistricting-how-to-save
tags:
- statistics
- http://schemas.google.com/blogger/2008/kind#post
- legacy-blogger
time_to_read: 5
title: 'statistical redistricting: how to save lots of time and money and get just
  about the same result'
---

*This was originally posted on blogger [here](http://www.russpoldrack.org/2010/10/statistical-redistricting-how-to-save.html)*.

I had promised myself that I wouldn't blog about politics, but this is really more about statistics so I think it's ok.<br /><br />David Sparks has posted a<a href="http://dsparks.wordpress.com/2010/10/18/k-means-redistricting/">n interesting piece about using statistical clustering to determine US Congressional districts</a>&nbsp;(h/t R-Bloggers). &nbsp;He uses k-means clustering, and then analyzes the "partisanship" of the resulting districts by assuming that districts with above-median population density are Democratic and those with below-median density are Republican (I'm not sure how good an assumption that is). &nbsp;The result is that you get much more reasonable looking districts than the crazy ones that politicians come up with, but the partisan balance doesn't seem to change (again, under the assumption that density=party). &nbsp;Here is an example of the map for Texas:<br /><br /><div class="separator" style="clear: both; text-align: center;"><a href="http://dsparks.files.wordpress.com/2010/10/tx-cluster-redistricting-partisanship.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="261" src="http://dsparks.files.wordpress.com/2010/10/tx-cluster-redistricting-partisanship.png" width="320" /></a></div><br />This is, of course, way too reasonable to actually be put into practice.