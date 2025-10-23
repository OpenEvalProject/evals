# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31867.051](https://doi.org/10.7554/eLife.31867.051)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cellular adaptation through fitness-directed transcriptional tuning" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper presents a new striking theory on gene expression. It suggests that at the absence of an evolved cellular program to regulate gene expression according to the environmental conditions cells might resort to stochasticity to govern transcription of relevant genes. The paper suggests an intriguing feedback loop: stochastic noise allows certain cells to express the right gene to the right level (and other cells to the "wrong" level), these cells that, due to chance, expressed the protein to the right level get a signal to keep inducing the gene that improved their fitness. The presumed feedback allows cells to "know", somehow, that they should keep inducing that gene that conferred the high fitness or keep reducing genes if reduction improved their fitness; cells are also assumed to know to reverse changes in expression (up or down) if change if previous step was maladaptive.

Essential revisions:

The theory is intriguing, bold and novel. However, there are additional experiments that are essential to establish its use.

We find that experimentally addressing concerns 1and 2 of reviewer 2 is essential. The second two comments are optional – they will improve the study, but we leave it for you to decide.

Reviewer #1:

This study investigates an additional mechanism to traditional transcriptional regulation through the use of a randomized synthetic promoter controlling the expression of a bottleneck gene. This work provides substantial evidence supporting their hypothesis of allele-specific stochastic tuning driven by histone modification, and addresses several competing hypotheses, such as evolutionary pressure and global transcriptional changes. In total, we would recommend acceptance of this manuscript.

Reviewer #2:

This paper presents a new striking theory on gene expression. It suggests that at the absence of an evolved cellular program to regulate gene expression according to the environmental conditions cells might resort to stochasticity to govern transcription of relevant genes. The paper suggests an intriguing feedback loop: stochastic noise allows certain cells to express the right gene to the right level (and other cells to the "wrong" level), these cells that, due to chance, expressed the protein to the right level get a signal to keep inducing the gene that improved their fitness. The presumed feedback allows cells to "know", somehow, that they should keep inducing that gene that conferred the high fitness or keep reducing genes if reduction improved their fitness; cells are also assumed to know to reverse changes in expression (up or down) if change if previous step was maladaptive.

To test the notion, the authors built promoter-gene constructs in yeast in which they place a needed gene under a new promoter context. They starve the cell for the metabolite that is produced by the gene, forcing the cells to find new ways to express the needed gene. They use diverse unrelated promoters (noisy or synthetic) and they measure recovery from starvation under each. Despite being a novel challenge for the yeast, they find ways to overcome it within a few days. The authors claim that their observed recovery depends on promoter activity and noise, and they exclude mutations, and pre-challenge diversity as a source of adaptation. They strikingly show that the dynamics is dependent on several epigenetic regulatory proteins thus suggesting that histone modifications are mediating this stochastic tuning.

The theory is intriguing, bold and novel. The result with the chromatin modification proteins is striking. Though not complete the new theory is certainly exciting and should be brought to the attention of the community. Thus, publication in eLife is certainly supported in principle.

1) The most striking aspect of the presented theory is that there exists a postulated feedback from the fitness into the expression of the gene that determines the fitness. If true, this is ground breaking. But I'm still missing a direct experimental demonstration of this central claim. One way to show that could have been based on time lapse microscopy: follow cells as they express the fitness-affecting gene and measure simultaneously their growth rate and expression of that gene. A fitness-to-expression feedback could have been detected here if cells that happen to induce the right gene to the right amount were found to be more fit (say if cell doubling was measured and tracked from single cells) AND if the fitness-affecting gene was shown to further increase its expression level (or further decrease its expression as predicted from 𝛥𝐸! = 𝑘 ∙𝑠𝑔𝑛(𝛥𝐹t ∙ 𝛥𝐸t-1) + 𝜂) in those fit cells. A good negative control would have been to look in parallel at another unrelated gene whose expression does not affect fitness.

2) Time scales: a central question regarding this theory is on compatibility of the time scales involved. Noisy behavior of a promoter usually has "memory" (or "mixing times) in the order of a cell cycle, i.e. a cell that expressed highly a protein due to a stochastic fluctuation would "remember" that fluctuation for only one cell cycle and then decay back to the population average (such mixing times are typically observed, but perhaps not here). I think the current theory is based on the premise that a stochastic fluctuation, if beneficial, would be sustained for days due to the positive feedback from fitness (it took the cells here 5 days to show recovery). I'm not sure if time scales are compatible. Maybe a direct measurement of mixing time, along with the simulation, can clarify this point.

3) The presented theory is based on the notion that noisy promoters would generate the phenotypic diversity, from which adaptation takes place. I would have thus expected the authors to place the URA3 gene under the control of both high- and low-noise promoters for a comparison. Instead the two natural promoters are said to be chosen based on their conferring high noise. Aren't we missing a low noise promoter for comparison? The synthetic promoter might confer that property, but (i) is it conferring low noise? (a noise measurement would have been helpful for all promoters); (ii) even if it does, wouldn't it be better if they used a natural promoter that's characterized by low noise? Perhaps the replacement of the (TATA-containing) PSAM3 with TATA-free PARF1 is very helpful in that respect, but I'm not sure they showed that this TATA-free alternative is indeed noise reduced.

4) Towards excluding potential effect of mutations, the authors sequenced the strains around the relevant cis region. Could it be that the duplication detected at the URA3-mRuby cassette is a genetic change that confers advantage?
