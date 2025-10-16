# Peer review - Round 1

Editors:
- Claude Desplan, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62507.sa1](https://doi.org/10.7554/eLife.62507.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper provides significant insights into the superfamily of olfactory receptors and how it evolved: Your discovery of GRLs in multiple unicellular organisms supports the claim that this is a very old family, even if the sequence conservation is pretty low. However, a major advance results from your analysis of the tertiary structure of these proteins that takes advantage of the power of Rosetta to provide evidence that the GRL proteins are distant members of the same superfamily. This represents a significant advance in our understanding of the origins of this superfamily of proteins.

Decision letter after peer review:

Thank you for submitting your article "A putative origin of insect chemosensory receptors in the last common eukaryotic ancestor" for consideration by eLife. Your article has been reviewed by four peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Piali Sengupta as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The reviewers found that the paper provides significant insights into this family of receptors: First, your discovery of GRLs in multiple unicellular organisms supports the claim that you are dealing with a large family with plant homologs, although the analyses of sequence conservation remains speculative. However, the major advance results from the tertiary structures of these proteins that take advantage of the power of trRosetta to provide evidence that the GRL proteins are distant members of the same superfamily. This represents a significant advance in our understanding of the origins of this superfamily of proteins.

However, the reviewers had also two major concerns: One is the serious lack of technical details and you must provide more information about how many genomes were used in your initial search and discuss whether it was exhaustive or so stringent that more members of the family likely exist: Providing more technical details will help make the work more accessible. The second point is that functional data would be very useful, e.g. showing biochemically that distant members behave similarly to the fly proteins, or that they serve (or not!) as ligand-gated channels. If you have already acquired this type of data, they would strengthen your paper. However, a discussion of possible molecular functions would be sufficient in the absence of such data.

Reviewer #1:

Vertebrate and nematode odorant receptors (ORs) function as GPCRs, while insect ORs were derived from gustatory receptors (GRs) and function as ligand gated ion channels. However, the evolutionary origin of insect GRs is not clear. The manuscript of Benton, Dessimoz and Moi titled "A putative origin of insect chemosensory receptors in the last common eukaryotic ancestor" answered this key question. Following the previous studies that identified GR-like proteins (GRLs) in animals, and GR homologs, known as the DUF3537 domain-containing proteins in plants, they further identified and performed phylogenetic analysis on GRL proteins in unicellular eukaryotic organisms, including fungi, protists, and algae, the common ancestor of plants and animals.

Overall, the topic of this manuscript is very interesting and well written. The data are solid. Several key points have been addressed, including role of TM7, consistent predicted orientation of TM domains, presence of intracellular loops (like ORCO), conserved vs diverse regions on GRL proteins, and same origin for plant and animal GRLs. Therefore, I strongly recommend for publication, after the authors properly address the following concerns:

1) The major weakness is that there is no functional analysis. If any of GRL proteins is predicted to be a canonical chemical sensor, would it be possible to utilize Xenopus or another system to test the hypothesis?

2) If functional study is currently a big challenge, could the authors perhaps add some validation on GRL protein localization in a unicellular eukaryote? I wonder if antibody could be made and used to test membrane localization of GRL, or a tagged protein could be ectopically expressed in a cell line (or yeast).

3) "heteromeric (probably tetrameric) complexes composed of a tuning OR, which recognises odour ligands, and a universal co-receptor, ORCO" This describes a dimeric complex with one OR and one ORCO. It seems not consistent with "probably tetrameric"

4) Introduction paragraph three provides examples of non-chemosensation functions of GRL proteins. I suggest to expand and add a table or a supplemental table, which should include currently known expression patterns and functions of GR and GRL proteins in animals and plants.

Reviewer #2:

In this work, Benton and colleagues consider the evolutionary origin of the immense insect chemoreceptor family, which includes odorant receptors (ORs) and gustatory receptors (GRs). Past sequence mining from the Benton lab and others has suggested that distant members of the GRL family were found in diverse Protostomia and also homologous to a family of uncharacterized plant proteins containing the Domain of Unknown Function 3537. However, despite multiple GRL lineages being present in early branching deuterostomes, GRLs have been completely lost from the chordate lineage suggesting recurrent independent losses, obscuring their exact evolutionary trajectory. Here Benton and colleagues extend their genome mining analyses to identify 17 sequences from fungi, protista and unicellular plants that share the same overall topology and some of the poorly conserved sequence features of this family. Finally, they use the extraordinary power of trRosetta to predict candidate GRL structures from the diverse lineages de novo and demonstrate that they share the same distinct architecture as an experimental structure of an OR. By far the most impressive part of the manuscript is the structure prediction since it would argue that these distantly related members, even bearing little sequence conservation, fold into the same distinct helical arrangement. If correct, this would argue that the GRL family is incredibly ancient, originating in the last eukaryotic ancestor, 1.5-2 Billion years ago, which has important implications for thinking about how this immense family arose.

