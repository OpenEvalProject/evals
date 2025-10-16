# Peer review - Round 1

Editors:
- Sandeep Krishna, https://ror.org/03gf8rp76 National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79919.sa0](https://doi.org/10.7554/eLife.79919.sa0)

This paper develops evolutionary simulations to identify the type of molecular networks that can give rise to size control. The authors propose an evolutionary framework to find which factors select for particular mechanisms in cell size control. They show that the evolution of a specific cell size control mechanism is dependent on the cell cycle structure.


---

# Peer review - Round 1

Editors:
- Sandeep Krishna, https://ror.org/03gf8rp76 National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79919.sa1](https://doi.org/10.7554/eLife.79919.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Evolution of cell size control is canalized towards adders or sizers by cell cycle structure and selective pressures" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Kabir Husain (Reviewer #1); Shiladitya Banerjee (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers liked many aspects of the manuscript but have suggested a number of revisions, which include showing the robustness of the results, a better justification of the assumptions/methods, a comparison with existing data and mathematical approaches, including clarification of how the evolutionary approach differs from other approaches, and a more careful rewording of the conclusions. Please address all of the reviewer comments (see below).

Reviewer #1 (Recommendations for the authors):

Figures and text:

I think the paper would be greatly strengthened by less dense Figures. As it stands, I found it difficult to figure out what the main points are. As an example: the main point of Figure 5, as I understand it, might be best served by a time-series plot of Slope \Δ-V_{cycle}, or some other summary statistic that shows the transient evolution of a sizer. Otherwise, this point is buried in the legend of panels B, E, and H.

On feedback control mechanisms:

There are no statistical summaries of the simulations described in Figures 2 and 3 of the main text -- Only Figure 4 (whose simulations are initialised with the evolved Model A1) contains statistics on evolved networks. If I understand the text, all the simulations resulted in topologically similar networks -- is this the case. What is the range of CV_births, and does the achieved CV_birth depend on the molecular implementation of the feedback control (PPI, dimerisation, transcriptional control), or do these molecular details affect the \Δ-V_{slope}?

On adders vs sizers (Figures4, 5, and lines 557 to 561 in the discussion):

Figure 4, 5, and the text around it, suggest that the CV_{birth} for adders is lower than that of sizers, in contrast to the common view that sizers are better at controlling cell size. I wonder if the distinction is between the *steady-state CV_{birth}* and the time taken to return to equilibrium from a large 'perturbation' of the cell size?

If it is true that adders are better at the former, but sizers are better at the latter, then would this also explain why cell size control late in the cycle tends to favour sizers? The intuition perhaps being that size control later in the cycle needs to deal with perturbations that occurred earlier in the cell cycle (as suggested by Lines 557 to 561)?

Reviewer #2 (Recommendations for the authors):

We have the following specific comments and recommendations for the authors.

1. Lines 74-77: This is the one piece of the introduction where readers unfamiliar with the eukaryotic cell cycle would be confused. Including background information about G1/S and S/G2/M phases would help expand the target audience of the paper since the techniques discussed therein are widely applicable.

2. Lines 101-106: The "poisson rate that corresponds to the deterministic rate" is unclear. These two sentences could be elaborated on further since significant prior knowledge of the reader is currently assumed.

3. Line 115: "While size-dependent growth mechanisms exist and do support size homeostasis" – This assertion should be backed up with relevant citations.

4. Lines 209-210: "Upon passing the G1/S transition, we assume cells are committed to division and there is a fixed time delay before they divide thus modeling S/G2/M as a timer." – What motivates this assumption? A citation or further discussion is warranted.

5. Line 285: This would be a good place for a citation to direct readers to sources discussing concentration vs quantity sensing. Note that in the bacterial size control literature, quantity sensing of division initiators has been shown to regulate adder behavior (Si et al., Curr Biol 2019).

6. Figure 1B: The dashed grey line is defined afterwards in 1C. It would be good to include it in the defined interactions here instead. In addition, the clarity of this schematic would be better with a line showing how the final network becomes the initial network in the next epoch.

7. Lines 301-302: "… its production is completely shut down in S/G2/M" does not come through clearly in the associated figure. You should clearly describe the chosen dynamics for the inhibitor protein in different phases of the cell cycle, and justify why the choices are different from known inhibitors such as Whi5.

8. Figure 2A: The message of this figure is not presented clearly. There is clustering with high CV volume and low N, another with negligible CV volume and widespread N division, and then the circled optimum. However, the trajectory of how a network evolves is not clear in this picture. Do all of them converge to the optimum eventually? Do they move to low CV before high N division or at the same time? How many epochs does it take to cross the large gap between the clustered networks and the optimum? Recommend somehow indicating sample evolutionary trajectories in addition to the aforementioned clarifications to remedy this issue. Additionally, why are there no numerical values in the axes? This makes it very difficult to assess the degree to which original values have changed.

