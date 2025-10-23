# Peer review - Round 1

Editors:
- Leslie C Griffith, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41412.020](https://doi.org/10.7554/eLife.41412.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Subunit exchange enhances information retention by CaMKII in dendritic spines" for consideration by eLife. Your article has been reviewed by Gary Westbrook as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous. The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Summary:

The main goal of the work is to assess the impact on the stability of CaMKII phosphorylation states (a proposed switch for memory storage) of CaMKII subunit exchange, both between holoenzymes within the postsynaptic density (PSD) and of such exchange between the PSD and the spine itself. The question is a relevant one on an important topic and the simulations appear to be carried out with due care using a reasonable model of the biochemical pathways involved.

Essential revisions:

1) In many places the results are demonstrated by simulation, but little intuition is provided as to why these results occur. For example, any differences in behavior of prior models should be explained in terms of a causal link between which parameters are altered, or which additional reactions are in place, and how they impact the prior models. Some of the results (increased stability) are to be expected, as exchange between holoenzymes allows the majority to rescue the state of any individual that has by chance fluctuated away from the preferred state. Such intuition should be stated clearly.

2) One important, specific criticism is on the discussion of a dual decay rate of the CaMKII activation. Lack of fit to a single exponential does not provide evidence for a dual decay rate process, by which I think you mean a good fit to a double exponential. If you wish to make a positive statement about the type of decay process (rather than the currently justified negative statement-lack of fit to a single exponential) please fit with other functions and show the dual exponential is significantly better than other choices, using a criterion like AIC. Furthermore, in the Discussion section, you relate your non-exponential finding to a fractional power-law decay. However, I believe that both the dual-exponential and the fractional power-law functions decay more rapidly at short time-scales and more slowly at long time-scales than a single exponential. Yet your "best fit" exponential shows the error to be in the opposite direction. I think these discussions about power-laws and/or dual decay should be removed or reframed, unless a clear good fit to one of these other functions can be demonstrated.

3) The impact statement is not quite accurate. The authors have not shown, as far as I can see, that subunit exchange generates diverse timescales of information storage (and to be honest, it is unclear what "diverse timescales of information storage" really means). First, the decay of activity may not be a dual exponential, and second, it is unclear that subunit exchange is essential to produce the types of decay observed, given the large number of parameters in the system.

4) There were questions regarding the activation state of CaMKII and how some of the authors' parameters are defined. The most surprising result was that there is somehow an increase in "active" CaMKII (which one infers to mean Thr286 phosphorylated CaMKII) immediately in the presence of subunit exchange. When previously described, subunit exchange enhanced CaMKII activation at later times but did not affect early time points. To fully understand this, it is necessary for the authors to clearly define the following: (1) What is 'active' CaMKII, (2) what is the rate they are using for CaMKII activation (again assuming this to mean rate of Thr286phosphorylation) (3) What is the relationship between this initial rate of phosphorylation and subunit exchange. Some of this information is in the manuscript, but I think it needs to be more explicitly stated.

5) Figure 1C, where did these values/frequencies arise from?

6) Why was there no CaMKII activity in the absence of exchange (subsection “Subunit exchange facilitates the spread of CaMKII activity”)? Initial CaMKII activation should not be so affected by subunit exchange as this is actually faster than exchange itself.

7) The data in Figure 4B and 4C -> what is the explanation for the discrepancy in the affect on activity at 2 subunit exchange rates between 4B and 4C? (i.e. there is a large effect at 80 nM ca but zero effect at 120 nM ca).

8) Comments on the model: The assumption that both subunits within a vertical dimer are phosphorylated and dephosphorylated together is a large assumption – meaning that there is no direct evidence for this. I think this is OK to do, but it should be stated in the text as well.

9) Phosphorylation of CaMKII is mentioned many times, but it's never specified that it is Thr286phosphorylation. This should be made clear.

10) It is true that the rate of exchange in the cell is not known (subsection “Subunit exchange”). However, from in vitro experiments in Stratton et al., 2014; at ~4 μM CaMKII subunit concentration, the half-life of exchange is roughly 15 minutes. The rate was shown to increase at higher concentrations of CaMKII – so one could potentially extrapolate to the concentrations in the neuron (estimated to be roughly 100 μM in the spine).

11) Are newly synthesized holoenzymes considered in the model?
