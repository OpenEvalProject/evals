# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93050.sa0](https://doi.org/10.7554/eLife.93050.sa0)

This valuable study develops the Region of Attainable Redaction (ROAR), which quantifies the potential sensitivity of conclusions due to omitted data in two-arm clinical trials and studies of associations between dichotomous outcomes and exposures. The idea is supported by solid numerical examples and an application to a large meta-analysis. The concept of ROAR is a useful reminder of the fragility of some clinical findings.


---

# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93050.sa1](https://doi.org/10.7554/eLife.93050.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Region of Attainable Redaction, an extension of Ellipse of Insignificance analysis for gauging impacts of data redaction in dichotomous outcome trials" for consideration by eLife. I apologize for the long delay in reviewing your article. I had a great deal of trouble identifying reviewers who were willing and available to review. I (Phil) have reviewed your article as the Reviewing Editor, and the evaluation has been overseen Detlef Weigel as the Senior Editor.

Please see my recommendations below to help you prepare a revised submission.

Reviewer #1 (Recommendations for the authors):

In this article, Dr. Grimes develops the Region of Attainable Redaction (ROAR), which is a simple metric for the potential sensitivity of reported findings in two-arm randomized clinical trials due to omitted data. The idea of ROAR is to quantify the minimum number of hypothetical observations that – had they existed but not been reported – would have changed a statistically significant finding to a non-statistically significant finding. The author helpfully includes an easy-to-use online app and, for those interested, computer code. The strengths of this work include its ease of use and its intuitive meaning. Weaknesses include its limited scope of application, as discussed below.

The method is nominally applicable to any analysis of a binary outcome with two exposures in which a chi-squared test is appropriate. The intended use is for randomized clinical trials, but the utility of ROAR seems limited here given the expected rigor and reporting requirements for such studies, including preregistration, multiple levels of scientific and ethical review, and reporting requirements. Given this, it seems unlikely that the published analysis of a clinical trial could successfully "hide" observations. Although the Discussion notes that it is applicable to cohort and ecological studies, presumably any such observational study would adjust for other predictors and potential confounders in addition to the exposure of interest. Thus, it is not clear how applicable the concept of ROAR, which is an unadjusted analysis, is for such studies.

Dr. Grimes also applies ROAR to a large meta-analysis of vitamin D supplementation (exposure) and cancer mortality (outcome). This application seems more appropriate than those mentioned above. The key finding is that, in a meta-analysis of more than 39000 patients with 865 deaths, the statistical significance of the of 0.85 estimated risk ratio would be lost had there been just 14 additional (unreported) subjects in the exposure arm who had the outcome. Driving this surprising result is the low baseline risk of mortality in either group. For more prevalent events, the number would be much greater than 14.

A final weakness is in the author's claim in the Discussion that "[ROAR] can be employed…to detect the fingerprints of questionable research practices and even research fraud." This claim is surprising and not substantiated in the article, as ROAR is presented as a sensitivity analysis and not a diagnostic tool.

– Is there utility for single trials which require rigorous definitions and reporting of enrolled, eligible, evaluable patients? It seems unlikely that subjects could simply be redacted from a particular trial.

– Why do the regions in Figures 1 and 2 have upper limits? Does this correspond to a switching of significance in the other direction?

– Tables 2 and 3 are probably not of interest to most eLife readers and could probably be moved to a supplement.

– The notation should be made clearer: a, b, c, and d are the reported data, whereas x and y are the hypothetical redacted data. I don't think this is explicitly stated anywhere. Also, I don't think n is defined anywhere, presumably, it is a+b+c+d.

– In the second sentence of the second paragraph of the methods, I think the grammar needs to be clarified to reflect the hypothetical nature of the statement. For example, I think instead of '…are jettisoned…' the past perfect form '…had been jettisoned…' would be more appropriate. But more than just this needs to be changed.

– In section "ROAR derivation and FOCK vector", fifth line down: the e in 'ye' should be subscripted.

– In section "Results", in points 1 and 2: it is written "p < 0039" presumably there is missing a decimal somewhere. And this should be an equality not an inequality.

– In section Introduction, the sentence "EOI analysis in robust and analytical, suitable not only for RCT analysis but for observational trials, cohort studies, and general preclinical work". Should be changed to "…is robust and analytical".

– In Table 4, the percentages are not clear to me. E.g. Experimental redaction tolerance 9.51%(10 subjects). I thought the tolerance would be 10/110 or 9.1%.

– I think I had a similar comment on the EOI paper, but the FOCK coordinates seem like they should be integer-valued in order to be clinically applicable since you cannot redact a fraction of an observation. Put differently, I think that the identification of x_e and y_e and r_min should comprise three steps: (i) first identify x_e* and y_e*, the real-valued solutions to g(x,y)=0 and then (ii) identify (x_e, y_e) as the integer-valued coordinates that are closest to x_e* and y_e* and still in the ROAR. Then (iii) r_min = x_e + y_e. For example, in the bottom half of table 4, you cannot redact a fraction of an observation,

– Can ROAR be used in case-control studies – if so what special considerations would there need to be? And what about other estimands besides a risk ratio? Can you add some discussion about this?