9. Lines 309-322: This paragraph is somewhat confusing, in particular lines 314-316. The motivation for the control volume is unclear, especially in the physical sense of why a cell would use a non-physical volume to control a transition. While the idea makes sense later in the supplementary material, it needs to be clear from the very start that the goal here is that the control volume is a tool to examine how size at G1/S affects the cycle time.

10. Figures 3A,3C: While intuitive, specifying the role of the dashed red line would improve clarity.

11. Figure 3D: The predictions for the cell cycle scatter appear much stronger than the scatter itself. Can you comment on this?

12. Figure 3B, D: Compare how the model predictions compare with binned means for the scatter.

13. Lines 357-361: The numbers of 120 simulations and 500 epochs appear to be chosen arbitrarily. Why did you choose these initial conditions, and are the results of your paper robust with respect to higher/lower values? If so, including that point here would strengthen the argument, especially with a brief discussion on the lower limit. In addition, roughly how long in time is an epoch? The speed at which evolution is occurring would be of interest to many readers.

14. Figure 4: 4B is created to resemble S. pombe. Do the other panels have real-life analogies or are they arbitrarily chosen for qualitative representations of the discussed effects in the main text?

15. Figures 2F, 2I, 5A, 5D, 5G, 6C: The second zoomed-in panel of 6C is essential to understand the inner-generational dynamics of your modeling. The first many-generation panel shows stability in V but fails to address the other variables and the multi-phase dynamics. The other figures (2F, 2I, 5A, 5D, 5G) would benefit greatly from either a similar treatment or just fewer generations. The stability can be shown with significantly fewer divisions than are currently used.

16. Figure 5B: The ΔV scatters for S/G2/M and the whole cycle could be grouped into two – a positive correlation and a negative correlation. A best fit to the entire scatter is misleading therefore and does not describe the correlation trend.

17. Lines 539-542: Why is a one-step implementation of size control discarded? Surely a simpler control mechanism could be preferred naturally despite being a lesser theoretical interest in evolution simulations.

18. Lines 793-794: In this paper, you consider parallels to organisms that divide asymmetrically, such as budding yeast. Have you run simulations considering asymmetric division? Surely that would impact cell size distribution and variability.

19. Lines 794-795: Wouldn't disregarding one of the two daughter cells add a bias against faster dividing cells? I.e. if the number of divisions is one of your fitness functions, doesn't this method eliminate the natural advantage of a relatively larger population size for multi-cell level exponential growth? Also an issue at S130-132.

20. Lines 801-802: How is the extraction of the nullcline performed?

21. 829: Recommend providing the conversion from the arbitrary units used to physical values, here and all other figures.

22. 838-839: Model A2 does not receive an explanation comparable to A1 in this figure; either move to supplemental materials or explain it clearly as well.

23. Figures 6H, 6I, 6J: These subfigures are not very clear, together with captions for 6I and 6J that do not sufficiently explain to the reader how they are read. Why is the Burst Amplitude axis extended so far beyond the heatmap?

24. S120-S121: How do these theta and n theta values come to be? Currently, it seems like they are chosen with no supporting reasoning or explanation.

25. S239: V target missing a capital T.

26. S328-S329: Need to use a left apostrophe rather than two right apostrophes for epoch and generation.

27. Eq. (S18): Why do you minimize m+1 rather than just m?

28. S406-S408: Why do you choose these interactions to include? How much of all biochemical interactions do they encompass together? Are there others that you are aware of that you are choosing to neglect, and why? Can you provide citations and/or an argument to motivate this choice? This is another crucial ansatz for your modeling that needs to be discussed more carefully.

29. Supplementary Section 4: Translating the arbitrary units into physical values (when possible) would be immensely useful/helpful here.

30. Figure S6E: Why does cut off just below 1 (here, and not in any other plots)?

31. Since the model is generally applicable to any organism, comparisons to size control in bacterial cells (even qualitative) would be useful to widen the appeal. For example, could you predict why almost all bacterial cells (even evolutionary divergent ones) behave as adders? It has been shown that adder is regulated by threshold accumulation of an initiator protein that is produced at a rate proportional to cell volume, which your model could perhaps capture. Furthermore, many bacterial cells also exhibit biphasic size regulation during the cell cycle. It has been shown that Bacillus subtilis behave as sizers during the first phase, followed by a timer phase till division (DOI:10.1016/j.cub.2020.04.030). By contrast, Caulobacter crescentus cells implement a timer first, followed by an adder phase of size control (DOI:10.1038/nmicrobiol.2017.116). Both these organisms behave as approximate adders overall.
