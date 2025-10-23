# Peer review - Round 1

Editors:
- Andrew J King, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55539.sa1](https://doi.org/10.7554/eLife.55539.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "A sensorimotor model shows why a spectral jamming avoidance response does not help bats deal with jamming" for consideration by eLife. Your article has now been reviewed by three peer reviewers, and the evaluation has been overseen Andrew King as the Senior Editor and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Dieter Vanderelst (Reviewer #1); James A. Simmons (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper addresses an important and long-standing question in the field of echolocation, namely whether bats require a jamming avoidance response to avoid mutual interference among multiple bats flying in the same location while hunting for flying insects. The authors' study provides an excellent example of the application of computational modeling, supported by parameterization from the large body of experimental evidence in bat echolocation, to address a complicated question about sensory ecology. It is well established under laboratory conditions that bats change their echolocation frequencies in the presence of other bats or when a tonal jamming signal is delivered at frequencies at or near the ending frequency of their biosonar calls. The principal conclusion from this study is that these frequency shifts do not materially improve prey capture, raising the possibility that the jamming avoidance response is a solution proposed to solve a largely non-existent problem.

Revisions:

Although all three reviewers were generally enthusiastic about this paper, they raised several concerns and made a number of suggestions that will need to be addressed before it can be considered suitable for publication. Most of these points are relatively minor, and concern issues of clarity and presentation. However, it was pointed out that the manuscript does not adequately cite previous literature and that the modelling results are over-interpreted because of the availability, at least in natural environments, of other cues that help to discriminate between other bat sounds and echoes. In addition, some questions were raised about the model.

1) The manuscript includes unsupported claims of novelty (start of Discussion) and does not cite all the relevant literature. Several papers have previously quantified the probability of jamming (Jarvis et al., 2013; Lin and Abaid, 2015; Beleyur and Goerlitz, 2019,). Moreover, a paper (Cvikel et al., 2015) from the same lab has investigated the question of decreasing hunting performance, albeit with a simpler computational model lacking the sensory detail in this current work. One of the primary conclusions “..that jamming is less of a problem than previously suggested” has also previously been shown by Beleyur and Goerlitz, 2019, with a similar approach of biologically parameterized detailed sensory simulations. This work should be cited at appropriate places in the manuscript, as this will help readers to contextualize the findings.

2) The studies that demonstrate putative frequency jamming avoidance responses (JARs) in bats did not go further with interpretation than saying that JARs are just one of several dimensions along which bats could distinguish echoes of their own broadcasts to discriminate against similar but not identical sounds of other bats. For example, changing pulse times and FM sweep slopes provide ample opportunities for discriminating among multiple other bat sounds and echoes. The modeling work in this manuscript establishes that the frequency JAR is not by itself a critical dimension for avoiding mutual interference. For this reason, the work is an eminently valuable contribution, but the interpretation is too strong since other cues are typically available too. Furthermore, in at least one study, the shifts in frequency are related to pulse-echo ambiguity or self-jamming in complex scenes (Hiryu et al., 2010). This is a much more difficult problem than mutual interference in groups of bats, so the authors should be guarded in their interpretation of the contribution to JARs to the ecology of echolocating bats and specifically why they occur if they do not materially enhance prey interception.

3) In the manuscript's filterbank model, the envelope detector is described as removing phase information and is similar to several loosely auditory-inspired models of echolocation (Wiegrebe, 2008; Peremans and Hallam, 1998; Boonman and Ostwald, 2007). However, a more biologically realistic model with half-wave rectification and 10 kHz low-pass filtering performs the same as a crosscorrelating receiver (Sanderson et al., 2003). In general, there is a lot of work on time-frequency methods that are equivalent to matched filtering, but the authors choose a model that removes phase information even though behavioral tests of both bats and dolphins suggest that echo phase may be perceived. It would be helpful if the authors give their reason for this limitation of their filterbank model, particularly as inclusion of phase information would likely strengthen the study's findings.

4) When the authors model localization errors due to jamming, they do this by assuming that a lower SNR leads to larger errors (Equations 9 and 10). This is appropriate, but it is not the whole picture. Interference between echoes could obscure spectral cues needed for localization. This is not taken into account in this model. The authors should at least acknowledge the possibility of spectral interference and state why they do not model it explicitly.

5) More attention needs to be paid to the writing as various terms are used loosely, introduced without definition, or used interchangeably.
