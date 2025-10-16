# Peer review - Round 1

Editors:
- Karen Adelman, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41461.029](https://doi.org/10.7554/eLife.41461.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Reporter-ChIP-nexus reveals contribution of initiator sequence to RNA Polymerase II pausing" for peer review at eLife. Your article has been evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aviv Regev as the Senior Editor.

Summary:

In this work, the Zeitlinger lab uses ChIP-nexus (a high-resolution form of ChIP-seq developed in the Zeitlinger lab) combined with a reporter system to study the contribution of promoter DNA sequence to the stability of paused polymerase. Using D. pseudoobscura promoters in the reporter plasmid in a D. melanogaster genomic background, they show that initiation, pausing, and the stability of pausing are recapitulated on the plasmids. This is important validation of the usefulness of the system. Promoter swapping and targeted mutagenesis of reporter promoters then yielded three main results: 1) the downstream region of promoters was important for pause stability, 2) a TATA-box is associated with pause instability, and 3) a strong initiator consensus with a G at +2 was critical for pause stability.

The reviewers all found the ChIP-nexus technique to be powerful, with the potential for high throughput screens with this strategy. However, as presented here, the assay is very low throughput. Incredibly, most of the authors conclusions are drawn from a single perturbation of single test promoter sequence. The work herein is thus considered preliminary, and requires additional validation prior to publication.

In short, the very limited, highly context-dependent data presented in this manuscript reduces enthusiasm for both the assay and the strength of the authors' conclusions. If concerns can be addressed with additional experiments, however, the reviewers are happy to consider a revised manuscript.

Essential revisions:

1) The authors must test each of the promoter mutations in several promoter contexts to validate findings. We recommend that every mutation be tested in at least 3 different promoter backgrounds to allow for reasonable confidence in conclusions.

2) The drug triptolide has been used by a number of groups to measure the stability of paused RNAPII and all data thus far converges towards a median half-life of paused RNAPII on the order of around 5-10 min. Genes that have polymerase remaining at 1 h of triptolide treatment are thus extreme outliers. As such, it is a shame that the authors have selected this type of hyper-stable promoter for use in their assay, as it makes it very difficult- if not impossible- to extrapolate from this extreme case to normal promoter behavior. In the absence of experiments on a more typical promoter, the reviewers are concerned that the results presented here will not be broadly applicable. Thus, when additional promoters are tested, we strongly recommend that the authors select promoters with decay rates more in line with the average gene, and use a more relevant time point for triptolide treatment, on the order of 5-20 min.

3) To better support the authors claims, they should perform a genomic analysis with their existing data on the stability of pausing at promoters with various combinations of the TATA and Inr elements. They already have the melanogaster data from Kc cells +/- triptolide and should have plenty of sequencing depth given the number of plasmids analyzed. Thus, in theory, this would simply require analysis of the genomic reads without additional experimentation. This would serve to corroborate the results and generalize the model to more promoters.

4) The claim that the reporter assay recapitulates the genomic assay could also use strengthening. This point is supported by 8 genes in the current manuscript, which is probably not enough for statistically rigorous conclusions. Figure 2—figure supplement 2 shows the 8 examples, and there is quite some variability in them. The question is how much variability, how to quantify it, and whether or not conclusions can be made given this variability. Given that a lot of conclusions are drawn from comparing the shapes of these promoter distributions, I would think the extent to which they can be reliably made is important. dve, the gene selected for the majority of mutational tests, is an example that shows differences between genomic and reporter contexts.

One idea is to bin the promoters into, say 10-20bp bins, and compare the normalized read counts across the bins for the reporter and genomic assay. Then the mean squared error or the correlation coefficient can be computed comparing the reporter and the genomic assay, and the degree of variability can be measured across more genes. This would at least give us some context for how much variability can be expected, and if the differences observed due to the mutations are significantly more than that baseline difference. This analysis or something similar is considered critical.

5) The novelty of finding a strong initiator at highly paused genes is severely over-exaggerated and previous literature is inadequately cited. The connection between Initiator consensus elements, highly focused transcription initiation and high levels of paused RNAPII has appeared multiple times in the literature previously, at least as far back as 2008 (Hendrix et al., 2008), and also in 2010 (Gilchrist et al., 2010).

Further, pausing has been recapitulated on DNA sequences in vitro, thus we already know that DNA sequence is a major contributor to pausing. See many in vitro studies from the Gilmour lab (some cited) and also Adelman and Lis (2005).

Finally, the authors mention in the Discussion that functional data supporting a role for promoter sequences and pausing are missing. While they are correct that there is a dearth of these important functional studies, the Lis lab did a functional analysis pause elements in the Drosophila Hsp70 promoter, by inserting sequences that changed the position of these elements. See Kwak et al., 2013. Given that there are so few studies like this and the level of detail covering other aspects of the literature, I think this experiment is worth discussing in this context.

It doesn't take anything away from the authors' accomplishments to adequately cite previous research in a scholarly way. Appropriate citations must be added.

