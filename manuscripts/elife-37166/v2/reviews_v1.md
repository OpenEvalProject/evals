# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37166.036](https://doi.org/10.7554/eLife.37166.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "MAPLE (Modular Automated Platform for Large-scale Experiments), a robot for integrated animal-handling and phenotyping" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ronald L Calabrese as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Giorgio F. Gilestro (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this Tools and Resources manuscript, the authors report on developing a multifunctional robot system for handling model organisms. Specifically, they developed a Modular Automated Platform for Largescale Experiments (MAPLE), an organism handling robot capable of conducting lab tasks and experiments, and then adapted it with different organism specific modules and used it to conduct common experimental procedures in Saccharomyces cerevisiae, Caenorhabditis elegans, Physarum polycephalum, Drosophila melanogaster, and Bombus impatiens. They focused on its applicability to D. melanogaster. They show in detail how it can be used to reduce the time commitment to virgin collection with high fidelity. They also use it to study dyadic social interactions. They replicate previous experimental results on the role of visual and olfactory cues and specificity of dyadic interaction and produce the novel result that dyadic interactions persist over multiple days. Thus, they demonstrate it's potential in the laboratory. They provide detailed methods and open source plans for producing a MAPLE, and they convincingly argue that the modular design will allow innovation and adaption to new organisms and experimental procedures. This should be a useful tool for many research labs.

Essential revisions:

The discussion requested by reviewer #2 of potential liquid handling is important and should be directly addressed.

There is a specific concern about the social network biology raised by reviewer #2 that should be addressed.

There is a specific concern raised by reviewer #2 for comparisons to manual processes for animals other than flies that should be addressed.

Both reviewer #2 and #3 want a more thorough discussion of the limitations of MAPLE and provide clear indications of how to proceed in their comments.

All reviewers agree that the manuscript could be made more concise, especially given the extensive supplementary material.

Reviewer #2:

- There is no comparison of MAPLE's capability to manual experimenters for any other organism making it difficult to determine if the initial feasibility demonstrations represent true advances in throughput with automation or automation alone. For example, measuring videos of multiple plates of C. elegans is a rather trivial advance, as switching plates on any standard behavior tracking system takes only a few seconds. A real advance for C. elegans would be the ability to pick (or liquid-transfer) or chunk populations of automatically maintained worms to new plates without damaging them for phenotypic analysis.

- Does MAPLE have liquid-handling capabilities? If not, can it be adapted to? It would be ideal if a drug treatment and/or the same robot that handles animals could apply liquid or gaseous stimuli. For example, MAPLE could administer repeated doses of chemicals to a single fly at precise times over long time scales to see how this alters dyad behavioral structure. While it is likely beyond the scope of the present work to build in liquid-handling capabilities to MAPLE it would be beneficial to discuss this limitation and potential ways this important capacity might be incorporated into the system.

- The authors present their social arena arrays as a solution to the problem of maintaining object ID during population-based social interaction assays. While it does solve the problem of maintaining object IDs, this experiment now gives the flies a choice between a partner and a wall, not a partner or another fly. While novel data presented here are convincing that individual flies prefer certain other flies consistently, it is still not clear whether this individual preference would be consistent if in a population of other interacting flies/potential partners. This limitation and implications for understanding Drosophila social architecture should be discussed.

- There should be a succinct cross-species discussion and comparison of the extensive number of microfluidic devices designed for the same purpose as MAPLE. These systems allow for easy animal handling, automation and high-throughput phenotyping and are available for many of the organisms studied in this work. MAPLE offers several advantages of these systems that should be discussed. In addition, there should be a mention of caveats- of areas in which the system has limitations.

Reviewer #3:

The only weakness of this work is that it is not clearly stated what the limitations of the system are at this stage and how easily (if at all) they could be solved. The manuscript has a very general "optimistic" outlook and it is not clear for me as a reader whether MAPLE could work out of the box for my purposes, which may be quite different from the ones of the authors. The only reported weakness in the provided examples is the one shown in Figure 3. Perhaps the discussion could feature a more comprehensive analysis of strengths vs. weaknesses of the current system. Example of current weaknesses could be: can MAPLE set up crosses automatically beside collecting virgins? does it ever get stuck? what is the longest autonomous experiment in self-drive you performed? can multiple "phenotyping modules" operate at the same time?

Finally: I usually do not comment on writing style because I do enjoy reading manuscripts with different, personal touches. However, in this particular case, I think the manuscript would benefit quite a bit from being shortened. The Introduction, for instance, is quite repetitive and uses too many words to stress an important but relatively easy concept. Some of the results could probably be moved to supplementary or not being shown at all (for instance, Figure 3B does not really add much – it's enough to know what the error rate is. Knowing the position of the wrong vials in that particular trial is too much information).

This is ultimately a joint author/editorial decision, but my recommendation would be to shorten the manuscript quite a bit.
