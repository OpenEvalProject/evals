# Peer review - Round 1

Editors:
- Sophie Helaine, Imperial College London United Kingdom

Reviewers:
- Alexander Westermann, Helmholtz Centre for Infection Research Germany

## Review text

DOI: [10.7554/eLife.49748.039](https://doi.org/10.7554/eLife.49748.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Genetically diverse Escherichia coli adopt a common transcriptional program in patients with urinary tract infections" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alexander Westermann (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. All reviewers agreed on the importance of your work on characterising the transcriptional program of strains directly from patients. However, they raised serious technical questions with respect to the different processing of the RNA samples from patients, mice and in vitro, and potential confounding factors that cannot be eliminated without extensive new experiments. If you wished to address all the reviewers' concerns, we would be willing to assess the suitability for publication of an extensively revised version of this manuscript.

Reviewer #1:

This manuscript continues a large body of work by Mobley and co-workers to define a UPEC virulence genotype during human UTI. The authors use RNAseq to characterise a transcriptional program shared by a genetically diverse group of 14 UPEC strains harvested directly from the urine of infected patients. This revealed a signature defining upregulation of genes involved in translation, and demonstrating that UPEC grow rapidly during human UTI.

A major strength of this work is the transcriptome analysis of UPEC growth during human UTI, and comparison of this to growth in vitro and growth in the mouse model of UTI. The conserved transcriptional signature of the core genome during human UTI led to the important discovery that reprogramming occurs, and results in the allocation of cellular resources to support rapid growth during human UTI. It was comforting to see a conserved profile of transcription in humans and mice, an important finding that will be of great value to the field. In a broader context, this work provides new insight into UPEC adaptation to the human urinary tract. The transcriptional program that defines rapid growth during human UTI provides a framework to design novel therapeutics that block this phenotype in UPEC, an urgent need in the context of rapidly increasing antibiotic resistance.

Overall, I have no substantive concerns regarding the data or major conclusions.

Reviewer #2:

In the present study, Sintsova et al. profile expression of the core genome of 14 UPEC isolates right upon their collection from UTI patients and compare it with the corresponding bacterial transcriptome patterns when grown in vitro. In doing so, the authors identify a conserved expression pattern shared among all isolates, which is associated with an increased expression of mRNAs encoding ribosomal proteins and a reduced expression of metabolic genes in the in vivo isolates compared to the in vitro cultures. Based on this finding, the authors conclude that in vivo UPEC reallocates its resources to increase proliferation at the expense of metabolic activity, and consequently, that bacterial growth may be enhanced in the patient's bladder as compared to in vitro conditions. This would imply that one or several elusive host factors (present in the bladder but absent from the sterile-filtered urine) would enhance UPEC growth.

My major concern is that the study lacks enough data to support this hypothesis. The growth rate is deduced from the number of sequencing reads that map to genes for ribosomal proteins. This measure happens to fit with the growth behavior in vitro, when the authors compare UPEC replication in LB and sterile urine. However, this does not necessarily mean that the same applies in vivo. Given that this is their major finding, the authors may want to further support this speculation by in vivo data, e.g. by determining CFU counts in their mouse model over time of infection. Also, what would speak against their hypothesis is that genes for other cellular functions required for growth (such as DNA replication, cell division, etc.) appear not to be differentially expressed in vivo vs. in vitro.

Also with respect to the generation and analysis of RNAseq data, I have some comments:

– It remains unclear if the authors sequenced bacterial total RNA or rRNA-depleted RNA. The MICROBEnrich kit used, depletes polyadenylated transcripts (eukaryotic mRNAs and certain lincRNAs) as well as eukaryotic rRNAs, but does not efficiently deplete bacterial rRNA. Also the Illumina ScriptSeq v2 kit per se, does not deplete ribosomal transcripts. Therefore, it appears unclear why the authors state that "… rRNA-depleted stranded cDNA libraries…" were constructed. By the way, if indeed not actively depleted, reads mapping to bacterial rRNAs should also be increased in the in vivo samples (as are reads mapping to ribosomal proteins). In general, plots or tables that inform about RNA class distributions (% reads mapping to mRNAs, rRNAs, tRNAs, etc.) in the individual samples would be helpful.

– Why didn't the authors include published datasets in their analysis? This would seem particularly obvious for the data derived from their own previous (pilot) study (Subashchandrabose et al., 2014) that was based on 5 samples taken together with the 14 samples analyzed here.

Reviewer #3:

The manuscript "Genetically diverse uropathogenic Escherichia coli adopt a common transcriptional program in patients with urinary tract infections", by Sintsova et al., presents an RNAseq-driven analysis of UPEC gene expression from 14 UTI patients. The main experiment is to compare the expression of the bacteria directly isolated from the patients to the expression of the bacteria after growth in filter-sterilized, pooled human urine in vitro. The primary result is that bacteria isolated from the urine of patients have high expression of genes encoding proteins involved in DNA and protein synthesis: ribosomal proteins, rRNA and tRNA modification proteins, purine and pyrimidine metabolism.

The primary result was examined with a few analyses on the patient vs. in vitro urine expression. The analysis was split early between virulence genes/accessory genes and "core" genes that are present in all the strains. The analysis focused relatively quickly on the core genes, which included all the DNA and protein synthesis genes noted above. Further analysis of the core genes resulted in a few other general features that differentiated patient (infection) from in vitro growth: downregulation of amino acid biosynthesis, downregulation of sugar metabolism, downregulation of most sugar transporters, and upregulation of amino acid transporters.

An important set of validation experiments was then done with one strain, HM43, which was grown in LB (considered a "rich" lab media), a new batch of filter-sterilized urine, and multiple urine samples from mice that had been infected in their bladders with HM43. Using% of reads mapping to genes encoding ribosomal proteins and to genes encoding catabolic enzymes showed that the in vivo mouse infection samples again had a high proportion of ribosomal reads and low catabolic reads, more similar to the human patient expression data and not matched by the LB-grown bacteria. This last comparison was the main test the effect of a faster growth rate per se.

The authors then conclude that there is an infection-specific transcriptional program which is dedicated to high growth rate in urine. They further noted that the downstream regulated genes for 22 transcriptional factors were differentially expressed between patient infections and in vitro urine growth, and speculate that some environmental cues may be sensed and thereby lead to the observed high expression of DNA and protein synthesis genes.

I have one primary technical question about the experimental design and a question about the context within the UTI field. First, the authors have had substantial experience with doing RNAseq from patient urines, and take care to attempt to minimize the time between urine sample collection and RNAProtect addition (to be applauded). Also, all samples according to the Materials and methods are also stored in RNAProtect. One remaining issue is that it states that the "bacterial content of patient samples was enriched using MICROBEnrich kit". This raises a potential confounding variable that seems reasonable for explaining a large scale consistent different between patient samples and in vitro urine samples. For the HM43 mouse experiment, it is stated that "eukaryotic mRNA was depleted using dynabeads covalently linked with oligodT". This would seem to leave the eukaryotic ribosomal RNA still in the sample, but sequencing and mapping statistics for this experiment (similar to Table 1 for the human samples) are not included to check on this. Therefore, I am wondering whether the in vivo mouse samples were also treated differently than the in vitro LB and urine samples. Regardless, the authors should clarify the methods particularly for whether the MICROBEnrich was used only on the patient samples and explicitly not on the in vitro urine samples, and also they should similarly provide a bit more detail on the processing of the mouse samples.

In addition, the primary result from this paper has largely been described before. Bielecki et al. (2014) performed RNAseq on 21 strains from human UTI patients, 4 of which were subsequently grown in LB for to get an in vitro RNAseq data set; also of note these authors used MICROBEnrich for host RNA removal on the human patient samples, and they did rRNA depletion with a MICROBExpress kit for the in vitro samples. I suggest that the authors more explicitly acknowledge this previous work and the general observations that have already been made, which will help them to either better differentiate their current study or strengthen the overall result shared by the two papers by providing additional validating data.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Genetically diverse uropathogenic Escherichia coli adopt a common transcriptional program in patients with UTIs" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Neil Ferguson as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alexander Westermann (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The work presented here is a revised version of a previous submission. The original paper was deemed very interesting by reviewers, who however had raised several key issues, notably potential confounding of results due to differences in in vitro vs. in vivo RNA isolation/processing in the lab. The reviewers now agree that you have provided substantial new data to address these concerns and would be willing to consider this manuscript positively for publication. However, there are a list of points that should be addressed before this could be considered.

Essential revisions:

1) Could you explain how you selected the extra dataset provided in Figure 1—figure supplement 5 that suggests that MICROBEnrich has little effect on bacterial gene expression? Importantly, were these some of the genes that showed differential expression between the in vivo and in vitro samples? It is essential to include, if not already tested, at least some of the r-protein-encoding mRNAs in this analysis given their importance in the study.

2) Table 3: Only a small percentage of the reads from the in vivo samples map to the UPEC genome. Could you explain what the remainder of the reads might be derived from? Would they map to the host genome (thus indicating that bacterial enrichment is rather low-efficient), or is there any evidence that some of those non-UPEC reads might be derived from other causative agents of UTI?
