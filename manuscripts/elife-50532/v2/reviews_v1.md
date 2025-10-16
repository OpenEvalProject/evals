# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50532.sa1](https://doi.org/10.7554/eLife.50532.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work of Ramirez-Gomez et al., is an important contribution to our understanding of sperm chemotaxis in sea urchins, a historically important class of organisms in the unravelling of this phenomenon. It was in these that sperm activating peptides such as speract were first identified; these play a role in triggering calcium increases that regulate dynein motor activity and thereby control motility. Through studies of various species of sea urchins and theoretical analysis of the limits of gradient detection the authors identify the boundaries for detecting chemotactic signals of S. purpuratus spermatozoa, and show that sperm chemotaxis arises only when sperm are exposed to sufficiently steep speract concentration gradients They show further that sperm chemotaxis arises through coupling between recruitment of speract molecules during sperm swimming and the internal Ca2+ oscillator.

Decision letter after peer review:

Thank you for sending your article entitled "Sperm chemotaxis is driven by the slope of the chemoattractant concentration field" for peer review at eLife. Your article is being evaluated by Naama Barkai as the Senior Editor, a Reviewing Editor, and three reviewers.

Given the list of essential revisions, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

The reviewers had mixed opinions on this work, but reviewer #3 has raised a number of technical issues that need a clear response from you in order that we can reach a formal decision. Please pay particular attention to those items.

Reviewer #2:

There is nothing wrong with this paper. It gives a very thorough review of the well-researched field of chemotaxis including some solid modeling. The problem is that it isn't new or surprising (to me). The same manuscript was put online in June 2017 in bioRxiv with little note. The statement that "For almost three decades, chemotaxis had not been observed for the widely-studied S. purpuratus species under diverse experimental conditions, raising doubts about their chemotactic capabilities in response to the speract concentration gradients" is made without citation in both versions of the paper, but it doesn't seem to have been much of a mystery. The receptor density of low on S. purpuratis, which then requires a steeper gradient to overcome noise, as the authors have shown.

While there is nothing wrong here, it seems very academic and has previously attracted little attention, so I question why it should be published in eLife.

Reviewer #3:

I started the manuscript with excitement but it did not take long to recognise that the theoretical work has been not been implemented to sufficient standards of diligence; it appears unchecked for errors, both minor and fundamental, with examples of the latter including modelling assumption, equation solution and dimensions.

The limits of detection and the limits of when oscillators couple (e.g. that pendula on a wall are sufficiently coupled to synchronise) is interesting and is the concept in the context of chemotaxis explored here. However, thresholds by their nature are sensitive – the number of theoretical errors means that discussing and examining thresholds does not appear to be sound (as opposed to using controlled and justified approximations).

Hence, I am afraid I cannot recommend the manuscript for publication, with further details are below. I should note I have less confidence in the experimental aspects and leave this to other reviewers.

Equation (1):

- A list of assumptions should be provided with such equations. The authors have assumed a large Peclet number and it is not clear the Peclet number is large (it is, if the flagellum radius is used as the length scale, but the interaction of the fluid flow with the concentration field means such an assumption is not obviously valid). Appeal to Berg's paper is insufficient as the Peclet number is larger for bacteria, as the smaller the length scale the greater the effect of diffusion, and diffusion is dominant for an isolated bacterium. The assumption that Pe >> 1 is therefore a substantial one and should be justified – it is not clear, either way, whether it is true or false.

- The authors assume a spherical geometry for the flagellum. This is flawed. It is commented on in the SI and an alternative is given, but not used. I did not understand why an inappropriate and inaccurate approximation is used in the main text when the authors know this is an issue; no explanation seems to be present.

- The calculation of the receptor term, N/[N + πa/s], is for a spherical flagellum only and arises from interactions between the effects of adjacent receptors. For a fixed volume, as assumed, the sphere has minimal surface area and thus receptor interaction is highest given they are assumed placed at random. Thus, using the correct geometry with a fixed volume will reduce this receptor interaction effect and yet it is fundamental to the paper. Hence the authors are over-estimating the influence of one of the primary features they are testing for – this seems fundamental and one of the reasons I am recommending reject.

- s is the receptor effective radius not the chemoattractant radius (subsection “Species-specific differences in chemoattractant-receptor binding rates”).

Equation (5):

- This is also flawed. It is dimensionally incorrect as stated.

- To within a scaling to fix dimensions, it is the one-dimensional solution. Either the two-dimensional or three-dimensional solution is required here (depending on the gap between the cover slips, which does not appear to be given – my one comment on the experiments – the geometry should be clearly stated). The use of the incorrect spatial dimension changes the gradient term in the SDR expression and thus has major downstream impact, explicitly affecting what the authors are testing. Again, this seems fundamental in testing the chemoreception model and thus is a further reason I am recommending reject.

- Equation (5) does not respect the fact any solution without initial conditions imposed will satisfy invariance to shifts t -> t+q for any q and so cannot be correct (it needs t+t0 rather than t in the square root or t0 must be zero).

Equation (S4). Appendix 1 subsection “1.2. A condition for detecting a change in the chemoattractant concentration”. The chemoreception model uses the circumference of the sperm's circular path (v∆t) rather than its diameter, yet the diameter governs the range of concentrations the cell experiences. Given the ratio of circumference to diameter is π this constitutes a factor of π in the definition of SNR and feeds through to the rest of the paper. For studying thresholds, a factor of three can be very important and this contributes to my overall decision.

Appendix 1 subsection “1.1. On the estimate of maximal chemoattractant absorption” There are dimensional errors in the expression for the effective size of the binding site.

There are numerous points of presentation, only the more general are below as opposed to detailed minor points (e.g. no equation punctuation, use of ∂ for increments… which I have not documented).

- "Caution needs to be taken with the interpretations of the agreement of our data with such a generic model for coupled phase oscillators" – such a generic model does not pin down mechanism and an oscillator inheriting the frequency of its forcing does not seem unexpected, so I am also hesitant about what can be learnt from the interpretations. Similarly, for (over)statements in the manuscript e.g. "that spermatozoa exposed to steeper gradients experience lower uncertainty (i.e. higher SNR) to determine the direction of the source of the chemoattractant". Any theory with sensible monotonic relationships will show this trend so I am also not clear what is learnt from such observations. This is probably a point of presentation only, but I struggled on such points.

- It is unclear sometimes what is model prediction as statements that are derived from the models are often not stated as such making it harder to follow.

[Editors’ note: The editors accepted the authors’ plan for revisions asking for further expansion on certain points.]

3.2) Given the conviction of the authors, this should just be a simple case of providing an evidence-based estimate of the Peclet number for sperm (not bacteria – these are much smaller and thus unreliable for inferring the correct physical scales) to demonstrate transport is diffusively dominated. Such a demonstration is required.

3.3) Please evidence that is a legitimate approximation or use the expression for a cylinder. There is no demonstration that the difference between the two geometries does not change the presented results. Such evidence is required.

3.4) Please provide explicit evidence for your claims such that the use of this expression – based on a spherical flagellum – does not impact on the theoretical predictions and subsequent experimental comparisons, predictions, conclusions etc.
