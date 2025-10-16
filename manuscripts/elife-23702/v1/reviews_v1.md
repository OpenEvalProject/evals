# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23702.020](https://doi.org/10.7554/eLife.23702.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Engineering of a synthetic quadrastable gene network to approach Waddington landscape and cell fate determination" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom, Wenying Shou (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Gabor Balazsi (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

To quantitatively and experimentally understand Waddington's landscape analogy commonly used to depict multiple cell fates, authors constructed a genetic network called MINPA (mutual inhibition and positive autoactivation). By analyzing various sub-networks of MINPA and the full MINPA network, authors find that the full MINPA is capable of achieving the most fate states of mCherry/GFP expression patterns. A total of four states can be achieved, with low or high mCherry and GFP. Aided by modeling, the authors charted how the "energy" landscape of cell fates changes in the presence of various chemicals, and was able to "guide" cells to transit from one state to another by applying chemicals at the correct orders.

All three reviewers thought that your work was important and interesting. However, there are issues that will need to be clarified and addressed before acceptance. Details are provided in the reviewers' comments below. Please note that depending on your response, reviewers might conclude that additional major experiments could be necessary. To help us assess the likelihood of such an outcome, it would help if you responded to the critiques with a plan of action and a timetable for completion of the work recommended by the reviewers. The editor and reviewers will assess your response and provide a recommendation to assist you in preparing a revised submission.

Reviewer #1:

I enjoyed reading it as someone with an informal interest in landscape.

Figure 3B: Not clear to me that at C2, the mCherry state (red dot) has low GFP. Need to make the 3-dimensional illustration more clear.

Figure 3D: How long can the HH state be maintained? Does your model also predict the time scale of decay?

Needs to better describe how "potential" in Figure 4 is calculated.

Reviewer #2:

This is an important and interesting manuscript that investigates experimentally the possibility of multistability in a library of two-gene networks with increasingly complex connectivity consisting of mutual inhibition and positive autoregulation. This topology has counterparts in mammalian cell fate-regulatory networks. The library consists of several synthetic networks, with a number of regulatory links that systematically increases from 2 to 4. Analyzing the dynamics of these networks reveals that the one with all 4 links present has the highest chance for multistability, with more than 2 stable steady states for a broad range of parameters. These findings are experimentally validated with clever sequential induction experiments and hysteresis using 4 different inducers.

The manuscript represents an important step forward in synthetic biology and beyond, having relevance to many cell fate determination networks, including in higher organisms. Nonetheless, some details are clarifications are still needed.

Therefore, I recommend publication once the following comments can be addressed:

1) Synthetic biology often measures its progress by the number of genes in synthetic gene circuits. However, this view ignores the fact that biological complexity does not really correlate with gene number. In fact, biological complexity correlates with the number of regulatory connections. Some plants have more genes than us, humans. In fact, a 10-gene network may be much simpler from a dynamical or an information-processing perspective than a two-gene network – provided that the latter has more complex connectivity. The arguments on network complexity resulting from links rather than nodes may be a nice addition to the Discussion. See Science 292(5520):1315-6 (2001).

2) From the Methods it seems like these networks are on high-copy plasmids rather than integrated. What is the effect of plasmid copy number variation on the results? Could the plasmid be lost from some cells, generating the impression of multistability? Flow cytometry at multiple time points will provide at least a partial answer.

3) The sequential induction method is quite interesting and important for revealing multistability. However, its application to the T15 network (or other networks) could be explained better. I guess the sequence in which inducers are added determines how the network's dynamics changes from monostable to multistable – but the details may be important. If bistable, tristable, quadristable regions are small in the 4-dimensional space then the goal is to "hit" these regions as inducers are sequentially added. While this is shown for the toggle switch, it is unclear how was this done for the more complex networks. This should be much more clearly described, especially for T15 and possibly for some simpler networks. Overall, going from the toggle switch to T15 and even to simpler networks is a big step, which requires more explanation and investigation. In addition, to toggle switch would be worth adding to the experimentally measured networks as control, considering that its behavior is computationally predictable. Do the experiments validate the predictions in Figure 2A for the toggle switch?

Reviewer #3:

In this work, the authors quantified the cell fate decision making landscape through engineering the synthetic circuits. They have identified multiple states. They also considered the cell fate decision at different conditions. The results are interesting and I recommend its publication after revisions upon the following comments.

1) Recently, the theoretical advances have been able to identify the landscape and flux as the driving force of the global dynamics of the biological circuits (Proc. Natl. Acad. Sci. USA, 105: 12271-12276. (2008).). The quantification of the Waddington landscape has been achieved and is directly related to the underlying gene regulatory network for cell fate decision of stem cell differentiation and development (Proc. Natl. Acad. Sci. USA. 108(20):8257-8262(2011).). These should be reflected in the revision.

2) Furthermore, the multiple states have been predicted beyond the bistable states/switches without and with the epigenetic effects (Proc. Natl. Acad. Sci. USA. 108(20):8257-8262(2011); J. Phys. Chem. B, 115, 1254 (2011); Sci. Rep., 2,550 (2012); J R Soc Interface 10: 20130787 (2013); PLoS ONE. 9(8): e105216 (2014); Advances in Physics, 64:1, 1-137. (2015).). These should be reflected in the revision.

3) The authors should explain more clearly the physical and biological origins of the quadrastable states. Why the triple stable states are less likely than the quadrastable states? What is the origin of the LL state?
