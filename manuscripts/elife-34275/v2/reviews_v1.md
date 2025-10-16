# Peer review - Round 1

Editors:
- Kristin Scott, University of California, Berkeley, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34275.029](https://doi.org/10.7554/eLife.34275.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Optogenetic dissection of descending behavioral control in Drosophila" for consideration by eLife. Your article has been evaluated by Gary Westbrook (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: Andrew D Straw (Reviewer #2). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Cande and colleagues leverage three new tools to dissect the role of descending neurons in controlling Drosophila behavior: split-Gal4 lines targeting DNs, a high-sensitivity, long-wavelength optogenetic channel, and t-SNE based behavioral analysis. They claim that activation of most DNs yield stereotyped actions, these actions are common across DNs, and the resulting action depended on previous behavioral expression. The manuscript is well written and the study is very timely given the emergence of new tools permitting the comprehensive study of DNs and behavior. Perhaps the most valuable aspect of the paper will be by providing behavioral phenotypes to use when investigating the more detailed physiology and behavioral function of the relevant circuits. Although this is a very exciting study, significant concerns were raised regarding the video data and analysis that need to be addressed.

Essential revisions:

1) The Videos 1-5 purporting to illustrate the behaviors in question are not of sufficient quality and, in some cases, rather poorly processed. They have the following deficiencies, each of which calls into question the quality of the experiments and, therefore, the validity of the subsequent behavioral analysis:

i) Dark shaded regions appear in the video data (e.g., S03 1:58).

ii) Portions of flies are lost in some video data (e.g., S03 2:11).

iii) Boxes appear in lieu of fly images (e.g., S03 3:02).

iv) Fly orientations are sometimes wrong (e.g., S04 1;00).

v) In contrast to the text asserting that animals were imaged from the dorsal surface, flies seem to be recorded while walking on the dome (the reader sees their sides or ventral surfaces).

vi) The reader cannot easily see the relevant details of leg movements. They are rather fast. Perhaps it would help to add the human annotation information on each video segment to make it clear how the authors annotated the data.

vii) It would be useful to include longer than a couple seconds of fly videos between each cut. It is too difficult to look at extended behaviors in the current form and one cannot simply pause the video because many of the behaviors are dynamic.

2) Comparisons between experimental and control animals are not provided to the extent necessary. For example, to what extent does the entropy decrease following 'high-power' red light stimulation in control animals?

3) The watershed determination of behavior space do not seem well-aligned with the underlying heat map (Figure 1—figure supplement 2). Perhaps a higher-resolution image would better serve the authors.

4) The idea of looking at entropy reduction seems to assume that a DN's role would be to elicit specific actions rather than to modulate actions. For example, entropy would not be expected to be reduced if a DN changed behavioral state without biasing which final state was chosen.

5) In Figure 2—source data 1 and elsewhere, showing the t-SNE results without the underlying video data is too far removed from the real data to be useful to readers interested in interpreting or using the data presented in this study. Please provide relevant videos or tell the reader where to look within Videos 1-5.

6) Figure 5B is perplexing. Why should the experimental animals have a higher mutual information between behavioral states only a few seconds apart? Please expand.

7) There are apparent "anticipation" responses to light-off. For example, in Figure 4C and 4D, there are density changes starting just prior to the end of the lights-on period. Does this indicate that the flies anticipated the light change of the periodic stimulus, or is this an artifact arising from analysis? Please discuss.

8) There are apparently large differences between the behaviors exhibited by experimental and control flies prior to the stimulus onset (e.g. Figure 2C, F). Is this due to the repetitive nature of the stimulus? Where does this arise? Is it present already prior to the first lights-on event? If there are such large differences in fly behavior without optogenetic activation, it does makes me wonder if the two genotypes are in different states.

9) The authors need to make their data analysis methods more accessible by providing source code. They indicate that the tSNE embedding technique can be found in the Berman et al., 2014 paper, but I think it would be appropriate to link what seems to be the relevant source code on github https://github.com/gordonberman/MotionMapper. The authors additionally indicate that the statistical classification approach here is new and likely to be useful and I agree. Other aspects are also of likely useful, such as calculating mutual information. Therefore, as stated in the eLife guidelines, please "Include code used for data analysis."

10) The details of the "fly bubble" are not given. Another paper (Klibaite 2017) is referred to, but the construction details are not present in that paper, nor is even the word "bubble" mentioned.

11) It would be useful to link the behavioral findings with the underlying anatomy of DNs. Are DN inputs and outputs differently represented for different behaviors? The anatomy paper proposes different sets of DNs involved in locomotion versus flight. Do DN innervations in the VNC correlate with different behaviors? Some effort to relate the anatomy to the behavior seems important.
