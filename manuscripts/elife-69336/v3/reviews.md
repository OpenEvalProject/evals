# Peer review - Round 1

Editors:
- Marc Lipsitch, Harvard TH Chan School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69336.sa1](https://doi.org/10.7554/eLife.69336.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This is a comprehensive effort to compile excess mortality data during the ongoing COVID-19 pandemic, resulting in a regularly updated, publicly available data set from which other investigators can depart to answer their own questions, and in which these investigators show the range of "excess" mortality, ranging from negative excess in countries with little COVID-19 to as much as 50% excess over normal rates in hard-hit countries. This also permits estimation of underreporting of deaths and its variation in space and time. This will be a highly valuable resource for many.

Decision letter after peer review:

Thank you for submitting your article "The World Mortality Dataset: Tracking excess mortality across countries during the COVID-19 pandemic" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Marc Lipsitch as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor, Miles Davenport. The following individuals involved in review of your submission have agreed to reveal their identity: Simonsen (Reviewer #2); Ayesha Mahmud (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. Work is not connected to the vast literature on the topic. The authors are out-of-field statisticians and seem unaware of the literature in this domain. They had generate a baseline of expected mortality based on past years time series data, as one would do when estimating excess mortality for influenza. In this way their approach is a bit similar to that used by Murray et al., (Murray, Lancet 2006) to estimate the 1918 pandemic excess mortality above an annual baseline of surrounding years for a number of countries. The authors should consider at least including a reference for excess mortality estimation for each of the past influenza virus pandemics, and ponder whether it is possible to do the same that was done in these analyses to create a baseline of expected deaths that did NOT include winter-seasonal epidemic diseases like influenza (see the collected works of Olson et al., Viboud et al., Chowell et al., Olson et al., Simonsen et al., for the pandemics of 1918, 1957, 1968 and 2009). See also the latest thinking on the problem of sorting out true excess deaths from the disappeared traffic accidents, increased mental health deaths, and other complications by IHME.

2. No attempt to correct baselines for seasonal influenza. The authors use past years and generate a baseline that includes mid-winter seasonal influenza mortality. By doing so, the excess mortality estimates in the present manuscript represent excess above what is normal in a season. Thus, as the authors comment on, the excess mortality estimates are affected by the too high baseline which includes mortality due to influenza, RSV and other respiratory viruses that are now largely not circulating during the COVID-19 pandemic. Particularly, the "disappeared" influenza burden in 2020-2021 results in a meaningful underestimation of the true COVID-19 excess mortality. This problem of removing seasonal influenza from the baseline has actually been worked out by epidemiologists using various statistical approaches (sometimes harmonic terms, sometimes using influenza virus data from the WHO as predictors) in the field of epidemiology the literature mentioned above, but the entire literature of excess mortality estimation is missing from the reference list. One that I am very familiar with is Simonsen et al., Plos Med 2014 – but there are many many more similar published papers computing excess mortality for seasonal and recent pandemic influenza out there (look for Viboud, Chowell, Goldstein, Paget, Olson…..). I suggest you simply discuss this situation, and make reference to this – plus suggest others to work out ways to remove influenza from the baseline, for example incorporate WHOs seasonal influenza timeseries database data (FluNet.org) in the excess mortality regression models (to identify and remove excess mortality during influenza periods).

3. Varying COVID-19 study time for different countries. Another problem with the way they report the excess mortality is in the difference in follow-up time. Some countries have data up to March 2021, while others only until last summer. This should be dealt with in the estimates, for example by comparing countries with complete year 2000 data. It probably cannot be helped that some countries publish their data late, but the authors should highlight these issues of comparison between countries in the text.

4. About the finding of a 1.6x higher excess mortality than reported deaths. It seems important to say that this is a finding for countries with national vital statistics in near-real time, so things may be very different in countries where such data to not exist.

5. Figure 4. Can you explain the time shift between the reported and excess deaths in the United States? Must be a data issue. Also, would be better to choose line colors or width so that one can distinguish the two in black and white.

6. Please expand on the interpretation of excess deaths. From a causal perspective, the notion of excess deaths is:

Observed deaths in COVID period =

Expected deaths in COVID period (a) –

Deaths averted due to COVID (eg less flu due to NPIs, less traffic death, ) (b)+

Deaths directly caused by COVID (ie in people who were infected) (c)+

Deaths indirectly caused by COVID (starvation from lockdown, untreated cancer) (d)+

Net death from confounders (other events that were particular to that time period and caused or prevented deaths -- eg wars) (e)

+ Random variation.

The main thing I would like to see is more contextualization of the "undercount" to note something like this conceptual structure, explain what should make us think that the very few examples of (e) that are in the analysis really are the main ones, and perhaps some seasonal comparisons of the undercounts so that plausible hypotheses can be proposed for which factors are at play.

7) Is it possible to do the age-standardization for countries in the top 10 in Figure 3. For example, the countries in the bottom left panel to see if the ordering changes?

8) The timing of outbreaks in different countries will affect the estimate of excess mortality. You note, "We summed the excess mortality estimates across all weeks starting from the week t1 when the country reported its first COVID-19 death". First, how do we account for changes in reporting as an outbreak progresses in a country? Second, for countries that have a later introduction of the outbreak, and/or see a later peak relative to other countries (for example, India), then they will automatically have a smaller estimate of excess death because of right censoring of the data. How is this accounted for?

