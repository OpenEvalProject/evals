# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79031.sa0](https://doi.org/10.7554/eLife.79031.sa0)

The hippocampal cells that comprise the place cell map for the most part ‘remap’ between different environments – they change their preferred firing locations and rates. This article poses an important question about offline reactivation that has not been explicitly tested: are differences in firing rate preserved during sequential, temporally compressed offline replay events? They find that yes, individual neurons show context-specific firing rates during replay, an important finding and a confirmation of critical theoretical foundations in the field of learning and memory. The evidence is convincing, with good support for the claims. At the same time, this demonstration hinges on some relatively subtle methodological points specific to replay detection, and thus serves as an invitation to the field to further explore the precise structure of context-specific offline activity.


---

# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79031.sa1](https://doi.org/10.7554/eLife.79031.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Experience-driven rate modulation is reinstated during hippocampal replay" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Caleb Kemere as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) In their discussion, the reviewers agreed that there is prior work that demonstrates the concept that contextual information present as a rate-modulation in the CA1 place-code is also present in replay. It is important that your work cite these prior efforts. In particular, the work of Takahashi, 2015, Farooq et al. 2019, and Gupta et al. 2010 merit further consideration in terms of rate modulation, and Karlsson et al. 2009 in terms of replaying multiple environments. The reviewers were convinced that your work is sufficiently different from these in that it presents activity recorded in different mazes in subsequent sleep, but it is critical to place it among related works.

2) The reviewers agreed that a strength of the work was its focus on a particular question. In discussion, we concluded it was unfair and unnecessary to ask for substantial new analysis. That said, if the primary question the paper is answering is "Are the firing rate differences that mark maps of distinct experiences maintained during replay?" the paper would be stronger if it could report the extent to which this effect is general and not merely a characteristic of a small fraction of events that are already extremely distinct (i.e. "replays" vs "ripples"). To that end, at a minimum please report what fraction of ripples (i.e., putative replay events) your subsequent analyses capture. In addition, if it's relevant, it might also be worth reporting the sensitivity of the analyses to the significance threshold used for replay detection (e.g., what would happen if it dropped from 95% to 90%).

Reviewer #1 (Recommendations for the authors):

My two requests are that they repeat their analyses (a) for all ripples or population burst events and (b) repeat the analyses using all neurons.

Figure 1B. It is unclear what the decoded result looks like when only a few decoded positions appeared in the figures in the last row of the first column and the second row of the second column.

Page 10: "We found that place information alone was sufficient…". I think that this is not really an accurate statement. I think what the authors mean, and what would be more clear is "We found that the ensemble co-activity – i.e., which cells were active in a decoding bin – was sufficient…"

Similarly, "Next, we selectively removed place information without altering rate information…". I also don't love this formulation, though it is more true. I would simply say, "we removed the sequential order of firing".

Page 12. Discussion, second paragraph, the statement of the first key advance is confusing. Does it mean sequential information is better for replay detection and rate modulation is more suitable for context determination?

Page 19. The first equation at the top, how is P(x) defined?

Page 19. Replay events scoring and significance. In the weighted covariance equation, what is y?

Why is "Bayesian bias" score computed as the sum of the posterior probability matrix rather than decoded position likelihood?

Page 20. Reinstatement of rate modulation analysis

Paragraph 2, last two lines, do "replay events" in (2) and (3) include all replay events or only events when the cell fired?

Reviewer #3 (Recommendations for the authors):

The following methodological details need to be elaborated/clarified for replication purposes:

– It is unclear how much prior training the rats had. The first sentence of Results says they were trained to run, but this training is not described. While the tracks are novel, for replication purposes, it should be clear if they have had prior experience on any linear tracks prior to recording/implantation and how similar/distinct those training tracks were to the novel tracks used during the recordings.

– In the criteria for defining a place field, it is unclear how "stable spiking activity across the first half and second half" is quantified. The way in which the PPV is calculated is clear, but it is not clear what criteria defined "stable" vs. "unstable."

– When candidate replay events are speed-filtered, I'm guessing the authors mean that they kept only events when the rat's velocity was less than 5 cm/s. The text implies that they kept events with >5 cm/s.

– "In a few occasions, replay events were found to be significant for both tracks." For interpretation, please list the number (and percent) of such events.

In addition, while not necessary in my opinion for publication, I think analyzing direction-specific place fields may provide an even stronger argument (as you would effectively have 4 tracks for comparison rather than just 2).