6) Also related to the ambiguity in the number of promoters involved in each analysis: In the section "The Inr strongly contributes to the degree of Pol II pausing", I think it would be enhanced if the text listed the number of promoters examined for each group. For example, the text says "We first analyzed the naturally occurring Inr sequences from TATA-containing promoters versus those of stably paused promoters". I would like to know when reading this how many promoters are in each set leading to the observations e.g. that TATA-containing promoters have fewer Gs at the +2 position. In particular, when reading the caption for Figure 5A, it says n=132, and this implied that the other panels also used 132 promoters. However I expect that the other panels were based on a larger set (at least panel B). Ideally, more than 132 promoters would have been used for this analysis. Overall, added clarity on the number of promoter for Figure 5B and elsewhere would be helpful.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Reporter-ChIP-nexus reveals strong contribution of initiator sequence to RNA Polymerase II pausing" for consideration by eLife. This evaluation has been overseen by a Reviewing Editor and James Manley as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This revised version of the manuscript "Reporter-ChIP-nexus reveals strong contribution of initiator sequence to RNA Polymerase II pausing" is improved over the previous version as concerns the number of promoters and mutations analyzed. However, the way in which the data is discussed is still lacking in clarity, the caveats to interpretation are still not made clear, and the citation of prior literature is still lacking.

Thus, the manuscript is not determined to be acceptable in its current format. However, at this point the main criticisms of the work can all be addressed with text changes. Thus, we invite a resubmission if such changes are comprehensively made.

Essential revisions:

1) As the authors acknowledge in the Introduction, pausing takes place at all (or nearly all) genes. The duration and stability of pausing varies, but pausing appears to be an obligate part of the transcription cycle. Thus, the statement in the Abstract that "a G at the +2 position, is critical for Pol II pausing", is not accurate. The authors should change this to clarify that they mean 'stable pausing' or something of this sort. But a G and +2 is certainly not critical for the fundamental process of pausing itself.

2) The authors should note early in the Results section that 1h Triptolide treatment is a very long treatment, and that secondary effects are likely to occur during such extended intervals of transcription inhibition. Most labs use 2-20 minutes of Triptolide treatment to avoid such potential artifacts. We appreciate that the authors must rely on very long treatments to overcome the considerable noise in their assay, but this should be acknowledged as a potential source of artifact, and as a potential limitation to this study. This idea is briefly mentioned in the Discussion, but it must be noted in the Results section to make readers aware of this caveat.

3) The Bentley lab has recently questioned the interpretation of Triptolide data (in particular that using ChIP-based strategies such as in Shao et al. 17), noting that at some genes the Triptolide-mediated block to initiation traps Pol II at the TSS. This effect is evident at the Pino and pepck genes in this study. The authors should cite the recent work from the Bentley lab, and explain whether their ChIP-nexus assay gives them the spatial resolution needed to separate paused from un-initiated Pol II. This will help place the current work in a proper context, and will be clarifying for the field.

4) Based on the limited number of experiments aimed at testing the role of downstream promoter sequences, and the limitations in interpreting such experiments, the authors should be more circumspect in the conclusions drawn from these studies. We find it to be an over-reach that the authors conclude that downstream sequences affect pausing less than expected. Given the lack of data to this point, it is safest to note that this wasn't rigorously evaluated, and leave it at that.

5) We understand that the authors went into this study expecting the TATA box to elicit a strong effect on pausing, and that they were surprised that this is not the case. However, the large amount of inconclusive data presented on this topic, and the discussion thereof, is confusing. If the main conclusion is that TATA doesn't seem to have a strong effect on pause stability, and that any effect is highly context dependent and easily over-ridden by other sequences, then there is a much more straightforward way to present this. We strongly suggest that the authors simplify the presentation of the TATA data to focus on the main conclusion, rather than enumerating all the inconclusive or contradictory findings they obtained.

6) Given that computational assays have routinely defined the Inr consensus to have a G at +2, should this really be called the Inr-G variant? Instead, we recommend that this be considered the consensus. It should be clarified that this is the 'norm' and not something that deviates from the norm.

7) The discussion of pausing in its genomic context versus on a plasmid at the beginning of the Discussion is difficult to understand in light of the literature.

First, there have been a number of studies demonstrating that stable pausing does not involve downstream nucleosomes. The clearest of these demonstrations was Li and Gilmour, EMBO J, 2103). This paper should be cited and the authors should edit the first paragraph to reflect this work, and the fact that it is not at all surprising that pausing could take place on a plasmid or outside of the chromatin context.

8) It was demonstrated many years ago that pausing is rarely inhibitory in its endogenous context, because of the positive effect of the paused polymerase on maintaining open chromatin (Gilchrist G and D 2008). In this study, it was specifically demonstrated that the positive effect of pausing was clear in the endogenous context, but did not occur on a plasmid. Thus, it has been previously established that the effect of pausing on gene output is different on a plasmid than in the genome, and that any minor inhibitory effect seen on a plasmid is NOT borne out in the endogenous locus. Thus, it is perplexing that the authors claim that pausing is inhibitory based on their reporter assay- since this is known to be an inaccurate read-out of endogenous activity. Thus, the comments in the Discussion suggesting that the +2 G version of Inr would be inhibitory to transcription because it promotes pausing are unfounded and should be removed.