9) It would be good to add some discussion on how your excess mortality estimates compare to the many estimates available in the literature.

10) Figure 2 needs x axis labels.

11) A lot of the results are presented in a comparative framework but it's very difficult to compare excess mortality rates across different populations. Perhaps reframing some of this as a way to assess a country's own burden compared to its baseline rather than comparing across countries might be helpful.

12) Some discussion on why Peru seems to be such an outlier would be helpful (i.e. Figure 3).

13) Section 2.2 describes some adjustments (for e.g. for Ireland and Sweden). Some sensitivity analyses would be helpful. For example. the redistribution of deaths for Sweden ignores seasonality. What is the consequence of that assumption?

Reviewer #1 (Recommendations for the authors):

I found the use of t statistics confusing as t has another meaning (time) and while this may be standard in some fields it is not in epidemiology (presenting the t statistic rather than the p value)

Reviewer #2 (Recommendations for the authors):

Well done, nice paper. Alarming conclusion. Great resource for the field. A few things to fix.

Reviewer #3 (Recommendations for the authors):

Thanks to the authors for this nice paper, and for collecting and making all the data publicly available. Some comments and suggestions (in no particular order) are below:

1) Is it possible to do the age-standardization for countries in the top 10 in Figure 3. For example, the countries in the bottom left panel to see if the ordering changes?

2) The timing of outbreaks in different countries will affect the estimate of excess mortality. You note, "We summed the excess mortality estimates across all weeks starting from the week t1 when the country reported its first COVID-19 death". First, how do we account for changes in reporting as an outbreak progresses in a country? Second, for countries that have a later introduction of the outbreak, and/or see a later peak relative to other countries (for example, India), then they will automatically have a smaller estimate of excess death because of right censoring of the data. How is this accounted for?

3) It would be good to add some discussion on how your excess mortality estimates compare to the many estimates available in the literature.

4) Figure 2 needs x axis labels.

5) I think a lot of the results are presented in a comparative framework but it's very difficult to compare excess mortality rates across different populations. Perhaps reframing some of this as a way to assess a country's own burden compared to its baseline rather than comparing across countries might be helpful.

6) Some discussion on why Peru seems to be such an outlier would be helpful (i.e. Figure 3).

7) Section 2.2 describes some adjustments (for e.g. for Ireland and Sweden). Some sensitivity analyses would be helpful. For eg. the redistribution of deaths for Sweden ignores seasonality. What is the consequence of that assumption?
