# Peer review - Round 1

Editors:
- Huan Luo, Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69079.sa0](https://doi.org/10.7554/eLife.69079.sa0)

This single-author work, by combining real-time closed-loop EEG-TMS and sophisticated computational modelling to characterize ongoing brain states, impressively demonstrates the causal role and different functions of several prefrontal regions in modulating bistable perception, in a brain-state-dependent way.


---

# Peer review - Round 1

Editors:
- Huan Luo, Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69079.sa1](https://doi.org/10.7554/eLife.69079.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Causal roles of prefrontal cortex during spontaneous perceptual switching are determined by brain state dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tomas Knapen (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) The study is based on findings and methods in the author's previous fMRI work. However, since the current work employs EEG recording, it is important to add several validation and control analyses or data, including: (i) replication of the relationship between individual brain state dynamics and.bistable perception; (ii) providing data supporting that the EEG-channel-based TMS has high enough SNR to differentiate between neighboring regions in prefrontal cortex; (iii) fleshing out the numerical simulation procedure used to calculate dwelling time.

(2) Since the state transition in EEG signals is defined in terms of γ-band power, the authors should: (i) provide control data to exclude the involvement of microsaccade-related artifacts that might elicit the γ-band response, especially considering the structure-from-motion stimulus used here ; (ii) present time-frequency plots before/after state transition as well as TMS-triggered time-frequency plots to help readers have a transparent understanding of the state transition and TMS effects.

(3) Addressing the role of attention, i.e., is the effect of DLPFC stimulation on the dynamics of bistable perception mediated by changes in attentional state?

(4) Addressing the possible circular hypothesis testing (Page 10). Specifically, the models were fit by using EEG data (and behavior?) to calculate the energy landscape, so is it trivially expected that the dwell times seen behaviorally correlate with the energy barrier estimated by the model?

(5) Energy landscape is a very abstract term and needs to be fleshed out in terms of the present results, e.g., specifying functional roles of different regions of prefrontal cortex in bistable perception.

Reviewer #1 (Recommendations for the authors):

I find it hard to understand the impact statement, title, and abstract. A naive reader will likely find these sentences very hard to parse. A reader will likely wonder; What are the different causal roles of prefrontal cortex that are changing during bistable perception? What are hypothetical energy landscapes?

Abstract; presumable is overly vague; why not just presumed? Abstract sentences are also very long, this taxes the reader.

The initial paragraph of the results requires the reader to either be an expert in the author's previous energy landscape work, or take a lot of things at face value. I suggest this way of writing is going way to fast. I appreciate that the author wants to get to the 'meat' of the study, but this requires much more explanation.

Reviewer #2 (Recommendations for the authors):

An impressive study. My main suggestions are mostly stated in the public comments. Basically I'd like the author to explicitly discuss:

1. The role of attention. Is the effect of DLPFC stimulation on the dynamics of bistable perception mediated by changes in attentional state?

2. What are the functional roles of the different regions of DLPFC in bistable perception? Energy landscape is rather abstract. The author should help readers to gain some intuition about the link between brain states and perceptual states.

3. Reportability of perceptual states was proposed as an important factor in observing the PFC engagement in bistable perception. The author should discuss the implication of the current study on the significance of perceptual report for PFC's engagement in bistable perception.

4. The descriptions in the paper on "binocular rivalry".. "has been often explained by …" (pages 3 and 14) are inaccurate, should be revised.

Reviewer #3 (Recommendations for the authors):

1) A recent study (Weilnhammer et al., Curr Bio, 2021) showed that theta-burst TMS over IFC (same as pDLPFC here) prolonged percept duration. By contrast, continuous TMS here had null-effect (Figure 2c), and single-pulse inhibitory TMS reduced percept duration in the F-state (i.e., opposite to the Weilnhammer et al., finding). Since the Weilnhammer et al., paper was published after this manuscript was submitted (even though a bioRxiv version was available), it is not obligatory for the author to cite this paper. Nonetheless, in the revision, some discussion about potential sources of this discrepancy would be helpful.

2) Introduction, 1st paragraph states that the PFC has in particular been thought to be involved in spontaneous switching. But I think the evidence for a causal involvement in spontaneous switching is actually stronger in parietal cortex, given the long series of TMS studies there by Kanai and Rees.

3) Figure 5. How excitatory vs. inhibitory TMS was conducted should be described in the main text.

4) Results (Figure 5-6) should be described in the Results section, not Discussion.

5) The description of the maximum entropy model is rather inaccessible. Breaking it down, providing intuitions and code, and intermediate steps in intuitive/graphic language, would be helpful.
