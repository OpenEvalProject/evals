# Peer review - Round 1

Editors:
- Andrew J King, University of Oxford United Kingdom

Reviewers:
- Ehud Ahissar, Weizmann Institute of Science Israel

## Review text

DOI: [10.7554/eLife.41535.034](https://doi.org/10.7554/eLife.41535.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "What can facial mechanoreceptors tell the mouse brain about whisking?" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Andrew King as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal his identity: Ehud Ahissar (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study by Severson and colleagues provides a systematic examination of whisking information conveyed by different categories of facial mechanoreceptors in the mouse. The paper includes a detailed quantitative analysis of the motion of different facial regions associated with whisking and quantified how different populations of mechanoreceptors encode the position, phase, speed, acceleration and midpoint of whisking. This represents an important body of data for the understanding of vibrissa-based perception.

Essential revisions:

The reviewers agreed that this is a timely, well conducted and important piece of work, but raised several related questions over the possible causes of the non-mystacial vibrissae movements and what their functional role might be, as well as over some aspects of the analyses carried out.

1) An important issue is whether facial non-whisker receptors really convey whisking information, or whether this is just a side effect of the facial strain patterns caused by whisking. In other words, that facial non-whisker receptors convey some whisking information may be an unavoidable consequence of the fact that the skin, particularly at and around the whisker pad, moves when the whiskers do, and that the non-mystacial vibrissae also move in a correlated fashion. Furthermore, for hairy skin receptors, except those on the pad, whisk phase encoding is really quite weak (MI equaling around 1% of response entropy). This raises doubts over whether you are really demonstrating a pathway for whisking information.

2) To address this, the reviewers ask that you provide information, either from the literature (e.g., Grant et al., 2013) or from your own anatomical analysis, about the musculature. Do the vibrissae possess intrinsic muscles? If not, is their motion primarily driven via the skin or via extrinsic muscles? Whether their motion is active or passive, and what drives it, is important for both the interpretation of the data, and for future models attempting to use these data to address perceptual mechanisms (e.g., predictions for reafference delays and amplitudes would differ significantly in the passive and active cases).

3) A general aim was to investigate whether facial proprioception relies on reafferent activity of cutaneous low-threshold mechanoreceptors: wouldn't this be better served by comparing encoding of whisker motion to encoding of other forms of facial (e.g. gestural) movement? Similarly, the hypothesis (Abstract) that "redundant self-motion responses may provide the brain with a proprioceptive signal" robust against perturbations, is only very briefly touched upon in the Discussion, but could have been fleshed out. In the absence of such arguments, the manuscript reads as a quantification of measures whose functional relevance (and biological significance) is unclear.

4) The authors suggest that the non-whisker vibrissae can "provide the brain with a phase signal that is.… unperturbed by contacts". While this is in general correct, the authors should consider the reliability of the signal and its relevance to various tasks. Signals from the non-whisker vibrissae may vary significantly in different conditions, such as head-fixed versus freely moving versus palpating an object. Also, importantly, they would not be accurate enough to allow the determination of fine spatial phases (as with fine textures, for example) during palpation, a determination that should require a tight coupling between the phase/angular coding and contact coding in the same whisker (as whiskers are not strongly coupled in such cases). This point should be addressed in the paper, at least by discussing it and suggesting future experiments.

5) Can you identify ways in which the additional information provided by non-whisker coders might resolve ambiguities or become important? Perhaps different receptors might represent different aspects of the sensory signal, e.g. filtered over a particular frequency range. Or, given that you partially tracked facial movement, can you tell whether some receptors encoded cutaneous facial movement (over e.g. a particular dimension) better than whisking, i.e., can you quantitatively compare information about different forms of movement? If the whiskers are primarily driven passively through pad motion, might their signals be used to differentiate lateral from axial forces in contacting whiskers? Further discussion of how the coding of whisker speed might be used is also merited.

6) Another major issue is more technical and concerns the MI calculations. How safe are they against biases from limited sampling? How many observations per bin typically went into the analysis? How do MI values vary if one subsamples from the observations? Did the 2 ms resolution of sampling windows (equal to the experimental resolution, 1/500 Hz) take into account sampling considerations – i.e. given that kinematics were filtered < 30 Hz, and only varied slowly over 2 ms, would using a longer sampling window affect the calculations? Did you incorporate a delay between the stimulus and response windows, or did you take them to be simultaneous? If the latter, how did you account for response latency – wouldn't it be useful to set a gap between the windows, determined by maximizing MI as a function of gap length for a couple of experiments and then fixing across each data set?
