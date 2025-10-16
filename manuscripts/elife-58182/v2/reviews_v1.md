# Peer review - Round 1

Editors:
- Blake Wiedenheft, Montana State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58182.sa1](https://doi.org/10.7554/eLife.58182.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

While the mechanisms of CRISPR RNA-guided defense have been the subject of intense investigation, the regulatory mechanisms that govern the transcription of CRISPR loci remains relatively obscure. Here Stringer et al. demonstrate that Rho and Nus play opposing roles in regulating the length of CRISPR transcripts. Longer CRISPR transcripts result in more guides and may provide broad spectrum resistance, but short transcripts may result in higher concentrations of certain guides, providing higher levels of protection from fewer pathogens.

Decision letter after peer review:

Thank you for submitting your article "Transcription Termination and Antitermination of Bacterial CRISPR Arrays" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gisela Storz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Joe Bondy-Denomy (Reviewer #2).

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept manuscripts that they judge can stand as eLife papers without additional data, even if they feel that additional experiments would make the manuscript stronger. While the reviewers have identified additional experiments that would improve this work, and you are welcome to add these to the revised manuscript if conditions allow, the only required experiments are computational in nature.

Summary:

The authors construct a series of genetic mutants and use molecular methods to show that CRISPR transcription is terminated by Rho and that the Nus complex blocks Rho-dependent termination, resulting in longer CRISPR transcripts. The paper is well written, the results are convincing, and the work is of interest of a broad audience. However, it is not clear why the competing activities of Rho and Nus are important for regulation of these systems. When and where is the regulation of Rho and Nus relevant to the biological control of CRISPR expression? Are expression levels of Rho and Nus controlled in response to phage infection or plasmid conjugation?

Essential revisions:

Please include data for the H-NS knockout or explain why this is not included. Explain where the natural transcriptional start sites are located relative to the engineered promoter. Leader sequences are typically AT-rich and contain the promotor. What is the relevance of a GC-rich "Rut" if it is upstream of the natural promoter?

The authors detect SuhB occupancy in the CRISPR-II boxA region of S. Typhimurium (Figure 1), and from that observation conclude that Nus factors are also involved. SuhB is a relatively new addition to the Nus complex and only recently found to play a role in rRNA expression (Singh et al., 2016). It is unclear whether SuhB is always associated with Nus antitermination complexes, or if it might work alone, or with other factors at different promoters. Given this uncertainty and caveats of the Nus deletion/mutation experiments presented here, it is essential that the authors either perform additional experiments to test for relevant Nus factor(s) at the putative boxA sequences of both CRISPR arrays in S. Typhimurium, or revise the text to be more clear about the role of SuhB and the inferred role of Nus.

The authors show the high conservation of NusB in bacteria (Figure 7—figure supplement 1) to support the notion that Nus-mediated antitermination is a general mechanism employed in diverse CRISPR loci. However, it was SuhB which was detected at the CRISPR-II boxA sequence. The phylogenetic analysis should be performed on SuhB. Phylogenetic comparisons of CRISPRs, BoxA, SuhB and NusB may be necessary to speculate about the widespread distribution of this mechanism.

Figure 2B: Given the large difference in BCM treatment for the long construct, which has an ~10 fold impact over the BoxA mutation (which also has a 10-fold impact), this strong effect of the drug might necessitate a control transcript/fusion to assess the uptick in lacZ from any locus? Or is this BCM effect specific to the CRISPR array and therefore there is a second (or third or fourth) equally potent/important site that the authors have not identified?

Clarify why some experiments were only performed with CRISPR-II (Figures 1 and 2), while some were only performed with CRISPR-I (Figure 3 and Figure 1—figure supplement 1). Observations made about one locus were assumed to apply to the other. Include data for SuhB/Nus occupancy at boxA sequences for both CRISPR loci, and the effects of bicyclomycin on expression for each loci or explain why this has been omitted.

The boxA-dependent stimulation of promoter-distal spacer activity is assumed to be through a mechanism of antitermination. However, the data might equally support the possibility that SuhB facilitates/stimulates crRNA maturation rather than promoting antitermination, much like what was discovered at the rRNA operon (Singh et al., 2016). To distinguish between the two possibilities, it is necessary to check for RNAP occupancy at promoter -proximal vs -distal spacers or test the efficiency of CRISPR RNA processing with and without SuhB. Alternatively, temper the conclusion that the mechanism is antitermination SuhB dependent antitermination.

Clarify the statistical methods used in the ChIP-seq experiments. For example, in Figure 4A, it appears as though the purple data points indeed cluster away from the orange, but in Figure 4—figure supplement 2A, it is less clear which of the blue data points cluster away from the orange data points in a statistically significant manner.

Throughout the manuscript, it is implied that the proposed antitermination mechanism occurs in all CRISPR-Cas types, while experimental data was collected for only two Type I systems. It is important to explicitly state which CRISPR Type(s) were found to harbor boxA sequences (Figure 7A) to support the possibility that a general mechanism has been discovered and to clarify how this conclusion relates to the work presented by Lin et al., 2019.

Figure 7 was generated while working under the assumption that CRISPR arrays appear downstream of cas2. While this may be true for some CRISPR-Cas systems, this approach excludes many systems with slightly different genomic architectures. For a more unbiased approach, search for boxA sequences directly upstream of the first repeat in a CRISPR array. This approach is anticipated to provide more reliable evidence to support the general prevalence of boxA sequences upstream of CRISPR arrays.

The authors speculate that "Rho termination acts as a selective pressure to limit adaptation in species that lack an antitermination mechanism". However, the possible role of Rho in limiting adaption seems indirect at best. If Rho-dependent termination limits the number of different spacers that can be expressed from a single locus then this will limit selective pressures that maintain "older spacers", but the advantage this afford the host is unclear. Furthermore, role of Nus would be expected to have an opposing impact on CRISPR length, so it is unclear how this explains an abundance of short CRISPRs and the authors do not clarify how these observations fit with the numerous genomes that do have long CRISPRs.

Results first paragraph, specify what CRISPR-Cas Type and subtype you are working with.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Transcription Termination and Antitermination of Bacterial CRISPR Arrays" for further consideration by eLife. Your revised article has been evaluated by Gisela Storz (Senior Editor) and Blake Wiedenheft (Reviewing Editor).

We have reviewed the rebuttal and the revised manuscript. The revision sufficiently addresses the reviewer's concerns, with one important exception.

The authors provide convincing experimental evidence for the competing roles of Rho and Nus in CRISPR transcription, but I am still not convinced by the arguments about the how these factors impact CRISPR length.

One of the reviewers raised this concern during the review. They pointed to the following statement: "Rho termination acts as a selective pressure to limit adaptation in species that lack an antitermination mechanism". However, as the reviewer pointed out, "the possible role of Rho in limiting adaption seems indirect at best." In the rebuttal, the authors address the comment by stating that "Our data are insufficient to conclude that the presence of Rho causes many CRISPR arrays to be short, but we think this is likely in cases where there isn't an antitermination mechanism, and hence we discuss this, clearly framed as speculation." I agree that it is appropriate to speculate in the Discussion, but the third sentence of the Abstract states "We show that Rho termination functionally limits the length of bacterial CRISPR arrays". Data presented by the authors, clearly demonstrates that Rho limits the length of CRISPR transcripts and Nus antagonizes Rho-dependent termination, but as the reviewer points out, "the possible role of Rho in limiting adaption (i.e., length of the CRISPR locus) seems indirect at best".

Please clarify statements connecting the role of Rho to CRISPR length. Speculation should be omitted form the Abstract. In addition, please clarify the following statement "type II-C CRISPR-Cas systems have their CRISPR arrays oriented opposite to cas3". I suspect that the context of this statement is important, but I have read this several times and it still seems to me like the authors are suggestion that type-II systems have a cas3. Please clarify.