Overall, I have a few concerns that should be addressed:

1) The Materials and methods are quite sparse and require a lot of effort by the reader to appreciate how well controlled and vetted their results are. Only 17 members of the family were found across the genomes of fungi, protista and unicellular plants, derived from an even smaller subset of species, which the authors acknowledge is extremely sparse and implies either that they propagated by lateral gene transfer or were independently lost many times, making their evolutionary origin still a bit uncertain. The authors should provide more information about how many genomes were used in their initial search and discuss whether it was exhaustive or so stringent that more members of the family likely exist.

2) One complication of the limited number of sequences from unicellular eukaryotes is that the structure prediction relies on multiple sequence alignments largely built from GRs. This was not obvious from the Materials and methods. I only know this because I took one of their putative GRL sequences and submitted it to the trRosetta website and three hours later got the same structure prediction as in Figure 3 and the MSA the trRosetta algorithm used for prediction. While the algorithm for trRosetta has been previously published, for a general audience the paper would benefit from more detail about how it was used-both what was required as input (apparently just a single sequence plugged into the trRosetta website) and how to evaluate the output, beyond physical inspection. For example, in Figure 3C the assignment of proteins to their groups seems like an arbitrary delimitation without further explanation, since the score/distances between proteins are marginally different. Only in the figure legend it states: TM-scores of 0.0-0.30 indicate random structural similarity; TM-scores of 0.5-1.00 indicate that the two proteins adopt generally the same fold. The authors thus suggest a TM score of 0.27 as meaning Orco and HsapAdipoR1 are unrelated but a score of 0.53 as being indicative that VbraGRL2 and AthaAT3G20300 are part of the same structural family, but provide insufficient information to the reader to understand whether this is a stringent cutoff or not.

3) One important caveat that the authors should discuss and address is that given that the de novo structure prediction relies heavily on GR sequence covariation, is there any possibility that tertiary structural similarity is imposed onto these more distant members of the GRL family? Ideally the de novo structure prediction would be truly independent and based on similar numbers of GRL sequences from single-celled eukaryotes but this does not seem possible.

4) The central advance of this study over past work from the Benton lab (Benton, 2015; Hopf et al., 2015) is the dramatic improvement in structure prediction algorithms, which provide tantalizing information about structural similarity (barring the caveat in the point directly above.) I appreciate that the authors don't overstate their claims, suggesting that these GRL proteins may not serve the same function in different organisms but likely form ligand gated channels. To really move into novel territory, I wish the authors could probe the functional or biochemical properties of these ancient GRLs a bit further. For example, for these proteins to serve as ion channels likely requires a multimeric organization. Native gels could biochemically demonstrate this, providing powerful additional evidence that these are part of the same family. Alternatively, could sequence covariation provide evidence for this (e.g. Hopf, 2014). Either way, it would be valuable to discuss this additional feature that does not immediately fall out of the trRosetta predictions.

Reviewer #4:

Benton et al. is a well written study on the evolution of insect chemosensory receptors that uses bioinformatics-based approaches to identify putative GRL homologs in several species of unicellular eukaryotes. Both sequence and structure-based approaches are utilized to buttress the authors arguments that fungal and protista GRL homologs are an evolutionary link to DUF3537 proteins they have previously identified in plants and algae thereby extending this evolutionary relationship to "the last common eukaryotic ancestor"

While I am generally supportive of the authors rationale and recognize they have been careful to appropriately qualify their hypothesis throughout this work, I am somewhat disinclined to place a high degree of definitive value on the ab initio structural predictions which underscores much of this analysis. Even so, and despite the fact these evolutionary relationships between animal and plant GRLs are unlikely to ever be definitively tested, this hypothesis seems to me to be reasonable. That said, I remain underwhelmed by their significance.

Reviewer #5:

The insect chemoreceptor superfamily of ligand-gated ion channels is one of the largest and most diverse protein families known. Partly as a result of their extreme divergence, the evolutionary origins of the superfamily have been obscure. Following up on a previous proposal of relationship to a protein family that is widespread in plants, the authors discovered several convincingly related proteins encoded by fungal, protist, and algal genomes. While the relationship with the plant protein family remains remarkably distant, their three-dimensional modeling of these diverse proteins reveals convincing similarity and hence suggests the superfamily originated at or before the eukaryotic origin.

I have no substantive concerns. Previous objections to the distant relationship to the plant protein family on the basis of lack of three shared introns are not decisive given the rampant loss of introns in the unicellular genomes examined here. The details of the three-dimensional modeling are not my expertise, however these authors previously employed a related technique to generate a remarkably good model for the insect odorant receptors that was mostly confirmed by subsequently generated experimental structure.
