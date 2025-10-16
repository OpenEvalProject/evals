# Peer review - Round 1

Editors:
- Urszula Krzych, Walter Reed Army Institute of Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33105.043](https://doi.org/10.7554/eLife.33105.043)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Single cell RNA-seq reveals hidden transcriptional variation in malaria parasites" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor.

Given the list of essential revisions, including new experiments, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

Summary:

Lawniczak et al., utilize cutting edge technology to inspect the transcriptional dynamics of two malaria parasite species at single-cell resolution. In addition to generating new scRNA data, the authors make good use of existing public datasets, thoroughly remapping to updated genomes and reanalyzing from scratch for more reliable comparisons to the current work. This paper reports evidence that the canonical waveform model of transcription during the intra-erythrocytic development cycle (IDC), based on bulk analysis of synchronized cultures, is actually characterized by more discrete transitions that are only evident at single-cell resolution. They further implicate transcription factors that are temporally associated with key transition points and go on to discuss IDC independent genes. This is very well written paper and it is a very nice addition to the literature. The study presents a great deal of well-curated data. Collectively, the reviewers considered this work to be of a valuable contribution to the literature on the subject of discrete gene expression that as has been thought comes in waves in Plasmodium.

Essential revisions:

1) There was an agreement amongst the reviewers that the authors need to provide a more thorough but tempered discussion of intraerythrocytic development cycle transcriptomics. The authors are also requested to provide a more complete and transparent description of the methodology, particularly describing filtering method, as it could be the source of discrepant interpretations.

2) One of the possibly exciting observations is that pir genes may be needed for fertilization. Based on what is shown in the spreadsheets, this appears to be true. However, members of multigene families are known to be problematic, as they may mitotically recombine during routine culture and reads can map to multiple places in the genome-for example, one that is mentioned by the authors (PBANKA_1246400), although not mapping perfectly to other pir genes, still gives an e values of zero in BLASTN owing to stretches of identity that may be 60 bases or more long (e.g. PBANKA_0700061.1)). Although the authors say that this shouldn't be a problem and that the filters/parameters that they used should appropriate it would be good to see some sort of supportive data to make sure this isn't an alignment artifact. Maybe the authors could generate a figure with the actual RNA-seq sequences for a few genes? The sequences that are obtained in this single cell method might have a significantly higher error than other methods, and this could create alignment problems. Alternatively, perhaps the authors may want to prove some orthologous evidence?

3) The depiction of a discontinuous pattern of gene expression throughout the life cycle is not particularly convincing. Two issues may confound this description. Firstly, that pseudotime does not scale evenly to time (i.e. one unit of pseudotime may equal minutes at one part of the lifecycle and hours at another). This would undermine the ability to detect abrupt shifts. Secondly, through the life cycle there is a tremendous increase in RNA abundance. The detectability of genes through the lifecycle would vary along with this (as would the robustness of scRNAseq).
