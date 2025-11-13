# Fast turnover of genome transcription across evolutionary time exposes entire non-coding DNA to de novo gene emergence

## Authors

- Rafik Neme<sup>1</sup> ([ORCID: 0000-0001-8462-5291](https://orcid.org/0000-0001-8462-5291)) †
- Diethard Tautz<sup>1</sup> ([ORCID: 0000-0002-0460-5344](https://orcid.org/0000-0002-0460-5344)) †

### Affiliations

1. Max-Planck Institute for Evolutionary Biology Plön Germany

† Corresponding author

## Abstract

Deep sequencing analyses have shown that a large fraction of genomes is transcribed, but the significance of this transcription is much debated. Here, we characterize the phylogenetic turnover of poly-adenylated transcripts in a comprehensive sampling of taxa of the mouse (genus Mus), spanning a phylogenetic distance of 10 Myr. Using deep RNA sequencing we find that at a given sequencing depth transcriptome coverage becomes saturated within a taxon, but keeps extending when compared between taxa, even at this very shallow phylogenetic level. Our data show a high turnover of transcriptional states between taxa and that no major transcript-free islands exist across evolutionary time. This suggests that the entire genome can be transcribed into poly-adenylated RNA when viewed at an evolutionary time scale. We conclude that any part of the non-coding genome can potentially become subject to evolutionary functionalization via de novo gene evolution within relatively short evolutionary time spans.

## Introduction

Genome-wide surveys have provided evidence for 'pervasive transcription', i.e., much larger portions of the genome are transcribed than would have been predicted from annotated exons (Clark et al., 2011; Hangauer et al., 2013; Kellis et al., 2014). Most are expected to be non-coding RNAs (lncRNAs) of which some have been shown to be functional. However, the general conservation level of these additional transcripts tends to be low, which raises the question of their evolutionary turnover dynamics (Kutter et al., 2012; Kapusta and Feschotte, 2014). They are currently receiving additional attention, since they could be a source for de novo gene formation via a proto-gene stage (Carvunis et al., 2012; Ruiz-Orera et al., 2014; Neme and Tautz, 2014). It has been shown that de novo gene emergence shows particularly high rates in the youngest lineages (Tautz and Domazet-Loso, 2011), indicating that there is high turnover of such transcripts and genes between closely related species. Indeed, comparative studies of de novo genes between Drosophila species (Palmieri et al., 2014) and within Drosophila populations (Zhao et al., 2014) have confirmed this.

A number of possibilities have been discussed by which new transcripts are generated in previously non-coding regions, including single mutational events, stabilization of bi-directional transcription and insertion of transposable elements with promotor activity (Brosius, 2005; Gotea et al., 2013; Neme and Tautz, 2013; Wu and Sharp, 2013; Sundaram et al., 2014; Ruiz-Orera et al., 2015). Detailed analyses of specific cases of emergence of a de novo gene have shown that single step mutations can be sufficient to generate a stable transcript in a region that was previously not transcribed and translated (Heinen et al., 2009; Knowles and McLysaght, 2009). The unequivocal identification of de novo transcript emergence can only be made in a comparison between very closely related evolutionary lineages, where orthologous genomic regions can be fully aligned, even for the neutrally evolving parts of the genome (Tautz et al., 2013). While the available genome and transcriptome data for mammals and insects are sufficient to screen for specific cases of de novo transcript emergence, they are still too far apart of each other to allow a comprehensive genome-wide assessment. Our analysis here is therefore based on a new dataset that reflects a very shallow divergence time-frame for relatives of the house mouse (Mus musculus).

## Results

We selected populations, subspecies and species with increasing phylogenetic distance to the Mus musculus reference sequence (Keane et al., 2011). This reference was derived from an inbred strain of the subspecies Mus musculus domesticus and we use samples from three wild type populations of M. m. domesticus as the most closely related taxa, separated from each other by about 3,000–10,000 years. Further, we use samples from the related subspecies M. m. musculus and M. m. castaneus, which are separated since 0.3–0.5 million years. The other samples are recognized separate species with increasing evolutionary distances (Figure 1). We call this set of populations, subspecies and species collectively 'taxa' in the following. Altogether they span 10 million years of divergence, which corresponds to an average of 6% nucleotide difference for the most distant comparisons.

![Figure 1.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig1-v2.jpg)

**Figure 1.:** New genome sequences were generated for taxa with *. A common genome was constructed across all taxa (Figure 1—figure supplement 1) based on a mapping algorithm that is not affected by the sequence divergence between the samples (Appendix 1). Figure 1—figure supplement 2 shows the intersection of genome coverage between the named species.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The common genome represents the portion of the reference which is present and detectable across all species. The genome sequencing, processing and sequence analysis were done in the same way as for transcriptomes, effectively removing possible biases derived from sequencing and mapping. Note that the assignment of the common genome fraction was done after mapping all genomic and transcriptomic reads to the reference, i.e. the mapping process was not affected by a reduced mapping target.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Windows covered by all four species are used as the common genome (shown as the intersection of all species).

We obtained genome sequence reads for all taxa and mapped them to the mouse reference genome, using an algorithm that was specifically designed to deal efficiently with problems that occur in cross-mapping between diverged genomes (Sedlazeck et al., 2013; see Appendix 1 for validation). All regions that could be unequivocally mapped for all taxa were then used for further analysis. We refer to this as the 'common genome' which allows comparisons on those regions of the genomes which have not been gained or lost along the phylogeny, i.e., are common across all taxa (Figure 1—figure supplement 1). It represents 71.7% of the total reference genome length (Figure 1—figure supplement 2). Hence, we are nominally not analyzing about a third of the total genome length, but this corresponds to the highly repetitive parts for which unique and reliable mapping of transcriptomic reads would not be possible. Also, changes in transcription derived from gain or loss of genomic regions do not contribute to the patterns described below.

We chose three tissues for transcriptome sequencing, including testis, brain and liver. Previous studies had shown that testis and brain harbor the largest diversity of transcripts (Necsulea and Kaessmann, 2014). We sequenced only the poly-A+ fraction of the RNA, i.e., our focus is on coding and non-coding exons in processed RNA.

We use non-overlapping sliding windows of 200nt to assay for presence or absence of reads within the windows and express overall coverage as the fraction of windows showing transcription (see methods for details). We use only uniquely mapping reads, implying that we neglect the contributions and dynamics at repetitive loci. We display three thresholds of window coverage, the minimum being coverage by at least a single read, while the higher ones represent at least 10 and 100 reads respectively. The first serves as a very inclusive metric of low-level transcription, with the drawback of potentially including noise into the analysis, due to stochasticity in sampling, while the others represent thresholds for more abundant transcripts that are unlikely to be affected by sampling noise.

Among the three tissues analyzed, liver has the lowest overall read coverage while brain and testis have similar overall levels (Figure 2A–C). Combining the data from all three tissues or triplicating the read depth for one tissue (brain) increases the overall coverage in a similar way (Figure 2D,E).

![Figure 2.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig2-v2.jpg)

**Figure 2.:** (A–C) Liver, brain and testis, respectively, sequenced at approximately the same depth. (D) Combination of samples from A–D. (E) Additional sequencing of brain samples at 3x depth, compared to B. (F) Combination of all samples, including additional brain sequencing. Three coverage levels are represented by colors from light blue to dark blue: window coverage with at least 1, 10 and 100 reads. Taxon abbreviations as summarized in Figure 1, with closest to the reference genome to the left of each panel and most divergent one to the right. Note that the slight rise in low read coverage for the distant taxa could partially be due to slightly more mismapping of reads at this phylogenetic distance (see Appendix 1 for simulation of mapping efficiency), but is also affected by a larger fraction of singleton reads (compare Figure 4—figure supplement 1).

Figure 2F shows the total coverage across all tissues and all sequencing runs, which amounts to an average of 50.0 ± 2.5% per taxon. Hence, for each tissue, as well as in this combined set, we observe a very similar coverage in all taxa, with only a slight increase in the low expressed fraction for the most distant comparisons (see also legend Figure 2). This more or less stable pattern across phylogenetic time could either be due to the same regions being transcribed in all taxa, or a more or less constant rate of turnover of gain and loss of transcription between taxa.

To test these alternatives, we have asked which part of the transcribed window coverage is shared between the taxa and which is specific to the taxa. For this, we consider three classes: i) windows that are found in a single taxon only, ii) windows that are found in 2–9 taxa, i.e. more than one but not in all and iii) windows shared among all taxa (Figure 3; Figure 3—figure supplement 1 shows an extended version where class ii) is separated into each individual group). However, such an analysis could potentially be subject to a sampling problem, i.e. not finding a transcript in a taxon does not necessarily imply true absence, but could also be due to failure of sampling. This would be particularly problematic for singleton reads, since the probability of falsely not detecting one in a second sample that expresses it at the same level is about 37%. However, given that we ask whether it is detected in any of the other 9 taxa, the probability of falsely not detecting it if it exists across all of them becomes small (0.01%) (see also further analysis on singletons below).

