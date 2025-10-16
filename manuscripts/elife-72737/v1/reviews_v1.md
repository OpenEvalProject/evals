# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72737.sa1](https://doi.org/10.7554/eLife.72737.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Measuring Disagreement in Science" to eLife for consideration as a Feature Article. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by the eLife Features Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Chaomei Chen; Iana Atanassova.

The reviewers and editors have discussed the reviews and we have drafted this decision letter to help you prepare a revised submission.

Summary:

The paper focuses on a study of citation instances associated with disagreements in scientific publications. Qualified citation instances (citances) are identified based on two sets of terms: signal terms and filter terms. Signal terms indicate some forms of disagreement such as controversies and debates, whereas filter terms characterize common elements of scientific publications such as studies, ideas, methods, and results. Citances are validated by two coders from the authors. ScienceDirect articles are matched to the Web of Science articles so that matched articles can be classified into 800+ meso-level fields. The distribution and the rate of appearances of valid citances are presented among other quantitative and qualitative analyses.

The topic is important, and one important strength of the paper is the size of the dataset that is processed (over 4M papers in full text) and also the fact that the papers have been already classified into disciplinary fields and 817 meso-level fields by the previous work of the authors. This constitutes a standpoint that allows to perform large scale analyses and draw conclusions for the different disciplines.

The background of the work is presented generally well, although more detailed comparisons and differentiations are desirable to position the study in the literature in terms of the scope and depth with reference to relevant works. The method and the execution of the study is generally in good order. On the other hand, the presentation, especially some of the interpretations and some of the claims, needs attention in a number of places.

Essential revisions:

1) The title needs attention for a number of reasons. "Measuring Disagreement in Science" is an overstatement because, as the authors state in the Discussion section, their study is rather "an attempt at measuring" or "a proposal for a method of measurement".

Also, "scientific literature" would be more appropriate than "science" because the study is limited to scientific literature and other forms of scientific inquiries are beyond the scope of the study.

Similarly, "disagreement in citation contexts" would be more appropriate than "disagreement" because many other forms of disagreement are outside the scope of the study.

2) More details are needed in some places to allow other researchers to replicate the procedure. For example:

Line 138: Why was the Crossref API used to identify articles when the ScienceDirect database is hosted at CWTS?

Line 152: Why are these meso-level fields used? Are there alternatives?

Line 193: What are the sources of the preliminary signal terms? What are the specific steps for obtaining synonyms, e.g., using any standard and widely available resources such as WordNet?

Line 213. "filter terms within a four-word window of the signal" This expression seems a bit of ambiguous. Does it mean a filter term must be found no more than two words away from the signal term as illustrated by the following scenarios?

Some four-word windows of {signal}:

{filter} word1 word2 {signal}

{signal} word1 word2 {filter}

Presumably such windows do not contain sentence boundaries, e.g., "… word1 {filter}. {signal} word2 …" (since the citances are single sentences, correct?). If that is the case, it should be helpful if you can clarify this explicitly.

Line 222: How exactly was the selection of citances randomized?

3) The authors have cleverly shifted the issue of negative citation to the broader concept of disagreement. They have analyzed a corpus of sentences that all contain a citation, and their aim is to capture both paper-level and community-level disagreement. However, the example of community-level disagreement given Line 188 is not necessarily an instance of disagreement between the cited works/authors, as the authors state it. It might be (it is, actually, most of the times) a list of works that do mention the existence of a debate/controversy about a topic. I think it is a typical example of a citing author agreeing with the cited authors that there is disagreement on a topic ( = agreeing on disagreement). Choosing sentences with citations and cue terms marking disagreement does not in any way guarantee that the authors are expressing disagreement with the works they cite, but merely that there is disagreement in the literature on a topic at a given time. One may therefore ask what is the point of restricting the analysis to sentences with citations and not addressing the problem from the point of view of citation polarity or function, especially if the aim is to group together paper-level and community-level disagreement. I think the citations have the same function here as filter terms, but cannot be seen as the targets of the disagreement, as they are indeed line 373 and in some sections of the Supporting Information part.

4) I understand that precision is the priority in this study. Nevertheless, some equally useful vocabularies are not included in the list in Table 2. For example, commonly used terms that are missing from the list for 'studies' include research, investigation, inquiry, just to name a few. A more extensive list would certainly improve the hit rate. Similarly, some important omissions from the list for 'ideas' include concept and claim.

Please either redo this part of the analysis with more terms, or discuss how this is a limitation of the study.

5) Related to point 4, a quick review of the available dataset and the limitations provided by the authors show that the precision may not be good either. The authors claim that false positives are marginal. They may be right. But when it comes to making analyses at the journal level, this can distort the result somewhat. I will take just one example for lack of space: Figure 3, Soc and Hum, Electoral studies (which is emphasized in the figure) -> with a manual check, I identify 37% of the citations as false positives for this journal. The use of syntactic parsing could have filtered out the false positives from all the examples citing "presidential debates" for example. The problem is that we don't know the amount of false positives at all.

6) Is there an underlying principle that leads to the distinction between the paper- and community-level disagreements?

7) Line 260: Percent valid is defined as the percentage of citances labeled as valid by both coders.

This seems very subjective. If different individuals were chosen as the coders, then we may end up with possibly quite different results because it is quite conceivable that we can find another pair of coders who may make different judgements. Are there alternatives to make this part of the procedure more systematic and reproducible?

8) Line 402-403: prioritize precision … relatively rare.

If the methodology prioritizes precision, then your results cannot be used to support a conclusion that it is relatively rare because one of the many possible consequences of your priority choice is to lower the rate of appearances of qualified instances. If you expand the signal terms and filter terms, then the rate is likely to increase.

9) Line 420: a field is increasingly becoming consensual … (Smolin, 2007).

This interpretation is not particularly convincing. A consensual field is a dying field unless it finds new driving forces. It is essential to maintain the healthy growth of a field as well as to the career and social dynamics of individual researchers who choose the work in the field. On the other hand, consensus at lower levels such as topic levels can be reached without fundamentally damaging the growth of a field. I wonder what you would see if you normalize instances by article and/or by all citances (including non-disagreement citances).

10) Line 474. The framework needs more clarification. For example, how is it related to previous works on negations and uncertainties? For example, manually crafted signal terms vs. black-box approaches, especially for potentially subsequent expansions, coder-based validity vs information theoretic approaches, citer-citee disagreement vs incommensurable paradigms (one may never cite the other from an incommensurable paradigm), and the prevalence of disagreements expressed outside citances.

11) Please revise the manuscript at appropriate places to address the following points:

i) the study was restricted to English-language articles.

ii) the absence of a citation can be an even stronger marker of disagreement than a negative citation.

iii) disagreements in science can take place in other venues, such as conferences, and in other article types (such as book reviews).
