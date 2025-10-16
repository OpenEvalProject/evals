# Peer review - Round 1

Editors:
- Peter Rodgers, eLife , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21393.017](https://doi.org/10.7554/eLife.21393.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Decoupling of the Minority PhD Talent Pool & Assistant Professor Hiring in Medical School Basic Science Departments" to eLife for consideration as a Feature Article. Your article has been reviewed by two peer reviewers and the eLife Features Editor, and this decision letter has been compiled to help you prepare a revised submission.

Summary:

This paper attempts to examine issues related to the hiring and retention of PhD underrepresented minorities (URM) in assistant professor positions at academic medical centers. It uses a system dynamics (SD) model to assess expectations of how many PhD URM individuals we should expect to see entering assistant professor positions. While others (Myers & Husbands-Fealing, 2012; Heggeness et al. 2016) have examined issues of representation along the 'pipeline,' this work expands on those efforts by examining specifically issues related to hiring and the flow and stock of assistant professors in academic medicine centers and, specifically, URM hiring. Additionally, the extention to an SD model is a unique analysis for this population and with this data.

Essential revisions:

1) This might be a discipline issue, but I find it confusing that in the body of the paper and in the figures, the data source is not cited! It is only cited in the back as an appendix of sorts. Data sources should be cited throughout the text and at the bottom of each figure.

2) Equation documentation should improve. In your appendix you should use more conventional approaches for model documentation than simple copy-paste of Vensim formula. Also, report all your parameters in a table with proper references (fine if it appears in the Appendix). For model documentation example, see other SD works such as Ghaffarzadegan, Hawley and Desai, 2014.

3) Definitions of subgroups need to be more precise. Instead of saying "including[…]" or "(i.e. white)," precise definitions should be clearly articulated within the paper of exactly how subgroups are defined.

4) One of the weaknesses of an SD model is that you are not able to account for individual agents' behavior, like in agent-based models. Lots of changes in the external environment (e.g. changes in funding streams, policies, and alternative opportunities) have the potential to influence an individual agent's actions in ways that are not necessarily linear and not accounted for in the model the authors present.

5) While the authors acknowledge the issue of postdocs in the supporting documentation, they do not even mention postdocs in the main paper. The reality is that hardly anyone transitions directly from PhD receipt to an assistant professor position, and the postdoc experience is extremely diverse. What if the differences the authors are seeing here are not a result of stalled entrance into the assistant professor position, but rather stalled entrance into a postdoc that will make the individual attractive for an assistant professor position. This dilemma and absence in their model must, at a minimum, be discussed in the body of the paper. Ideally, the authors would be able to incorporate some assumptions about the postdoc phase into their model.

6) The authors have no data on who is applying for assistant professor positions (as they acknowledge in the third paragraph of the Discussion). Therefore, there is no way to really claim, as they do, that if institutions increased their efforts to hire more URM, this would increase diversity in the assistant professor pool.

7) In the main model there is no drop-out from the pool of people in the market (that is, people stay in the market forever). I see that in your sensitivity analysis you report that you have conducted an analysis of effect of drop-out from the pool of people in the market. Very good, but I would argue that this should be in the main model. You simulate the model until 2080, and by then the whole population has retired and many have died! So, simply replace the results of your sensitivity analysis as the main analysis. I understand that this might not affect the results, but it is a better modeling practice.

8) The simulation period of 55 years in future is simply too long. And the assumption that 73% of PhD graduates will be URM feels unrealistic unless you provide evidence (if 73% of a population are minorities, then they are ORM: over-represented minorities!). I suggest the authors to simulate for the next 1-2 decades; there are many things that can happen until 2080 which your model cannot predict and are out of the boundary of your analysis.

9) One may argue that the reason "URM Faculty Aspire P0" is much smaller than the "WR Faculty Aspire P0" is that you are assuming that hiring in faculty positions is proportional to population of the pools. URM might be weaker in the market or be discriminated. From a modeling standpoint, your model has two degrees of freedom, if you assume there is no "weight" toward hiring WR relative to URM, you end up with much higher "WR Faculty Aspire P0" anyway. I think the best way, but difficult, is to provide some references for this argument (that there is less faculty aspiration among URM). The easier way is to clarify that you are aware of this assumption and discuss its implications in your policy recommendation. You may need to modify your language throughout the paper too.
