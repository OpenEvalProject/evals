# Peer review - Round 1

Editors:
- Brian S Kim, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84042.sa0](https://doi.org/10.7554/eLife.84042.sa0)

Scratch assays are the gold standard for measuring itch in rodents. However, the current limitation is that this is performed manually which is enormously taxing in terms of hours spent counting scratching bouts. The authors have developed a valuable automatic system to quantify scratch behavior with high accuracy and provided a valuable tool for the field. This will be resourceful for the greater itch biology community.


---

# Peer review - Round 1

Editors:
- Brian S Kim, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84042.sa1](https://doi.org/10.7554/eLife.84042.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article " Scratch-AID: A Deep-learning Based System for Automatic Detection of Mouse Scratching Behavior with High Accuracy" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Catherine Dulca as the Senior Editor. The reviewers have opted to remain anonymous.

Reviewer #1 (Recommendations for the authors):

1. Can Scratch-AID be modified to quantify scratching bouts?

2. Saliency maps analysis suggest that the trained neural network is focusing on the movement of the hindleg to identify scratching. Although mice will spend the majority of their time scratching the injected or treated skin location, they do scratch uninjected/untreated area as well in both acute and chronic itch models. Different laboratories have different strategies to determine whether scratching to the untreated locations is included for quantification. Is Scratch-AID able to differentiate scratching directed towards treated vs untreated locations?

Reviewer #2 (Recommendations for the authors):

Mouse behavior assay is the primary readout for almost all itch research. The itch sensation triggers a stereotypical scratch-lick response by the ipsilateral hind paw, and several key parameters including the number of scratch bouts and total scratching duration can be precisely quantified and compared across genotypes and treatment groups. So far, the vast majority of itch behavior videos are manually scored, requiring hundreds of hours of labor and are prone to experimenter errors. In this paper, the authors introduce an automated system to replace the manual itch counting process. First, they designed a standardized videotaping box to produce consistent and high-quality videos of itch behaviors. They then annotated the videos frame by frame for scratch bouts, and trained a neural network to identify scratching behaviors with high precision. The system (named Scratch-AID by the authors) performed consistently with manual and reference scoring, and yielded key quantitative parameters (scratching bout counts and total scratching times). Saliency map revealed that the trained neural network focused on the scratching hind paw, which is consistent with what human observers look at. The authors further showed that Scratch-AID can be easily adapted to quantify scratching at slightly different sites (nape vs cheek), in response to different itch mediators (chloroquine vs histamine), in both acute and chronic itch models, and that it successfully revealed the effect of a generic anti-itch drug Benadryl. Overall, the model appears accurate and easily adaptable and can probably be widely used by the itch field.

There had been a few previous attempts to train neural networks to score itch behaviors (Kobayashi et al., 2021; Sakamoto et al., 2022). The main advance of this paper is the incorporation of a standardized recording system, and larger number of videos in the training dataset. The authors provided very detailed and thorough analyses of their own model, but did not compare its sensitivity and precision to the previous models. It is also unclear why the authors did not choose the high-speed video system that they previously published for detailed analyses of pain behaviors (Abdus-Saboor et al., 2019), despite evidence that multiple itch parameters can only be captured at high speed (Wimalasena, et al. 2021). The authors show that scratch-AID can accurately score multiple itch models (despite it being trained on chloroquine nape injection videos), but does not show whether it can distinguish itch behaviors induced by different mechanisms and mediators. For example, whether it can detect activation of different itch neuron populations (termed NP1, NP2 and NP3 by single cell transcriptomic analysis), or distinguish direct itch neuron activation by mediators such as chloroquine vs mast cell activators such as 48/80. Nonetheless, this study provides a great opportunity for the itch field to standardize behavior data acquisition and analysis, and will greatly enhance the throughput and quality of future itch behavior data.

The data are overall very convincing and the system an exciting advancement that will probably be widely used. I have some questions regarding data analysis and potential concerns for future users of the technology.

1. Does the model distinguish ipsilateral vs contralateral scratches?

2. Can the authors present the data in more detail? For example, present and compare both scratch bout count and total scratching time between scratch-AID and manual scoring for each of the itch models.

3. This is probably a given but can the authors provide evidence that the model clearly distinguishes pain (by capsaicin injection) vs itch (chloroquine and histamine)?

4. If all parameters are analyzed in more detail (average duration of scratch bouts, temporal distribution of scratches across the imaging period), can the model distinguish the differences between NP1(by β-alanine), NP2(by chloroquine) and NP3(by 5-HT) activation?

5. Can the model distinguish direct neuronal activation (chloroquine) vs immune cell activation (48/80, anti-IgE)?

6. Since the training is done with black mice, can the model detect itch behavior by white mice?

7. Can the authors comment on how the new system compares to previous itch-counting apparatus (such as SCLABA-REAL) and previous neural network models?

8. What's the max number of animals that can be recorded and analyzed in a single box?

9. Since video quality is vital for correct predictions by neural networks, can the authors comment on the influence of potential confounding factors (urine and feces, wear and tear of the acrylic imaging surface).

10. This is potentially a great opportunity for the itch field to standardize the itch behavior assay. Can the authors comment briefly in the discussion on other aspects of standardization such as time of the day for experiments (circadian rhythm), injection volumes, habituation, and sexual dimorphism?

11. Can the authors discuss how the rest of the field can apply the system in their own research? Will it be released as an open source software? And will the custom video box be commercially available?