![Figure 3.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig3-v2.jpg)

**Figure 3.:** Three classes are represented: i) windows that are found in a single taxon only, ii) windows found in 2–9 taxa and iii) windows shared among all 10 taxa (from left to right in each panel). Windows with transcripts were first classified as belonging to one of the three classes, independent of their coverage, and were then assigned to the coverage classes represented by the blue shading (from light blue to dark blue: window coverage with at least 1, 10 and 100 reads). Taxon names as summarized in Figure 1. Figure 3—figure supplement 1 shows an extended version where class ii) is separated into each individual group. Relative enrichment of annotated genes in the conserved class is shown in Figure 3—figure supplement 2.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Windows with transcripts were first classified as belonging to each of the sharing categories (from 1 to 10), independent of their coverage, and were then assigned to the coverage classes represented by the blue shading (from light blue to dark blue: window coverage with at least 1, 10 and 100 transcripts). Taxon names as summarized in Figure 1.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** The effect is most evident for protein-coding genes, but still present for non-coding genes.

Between 1 and 7% of transcribed windows are unique to one taxon only, with the more distant taxa showing the higher percentages (Figure 3). Most of these taxon-specific transcripts are lowly expressed (<10 reads per window), but the more distant taxa (MAT and APO in Figure 3I,J) show also some more highly expressed ones. We find a total of 6566 windows with read counts >50 that occur in a single taxon only, mostly in the long branches leading to MAT (1638 windows) and APO (4485 windows), but some also between the most closely related taxa (43 windows for DOM, including populations; 38 windows for MUS, including populations).

Approximately 18% of windows show transcripts shared across all taxa. These include most of the very highly expressed ones (>100 reads per window), but also a fraction of the low expressed ones (Figure 3). They are also enriched in annotated genes, especially in exons of protein coding genes, but also in non-coding genes (Figure 3—figure supplement 2). The class ii) windows (sharing between 2 and 9 taxa in Figure 3) represents the genes showing more or less turnover between taxa, with more turnover the more distant they are of each other (Figure 3—figure supplement 1). This class constitutes cumulatively the largest fraction (between 26 and 33% of whole genome coverage - Figure 3), supporting the notion of a fast turnover of most of the transcribed regions between taxa.

The taxon-specific turnover of transcripts is also reflected in a distance tree of shared coverage. Taxa that are phylogenetically closer to each other share more transcripts, i.e. the tree topology mimics that of a phylogenetic tree based on molecular sequence divergence (Figure 4A,B). This implies that the turnover of the transcripts is not random, but time dependent. However, the relative branch lengths are much extended for the more closely related taxa compared to the molecular distances, implying that there is a particularly high turnover between them.

![Figure 4.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig4-v2.jpg)

