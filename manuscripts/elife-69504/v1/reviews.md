# Peer review - Round 1

Editors:
- Audrone Lapinaite, https://ror.org/03efmqc40 Arizona State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69504.sa0](https://doi.org/10.7554/eLife.69504.sa0)

Prime editing (PE) is an emerging precision genome editing technology. It is based on the fusion of reverse transcriptase and Cas9 nickase guided by a modified guide RNA (pegRNA) to select the target site in the genomic DNA. The design of pegRNAs is not trivial and PE's editing efficiencies are low and highly dependent on the context. The authors of this manuscript have developed a surrogate reporter-based approach (PEAR) not only to identify but also to enrich for the cells that have been edited by PE. This approach will provide the means to better understand the molecular basis of PE (which could lead to the development of new, improved PEs) and improve the efficiency of PE mediated genome editing. This study, describing PEAR is of interest to the researchers in the basic biological, biomedical and agricultural sciences fields.


---

# Peer review - Round 1

Editors:
- Audrone Lapinaite, https://ror.org/03efmqc40 Arizona State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69504.sa1](https://doi.org/10.7554/eLife.69504.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "PEAR: a flexible fluorescent reporter for the identification and enrichment of successfully prime edited cells" for peer review at eLife. Your article is being evaluated by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation is being overseen by Didier Stainier as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jennifer Hamilton (Reviewer #3).

The main concern expressed by all four reviewers is that the PEAR technology has so far limited usefulness, at least as presented in the current version of the manuscript. In order to consider this manuscript for publication, we would like to see additional experiments demonstrating that this technology can be used to detect and enrich for PE edits in difficult-to-edit cell types and more elaborate prime edits beyond single nucleotide substitutions, such as insertions/deletions.

Reviewer #1:

Current reporter systems to detect prime editing outcomes are restricted to few target sequences and/or show a low signal. The aim of the study was to develop a reporter system for an easy, fluorescence-based detection of prime editing outcomes, that allows maximum flexibility for testing the target sequences and pegRNA designs in various cell types. Moreover, the authors aimed to use the developed reporter system as a plasmid-based surrogate marker to select/enrich for cells that undergo PE mediated chromosomal DNA modifications.

Strengths

The reporter is based on a split GFP protein separated by the last intron of the mouse Vim gene. The sequence of the functional 5' splice site is altered in such way, that splicing and therefore the GFP fluorescence is disrupted, however, they can be restored by prime editor harboring an appropriately designed pegRNA. In this case the DNA sequence that base pairs to the spacer region of the pegRNA is downstream of the splice site. This setup provides a gain-of-function fluorescent signal with minimal background and an unlimited flexibility to test and design pegRNAs for multiple target sequences and surrounding sequence context.

Since this setup allows to replicate the chromosomal site of interest on the surrogate reporter plasmid, it enables enrichment (~3 fold) of the cells that get edited at the chromosomal DNA site.

Since the reporter is on plasmid, it is easy to use, no need to create cell lines. In principle, it is not restricted to specific cell lines.

Weaknesses

Although the paper does have strengths, the main weakness of the paper is that not all of these strengths are directly demonstrated. In particular:

The authors imply that the surrogate reporter system they've developed is not restricted to one or a few cell lines. However, all the experiments were performed in one cell line (HEK293T).

The advantage of using prime editing instead of more efficient base editing is that this approach allows the introduction of all types of substitutions and/or precise indels. The authors demonstrated that their reporter system works well when PE is designed to substitute several nucleotides but there were no experiments performed to demonstrate how well this reporter system performs when designing pegRNAs to perform small or large indels.

1. The authors imply that the surrogate reporter system they've developed is not restricted to one or a few cell lines. The authors should demonstrate this by performing prime editing in different cells in the presence of their surrogate reporter system. It would be interesting to see if the PEAR would allow significant enrichment of PE edited cells such as K562 or U2Os which have quite low prime editing efficiencies (PMID: 31634902).

2. The authors aimed to demonstrate that indels introduced by nCas9 do not turn on GFP fluorescence (Figure 1c). However, this could result due to nCas9 being inactive during this experiment. The authors should perform an additional control experiment showing that nCas9 was active and introduced indels but at the same time did not turn on GFP fluorescence.

