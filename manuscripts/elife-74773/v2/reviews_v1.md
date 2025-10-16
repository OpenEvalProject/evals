# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74773.sa1](https://doi.org/10.7554/eLife.74773.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Identification of electroporation sites in the complex lipid organization of the plasma membrane" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Qiang Cui as Reviewing Editor and José Faraldo-Gómez as Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Helgi I. Ingolfsson (Reviewer #2); Rumiana Dimova (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Additional discussion on the magnitude of voltage/electric field relative to typical experimental values and implications on the simulation results.

2) Analysis of simpler membranes to explicitly establish key factors that dictate poration kinetics and mechanism.

The reviewers also raise a number of issues related to the validation of the coarse-grained model, presentation of technical details and wording in certain discussions.

Reviewer #2 (Recommendations for the authors):

I realize validation of the coarse-grained results are likely out of scope for this already quite extensive manuscript (i.e. currently a number of the lipids in the complex membranes used don't have AA force field parameters and a in-between complex mixture would have to be used, etc, etc), therefore, I tried to suggest the validation as future directions. I do have a number of more specific questions and comments listed below:

One perception and/or wording comment. The brain is commonly thought to be enriched in polyunsaturated lipids. But you write that APM has more PU than the BPM:

L100 "Compared with BPM, APM has lower fraction of cholesterol, higher fraction of phosphatidylcholine (PC) lipids and higher fraction of monounsaturated (MU) and polyunsaturated (PU) lipids in the top leaflet." and

L391 "Compared with BPMs, APMs contain a smaller fraction of cholesterol and fully saturated lipids and a greater fraction of polyunsaturated lipids,"

This looks to be correct from how you defined the PU group (including also double unsaturated tails), compared to the 0, 1, 2, 3+ grouping in Figure 1A in Ingolfsson et al., 2017 (ref 41). Also, same paper Table 1, shows that on average (for the lipid fraction) there are more unsaturations per tail in the BPM than in the APM. Maybe some explanation or redefinition could prevent confusion for future readers.

Somewhat ill-defined wording comment. When first reading the manuscript, I got the sense that the Bayesina analysis was giving different result than the lipid feature/ML analysis. After reading it more in-depth I understand that they show different results on different "things" propensity/time vs spatial location and therefore are complementary. Maybe some rewording in the manuscript can make this clearer. I think my biggest stumbling block was "however" instead of something like additionally.

P1,L22, "learning. However, by" However ….

P2 "However, by analysing poration kinetics with Bayesian survival analysis we then show that"

I really like the analysis in section 2.4, but confused by one thing. It looks like form Figure 5 – sup. 1 and Figure 5B that the model is unable to capture the initial delay in pore formation time, the initial ~2.5 ns discussed later due to the bilayer expansion. Is this my misunderstanding or due to granularity of the binned data and/or lack of x-d offset term in β?

P16, L354 "Since membranes are practically volume-incompressible, the increase in area is directly related to a decrease in thickness.". Did you check this in your case? i.e. this is true for actual bilaye area, and projected area for very small flat bilayers but not larger undulating bilayers. I know both the APM and BPM were equilibrated with Z restrains to make them mostly flat but Ingolfsson et al., 2017 Figure 4A shows they are not totally flat and the BPM has more local undulations.

P16, L355 "Membrane thinning is expected to facilitate pore formation, as water molecules need to travel shorter distance when bridging the membrane.". Yes, but is it possible to utilize the power of the simulations and check for water bridging more directly? Here I realize this might be outside the scope of this manuscript, but have you considered looking at local bilayer properties such as "defects" (water penetration to the tails) or local min water distance across the bilayer (water dependent and not lipids dependent like the very related bilayer thickness)?

P9, L215+. I was quite confused reading that paragraph (L215 to L226), granted I am not an ML expert, but maybe some further explanation is in order. Also, could the questions of overfitting vs need for more data for higher accuracy be solved by increasing the number of depolarizable/hyperpolarizable simulation repeats? and/or leaving out some data for validation checks?

Reviewer #3 (Recommendations for the authors):

1. One aspect that remains unclear in this work relates to how universal the reported findings are and whether the large fraction of species present in the simulations is essential to the reported outcome, especially regarding the dependence on membrane elasticity. Indeed, to establish this correlation, it would have been interesting, using the selected approaches to first explore simpler membranes, and in particular, directly compare the poration probability and kinetics as a function of composition and membrane leaflet asymmetry. Membrane compositions with only a few representatives of the major classes of components would have been a good start as this would allow direct comparison to experimental results and would be helpful to resolve the role of the main actors involved.

2. The introduction (paragraph starting at line 70) explains that experimentally, pores in lipid membranes are difficult to assess. Work on giant unilamellar vesicles showing direct imaging of pores in lipid membranes suggests the opposite and should be referenced here (see e.g. DOI: 10.1529/biophysj.104.050310 and DOI: 10.1002/advs.202004068).

3. It will be good to explicitly discuss the following: The poration of the membranes in the simulations occurs within the first 15 nanoseconds, implying that the findings apply to pulses of high amplitude and nanosecond duration, but not necessarily to pulses of lower field strength and in the micro- or millisecond range duration (i.e. including conditions used in medical applications). A comment about this is due.

4. The authors indicate that such short poration times are needed to minimize lateral diffusion and allow mapping of local membrane features. Presumably, lipid diffusion and mixing which is substantial on longer times scales, might jeopardize the validity of the findings for longer pulse duration. Could the authors introduce a discussion also about this aspect?

5. The authors should explicitly specify the solution in which the membranes are simulated and the ionic strength.

6. The finding that gangliosides are quite important for poration (Figure 4B) is very interesting. The authors should discuss possible reasons and potential implications. Along these lines (even though not directly comparable), there has been a recent report on the poration of GM1-doped vesicles which exhibit much longer pore lifetimes compared to PC membranes (DOI: 10.1073/pnas.1722320115).

7. The authors should explicitly specify whether the size of the simulation box adjusts to accommodate the area of the pores in the membrane and whether more than one pore are simultaneously detected in one membrane patch. In line 379, the authors state that one can assume that Ai ≈Aj because all membranes have the same total area. Do they refer to the area before or after the application of the field? Could the authors further clarify the connection between the number of possible pore nucleation sites (as suggested on line 373) and the total area of the membranes?

8. Similarly, how does the pore size compare to the size of the data points displayed in Figure 2. In the caption of Figure 2, to avoid confusion, the authors should specify that all points correspond to the first poration event.

9. Figure 3 —figure supplement 3: The authors state that these quantities are computed from equation (1), however the caption above the graphs indicates that these two plots correspond to data where either no field was applied or a non-porating field was applied (i.e., situations where no pore is supposed to form in the membrane). How were these two diagrams plotted as they compare non porated with porated locations? Please clarify this in the caption.

10. The data for change in the membrane area as a function of the square of the nonporating field strength (Figure 5D and supplement 4) should be discussed in terms of the stretching elasticity modulus of the membranes. Typical stretching elasticity moduli of single-lipid membranes lie around 250 mN/m (see e.g. DOI: 10.1016/S0006-3495(00)76295-3). To claim the validity of the reported correlation between poration and mechanics, it has to be clarified, whether the applied simulation force fields can be used to correctly reflect the membrane elasticity. To address this (if not already reported for the selected force fields), the authors should measure the stretching elasticity for single-lipid membranes and compare with experimental values.

11. Line 270: "is fairly time independent" should be reformulated and justified by further discussion. As the authors refer to the values of β_i of Figure 5 – Supplement figure 2, the trend in this figure shows two main problems: (i) the values are positive for the whole time interval which is inconsistent with Figure 5 showing only negative values, and (ii) the values look actually time dependent as for instance APM-hyp shows a drop of 25% of its initial value on the time interval where its related probability density displayed Figure 5 A is non zero. Please discuss this issue.