**Figure 4.:** (A) Molecular phylogeny based on whole mitochondrial genome sequences as a measure of molecular divergence (black lines represent the branch lengths, dashed lines serve to highlight short branches). (B) Tree based on shared transcriptome coverage of the genome, using correlations of presence and absence of transcription of the common genome. All nodes have bootstrap support values of 70% or more (n = 1000). (C) Tree based on shared transcriptome coverage of singleton reads only from subsampling of the extended brain transcriptomes. Left is the consensus tree with the variance component between samples depicted as triangles, right is the same tree, but only for the branch fraction that is robust to sampling variance. Taxon names as summarized in Figure 1. Figure 4—figure supplement 1 shows the fraction of singletons in dependence of each sample in each taxon, Figure 4—figure supplement 2 in dependence of read depth. Figure 4—figure supplement 3 shows an extended version of the analysis shown in 4C for higher coverage levels.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A-C) Liver, brain and testis, respectively, sequenced at approximately the same depth. (D) Combination of samples from A–D. (E) Additional sequencing of brain samples at 3x depth, compared to B. (F) Combination of all samples, including additional brain sequencing. Light gray indicates singletons observed in each individual sample/taxon combination. Dark gray indicates singletons across the whole experiment, i.e. not re-detected in any other tissue or taxon. Taxon abbreviations as summarized in Figure 1, with closest to the reference genome to the left of each panel and most divergent one to the right. Note that the rise in singleton number for the distant taxa can be ascribed to the longer branch length, i.e. absence of closely related taxa in which the singleton could have been re-detected.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig4-figsupp2-v2.jpg)

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** We used the deep sequenced brain samples to estimate the proportion of sampling artifacts in terminal branches, and effectively subtracted the proportion of artifacts to obtain reliable phylogenetic signals. Each brain sample was split in three completely independent samples of 100 million reads. Top: Trees constructed using: regions covered only with one read in each taxon, regions covered by 1 and 5 reads (very low expression), regions covered by any reads, regions above 10 reads (mid expression) and regions above 100 reads (high expression). The percentage shown indicates the average level of sampling artifacts for each threshold, derived from the length of the terminal branches not found in all replicates of each taxon, i.e. the uncorrelated portion across samples of the same origin. These numbers are highest for the lowly expressed regions, and are lowest for the highly expressed regions, and are more or less constant within comparisons. Once subtracted, the phylogenetic signal remains robust. Taxon names as summarized in Figure 1. The figure part with the 1 read fraction corresponds to Figure 4C.

To assess in how much this could be due a sampling variance problem at low expression levels, we have separately analyzed the transcripts that are represented by single reads only, since these should be most sensitive towards sampling problems. Depending on read depth and tissue, they constitute about 2–12% of the common windows when assessed on a per sample basis (Figure 4—figure supplement 1). However, most of these singletons in a given sample were re-detected in another tissue or another taxon (Figure 4—figure supplement 1), such that less than 2% are present in a given taxon (Figure 4—figure supplement 1) and less than 7% cumulatively throughout the whole dataset (Figure 4—figure supplement 2). We used the extended brain sample reads, split them into three non-overlapping sets of about 100 Mill reads for each taxon and constructed trees out of these sets using only the singleton reads. This is the equivalent of repeating the same experiment three times. We find indeed differences in the resulting trees, i.e. there is a measureable sampling variance. By constructing a consensus tree, we can partition the data into a variable and a common component. We find that 88% of the branch length is influenced by sampling variance, while the remaining 12% still recover the expected topology (Figure 4C). When we use a read coverage of 1–5 for the same analysis, we find that 52% of the branch length are subject to sampling variance and for all reads combined it is 35% (Figure 4—figure supplement 3). Hence, at the 100 Mill read level, we have a noticeable effect of sampling variance, but this does not erase the underlying signal. Also, the analysis in Figure 4B is based on 600 Mill reads per taxon, where sampling variance is expected to be further lowered.

The high dynamics of transcriptional turnover between taxa raises the question whether all parts of the genome might be accessible to transcription at some point in evolutionary time. To explore this possibility, we used a rarefaction approach to simulate the addition of one taxon at a time and used the curve to predict the behavior of adding more taxa than the ones in the present study. We compared this approach to a curve of increasing depth of sequencing, by taking subsets at 10% intervals to understand whether depth or taxonomic diversity have different behavior in this respect. We assume that in each species only a subset of the genome is transcribed, therefore the increase in depth of sequencing would saturate at some point below 100%. Conversely, if each taxon is transcribing slightly different portions of the genome due to a steady turnover, increasing the total number of sampled taxa should increase the saturation more than the increase that could be achieved by sequencing depth. This is indeed what we find. The addition of taxa indeed leads to a further increase in transcriptomic coverage, with a generalized linear model best describing the data as increasing in a logarithmic fashion (Figure 5A). In contrast, we observe an asymptotic behavior of the curve for increasing depth of sequencing, with apparent saturation reached at 84.1%, close to the 83.2% that we have already achieved (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig5-v2.jpg)

**Figure 5.:** (A) Sequencing depth saturation as estimated from an increase in the number of taxa. (B) Sequencing depth saturation as estimated from increasing read number. Blue dots indicate increases per sub-sampled sequence fraction or taxon added from our dataset. Gray dotted line indicates the predicted behavior from the indicated regression, and gray area shows the prediction after doubling the current sampling either by additional taxa (A) or in sequencing effort (B). Each analysis was tested for logarithmic and asymptotic models. Best fit was selected from ΔBIC, with Bayes factor shown and qualitative degree of support shown. Standard deviations are shown as black lines in A, and are too small to display in B (note that due to the sampling scheme for this analysis, the values above 50% are not statistically independent and that the 100% value constitutes a single data point without variance measure).

Combined with the previous results, this allows two major conclusions. First, random transcriptional noise (technical or biological) or deficiencies in sampling low level transcripts should not be major factors in our analysis, since saturation with sequencing depth would not be possible under a singleton dominated regime. Furthermore, low level transcripts (including singletons) have detectable biological signal (Figure 4C). Second, the data are consistent with the above outlined ideas that the evolutionary turnover leads to steady – and almost unlimited – transcriptional exploration of the genome, when summed over multiple parallel evolutionary lineages and taxa.

The above overall statistical consideration would still allow for the possibility of the existence of a few scattered genomic islands that are not accessible to transcription because of structural reasons (so-called transcriptional deserts – Montavon and Duboule, 2012) or heterochromatically packed because they are not encoding genes required in the respective tissues. Hence, we analyzed also the size distribution of transcript-free genomic regions in our dataset. We find that the maximum observed length of non-transcribed regions is 6 kb (Figure 6), suggesting that apparent transcriptional deserts in one taxon are readily accessible to transcription in other taxa, at least for the non-repetitive windows of the genome that are analyzed here.