3. The advantage of using prime editing instead of more efficient base editing is that this approach allows the introduction of all types of substitutions and/or precise indels. The authors demonstrated that their reporter system works well when PE is designed to substitute several nucleotides. Is it possible to use this system for designing pegRNAs to perform small or large indels?

Reviewer #2:

Simon and colleagues report on the development of a fluorescent reporter system, PEAR, which facilitates the enrichment and isolation of cell populations edited by prime editors (PEs). The strength of this reported method is that it can increase the likelihood of identifying cells that have undergone successful prime editing at target loci. In addition, the relative ease of use of the reporter system will make it easily adoptable by other researchers. However, there are several weaknesses in the manuscript in its current form including but not limited to the following: (i) Relative limited number of target loci that were used to validate the PEAR-based system, (ii) Lack of demonstration that the PEAR-based system works across multiple cell lines including those recalcitrant to genome modification, (iii) Missing off-target analysis as it relates to PEAR-induced editing events, (iv) Insufficient statistical analysis, and (v) Missing comparisons to gold-standard methods of editing enrichment. Because of these significant weaknesses, I do not recommend the manuscript to be published in its current form.

I recommend the authors address the following points prior to publication:

(1) As it relates Figure 3b, the standard for analyzing these types of editing events would be an NGS/HTS analysis of the targeted loci to see the individual allelic outcomes from the editing. As in currently stands, the authors only perform Sanger sequencing of the bulk populations. On a related note, does PEAR-based enrichment also increase the frequency of indel formation relative to transfection or no-enrichment? The current Sanger sequencing-based analysis does not provide this sort of insight.

(2) In Figure 3b, the authors do not perform any off-target analysis of prime editor activity. At minimum, the authors should PCR amplify the most-likely off-target loci and confirm that PEAR-based enrichment does not increase likelihood of off-target events. In addition, the authors should ensure that the pegRNA and nicking sgRNA targeting the PEAR plasmids do not induce off-target edits.

(3) In Figure 3b, the authors perform comparison against reporters of transfection. However, much of the field are using reporters of expression for enriching gene editing events. The authors should make similar comparisons to demonstrate the utility of their method.

(4) The authors only perform analysis of PEAR in bulk sorted cell populations. Although such enrichment is useful the authors do not provide any analysis of clonally isolated cell populations to determine the utility of PEAR in such applications.

(5) The authors only perform analysis on 3 genomic loci which does not provide a good indication of the broad utility of PEAR-based enrichment strategies. It is recommended that the authors demonstrate the utility of PEAR-based enrichment methods in the context of additional loci including those that are recalcitrant to typical PE strategies. In addition, the authors should demonstrate the utility of PEAR in the context of other types of PE-driven edits (i.e. small deletions, insertions) in addition to single base pair changes.

(6) Is the fluorescent signal associated with the PEAR plasmids transient? Are there a certain number of passages required to lose the fluorescent signal? Along similar lines, the authors should at least discuss what strategies can be taken to ensure there is not genomic integration of the PEAR reporter plasmids.

(7) The authors only perform PEAR based enrichment with HEK293 cells, which are very amenable to gene editing. To demonstrate the broad utility of this tool the authors should perform additional experiments in other cells lines, including those such a primary cells or pluripotent stem cells which are resistant to genetic modification.

(8) Throughout the manuscript, information about statistical analysis, number of biological replicates, and other information related to scientific rigor are missing.

Reviewer #3:

Prime editing is an exciting new tool in the CRISPR genome editing toolbox which can introduce targeted sequence insertions, deletions and base substitutions. New strategies to enrich for prime edited cells would abrogate the need for time-consuming single-cell sorting and clonal expansion. Simon and colleagues sought to develop a method for easily recovering prime edited cells. Such a method would be useful, as prime editing thus far has only reached moderate levels of efficiency. To achieve this, the authors developed a fluorescence-on, plasmid-based reporter that, when successfully prime edited, repairs a damaged splice site and leads to expression of a fluorescent transgene.

