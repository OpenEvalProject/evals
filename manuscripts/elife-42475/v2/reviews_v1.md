# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.42475.063](https://doi.org/10.7554/eLife.42475.063)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Optogenetic control shows that kinetic proofreading regulates the activity of the T cell receptor" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Arup Chakraborty as the Senior Editor and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please aim to submit the revised version as a Tools and Resources paper (see comment below).

Summary:

The authors construct a light operated TCR using PhyB tetramers and a TCR modified with the PIF ligand and GFP. PhyB interaction with PIF is 100% turned off by far red light and 80% activated by red light, with the 20% off state in red light due to a probability of red light also turning the PhyB off. In the dark, the molecules maintain their state with a slow dark reversion of the off state. They trigger Jurkat cells expressing the PIF-TCR with the PhyB tetramers in on state and observe Calcium flux. They then note that 660 nm excitation drives an accelerated dissociation in proportion to intensity without changing the on-rate. They accelerate the dissociation with brighter red light to generate a dataset to test the kinetic proofreading model. The data and model suggest that in the conditions tested, the relevant time frame for interaction with the receptor that enables a calcium flux is 16 s.

This system has excellent properties for controlling kinetics using light. One might expect light to be used for spatial control, so its novel to apply this effectively to a problem in kinetic discrimination. Additional work would be needed to understand how this relates to selection thresholds, but together with the paper from the Weiner lab, this paper makes a strong case that optical control will be a powerful tool for understanding the role of kinetics in immunoreceptor signaling. As a technical paper that develops a tool, this is an interesting paper and could be published in the Tools and Resources category.

We do not think that the paper resolves the question of how kinetic proofreading occurs in any comprehensive way, which is what the authors set out to address. A number of technical points about the method need to be addressed. Furthermore, somewhat disturbingly, the vast literature in the field is cited in a selective manner. Below, we provide guidance on both these important issues.

Essential revisions:

1) The statements about affinity are too simplistic in the current understanding of the TCR-pMHC interactions. We suggest they replace affinity with potency (meaning functional potency).

2) When you introduce PhyB-PIF interaction rules you should state the affinity of the 100% on state. From PMID: 19749742 seems to be 20-100 nM in vivo. Would this allow them to load a cell with soluble PhyB and study the rate of dissociation, perhaps in a flow cell by microscopy? It would be fantastic to have a monomeric dissociation rate under different illumination conditions for the modeling.

3) Would it be possible to pre-load the tetramer to the cells to initiate a signaling condition and then illuminate to different intensities of 660 light to change the signaling state? It’s possible that already bound tetramers would remain bound even as the PhyB starts to cycle faster and this may result in a reset of signaling- loss with faster cycling, for example. Alternatively, could the authors link the PhyB to increase the valency such that the change in off-rate would not impact binding (due to greater rebinding). Perhaps a quantum dot or liposome decorated with multiple PhyB could be use employed. See: PMID: 17077145 or PMID: 9300688 for examples. These points need to be discussed.

4) The claim that you only affect half-life and no other parameter with the optogenetic method you employ is not supported by the data. The LOV2 system requires a conformational change to get the dissociation you need to end engagement (this is clearly stated in the text) and hence, you cannot know that the force of CAR interaction with the ligand is not changed in blue light when this conformational change takes place. Establishing this claim for no force change requires a direct test a la Chen Zhu's method to determine if this fundamental postulate of the method is true or not. This point needs to be discussed.

5) A number of relevant papers need to be cited that are pertinent, and the present results related to these studies. A small sampling of the missing literature are:a) The work from the Davis lab from several years ago on using caged pMHCs that were sensitive to light, which allowed measurements that described the speed at which signals propagate downstream.b) The role of rebinding that allows ligands with short half-lives to signal, described by work from eight years ago by Van der Merwe and co-workers (Immunity) and Huseby and co-workers (PNAS).c) The role of co-receptors, amount of active Lck and diffusion in kinetic proof reading described by Stepanek et al., 2014.d) You also ignore the data the Germain lab, and others, have presented showing that the same ab TCR signals differently in DP thymocytes vs. mature cells [in particular, allows meaningful propagation of signals for gene expression in DP with pMHC ligands incapable of electing the same response or biochemical changes in a mature T cell], meaning that intracellular events can control signal propagation separately from occupancy, half-life or mechanosensing.

6) The model for proofreading is a bit strange. Many people have made models that are far more realistic and incorporate feedback, including several papers from the Germain lab (Madrenas et al., 1995; Madrenas et al., 1997; Altman and Germain, 2005 and Nature. 2002 Nov 28;420(6914):429-34), Chakraborty and Palmer, Chakraborty and Weiss, and the more theoretical efforts by Murugan, Huse, and Leibler. These papers should at least be cited and briefly discussed.

7) The estimate of 3 proofreading steps is undoubtedly wrong. The various steps do not have the same time scales and there are feedback loops. These effects make the model's fit to obtain n very difficult to interpret. This part needs to be deleted.
