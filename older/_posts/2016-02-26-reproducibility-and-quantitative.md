---
date: '2016-02-26T07:10:00.001-08:00'
description: ''
published: true
slug: 2016-02-26-reproducibility-and-quantitative
tags:
- http://schemas.google.com/blogger/2008/kind#post
- legacy-blogger
time_to_read: 5
title: Reproducibility and quantitative training in psychology
---

*This was originally posted on blogger [here](http://www.russpoldrack.org/2016/02/reproducibility-and-quantitative.html)*.

We had a great Town Hall Meeting of our department earlier this week, which was focused on issues around reproducibility, which <a href="http://babieslearninglanguage.blogspot.com/2016/02/town-hall-on-methodological-issues.html">Mike Frank has already discussed in his blog</a>. &nbsp;A number of the questions that were raised by both faculty and graduate students centered around training, and this has gotten many of us thinking about how we should update our quantitive training to address these concerns. &nbsp;Currently the graduate statistics course is fairly standard, covering basic topics in probability and statistics including basic probability theory, sampling distributions, null hypothesis testing, general(ized) linear models (regression, ANOVA), and mixed models, with exercises done primarily using R. &nbsp;While many of these topics remain essential for psychologists and neuroscientists, it's equally clear that there are a number of other topics that we might want to cover that are highly relevant to issues of reproducibility:<br /><br /><ul><li>the statistics of reproducibility (e.g., implications of power for predictive validity; <a href="http://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124">Ioannidis, 2005</a>)</li><li>Bayesian estimation and inference</li><li>bias/variance tradeoffs and regularization</li><li>generalization and cross-validation</li><li>model-fitting and model comparison</li></ul><div>There are also a number of topics that are clearly related to reproducibility but fall more squarely under the topic of "software hygiene":</div><div><ul><li>data management</li><li>code validation and testing</li><li>version control</li><li>reproducible workflows (e.g., virtualization/containerization)</li><li>literate programming</li></ul><div>I would love to hear your thoughts about what a 21st century graduate statistics course in psychology/neuroscience should cover- please leave comments below!</div></div>

---

## 15 comments captured from [original post](http://www.russpoldrack.org/2016/02/reproducibility-and-quantitative.html) on Blogger

**Dr Cyril Pernet said on 2016-02-26**

Literate programming is an interesting thing - it doesn't need to be taught, it can be demonstrated. For instance, make a R script to demonstrate the logic of linear modeling (http://www.sbirc.ed.ac.uk/cyril/glm/GLM_lectures.html). If we start teaching such that the lectures are literate programming (rather than boring ppt), students get use to<br />- express/convert a though in a bit of code<br />- relates code to maths (seriously, density functions, integrals, kernels etc are easier to understand using a computer - http://www.ted.com/talks/conrad_wolfram_teaching_kids_real_math_with_computers?language=en)<br />- become accustom to literate programming<br /><br />Maybe instead of an essay, we should ask to express and solved a problem that way. I don't need to convince you that sharing data and code is the only way .. and teaching student using literate programming make them use to do that (I think)

**Song said on 2016-02-26**

Am planning course specifically in open science/reproducible research right now at Karolinska Institutet. Have proposed as learning objectives that students should be able to: <br />• Account for reproducibility problems in research because of issues such as small sample sizes, bias, and incomprehensive methods reporting<br />• Recognize questionable research practices, discuss their prevalence, identify methods to discourage their use<br />• Find and apply field-specific guidelines for reporting research with different designs<br />• Preregister research protocols and assess others’ preregistered research protocols<br />• Identify suitable repositories and publish scientific works using self-archiving<br />• Annotate, describe, anonymize, and openly publish scientific data and analysis code<br />• Find, acquire, and analyse data published openly in different formats<br />• Integrate and accumulate data across studies (meta-analysis)<br /><br />*Sorry for delete and re-post, trying to sign with my name. /G Nilsonne

**Chris Gorgolewski said on 2016-02-26**

While in grad school I tough (together with +Mike Hull) a 12 week class called &quot;Introduction to Research Computing&quot;. We spoke about practical software skills such as python programming, version control, automatic figure generation, MATLAB code optimization and others.<br /><br />If I were to teach it now I would try to add something about reproducibility, notebooks, and pitfals of p-hacking.<br /><br />https://github.com/chrisfilo/IntroductionToResearchComputing

**Michael Frank said on 2016-02-26**

This is great, Russ. I think it might be helpful to have students begin grad school with an orientation to some of the computing concepts, and then move towards methodological and statistical concepts along the way. Imagine a first-year sequence that walked students through how to set up a project and the appropriate environment for managing data/analysis/writeup, taught them how to code up the experiment and run it, and then introduced the statistical techniques necessary for analysis. This sequence would proceeding in parallel with their development of a first-year project, so they'd presumably get both course projects and research experience and have an opportunity to apply the same toolset to both...

**Unknown said on 2016-02-26**

I agree with Cyril. I see the topics listed as &quot;software hygiene&quot; as a vehicle to teaching the other topics; however,  that might be a product of having to learn it on-the-fly during/post graduate training. <br /><br />I think putting students in practical situations is like immersion learning for these issues.  &quot;Your regression model is highly significant? Show me it can generalize to an individual that isn't included in the model. How? Use cross-validation. It doesn't work? Why?&quot;  <br /><br />In my view, researchers should all be knowledgeable of these techniques and issues, but many choose to collaborate with &quot;data scientists&quot; or statisticians, who have all the technical and math expertise but often know little about how to appropriately use the data.  It seems clear that powerpoint-laden lectures divulging theory are not enough, but how do you determine how much  programming should be taught concurrent to stats?  I think the 21st century shift in data practices and communication demand these skills, but they may not belong in a graduate stats-specific course.  I found that there were highly variable level of programming skill in my graduate cohort, so it would likely slow progress down quite a bit.  Specifically, the statistics of reproducibility, generalization/cross-validation, model-fitting, &amp; and model comparison would be my top votes for inclusion in a stats focused course.  That being said, I think it would be a really good idea to include the programming aspects in a pre-requisite, complimentary, or supplementary type course. <br /><br /><br /><br />

**Unknown said on 2016-02-26**

I work a few of those topics into my course on regression. There are a few points in general regression topics where you can talk about bias/variance tradeoffs naturally. We also deal with differences between structural models and predictive models, and bring up how you might make different choices (and have different tests) depending on your goal. At the end, we have a whole day devoted to not making mistakes, why coding is better than spreadsheets, etc. So, I think it's possible to fold those topics into your current courses for the most part. It just takes an effort to re-tailor those topics to practices now (vs ones our ancestors were obsessed with like sequential F tests).<br /><br />Updating this further based on Cyril's point: I also have R code for every lecture that goes over multiple ways of calculating key statistics (not using lm's output) such as using algebraic formulas, calculating solely from the variance-covariance matrix, matrix algebra, etc. This serves two goals of having them (1) learn some computational skills and (2) understand the formulas and principles by working with them. <br /><br />So it is definitely possible to teach almost everything off that list be folding into the current classes.<br /><br />Fox's book &quot;Applied Regression Analysis and Generalized Linear Models&quot; makes the incorporation of these concepts somewhat seamless, in my opinion. His chapters on Robust Regression, Bootstrapping, and Model Selection, Averaging, and Validation are a gold mine for these basic concepts that other books don't have (or don't do as well)

**david said on 2016-02-26**

Good paper on &quot;software hygiene.&quot; Something to consider for assigned readings:<br /><br />http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf

**tal said on 2016-02-26**

When I was at Colorado, I taught a graduate project-building course that amounted to something like &quot;scientific computing for psychologists&quot;. I think the students liked it, and some very nice projects came out of it... but the main limitation from my perspective was the huge variability in technical ability coming into the course. Some students were basically software developers, and others had never seen for-loops before. I agree with Michael Frank that the optimal approach would require multiple courses.<br /><br />My preferred sequence would probably be: (i) Programming for psychologists (which students can test out of), which, in addition to standard stuff (data types, control structures, etc.), would cover programming concepts and applications relevant to psychologists (e.g., a lot of text processing, numerical computing, and stimulus presentation, not much about algorithms, systems, etc.). (ii) Scientific computing for psychologists, which would assume basic programming ability, and focus on all the stuff you're talking about here (version control, interactive notebooks, reproducibility, etc.), and get students to a point where they're managing all their data/analysis/code properly. Then (iii) Project-building, where students carry out technically-oriented projects that focus on their own particular area of research. The last course wouldn't be mandatory, but perhaps strongly encouraged.<br /><br />Of course this leave aside the question of what to do with conventional stats and/or research methods. Having 4 required methods courses seems like a bit much, but I'm not sure how much one could really compress things down. The reality is that there's just more to learn these days, if you don't already have a strong technical background. (So maybe a more realistic solution is to only accept students who come in with many of these skills.)

**practiCal fMRI said on 2016-02-26**

Hi Russ, where do the issues of experimental design and systematic errors come in? Power is important but won't fix a bad study design or confounding variables.

**Russ Poldrack said on 2016-02-26**

Good point - some of the issues around study design would presumably be discussed in courses that are more area-specific, since they will often vary across different research domains, though certainly there are many issues (e.g., confounding) that are general and should probably be discussed here.

**MD said on 2016-02-26**

In my own stats course, I've been covering issues related to reproducibility and questionable research practices for about 5 years. Each year, I give our incoming graduate students a questionnaire about scientific practices and the crisis of confidence. What I find most striking, is that (a) most students (~60%-80% in any given year) report that they've worked in labs where researchers engaged in optional stopping, flexibility of analysis, and HARKing, and (b) almost none of them have heard of the crisis of confidence or issues surrounding reproducibility prior to coming to graduate school. Graduate school shouldn't be their first introduction. In case anyone is wondering, our students come from a variety of institutions ranging from small liberal arts colleges to Ivy league and equivalent research institutions.

**Unknown said on 2016-02-26**

Not mentioned above, but very much needed, is training in tools for building theories. Relatedly, psychology would benefit from a priori theory building (and analysis). And places to publish this sort of work. -- Pat Shafto

**Unknown said on 2016-02-26**

Hi Russ, interesting ideas. My own take is that the most important thing is to help students think more critically about data analysis. In a way, the goal would be to teach statistics not as a set of disparate techniques (ANOVA, regression, etc.) but as &quot;statistical modeling&quot;, a way to model data so that we can understand patterns and structure in data. This is all very natural if one embraces a Bayesian mindset, and different analyses map to different ways of modeling the data. I'm reading a book right now that might be the best book ever in terms of basic exposition and didactical approach to this: http://xcelab.net/rm/statistical-rethinking/ The book is so well written that I've enjoyed reading even Chapter 1! It goes without saying that students need to learn to program; if not in R (it's rather cryptic), some version of Python, or even a probabilistic language like Stan.

**Brad Wyble said on 2016-02-26**

I think it's a shame that custom permutation tests aren't taught routinely in grad stats.  They can be written easily in any language, and are so flexible that they can sometimes find a way to test for differences that traditional approaches aren't well suited for.

**v said on 2016-02-26**

There should be a required entry level course for all new graduate students that covers the basics, and then a higher department (eg, research computing) should offer regular advising and office hours for all students, faculty, and staff.