![Figure 6.](https://cdn.elifesciences.org/articles/09977/elife-09977-fig6-v2.jpg)

**Figure 6.:** Size distribution of regions not covered in any transcript (green) versus size distribution of regions with at least one transcript (blue).

## Discussion

Various studies have shown that many more regions of the genome are transcribed than are annotated as exons (Ponting and Belgard, 2010; Kapranov and St. Laurent, 2012). The significance of this additional transcription has been largely unclear and it has even been considered as noise, either biological or technical. Here we were able to trace the turnover of these extra transcripts. Our data suggest that many have sufficient stability to reflect a phylogenetic distance distribution that mimics the phylogeny of the taxa. Hence, they should not simply be considered as noise. Rather, their lifetime should be sufficient to expose them to evolutionary testing and in this way they become a substrate for de novo evolution of genes. On the other hand, they appear to have only a limited lifetime in case they do not acquire a function, i.e. there is also high turnover of the transcribed regions between taxa. This turnover has as a consequence that within a timespan of a few million years practically the whole genome is covered by transcription at some point in time, i.e. no major transcript-free islands exist.

We have here sampled only three tissues. If more tissues and more life stages were sampled, one would expect an even higher coverage of the genome within a given taxon. Such deep analyses have been done in the ENCODE projects (http://www.genome.gov/10005107) and they have confirmed pervasive transcription (Clark et al., 2011; Hangauer et al., 2013; Kellis et al., 2014) at the single-taxon level. Still, we expect that the turnover of transcribed regions between taxa would also apply to the other tissues and stages, i.e. evolutionary testing of new transcripts would relate to all tissues and stages. This turnover is contrasted by the set of conserved genes across taxa, for which even the expression levels may be maintained across larger evolutionary distances (Pervouchine et al., 2015).

We see a particularly large number of lineage-specific transcripts among the most closely related taxa. This becomes most evident in the distance tree in Figure 4B where the branch length of the three populations of M. m. domesticus, which have separated only a few thousand years ago, are almost as long as those of the sister species M. spretus that has separated almost 2 Mill. years ago. Although this is partially influenced by sampling variance of low expressed transcripts (Figure 4C), this suggests that at the very short evolutionary distances (thousands of years) there is an even higher turnover of transcripts than at the longer time frames (millions of years). Such a pattern of unequal rates suggests that weak selection could act against many newly arising transcripts, such that they can exist for a short time at a population scale, but not over an extended time. Hence, we expect that the presence of such transcripts will be polymorphic at the population level, similar as it has been shown in Drosophila (Zhao et al., 2014). We have done a preliminary analysis of transcriptional variance between four individuals of each of the taxa and find this expectation fulfilled, but a more extensive study is required to obtain reliable data at this level.

We expect that a fraction of new transcripts interacts with other genes and cellular processes, either via providing a positive function or via being slightly deleterious. Our data do not allow at present to speculate on how large this 'functional' fraction would be, but this could become subject to future experimental studies. It is also as yet open whether the transcripts exert their functions as RNAs or via translation products. The analysis of ribosome profiling data has shown that many RNAs that were initially classified as non-coding can be associated to ribosomes, i.e. are likely translated (Wilson and Masel, 2011; Carvunis et al., 2012; Ruiz-Orera et al., 2014). On the other hand, when tracing the origin of de novo genes, one finds frequently that they act first as RNA and acquire open reading frames only at a later stage (Cai et al., 2008; Kapranov and St. Laurent, 2012; Reinhardt et al., 2013 - see discussion in Schlötterer, 2015). For some of the de novo evolved genes in Drosophila it has been shown that they have assumed essential functions for the organism, such that knockouts of them are lethal (Chen et al., 2010). Global analyses of new gene emergence trends suggest that the de novo evolution process has been active throughout the evolutionary history (Neme and Tautz, 2013). Hence, the possibility of a transition from new transcript emergence over acquisition of reading frames towards assuming essential genetic functions is well documented.

The idea that many de novo transcripts are slightly deleterious is concordant with the fact that various cellular processes maintain a balance between RNA transcription and degradation (Houseley and Tollervey, 2009; Jensen et al., 2013). In yeast and mammals it has been shown that several molecular pathways exist that degrade excess transcripts, in particular the ones from bidirectional promoter activity (Jensen et al., 2013; Wu and Sharp, 2013). Hence, the fact that many of the transcripts found by deep sequencing occur only at low levels does not necessarily imply a low level of transcription, but could alternatively be due to fast targeting by a degradation machinery.

**Table 1.**
 Genome sequencing and read mapping information relative to the C57Bl/6 reference strain (GRCm38.3/mm10).


<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Uniquely mapping reads (MAPQ &gt;25)</th>
      <th>Mean coverage depth (window based)</th>
      <th>Reference coverage (% windows)</th>
      <th>Total sequence divergence*</th>
      <th>Accession Reads</th>
      <th>Accession BAMs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Apodemus uralensis</td>
      <td>4.46E+08</td>
      <td>40x</td>
      <td>78.23%</td>
      <td>5.60%</td>
      <td>ERS942341</td>
      <td>ERS946059</td>
    </tr>
    <tr>
      <td>Mus mattheyi</td>
      <td>5.58E+08</td>
      <td>52x</td>
      <td>77.19%</td>
      <td>4.50%</td>
      <td>ERS942343</td>
      <td>ERS946060</td>
    </tr>
    <tr>
      <td>Mus spretus</td>
      <td>7.71E+08</td>
      <td>52x</td>
      <td>93.91%</td>
      <td>1.70%</td>
      <td></td>
      <td>ERS946096**</td>
    </tr>
    <tr>
      <td>Mus spicilegus</td>
      <td>6.16E+08</td>
      <td>57x</td>
      <td>84.39%</td>
      <td>1.60%</td>
      <td>ERS942342</td>
      <td>ERS946061</td>
    </tr>
  </tbody>
</table>

_* The percentage of divergence was estimated from mappings using NextGenMap (Sedlazeck et al., 2013). Only uniquely mapping reads were considered and mapping quality greater than 25. Variation was estimated from the alignments using samtools mpileup (Li et al., 2009). Divergence was calculated as number of changes divided by the genome size.** Corresponds to study accession PRJEB11535. All other accessions deposited under studies PRJEB11513 and PRJEB11533._

**Table 2.**
 Transcriptome reads from each sample sequenced, mapped and normalized.


<table>
  <thead>
    <tr>
      <th>Taxon Code</th>
      <th>Tissue</th>
      <th>Lanes</th>
      <th>QC-passed reads</th>
      <th>Mapped reads</th>
      <th>(% total)</th>
      <th>Normalized subset</th>
      <th>(%total)</th>
      <th>(% mapped)</th>
      <th>Accession Reads*</th>
      <th>Accession BAMs**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DOMCB</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.30E+08</td>
      <td>1.26E+08</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>70%</td>
      <td>73%</td>
      <td>ERS946023</td>
      <td>ERS942305</td>
    </tr>
    <tr>
      <td>DOMCB</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.41E+08</td>
      <td>1.17E+08</td>
      <td>83%</td>
      <td>9.07E+07</td>
      <td>64%</td>
      <td>77%</td>
      <td>ERS946025</td>
      <td>ERS942306</td>
    </tr>
    <tr>
      <td>DOMCB</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.26E+08</td>
      <td>1.22E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>94%</td>
      <td>98%</td>
      <td>ERS946026</td>
      <td>ERS942307</td>
    </tr>
    <tr>
      <td>DOMMC</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.17E+08</td>
      <td>1.13E+08</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>78%</td>
      <td>81%</td>
      <td>ERS946027</td>
      <td>ERS942309</td>
    </tr>
    <tr>
      <td>DOMMC</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.34E+08</td>
      <td>1.09E+08</td>
      <td>81%</td>
      <td>9.07E+07</td>
      <td>68%</td>
      <td>84%</td>
      <td>ERS946029</td>
      <td>ERS942310</td>
    </tr>
    <tr>
      <td>DOMMC</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.42E+08</td>
      <td>1.37E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>83%</td>
      <td>87%</td>
      <td>ERS946030</td>
      <td>ERS942311</td>
    </tr>
    <tr>
      <td>DOMAH</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>9.49E+07</td>
      <td>9.15E+07</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>96%</td>
      <td>100%</td>
      <td>ERS946019</td>
      <td>ERS942301</td>
    </tr>
    <tr>
      <td>DOMAH</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.16E+08</td>
      <td>1.02E+08</td>
      <td>88%</td>
      <td>9.07E+07</td>
      <td>78%</td>
      <td>89%</td>
      <td>ERS946021</td>
      <td>ERS942302</td>
    </tr>
    <tr>
      <td>DOMAH</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.61E+08</td>
      <td>1.55E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>74%</td>
      <td>77%</td>
      <td>ERS946022</td>
      <td>ERS942303</td>
    </tr>
    <tr>
      <td>MUSKH</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.33E+08</td>
      <td>1.28E+08</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>69%</td>
      <td>72%</td>
      <td>ERS946035</td>
      <td>ERS942313</td>
    </tr>
    <tr>
      <td>MUSKH</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.03E+08</td>
      <td>9.07E+07</td>
      <td>88%</td>
      <td>9.07E+07</td>
      <td>88%</td>
      <td>100%</td>
      <td>ERS946037</td>
      <td>ERS942314</td>
    </tr>
    <tr>
      <td>MUSKH</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.36E+08</td>
      <td>1.31E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>87%</td>
      <td>91%</td>
      <td>ERS946038</td>
      <td>ERS942315</td>
    </tr>
    <tr>
      <td>MUSVI</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.23E+08</td>
      <td>1.19E+08</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>74%</td>
      <td>77%</td>
      <td>ERS946031</td>
      <td>ERS942317</td>
    </tr>
    <tr>
      <td>MUSVI</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.23E+08</td>
      <td>9.47E+07</td>
      <td>77%</td>
      <td>9.07E+07</td>
      <td>74%</td>
      <td>96%</td>
      <td>ERS946033</td>
      <td>ERS942318</td>
    </tr>
    <tr>
      <td>MUSVI</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.32E+08</td>
      <td>1.27E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>90%</td>
      <td>93%</td>
      <td>ERS946034</td>
      <td>ERS942319</td>
    </tr>
    <tr>
      <td>CAS</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.21E+08</td>
      <td>1.16E+08</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>76%</td>
      <td>79%</td>
      <td>ERS946039</td>
      <td>ERS942321</td>
    </tr>
    <tr>
      <td>CAS</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.23E+08</td>
      <td>1.01E+08</td>
      <td>82%</td>
      <td>9.07E+07</td>
      <td>74%</td>
      <td>90%</td>
      <td>ERS946041</td>
      <td>ERS942322</td>
    </tr>
    <tr>
      <td>CAS</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.23E+08</td>
      <td>1.19E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>96%</td>
      <td>100%</td>
      <td>ERS946042</td>
      <td>ERS942323</td>
    </tr>
    <tr>
      <td>SPI</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.34E+08</td>
      <td>1.29E+08</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>68%</td>
      <td>71%</td>
      <td>ERS946043</td>
      <td>ERS942325</td>
    </tr>
    <tr>
      <td>SPI</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.05E+08</td>
      <td>9.82E+07</td>
      <td>93%</td>
      <td>9.07E+07</td>
      <td>86%</td>
      <td>92%</td>
      <td>ERS946045</td>
      <td>ERS942326</td>
    </tr>
    <tr>
      <td>SPI</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.44E+08</td>
      <td>1.38E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>83%</td>
      <td>86%</td>
      <td>ERS946046</td>
      <td>ERS942327</td>
    </tr>
    <tr>
      <td>SPR</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.09E+08</td>
      <td>1.05E+08</td>
      <td>96%</td>
      <td>9.15E+07</td>
      <td>84%</td>
      <td>87%</td>
      <td>ERS946047</td>
      <td>ERS942329</td>
    </tr>
    <tr>
      <td>SPR</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.35E+08</td>
      <td>1.20E+08</td>
      <td>89%</td>
      <td>9.07E+07</td>
      <td>67%</td>
      <td>76%</td>
      <td>ERS946049</td>
      <td>ERS942330</td>
    </tr>
    <tr>
      <td>SPR</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.34E+08</td>
      <td>1.29E+08</td>
      <td>96%</td>
      <td>1.19E+08</td>
      <td>88%</td>
      <td>92%</td>
      <td>ERS946050</td>
      <td>ERS942331</td>
    </tr>
    <tr>
      <td>MAT</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.12E+08</td>
      <td>1.04E+08</td>
      <td>93%</td>
      <td>9.15E+07</td>
      <td>82%</td>
      <td>88%</td>
      <td>ERS946051</td>
      <td>ERS942333</td>
    </tr>
    <tr>
      <td>MAT</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.23E+08</td>
      <td>1.12E+08</td>
      <td>91%</td>
      <td>9.07E+07</td>
      <td>74%</td>
      <td>81%</td>
      <td>ERS946053</td>
      <td>ERS942334</td>
    </tr>
    <tr>
      <td>MAT</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.32E+08</td>
      <td>1.23E+08</td>
      <td>93%</td>
      <td>1.19E+08</td>
      <td>90%</td>
      <td>97%</td>
      <td>ERS946054</td>
      <td>ERS942335</td>
    </tr>
    <tr>
      <td>APO</td>
      <td>Brain</td>
      <td>0.33x</td>
      <td>1.36E+08</td>
      <td>1.18E+08</td>
      <td>87%</td>
      <td>9.15E+07</td>
      <td>67%</td>
      <td>78%</td>
      <td>ERS946055</td>
      <td>ERS942337</td>
    </tr>
    <tr>
      <td>APO</td>
      <td>Liver</td>
      <td>0.33x</td>
      <td>1.13E+08</td>
      <td>1.00E+08</td>
      <td>89%</td>
      <td>9.07E+07</td>
      <td>80%</td>
      <td>91%</td>
      <td>ERS946057</td>
      <td>ERS942338</td>
    </tr>
    <tr>
      <td>APO</td>
      <td>Testis</td>
      <td>0.33x</td>
      <td>1.38E+08</td>
      <td>1.20E+08</td>
      <td>87%</td>
      <td>1.19E+08</td>
      <td>86%</td>
      <td>99%</td>
      <td>ERS946058</td>
      <td>ERS942339</td>
    </tr>
  </tbody>
</table>

_All accessions deposited under studies PRJEB11533* and PRJEB11513**._

Our results provide an evolutionary dynamics perspective where emergence, functionalization and decay of gene functions should be seen as an evolutionary life cycle of genes (Neme and Tautz, 2014). De novo gene birth should no longer be considered as the result of unlikely circumstances, but rather as an inherent property of the transcriptional apparatus and thus a mechanism for testing and revealing hidden adaptive potential in genomes (Brosius, 2005; Masel and Siegal, 2009). Within this evolutionary perspective, any non-genic part of the genome has the possibility to become useful at some time.

**Table 3.**
 Additional sequencing effort, focused only on brain samples. Reads sequenced, mapped and normalized.


<table>
  <thead>
    <tr>
      <th>Taxon Code</th>
      <th>Tissue</th>
      <th>Lanes</th>
      <th>QC-passed reads</th>
      <th>Mapped reads</th>
      <th>(% total)</th>
      <th>Normalized subset</th>
      <th>(% total)</th>
      <th>(% mapped)</th>
      <th>Accession Reads</th>
      <th>Accession BAMs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DOMCB</td>
      <td>Brain</td>
      <td>1x</td>
      <td>3.89E+08</td>
      <td>3.76E+08</td>
      <td>97%</td>
      <td>3.19E+08</td>
      <td>82%</td>
      <td>85%</td>
      <td>ERS946024</td>
      <td>ERS942308</td>
    </tr>
    <tr>
      <td>DOMMC</td>
      <td>Brain</td>
      <td>1x</td>
      <td>3.76E+08</td>
      <td>3.64E+08</td>
      <td>97%</td>
      <td>3.19E+08</td>
      <td>85%</td>
      <td>88%</td>
      <td>ERS946028</td>
      <td>ERS942312</td>
    </tr>
    <tr>
      <td>DOMAH</td>
      <td>Brain</td>
      <td>1x</td>
      <td>3.46E+08</td>
      <td>3.35E+08</td>
      <td>97%</td>
      <td>3.19E+08</td>
      <td>92%</td>
      <td>95%</td>
      <td>ERS946020</td>
      <td>ERS942304</td>
    </tr>
    <tr>
      <td>MUSKH</td>
      <td>Brain</td>
      <td>1x</td>
      <td>4.64E+08</td>
      <td>4.49E+08</td>
      <td>97%</td>
      <td>3.19E+08</td>
      <td>69%</td>
      <td>71%</td>
      <td>ERS946036</td>
      <td>ERS942316</td>
    </tr>
    <tr>
      <td>MUSVI</td>
      <td>Brain</td>
      <td>1x</td>
      <td>4.13E+08</td>
      <td>4.00E+08</td>
      <td>97%</td>
      <td>3.19E+08</td>
      <td>77%</td>
      <td>80%</td>
      <td>ERS946032</td>
      <td>ERS942320</td>
    </tr>
    <tr>
      <td>CAS</td>
      <td>Brain</td>
      <td>1x</td>
      <td>4.35E+08</td>
      <td>4.21E+08</td>
      <td>97%</td>
      <td>3.19E+08</td>
      <td>73%</td>
      <td>76%</td>
      <td>ERS946040</td>
      <td>ERS942324</td>
    </tr>
    <tr>
      <td>SPI</td>
      <td>Brain</td>
      <td>1x</td>
      <td>4.31E+08</td>
      <td>4.16E+08</td>
      <td>97%</td>
      <td>3.19E+08</td>
      <td>74%</td>
      <td>77%</td>
      <td>ERS946044</td>
      <td>ERS942328</td>
    </tr>
    <tr>
      <td>SPR</td>
      <td>Brain</td>
      <td>1x</td>
      <td>3.87E+08</td>
      <td>3.73E+08</td>
      <td>96%</td>
      <td>3.19E+08</td>
      <td>82%</td>
      <td>85%</td>
      <td>ERS946048</td>
      <td>ERS942332</td>
    </tr>
    <tr>
      <td>MAT</td>
      <td>Brain</td>
      <td>1x</td>
      <td>3.62E+08</td>
      <td>3.40E+08</td>
      <td>94%</td>
      <td>3.19E+08</td>
      <td>88%</td>
      <td>94%</td>
      <td>ERS946052</td>
      <td>ERS942336</td>
    </tr>
    <tr>
      <td>APO</td>
      <td>Brain</td>
      <td>1x</td>
      <td>4.33E+08</td>
      <td>3.77E+08</td>
      <td>87%</td>
      <td>3.19E+08</td>
      <td>74%</td>
      <td>84%</td>
      <td>ERS946056</td>
      <td>ERS942340</td>
    </tr>
  </tbody>
</table>

_All accessions deposited under studies PRJEB11533* and PRJEB11513**._

## Material and methods

### Sampled taxa

The youngest divergence point sampled, at about 3,000 years, corresponds to the split between two European populations of Mus musculus domesticus(Cucchi et al., 2005) one from France (Massif Central = DOMMC) and one from Germany (Cologne-Bonn area = DOMCB) (Ihle et al., 2006). These European populations in turn have diverged from an ancestral M. m. domesticus population in Iran (Ahvaz = DOMAH) about 12,000 years ago (Hardouin et al., 2015). The European M. m. domesticus are also the closest relatives of the reference genome, the C57BL/6J strain Didion and de Villena, 2013).

We included two populations of Mus musculus musculus; one from Austria (Vienna = MUSVI) and one from Kazakhstan (Almaty = MUSKH). These two populations are supposed to have a longer divergence between then the European M. m. domesticus populations, but a more accurate estimate is currently not available. We set the divergence for analyses at around 10,000 years as an approximate estimate. M. m. domesticus has diverged from M. m. musculus and Mus musculus castaneus about 0.4 to 0.5 million years ago, with a subsequent divergence, not long after, between M. m. musculus and M. m. castaneus (Suzuki et al., 2013). We included M. m. castaneus (CAS) from Taiwan as a representative of the subspecies.

To account for longer divergence times, we included Mus spicilegus (SPI; estimated divergence of 1.2 million years); Mus spretus (SPR; estimated divergence of 1.7 million years)(Suzuki et al., 2013); Mus matteyii (MAT; subgenus Nannomys), the North African miniature mouse (estimated divergence of 6.6 million years) (Catzeflis and Denys, 1992; Lecompte et al., 2008), and Apodemus uralensis, the Ural field mouse (APO; estimated divergence of 10.6 million years) (Lecompte et al., 2008).

The population-level samples (M. m. domesticus and M. m. musculus) included are maintained under outbreeding schemes, which allows for natural polymorphisms to be present in the samples. All other non-population samples are kept as more or less inbred stock, and therefore fewer polymorphisms are expected. All mice were obtained from the mouse collection at the Max Planck Institute for Evolutionary Biology, following standard rearing techniques which ensure a homogeneous environment for all animals. Mice were maintained and handled in accordance to FELASA guidelines and German animal welfare law (Tierschutzgesetz § 11, permit from Veterinäramt Kreis Plön: 1401–144/PLÖ-004697).

A total of 60 mice were sampled, as follows: Eight male individuals from each population-level sample (outbreds), Iran (DOMAH), France (DOMMC), and Germany (DOMCB) of Mus musculus domesticus, and Austria (MUSVI) and Kazakhstan (MUSKH) of Mus musculus musculus. Four male individuals from the remaining taxa (partially inbred): Mus musculus castaneus (CAS), Mus spretus (SPR), Mus spicilegus (SPI), Mus mattheyi (MAT) and Apodemus uralensis (APO). Mice were sacrificed by CO2 asphyxiation followed immediately by cervical dislocation. Mice were dissected and tissues were snap-frozen within 5 min post-mortem. The tissues collected were liver (ventral view: front right lobe), both testis and whole brain including brain stem.

### Genome sequencing

One individual from each of M. spicilegus, M. spretus, M. mattheyi, and Apodemus uralensis were selected for genome sequencing. DNA was extracted from liver samples. DNA extraction was performed using a standard salt extraction protocol. Tagged libraries were prepared using the Genomic DNA Sample preparation kit from Illumina, following the manufacturers’ instructions. After library preparation, the samples were run in IlluminaHiSeq 2000 at a depth of approximately 2.6 lanes per genome. Library insert size is ~190bases and paired-end reads were 100 bases long. Library preparation and sequencing was performed at the Cologne Center for Genomics. Sequencing read statistics are provided in Table 1. Data are available under the study accessions PRJEB11513, PRJEB11533 and PRJEB11535, from the European Nucleotide Archive (http://www.ebi.ac.uk/ena/).

### Transcriptome sequencing

The sampled tissues of each taxon were used for RNA extraction with the RNAeasy Mini Kit (QIAGEN) and RNA was pooled at equimolar concentrations. RNA quality was measured with the Agilent RNA Nano Kit, for the individual samples and pools. Samples with RIN values above 7.5 were used for sequencing. Library preparation was done using the Illumina TruSeq library preparation, with mRNA purification (poly-A+ selection), following manufacturers’ instructions. Sequencing was done in Illumina HiSeq, 2000 sequencer. Libraries for each group were tagged, pooled and sequenced in a single lane, corresponding to approximately one third of a HiSeq2000 lane. Library insert size is ~190bases and paired-end reads were 100 bases long. Additional sequencing of the brain samples was performed to identify potential limitations in depth of sequencing. For this, each brain library was sequenced on a full lane of a HiSeq2000. All library preparation and sequencing was done at the Cologne Center for Genomics (CCG). Sequencing read statistics are provided in Tables 2 and 3. Data are available under the study accessions PRJEB11513 and PRJEB11533, from the European Nucleotide Archive (http://www.ebi.ac.uk/ena).

### Raw data processing

All raw data files were trimmed for adaptors and quality using Trimmomatic (Lohse et al., 2012). The quality trimming was performed basewise, removing bases below quality score of 20 (Q20), and keeping reads whose average quality was of at least Q30. Reads whose trimmed length was shorter than 60 bases were excluded from further analyses, and pairs missing one member because of poor quality were also removed from any further analyses.

### Mapping

The reconstruction of transcriptomes using high-throughput sequencing data is not trivial when comparing information across different species to a single reference genome. This is due to the fact that most of the tools designed for such tasks do not work in a phylogenetically aware context. For this reason, any approximation which deals with fractional data (i.e. any high-throughput sequencing setup available to this date) is limited by the detection abilities of the software of choice and by the quality of the reference (transcriptome and genome).

Given the high quality state of the mouse genome repositories, we decided to take a reference-based approach, in which all analyses are centered in the reference genome of the C57BL/6 laboratory strain of Mus musculus domesticus, which enables direct comparisons across all species based on the annotations of the C57BL/6 laboratory strain.

Transcriptome and genome sequencing reads were aligned against the mm10 version of the mouse reference genome (Waterston et al., 2002) from UCSC (Karolchik et al., 2014) using NextGenMap which performs extremely well with divergences of over 10% compared to other standard mapping software (Sedlazeck et al., 2013), as confirmed by our own simulations (Appendix 1). The program was run under default settings, except for --strata 1 and --silent-clip. The first option enforces uniquely mapping reads and the second drops the unmapped portion of the reads, to avoid inflating coverage statistics. This is particularly relevant around exon-intron boundaries, where exonic reads are forced into intronic regions unless this option is set.

We produced normalized versions of the alignments per tissue. This was achieved by counting the total amount of uniquely mapped reads in each taxon for each tissue, and sampling without replacement a fraction of each file which would result in the roughly the same absolute number of uniquely mapped reads for all samples of the same tissue (summarized in Table 2 and Table 3).

### Coverage statistics

We performed coverage statistics on 200 bp windows, to minimize problems derived from the fractional nature of the data, in which a few nucleotides could be absent from a sequenced fragment due to the preparation of the samples, low quality towards read ends, or a few mismatches during mapping. Coverage statistics were computed from normalized alignment files with the featureCounts program from the Subreads suite (Liao et al., 2014). In order to avoid counting reads twice if they would span two windows (which would be the case for most reads), we assigned reads to the window where more than half of the read was present.

Genomic reads were used as a metric of empiric mapability for the coverage statistics, i.e. to identify which regions can be reliably detected. For this, we removed from the mapping results against the reference genome (see above) all regions that were not mapped across the phylogeny based on the genomic reads from the taxa more than 1 Mill years apart. The remaining portion we call the ‘common genome’ in all analyses. It is important to highlight that this is not the same as synteny, since we did not perform any co-linearity analyses between fragments, but rather represent the mere presence in the species, in any possible order. The common genome serves to limit mapping artifacts, since the reads observed in each window must not only be uniquely mapping, but also be present and detectable in all the genomes considered.

We report coverage only from windows in the common genome for several reasons. First, we want to compare changes in transcription in regions which are present across all taxa, so the region must be present at the genome level. Second, the observation of transcriptome coverage on a region of the reference genome without genomic coverage from the respective taxon could represent mapping artifacts. Thus by enforcing coverage on both levels, and in all taxa at the genomic level, we reduce mapping artifacts and errors. Third, we assume that the transcriptional properties of the common genome should be general enough that they represent the properties of each of the genomes of the taxa under study. Summary data for coverage of all genomes and transcriptomes are available under the Dryad accession associated with this manuscript (doi:10.5061/dryad.8jb83).

### Reconstruction of phylogenetic relationships

We performed genome-wide correlations of coverage to infer distance between the taxa under study. Correlations of two types were initially used: rank-based (spearman correlation) and binary (phi correlation). From correlation matrices, we constructed Manhattan distance matrices and from those we further constructed neighbor-joining trees to describe the proximity between any two taxa based on shared transcriptome information. We focus mostly on the presence or absence of transcriptional coverage. For this reason, we used only the binary correlations in the figures. In this representation, closely related organisms have more shared transcriptomic coverage than distantly related organisms. Analyses were performed in R, using the function dist() from the stats package and nj() from the ape package (Paradis et al., 2004).

Additionally, whole mitochondrial genomes were obtained for each taxon as consensus sequences from mapped reads using samtools mpileup (Li et al., 2009). The sequences were aligned with MUSCLE (Edgar, 2004), and a NJ tree was constructed with the dist.dna() and nj() functions from the ape package Paradis et al., 2004). All trees were tested with 1000 bootstraps with the boot.phylo() function from the ape package. Reported nodes have a support of 70% or greater.

### Estimation of sampling variance from brain samples

The extensive sequencing of brain samples were used to obtain estimates of how sampling might affect the terminal branch lengths of trees based on low coverage regions. For this, we split the alignments into three non-overlapping sets of 100 million reads per taxon, such that each set would contain sets of independent observations. Paired-read relationships were maintained, so that pairs of the same fragments would be in the same set. From this, we obtained trees as mentioned before, and the portions of the branches of each taxon which were shared across sets were considered as robust to sampling biases, while the discordant portions between samples were considered to be due to sampling variance. Summary data from subsampled sets are available under the Dryad accession associated with this manuscript (doi:10.5061/dryad.8jb83).

### Rarefaction and subsampling

Transcriptome experiments tend to be limited by the depth of sequencing, with highly expressed genes being relatively easy to sample, and rare transcripts becoming increasingly difficult to find. Given the large amount of data generated, we investigated whether our data show signals of coverage saturation from subsets of the data of different sizes. The total experiment, comprising ten taxa, corresponds to 6.4 x 109 reads (or 6.4 billion reads). We subsampled (samtools view -s) portions of mapped reads for each taxon, ranging between 10% to 100%, at 10% intervals. The observation of coverage saturation in this case would indicate that our sequencing efforts likely cover most of the transcribed regions of the common genome. Summary data are available under the Dryad accession associated with this manuscript (doi:10.5061/dryad.8jb83).

In parallel, we estimated the individual and combined contribution of each taxon to the transcriptomic coverage of the common genome. Not all samples have the same phylogenetic distance to each other (some species have more representatives than others). To account for this we generated one hundred arrays of the ten taxa with random order, and recorded the coverage after the addition of each taxon in each array. The observation of coverage saturation in this setup would indicate that taxonomic sampling is sufficient to cover most of the potentially transcribed regions of the common genome.

In order to estimate whether our data continued to increase or approached saturation, we tested two alternative models: a generalized linear model with logarithmic behavior (ever increasing) or a self-starting nonlinear regression model (saturating). The best fit was decided based on the minimum BIC value between the two models, and an estimate of the Bayes factor was computed from the difference of BIC values and support was obtained from standard criteria (Kass and Raftery, 1995). Analyses were performed in R, using the functions glm(), nls(), SSasymp(), and BIC() from the stats package (R Core Team, 2014).

### Analysis of transcribed and non-transcribed regions across the genome

Transcribed and non-transcribed windows of the common genome were defined by the continuous presence or absence of transcriptomic coverage from mapping information of each taxon and tissue. Neighboring transcribed regions across species were combined to obtain stretches of transcriptionally active common genome.

### Enrichment of annotations from the mouse reference