The authors nicely demonstrate that sorting out fluorescent, reporter-positive cells enriches for successful prime editing in the cellular genome. Prime editing of the surrogate plasmid reporter robustly enriched for successful prime editing in a genomically-integrated transgene. Interestingly, this method was also successful when one pegRNA drove prime editing of the plasmid reporter and one pegRNA directed a single base change in endogenous genes (FANCF, RNF2, HEK3).

One key feature of prime editing is that it can be used to make complex genomic alterations such as templated sequence insertions. This has been used to epitope tag endogenous genes (FLAG/His6 tags) and make prime editing distinct from base editors, which aim to alter single base pairs. A weakness of the work presented by Simon and colleagues is that they limit testing of the PEAR reporter to enrichment of cells following single base pair modifications in endogenous genes. In this context, the PEAR reporter was very good at enriching for prime edited cells but it is an open question as to how well PEAR would allow for the enrichment of more complex prime edits (such as multiple base changes or sequence insertions/deletions). Additionally, it is unclear how well the PEAR reporter would enrich for prime-edited cells edited at low efficiency (<10%), where enrichment would be most valuable. Lastly, the PEAR reporter functioned well in the cell line tested (HEK293Ts) but it is unknown how this strategy would work in other immortalized cell lines or primary cells. The PEAR reporter would be a boon if it could successfully enrich for prime edited cell types that are not amenable to single cell sorting and clonal expansion (such as primary cells or cell lines that are difficult to grow up from a single cell, such as Calu-3s).

Together, the authors achieved their aim of developing a fluorescence-on reporter that allows for the enrichment of prime edited cells, both when the prime edit is made in a genomically-integrated transgene or at an endogenous genomic site. This tool will be useful for the genome editing community and/or researchers who wish to introduce minimal base pair changes in HEK293T cells.

In the discussion, the authors state that "The tolerance of the 5' splice site for substitutions makes the sequences of the target region of the PEAR plasmid easily adjustable." The manuscript would be strengthened if the authors demonstrate that this is true.

Reviewer #4:

The manuscript by Dorottya Simon and colleagues describes a reporter of prime editing activity, dubbed PEAR. Prime editing is a next-generation CRISPR-based genome editing strategy. Prime editing relies on a CRISPR enzyme appended with a reverse transcriptase and a stretch of single-stranded RNA that can be used as a template for a reaction that extends a genomic DNA "primer", ultimately incorporating the RNA-templated information into the genome. Some incarnations of prime editing incorporate a second, nicking CRISPR enzyme that can increase the frequency of desired outcomes. Prime editing efficiencies typically surpass those of homology-directed repair, but often lag behind those of base editing or cutting-based editing (the introduction of insertions/deletions). Prime editing outcomes remain somewhat unpredictable and the approach would greatly benefit from an improved "guidebook" that outlines the best practices for the technique. To this end, the PEAR reporter may facilitate high-throughput examination of new prime editing strategies, in turn resulting in a greater understanding of the technique.

A strength of this system is the substantial flexibility with respect to the spacer (targeting RNA / targeted DNA) sequence that can be used. A PAM (protospacer-adjacent motif) is required at the "business end" of the prime editing, but otherwise there is considerable freedom in terms of the guide RNA (spacer) that can be used. The PEAR system also allows enrichment of prime-edited populations, allowing the researcher to triple

A potential disadvantage is that the PEAR cassette – whether in plasmid form or following transfection or incorporation – will not be likely to capture all the qualities of a truly endogenous locus. Indeed, these qualities (and their diversity) play a critical role in determining why certain prime editing attempts fare drastically better than others. Loss of this diversity might limit the reporter's capacity for elucidating the determinants of efficient prime editing.

The following comments are intended to improve the manuscript.

"more precise CRISPR tools; base" … this should not be a semicolon. Consider a pair of dashes, and adjusting "developed, that can" to "developed, and these enzymes can"

"BEs'." no apostrophe needed; "of BEs" conveys the possessive.

Figure 1e: the black text can be hard to see when it is in front of the black data points.

"former observations that indels cannot, only substitution mutations" … This seems incorrect.
