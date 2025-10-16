# Peer review - Round 1

Editors:
- Wendy S Garrett, Harvard T.H. Chan School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95058.4.sa0](https://doi.org/10.7554/eLife.95058.4.sa0)

This study presents a valuable observation of how deletion of a major repair protein in bacteria can facilitate the rise of mutations that confer resistance against a range of different antibiotics. The data presented are convincing, and the authors addressed the concerns raised by the reviewers in their resubmission, improving the strength of their findings.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95058.4.sa1](https://doi.org/10.7554/eLife.95058.4.sa1)

Summary:

Jin et al. investigated how the bacterial DNA damage (SOS) response and its regulator protein RecA affects the development of drug resistance under short-term exposure to beta-lactam antibiotics. Canonically, the SOS response is triggered by DNA damage, which results in the induction of error-prone DNA repair mechanisms. These error-prone repair pathways can increase mutagenesis in the cell, leading to the evolution of drug resistance. Thus, inhibiting the SOS regulator RecA has been proposed as means to delay the rise of resistance.

In this paper, the authors deleted the RecA protein from E. coli and exposed this ∆recA strain to selective levels of the beta-lactam antibiotic, ampicillin. After an 8h treatment, they washed the antibiotic away and allowed the surviving cells to recover in regular media. They then measured the minimum inhibitory concentration (MIC) of ampicillin against these treated strains. They note that after just 8 h treatment with ampicillin, the ∆recA had developed higher MICs towards ampicillin, while by contrast, wild-type cells exhibited unchanged MICs. This MIC increase was also observed in subsequent generations of bacteria, suggesting that the phenotype is driven by a genetic change.

The authors then used whole genome sequencing (WGS) to identify mutations that accounted for the resistance phenotype. Within resistant populations, they discovered key mutations in the promoter region of the beta-lactamase gene, ampC; in the penicillin-binding protein PBP3 which is the target of ampicillin; and in the AcrB subunit of the AcrAB-TolC efflux machinery. Importantly, mutations in the efflux machinery can impact the resistance towards other antibiotics, not just beta-lactams. To test this, they repeated the MIC experiments with other classes of antibiotics, including kanamycin, chloramphenicol, and rifampicin. Interestingly, they observed that the ∆recA strains pre-treated with ampicillin showed higher MICs towards all other antibiotics tested. This suggests that the mutations conferring resistance to ampicillin are also increasing resistance to other antibiotics.

The authors then performed an impressive series of genetic, microscopy, and transcriptomic experiments to show that this increase in resistance is not driven by the SOS response, but by independent DNA repair and stress response pathways. Specifically, they show that deletion of the recA reduces the bacterium's ability to process reactive oxygen species (ROS) and repair its DNA. These factors drive the accumulation of mutations that can confer resistance towards different classes of antibiotics. The conclusions are reasonably well-supported by the data, but some aspects of the data and the model need to be clarified and extended.

Strengths:

A major strength of the paper is the detailed bacterial genetics and transcriptomics that the authors performed to elucidate the molecular pathways responsible for this increased resistance. They systemically deleted or inactivated genes involved in the SOS response in E. coli. They then subjected these mutants to the same MIC assays as described previously. Surprisingly, none of the other SOS gene deletions resulted in an increase in drug resistance, suggesting that the SOS response is not involved in this phenotype. This led the authors to focus on the localization of DNA PolI, which also participates in DNA damage repair. Using microscopy, they discovered that in the RecA deletion background, PolI co-localizes with the bacterial chromosome at much lower rates than wild-type. This led the authors to conclude that deletion of RecA hinders PolI and DNA repair. Although the authors do not provide a mechanism, this observation is nonetheless valuable for the field and can stimulate further investigations in the future.

In order to understand how RecA deletion affects cellular physiology, the authors performed RNA-seq on ampicillin-treated strains. Crucially, they discovered that in the RecA deletion strain, genes associated with antioxidative activity (cysJ, cysI, cysH, soda, sufD) and Base Excision Repair repair (mutH, mutY, mutM), which repairs oxidized forms of guanine, were all downregulated. The authors conclude that down-regulation of these genes might result in elevated levels of reactive oxygen species in the cells, which in turn, might drive the rise of resistance. Experimentally, they further demonstrated that treating the ∆recA strain with an antioxidant GSH prevents the rise of MICs. These observations will be useful for more detailed mechanistic follow-ups in the future.

Weaknesses:

Throughout the paper, the authors use language suggesting that ampicillin treatment of the ∆recA strain induces higher levels of mutagenesis inside the cells, leading to the rapid rise of resistance mutations. However, as the authors note, the mutants enriched by ampicillin selection can play a role in efflux and can thus change a bacterium's sensitivity to a wide range of antibiotics, in what is known as cross-resistance. The current data is not clear on whether the elevated "mutagenesis" is driven by ampicillin selection or by a bona fide increase in mutation rate.

Furthermore, on a technical level, the authors employed WGS to identify resistance mutations in the ampicillin-treated wild-type and ∆recA strains. However, the WGS methodology described in the paper is inconsistent. Notably, wild-type WGS samples were picked from non-selective plates, while ΔrecA WGS isolates were picked from selective plates with 50 μg/mL ampicillin. Such an approach biases the frequency and identity of the mutations seen in the WGS and cannot be used to support the idea that ampicillin treatment induces higher levels of mutagenesis.

Finally, it is important to establish what the basal mutation rates of both the WT and ∆recA strains are. Currently, only the ampicillin-treated populations were reported. It is possible that the ∆recA strain has inherently higher mutagenesis than WT, with a larger subpopulation of resistant clones. Thus, ampicillin treatment might not, in fact, induce higher mutagenesis in ∆recA.

Summary of revised manuscript:

In their revisions, the authors have addressed my major concerns with additional experiments and changes to the text. Thank you!


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95058.4.sa2](https://doi.org/10.7554/eLife.95058.4.sa2)

Summary:

In the present work, Zhang et al investigate the involvement of the bacterial DNA damage repair SOS response in the evolution of beta-lactam drug resistance in Escherichia coli. Using a combination of microbiological, bacterial genetics, laboratory evolution, next-generation, and live-cell imaging approaches, the authors propose short-term (transient) drug resistance evolution can take place in RecA-deficient cells in an SOS response-independent manner. They propose the evolvability of drug resistance is alternatively driven by the oxidative stress imposed by accumulation of reactive oxygen species and compromised DNA repair. Overall, this is a nice study that addresses a growing and fundamental global health challenge (antimicrobial resistance).

Strengths:

The authors introduce new concepts to antimicrobial resistance evolution mechanisms. They show short-term exposure to beta-lactams can induce durably fixed antimicrobial resistance mutations. They propose this is due to compromised DNA repair and oxidative stress. Antibiotic resistance evolution under transient stress is poorly studied, so the authors' work is a nice mechanistic contribution to this field.

Weaknesses:

The authors revisions have significantly addressed weaknesses previously identified earlier in the review process.
