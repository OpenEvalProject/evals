# Contesting the presence of wheat in the British Isles 8,000 years ago by assessing ancient DNA authenticity from low-coverage data

## Authors

- Clemens L Weiß<sup>1</sup>
- Michael Dannemann<sup>2</sup> ([ORCID: 0000-0002-7076-8731](https://orcid.org/0000-0002-7076-8731))
- Kay Prüfer<sup>2</sup>
- Hernán A Burbano<sup>1</sup> †

### Affiliations

1. Research Group for Ancient Genomics and Evolution, Department of Molecular Biology Max Planck Institute for Developmental Biology Tübingen Germany
2. Department of Evolutionary Genetics Max Planck Institute for Evolutionary Anthropology Leipzig Germany

† Corresponding author

## Abstract

Contamination with exogenous DNA is a constant hazard to ancient DNA studies, since their validity greatly depend on the ancient origin of the retrieved sequences. Since contamination occurs sporadically, it is fundamental to show positive evidence for the authenticity of ancient DNA sequences even when preventive measures to avoid contamination are implemented. Recently the presence of wheat in the United Kingdom 8000 years before the present has been reported based on an analysis of sedimentary ancient DNA (Smith et al. 2015). Smith et al. did not present any positive evidence for the authenticity of their results due to the small number of sequencing reads that were confidently assigned to wheat. We developed a computational method that compares postmortem damage patterns of a test dataset with bona fide ancient and modern DNA. We applied this test to the putative wheat DNA and find that these reads are most likely not of ancient origin.

## Introduction

The evolutionary reconstruction of the past has been greatly enriched by direct interrogation of ancient DNA (aDNA) from plants and animal remains (Shapiro and Hofreiter, 2014). Although a vast proportion of flora and fauna do not fossilize, traces of their DNA may be preserved in sediments allowing the characterization of past biodiversity (Pedersen et al., 2015). A challenge to exploiting such resources is the ubiquitous threat of contamination with exogenous DNA. Therefore, special sample preparation procedures have been developed to reduce DNA contamination (Cooper and Poinar, 2000). Nevertheless, it remains difficult to estimate how well preventive measures work. If contamination is a possible explanation for the result, it is crucial to exclude this possibility by giving positive evidence for the authenticity of aDNA (Prüfer and Meyer, 2015). Fortunately, a large number of full-length DNA sequences can be generated using next generation sequencing, which allows for the authentication of aDNA. In aDNA an excess of C-to-T (cytosine to thymine) substitutions occur at the 5′ and 3′ ends of molecules (or its mirror image G-to-A (guanine to adenine) at the 3′ end, depending on the library protocol employed). When considering the 5′ end of sequences, the excess of C-to-T substitutions is highest at the first base and decreases exponentially towards the center (Figure 1A). This pattern is the result of cytosine deamination to uracil in single stranded overhangs (Briggs et al., 2007). Since it is present in aDNA-derived sequences but absent in much younger samples, it has been used as an authentication criterion in aDNA experiments (Krause et al., 2010; Prüfer and Meyer, 2015).

![Figure 1.](https://cdn.elifesciences.org/articles/10005/elife-10005-fig1-v1.jpg)

**Figure 1.:** (A) C-to-T substitutions at the 5′ end from a whole library of historic Solanum tuberosum (ancient DNA). The line shows the fit with the exponential distribution and the box the goodness-of-fit p-value. (B) C-to-T substitutions at the 5′ end from a whole library of present-day Triticum aestivum (modern DNA). Line and box as in (A).

Smith et al. analyzed sediments from Bouldnor Cliff, a submerged archeological site in the United Kingdom, and suggested the presence of domesticated wheat 8000 years ago based on sedimentary ancient DNA (sedaDNA). This is 2000 years earlier than expected based on archeological remains in the British Isles and 400 years earlier than in nearby European sites (reviewed in Smith et al.). Since Smith et al. did not find wheat pollen or archeological remains associated with wheat cultivation, they conclude that the wheat presence in Bouldnor Cliff was the result of trading.

In total they produced ∼72 million Illumina reads, of which they robustly assigned 152 to wheat (Triticum), with dozens more (160 reads) to higher taxonomic ranks that include wheat. Smith et al. took state-of-the art preventive measures to avoid contamination and exercised great effort to ensure the accuracy and robustness of their phylogenetic assignments. The authors attempted to authenticate the aDNA molecules based on the expected excess of C-to-T substitutions, but because of the very small number of reads assigned to wheat, they failed to do so using standard approaches. As a result of that, the authors did not present any positive evidence for the ancient origin of their reads. Here we present an approach that compares the pattern of C-to-T substitutions in a set of test reads with the distributions of C-to-T substitutions in reads from known ancient- and modern-DNA and apply this approach to sedaDNA from Smith et al.

## Results and discussion

Although the excess of C-to-T substitutions at the 5′ end occurs at different magnitudes in samples of different ages, the exponential increase of substitutions towards the end is a ubiquitous pattern in aDNA studies (Sawyer et al., 2012). In order to score the presence of this pattern in various datasets, we fitted an exponential function and evaluated the goodness of fit by using a one-sided t-test to test for significant exponential decay. As expected, true aDNA libraries show significant goodness-of-fit p-values (Figure 1A), whereas non-significant goodness-of-fit p-values, neither decay nor growth, are observed in libraries derived from modern DNA (Figure 1B). A given C-to-T damage pattern plot can thus be summarized by its goodness-of-fit p-value that when it is significant indicates C-to-T exponential decay at the 5′ end (Figure 1A).

We resampled (with replacement) 10,000 sets of 150 sequences from a library of historic Solanum tuberosum collected in 1846 (Yoshida et al., 2013a). The number was selected to be comparable to the 152 reads that Smith et al. assigned to wheat. An empirical distribution of goodness-of-fit p-values was generated by performing the goodness-of-fit test for each subsample (Figure 2A). When we evaluate the sedaDNA goodness-of-fit p-value, we find that it falls within the upper 3% of subsamples with the least good fit. We can therefore reject the null hypothesis that the sequences assigned to wheat are as ancient as the historic S. tuberosum library. We repeated the whole procedure using this time a modern wheat library to generate the distribution of goodness-of-fit p-values (Figure 2A) and find a better match (p = 0.83). Thus, we cannot reject the hypothesis that the sequences assigned to wheat are of modern origin.

![Figure 2.](https://cdn.elifesciences.org/articles/10005/elife-10005-fig2-v1.jpg)

**Figure 2.:** (A) The histograms in the center panel show the empirical distributions of goodness-of-fit p-values of subsamples of 150 reads from ancient and modern DNA (same libraries as in Figure 1). The dotted red line indicates the location of the goodness-of-fit p-value from reads assigned to wheat in sedimentary ancient DNA. The four surrounding panels show cytosine to thymine (C-to-T) substitutions at the 5′ end extracted from different point of the goodness-of-fit p-value distributions, and from the reads assigned to wheat in sedimentary ancient DNA. (B) Variation of the empirical p-value of the test depending on the goodness-of-fit p-value of the whole library used to generate the empirical distribution. Numbers adjacent to the points indicate the percentage of C-to-T substitutions at first base. Red arrow indicates the aDNA library used as test in Figure 3A. Purple arrow indicates the library used to generate the empirical distribution of goodness-of-fit p-values in Figure 3A–C.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/10005/elife-10005-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** The line shows the fit with the exponential distribution. The goodness-of-fit p-value is indicated in the upper right corner.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/10005/elife-10005-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** The histograms shows the empirical distributions of goodness-of-fit p-values of subsamples of 150 reads from a 7.000-year-old Mesolithic human from La Braña site in Northern Iberia. The dotted red line indicates the location of the goodness-of-fit p-value from reads assigned to wheat in sedimentary ancient DNA.

We sought to investigate how the test behaves when the empirical distribution of goodness-of-fit p-values is generated from different aDNA libraries. For this purpose we used a set of samples from animal (Sawyer et al., 2012) and plant remains (Yoshida et al., 2013) with an age of 85–170 years before present, and scored the sedaDNA wheat sequences against distributions generated from these libraries (subsamples of 150 sequences again). We observed that the goodness-of-fit p-value for the libraries is positively correlated with the empirical p-value for the sedaDNA wheat sequences tested against them (Figure 2B). Using a significance level of 0.05, we rejected the hypothesis that the wheat sequences are of ancient origin with 7 out of 13 libraries used in our test (Figure 2B). Thus, the purportedly 8000-year old wheat sequences show a less pronounced deamination pattern than many plant and animal samples with an age of less of 200 years. Finally, we took a less conservative approach and scored the sedaDNA against a distribution of goodness-of-fit p-values (subsamples of 150 read) generated from a 7000-years-old human Mesolithic sample from la Braña site in Northern Iberia (Olalde et al., 2014). La Braña is a site with cold environment and stable thermal conditions that has yielded exceptionally well conserved human fossils with ∼50% of human endogenous DNA that reach a ∼15% C-to-T substitution rate at the 5′ end (Olalde et al., 2014a) (Figure 2—figure supplement 1). We could reject the null hypothesis that the sedaDNA reads are as ancient as the sample from la Braña (p = 0.0014), a sample that is closer in time with the allegedly 8000-year-old wheat reads (Figure 2—figure supplement 2). It is worth pointing out that almost all 10,000 subsamples from la Braña had a very low (close to 0) goodness-of-fit p-value, even though we subsample only 150 reads (Figure 2—figure supplement 2).

We assessed the statistical power of the test by testing both an aDNA (Figure 3A) and a modern DNA library (Figure 3B) against a distribution built from a bona fide aDNA library, while varying the number of sampled sequences. Whereas the hypothesis that a true aDNA library is ancient was never rejected (Figure 3A), the hypothesis that a modern library has ancient origin could be rejected only when sufficient number of sequences were used for the subsample test (in tests with more than 300 reads the median empirical p-value was always below 0.05) (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/10005/elife-10005-fig3-v1.jpg)

**Figure 3.:** (A) Variation of the empirical p-value of the test depending on the number of reads sampled from an ancient DNA library (indicated with red arrow in Figure 2B). (B) Variation of the empirical p-value of the test depending on the numbers of reads subsampled from modern DNA Triticum aestivum library (same library used to generate the distribution of empirical goodness-of-fit p-values in Figure 2A). (C) Variation of the empirical p-value of the test depending on the size of sample sets from sedimentary ancient DNA reads mapped directly to the T. aestivum genome. Box-and-whisker plots were built based on 1000 tests. Layers as reported in Smith et al. i.e. layer 1 (most superficial), layer 4 (more deep).

Finally, we skipped the phylogenetic curation step applied by Smith et al. to reduce the number of false positive wheat alignments, and mapped all reads sequenced by Smith et al. to the wheat genome. After stringent filtering of sedaDNA mappings we repeated our test varying the size of the subsample sets from 100 to 1000 reads. The empirical p-value was dependent on the number of reads tested, and declined with an increasing number of tested reads for all layers of sediments sequenced in Smith et al (Figure 3C). This pattern resembled the one obtained from a modern DNA library (Figure 3B). As for the phylogenetic curated 152 sequences, we were able to reject the hypothesis that the mapped reads are of ancient origin (mean p-value < 0.05 for all tests with more than 400 reads for layers 1–2 and 4, and 800 reads for layer 3). Our analysis also shows that the 152 sequences after phylogenetic curation are not a biased subsample from the distribution of all wheat-matching sequences.

We were able to reject the hypothesis that the sequences assigned to wheat by Smith et al. are of ancient origin. This is true even when we compared the putative 8000 year old sequences with only century old samples that show much lower deamination signatures. This means that a scenario in which wheat was transported to the Bouldnor Cliff site 8000 years ago is unwarranted. Our approach for authentication of aDNA can be used even with a very small number of sequences, and we hope that it will proof useful to test for positive evidence of authenticity for ancient DNA studies whose conclusions rely heavily on the ancient origin of the analyzed sequences.

## Materials and methods

### Read processing for bona fide ancient and modern DNA samples

Reads from most of the samples were downloaded from the European Nucleotide Archive (Table 1 and Supplementary file 1), with the exception of the Gorilla gorilla reads that were provided directly by the authors (Sawyer et al., 2012). Adapters were trimmed for both paired- and single-end runs using the program Skewer (version 0.1.120) using default parameters (Jiang et al., 2014). For paired-end runs (Supplementary file 1) forward and reverse reads were merged requiring a minimum overlap of 10 base pairs (bp) using the program Flash (version 1.2.11) (Magoc and Salzberg, 2011). Merged or single-end reads were mapped as single-end reads against their respective nuclear or organellar genomes: S. tuberosum nuclear genome (Potato Genome Sequencing Consortium et al., 2011), Solanum lycopersicum nuclear genome (The Tomato Genome Consortium, 2012), Triticum aestivum nuclear genome (International Wheat Genome Sequencing C, 2014), G. gorilla mitochondrial genome (Xu and Arnason, 1996), Homo sapiens nuclear genome (Genome Reference Consortium Human Build 37). The mapping was carried out using BWA-MEM (version 0.7.10) with default parameters, which include a minimum read length of 30 bp (Li, 2013). PCR duplicates were removed after mapping using bam-rmdup (available at https://github.com/udo-stenzel/biohazard), which computes a consensus sequence for each cluster of duplicated sequences. Alignments were stored in the bam format (Li et al., 2009).

**Table 1.**
 Provenance of samples


<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Type of DNA</th>
      <th>Age</th>
      <th>Reference</th>
      <th>Study ID</th>
      <th>Sample/run ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Metagenomics sample</td>
      <td>Sedimentary</td>
      <td>8030-7908*</td>
      <td>Smith et al., 2015</td>
      <td>PRJEB6766‡</td>
      <td>ERR567364‡</td>
    </tr>
    <tr>
      <td>Metagenomics sample</td>
      <td>Sedimentary</td>
      <td>8030-7908*</td>
      <td>Smith et al., 2015</td>
      <td>PRJEB6766‡</td>
      <td>ERR567365‡</td>
    </tr>
    <tr>
      <td>Metagenomics sample</td>
      <td>Sedimentary</td>
      <td>8030-7908*</td>
      <td>Smith et al., 2015</td>
      <td>PRJEB6766‡</td>
      <td>ERR567366‡</td>
    </tr>
    <tr>
      <td>Metagenomics sample</td>
      <td>Sedimentary</td>
      <td>8030-7908*</td>
      <td>Smith et al., 2015</td>
      <td>PRJEB6766‡</td>
      <td>ERR567367‡</td>
    </tr>
    <tr>
      <td>Metagenomics sample</td>
      <td>Sedimentary</td>
      <td>8030-7908*</td>
      <td>Smith et al., 2015</td>
      <td>PRJEB6766‡</td>
      <td>ERR732642‡</td>
    </tr>
    <tr>
      <td>T. aestivum</td>
      <td>Modern</td>
      <td>NA</td>
      <td>Chapman et al., 2015</td>
      <td>PRJNA250383‡</td>
      <td>SRR1170664‡</td>
    </tr>
    <tr>
      <td>S. tuberosum</td>
      <td>Ancient</td>
      <td>135†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR267886‡</td>
    </tr>
    <tr>
      <td>S. tuberosum</td>
      <td>Ancient</td>
      <td>137†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR267882‡</td>
    </tr>
    <tr>
      <td>S. tuberosum</td>
      <td>Ancient</td>
      <td>149†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR330058‡</td>
    </tr>
    <tr>
      <td>S. tuberosum</td>
      <td>Ancient</td>
      <td>165†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR267872‡</td>
    </tr>
    <tr>
      <td>S. tuberosum</td>
      <td>Ancient</td>
      <td>166†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR267868‡</td>
    </tr>
    <tr>
      <td>S. tuberosum</td>
      <td>Ancient</td>
      <td>166†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR957324‡</td>
    </tr>
    <tr>
      <td>S. tuberosum</td>
      <td>Ancient</td>
      <td>167†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR267868‡</td>
    </tr>
    <tr>
      <td>S. lycopersicum</td>
      <td>Ancient</td>
      <td>136†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR267884‡</td>
    </tr>
    <tr>
      <td>S. lycopersicum</td>
      <td>Ancient</td>
      <td>139†</td>
      <td>Yoshida et al., 2013</td>
      <td>PRJEB1877‡</td>
      <td>ERR267878‡</td>
    </tr>
    <tr>
      <td>G. gorilla</td>
      <td>Ancient</td>
      <td>83†</td>
      <td>Sawyer et al., 2012</td>
      <td>NA</td>
      <td>107¶</td>
    </tr>
    <tr>
      <td>G. gorilla</td>
      <td>Ancient</td>
      <td>100†</td>
      <td>Sawyer et al., 2012</td>
      <td>NA</td>
      <td>109¶</td>
    </tr>
    <tr>
      <td>G. gorilla</td>
      <td>Ancient</td>
      <td>100†</td>
      <td>Sawyer et al., 2012</td>
      <td>NA</td>
      <td>110¶</td>
    </tr>
    <tr>
      <td>G. gorilla</td>
      <td>Ancient</td>
      <td>103†</td>
      <td>Sawyer et al., 2012</td>
      <td>NA</td>
      <td>114¶</td>
    </tr>
    <tr>
      <td>Homo sapiens</td>
      <td>Ancient</td>
      <td>7000*</td>
      <td>Olalde et al., 2014</td>
      <td>PRJNA230689‡</td>
      <td>SRR1045127</td>
    </tr>
  </tbody>
</table>

_*B.P. (before present years).†Calculated from collection date (in years).‡IDs from the European Nucleotide Archive.¶IDs from Sawyer et al., 2012._

### Read processing for sedimentary DNA from Smith et al., 2015a

We used two different approaches to process the reads from sedimentary DNA (Smith et al., 2015).

Phylogenetic curated reads: we used a set of 152 reads assigned to tribe Triticeae and to genus Triticum by Smith et al. after phylogenetic curation. However, we consider the complete sequence and do not exclude the initial 10 nucleotides as was done in the original processing (Smith et al., 2015). Reads were then aligned to the wheat genome as described above.

All sedimentary DNA reads: we aligned independently reads from all four layers sequenced by Smith et al. to the T. aestivum nuclear genome (International Wheat Genome Sequencing C, 2014). Duplicates were removed and only alignments with mapping quality greater or equal than 30 were used for further analysis. Additionally, we include a sequence complexity filter based on entropy, which removed low complexity reads with entropy less or equal to 50. The entropy filtering was carried out with prinseq-lite (version 0.20.4) (Schmieder and Edwards, 2011).

### Exponential function fitting and calculation of goodness-of-fit p-value

For each set of aligned reads (complete libraries or subsamples) the C-to-T substitutions patterns along the 5′ end of the read were assessed using the program PMDtools (Skoglund et al., 2014). We fitted an exponential function to the frequency of C-to-T substitutions for the first 20 nucleotides at the 5′ end. The fitting was performed in R (http://www.r-project.org) using the nls function, which determines the nonlinear least squares estimates of the parameters in a nonlinear model. The fitting was carried out with the model formula: y ∼ N∗exp(−rate∗x). From the nls fitting we obtained the t-value and degrees of freedom for the rate parameter and then calculated a goodness-of-fit p-value by using a one-sided t-test.

### Generation of empirical distributions of goodness-of-fit p-values

Subsets of different alignment numbers were randomly sampled (with replacement) 10,000 times from alignments stored in the bam format (Li et al., 2009). The random sampling was performed using samtools view (Li et al., 2009). For every subset of alignments we assessed the fraction of C-to-T substitutions, fitted an exponential function and calculated a goodness-of-fit p-value as explained above.

### Calculation of test empirical p-value

Phylogenetic curated reads: we compare the goodness-of-fit p-value of our test set of 152 sedimentary DNA reads with distributions of goodness-of-fit p-values generated from bona fide modern and ancient DNA. For the distribution of goodness-of-fit p-values from aDNA, we count how many of them are equal or greater than the sedimentary DNA goodness-of-fit p-value. To calculate the empirical p-value of the test we subsequently divided this number by the total number of values in the empirical distribution. With this approach we test the null hypothesis that the test set of reads contains a signal of ancient DNA damage that is comparable or even more pronounced than the signal in the aDNA library used to generate the empirical distribution of goodness-of-fit p-values.

For the distribution of goodness-of-fit p-values from modern DNA, we count how many of them were smaller or equal than the sedimentary DNA goodness-of-fit p-value. We calculate the empirical p-value of the test by dividing this number by the total number of p-values in the empirical distributions. With this approach we test the null hypothesis that the test set of reads matches the absence of ancient DNA damage patterns seen in reads of modern origin.

All sedimentary DNA reads: We tested independently alignments from each of the layers sequenced by Smith et al. using a bona fide aDNA sample for the generation of the distribution of goodness-of-fit p-values. For each layer we tested 10 sets of different numbers of reads (from 100 to 1000 reads, with increments of 100 reads). For each layer and for each number of reads in the test set we repeated the test and calculated the empirical p-value 1000 times as described above.

Other ancient DNA and modern DNA libraries were tested using the same procedure.
