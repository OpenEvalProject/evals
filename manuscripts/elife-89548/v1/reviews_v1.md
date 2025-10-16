# Peer review - Round 1

Editors:
- Bruce Stillman, Cold Spring Harbor Laboratory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89548.4.sa0](https://doi.org/10.7554/eLife.89548.4.sa0)

The article addresses the mechanism of initiation of DNA replication in human cells by analyzing published data on the location of origins of DNA replication and the location of binding sites in the genome for ORC and MCM2-7 complexes. There are some useful analyses of existing data but there are concerns regarding the conclusion that there might be alternative mechanisms for determining the location of origins of DNA replication in human cells compared to the well-known mechanism known from many eukaryotic systems, including yeast, Xenopus, C. elegans, and Drosophila. The lack of overlap between binding sites for ORC1 and ORC2, which are known to form a complex in human cells, is a particular concern and points to the evidence for the accurate localization of their binding sites in the genome being incomplete.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89548.4.sa1](https://doi.org/10.7554/eLife.89548.4.sa1)

In the best genetically and biochemically understood model of eukaryotic DNA replication, the budding yeast, Saccharomyces cerevisiae, the genomic locations at which DNA replication initiates are determined by a specific sequence motif. These motifs, or ARS elements, are bound by the origin recognition complex (ORC). ORC is required for loading of the initially inactive MCM helicase during origin licensing in G1. In human cells, ORC does not have a specific sequence binding domain and origin specification is not specified by a defined motif. There have thus been great efforts over many years to try to understand the determinants of DNA replication initiation in human cells using a variety of approaches, which have gradually become more refined over time.

In this manuscript Tian et al. combine data from multiple previous studies using a range of techniques for identifying sites of replication initiation to identify conserved features of replication origins and to examine the relationship between origins and sites of ORC binding in the human genome. The authors identify (a) conserved features of replication origins e.g. association with GC-rich sequences, open chromatin, promoters and CTCF binding sites. These associations have already been described in multiple earlier studies. They also examine the relationship of their determined origins and ORC binding sites and conclude that there is no relationship between sites of ORC binding and DNA replication initiation. While the conclusions concerning genomic features of origins are not novel, if true, a clear lack of colocalization of ORC and origins would be a striking finding. However, the majority of the datasets used do not report replication origins, but rather broad zones in which replication origins fire. Rather than refining the localisation of origins, the approach of combining diverse methods that monitor different objects related to DNA replication leads to a base dataset that is highly flawed and cannot support the conclusions that are drawn, as explained in more detail below.

Methods to determine sites at which DNA replication is initiated can be divided into two groups based on the genomic resolution at which they operate. Techniques such as bubble-seq, ok-seq can localise zones of replication initiation in the range ~50kb. Such zones may contain many replication origins. Conversely, techniques such as SNS-seq and ini-seq can localise replication origins down to less than 1kb. Indeed, the application of these different approaches has led to a degree of controversy in the field about whether human replication does indeed initiate at discrete sites (origins), or whether it initiates randomly in large zones with no recurrent sites being used. However, more recent work has shown that elements of both models are correct i.e. there are recurrent and efficient sites of replication initiation in the human genome, but these tend to be clustered and correspond to the demonstrated initiation zones (Guilbaud et al., 2022).

These different scales and methodologies are important when considering the approach of Tian et al. The premise that combining all available data from five techniques will increase accuracy and confidence in identifying the most important origins is flawed for two principal reasons. First, as noted above, of the different techniques combined in this manuscript, only SNS-seq can actually identify origins rather than initiation zones. It is the former that matters when comparing sites of ORC binding with replication origin sites, if a conclusion is to be drawn that the two do not co-localise.

Second, the authors give equal weight to all datasets. Certainly, in the case of SNS-seq, this is not appropriate. The technique has evolved over the years and some earlier versions have significantly different technical designs that may impact the reliability and/or resolution of the results e.g. in Foulk et al. (Foulk et al., 2015), lambda exonuclease was added to single stranded DNA from a total genomic preparation rather than purified nascent strands, which may lead to significantly different digestion patterns (ie underdigestion). Curiously, the authors do not make the best use of the largest SNS-seq dataset (Akerman et al., 2020) by ignoring these authors separation of core and stochastic origins. By blending all data together any separation of signal and noise is lost. Further, I am surprised that the authors have chosen not to use data and analysis from a recent study that provides subsets of the most highly used and efficient origins in the human genome, at high resolution (Guilbaud et al., 2022).

References

Akerman I, Kasaai B, Bazarova A, Sang PB, Peiffer I, Artufel M, Derelle R, Smith G, Rodriguez-Martinez M, Romano M, Kinet S, Tino P, Theillet C, Taylor N, Ballester B, Méchali M (2020) A predictable conserved DNA base composition signature defines human core DNA replication origins. Nat Commun, 11: 4826

Foulk MS, Urban JM, Casella C, Gerbi SA (2015) Characterizing and controlling intrinsic biases of lambda exonuclease in nascent strand sequencing reveals phasing between nucleosomes and G-quadruplex motifs around a subset of human replication origins. Genome Res, 25: 725-735

Guilbaud G, Murat P, Wilkes HS, Lerner LK, Sale JE, Krude T (2022) Determination of human DNA replication origin position and efficiency reveals principles of initiation zone organisation. Nucleic Acids Res, 50: 7436-7450

Update in response to authors' comments on the original review:

While the authors have clarified their approach to some aspects of their analysis, I believe they and I are just going to have to disagree about the methodology and conclusions of this work. I do not find the authors responses sufficiently compelling to change my mind about the significance of the study or veracity of the conclusions. In my opinion, the method for identification of strong origins is not robust and of insufficient resolution. In addition, the resolution and the overlap of the MCM Chip-seq datasets is poor. While the conclusion of the paper would indeed be striking and surprising if true, I am not at all persuaded that it is based on the presented data.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89548.4.sa2](https://doi.org/10.7554/eLife.89548.4.sa2)

Tian et al. performed a meta-analysis of 113 genome-wide origin profile datasets in humans to assess the reproducibility of experimental techniques and shared genomics features of origins. Techniques to map DNA replication sites have quickly evolved over the last decade, yet little is known about how these methods fare against each other (pros and cons), nor how consistent their maps are. The authors show that high-confidence origins recapitulate several known features of origins (e.g., correspondence with open chromatin, overlap with transcriptional promoters, CTCF binding sites). However, surprisingly, they find little overlap between ORC/MCM binding sites and origin locations.

Overall, this meta-analysis provides the field with a good assessment of the current state of experimental techniques and their reproducibility, but I am worried about: (a) whether we've learned any new biology from this analysis; (b) how binding sites and origin locations can be so mismatched, in light of numerous studies that suggest otherwise; and (c) some methodological details described below.

-- I understand better the inclusion/exclusion logic for the samples. But I'm still not sure about the fragments. As the authors wrote, there is both noise and stochasticity; the former is not important but the latter is essential to include. How can these two be differentiated, and what may be the expected overlap as a function of different stochasticity rates?

-- Many of the major genomic features analyzed have already been found to be associated with origin sites. For example, the correspondence with TSS has been reported before:

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6320713/

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6547456/

-- Line 250: The most surprising finding is that there is little overlap between ORC/MCM binding sites and origin locations. The authors speculate that the overlap between ORC1 and ORC2 could be low because they come from different cell types. Equally concerning is the lack of overlap with MCM. If true, these are potentially major discoveries that butts heads with numerous other studies that have suggested otherwise.

The key missing dataset is ORC1 and ORC2 CHiP-seq from the same cell type. This shouldn't be too expensive to perform, and I hope someone performs this test soon. Without this, I remain on the fence about how much existing datasets are "junk" vs how much the prevailing hypothesis about replication needs to be revisited. Nonetheless, the authors do perform a nice analysis showing that existing techniques should be carefully used and interpreted.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89548.4.sa3](https://doi.org/10.7554/eLife.89548.4.sa3)

Summary: The authors present a thought-provoking and comprehensive re-analysis of previously published human cell genomics data that seeks to understand the relationship between the sites where the Origin Recognition Complex (ORC) binds chromatin, where the replicative helicase (Mcm2-7) is loaded, and where DNA replication actually begins (origins). The view that these should coincide is influenced by studies in yeast where ORC binds site-specifically to dedicated nucleosome-free origins where Mcm2-7 can be loaded and remains stably positioned for subsequent replication initiation. However, this is most certainly not the case in metazoans where it has already been reported that chromatin bindings sites of ORC and Mcm2-7 do not necessarily overlap, nor do they always overlap with origins. This is likely due to Mcm2-7 possessing linear mobility on DNA (i.e., it can slide) such that other chromatin-contextualized processes can displace it from the site in which it was originally loaded. Additionally, Mcm2-7 is loaded in excess and thus only a fraction of Mcm2-7 would be predicted to coincide with replication start sites. This study reaches a very similar conclusion of these previous studies: they find a high degree of discordance between ORC, Mcm2-7, and origin positions in human cells.

Strengths: The strength of this work is its comprehensive and unbiased analysis of all relevant genomics datasets. To my knowledge, this is the first attempt to integrate these observations. It also is an important cautionary tale to not confuse replication factor binding sites with the genomic loci where replication actually begins, although this point is already widely appreciated in the field.

Weaknesses: The major weakness of this paper is the lack of novel biological insight and that the comprehensive approach taken failed to provide any additional mechanistic insight regarding how and why ORC, Mcm2-7, and origin sites are selected or why they may not coincide.
