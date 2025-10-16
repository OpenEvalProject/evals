# Author response - Round 1

Authors:
- Albert Tsai ([ORCID: 0000-0002-1643-0780](https://orcid.org/0000-0002-1643-0780))
- Mariana RP Alves ([ORCID: 0000-0002-0796-2101](https://orcid.org/0000-0002-0796-2101))
- Justin Crocker ([ORCID: 0000-0002-5113-0476](https://orcid.org/0000-0002-5113-0476))

## Response text

DOI: [10.7554/eLife.45325.017](https://doi.org/10.7554/eLife.45325.017)

[Editors' note: the authors’ plan for revisions was approved and the authors made a formal revised submission.]

Essential points to address are the following:

1) The connection between enhancers, Ubx protein concentration, transcriptional output, and phenotype. Although different concentrations of Ubx are measured at the deleted vs. wild-type locus, an important point that the three reviewers agree upon is that gene expression levels and Ubx concentrations are not well correlated. There appear to be other unexplained factors that are influencing the expression of svb that do not correlate with the TF concentration. Thus, it is unclear whether the experiments described here support or reject the hypothesis laid out in the "multi-enhancer "hubs" improve robustness by increasing transcription factor retention near transcription sites."

The reviewers are correct to point out that there are multiple inputs that control the response of the svb locus (Stern and Orgogozo, 2008). Therefore the response function of svb could have a positive but complicated relationship to Ubx concentrations and would depend on more than Ubx alone. We now state this in the second paragraph of the Discussion. However, Ubx is a crucial driver of svb and, specifically, also DG3 expression in the ventral region of the A1 segment (Crocker et al., 2015) and Figure 1 of this manuscript. We specifically focused most of our analyses and quantifications in A1. We now state this in the Results section, “Transcription sites from the DG3‐ deletion allele have weaker Ubx microenvironment and lower transcriptional output”.

Within this specific body segment, Ubx intensity near svb transcription sites would be a reasonable metric of how local transcription factor concentrations changed when we perturbed the system through mutations and elevated temperature. We now state this in the Results section “Transcription sites from the DG3‐deletion allele have weaker Ubx microenvironment and lower transcriptional output”. With these caveats in mind, we did observe increased Ubx concentrations and around the wildtype svb transcription sites (Figure 3C, lower right panel) compared to the deletion allele, and increased phenotype resilience for the wildtype allele at 32 °C. In the svbBAC rescue, we also observed that colocalized svbBAC and DG3‐deleted svb allele had both higher Ubx concentrations and svb transcriptional outputs (Figure 4F). We, therefore, believe that our results support the idea that multi enhancer hubs help transcriptional factor retention and can ultimately lead to a more robust phenotype. We believe the analysis that the reviewers suggested below also supports our hypothesis of improved transcriptional factor retention with complexed enhancers.

The authors must consider further whether the global measurements shown in Figure 3 are the most effective measure of this proposed correlation, or whether a more fine-grained analysis might support the idea that boosted Ubx levels from complexed enhancers are driving transcription. As noted below, the authors might show scatter plots of Ubx concentration vs. svb transcription within each condition. A positive correlation would support their hypothesis.

We have modified the analysis in Figure 3C to show svb transcription vs. Ubx intensity. There is initially a positive correlation between svb transcriptional output and Ubx intensity, in line with the reviewers’ proposal. This trend dissipates at higher Ubx and svb intensities, indicating that the response of svb output to Ubx concentration is not a simple relationship. Capturing the exact dependence of transcriptional output on Ubx concentration is difficult for the reasons we stated in the second paragraph of the Discussion (e.g., multiple binding sites in enhancers and overlapping expression patterns). To fully address this would require future live imaging experiments that can track the gene locus regardless of its transcriptional state, in addition to reporting on its transcriptional activity and transcription factors around it. Numerous new reagents (fly lines, tagged proteins, etc.) are being developed in the lab to address this.

The trichome phenotype is also not directly correlated to the transcriptional outputs and Ubx concentrations, and as mentioned in the Discussion, further layers of regulation are likely in play. This idea needs to be more fully fleshed out.

We now have a new figure (Figure 6) summarizing our hypothesis and referred to this figure throughout the Discussion to clarify our proposed mechanism. In short, we propose in our revised Discussion that 1) the relationship between Ubx concentration and svb transcriptional output is positive but complex, likely involving additional factors (paragraph two) and 2) the relationship between svb transcriptional output and phenotype is sigmoidal (paragraph four) and the wild‐type system operates in a saturated regime under ideal conditions (paragraph five). The processes leading to the response functions in 1 and the phenotypical tolerance to a range of svb out in 2 remain to be investigated (paragraphs two and five), specifically with live imaging approaches. As mentioned in the previous paragraph, work is currently ongoing in the lab to address this.

A finding related to "enhancer hubs boosting local concentration" is the finding that an ectopic BAC appears not to influence Ubx concentration in a wild-type svb background, only in a deletion background. Does this finding indicate that such hub formation is saturable? And if so, does this indicate that the wild-type svb locus forms a local hub with enhancers in the immediate vicinity, and trans-complementation is not a normal feature of svb function?

We agree with the reviewers that hub formation is saturable, based on this observation. We also believe that local hub formation with the cis‐regulatory region of the wildtype svb is sufficiently in saturation to deal with environmental challenges as seen in trichome numbers. We now state this in the Discussion (paragraph five). Our data, however, does not provide a direct answer as to if trans‐ chromosomal interactions are a normal feature of svb or other genes. Ongoing efforts in the lab to characterize and map these long‐range interactions through imaging and genomics approaches should shed light on their functional impact during development in the future.

2) A second point raised concerned the exact cis regulatory regions in play. A minimal DG3 enhancer drives gene expression in ventral abdominal stripes, but does not rescue Ubx concentrations from a trans setting. A larger deletion that includes DG3 as well as additional Ubx binding regions (that are not sufficient for, but may be part of, ventral DG3-related activity) impacts transcription, trichome development, and robustness. A yet larger cis-regulatory domain on a BAC rescues some aspects of gene expression and Ubx concentration. The interpretation conflates DG3 with the function of the deleted region; reviewers noted that a more careful interpretation would differentiate results from each of these different cis elements. For instance, the lack of trans-rescue by the DG3 enhancer alone may be due to the inability of a short segment to transvect effectively. The interpretation should explicitly take into account known properties of transvecting regulatory loci in Drosophila.

We agree that we should take into account the efficiency of the rescue locus in finding the svb locus as an important factor in if phenotype rescue takes place. We now state that DG3 alone as the rescue locus might have failed due to its inability to pair with the svb locus in the Discussion (paragraph four). We also now compare and contrast the svbBAC‐svb interactions that we observed with transvection and hypothesize that the addition of other topological elements such as insulator to DG3 could overcome this problem (paragraph four). We further state that the svbBAC did not rescue trichomes in regions where DG3 provided exclusive coverage, suggesting that the rescue BAC rescued the phenotype by overdriving the other ventral enhancers E3 and 7 rather than directly restoring DG3 function.

3) Several aspects can be addressed by better justification and explanation of methods and data presentation, including

– Why sometimes either A1 or A2 trichomes are quantitatively assessed, depending on the figure;

This issue was an oversight on our part, and we have updated all the main figures where we counted trichomes to be from the A1 segment for consistency. We moved data from the A2 segment to figure supplements as they also show a similar but weaker trend as in A1. We speculate that this is due to additional factors at work as DG3 in the A2 segment responds to additional inputs beyond Ubx, as explained in the Results section “The DG3 enhancer responds specifically to Ubx in the A1 segment”.

– The use of one-tailed (vs. two-tailed) T-tests for statistical relevance;

We have changed our test to two‐tailed T‐tests throughout, as is the standard. This did not change of our findings.

– Recommendations for inclusion of both 25C and 32C phenotypes and data uniformly, and;

We added trichome images from 32 C to Figure 2 and for the data analysis involving Ubx intensity and svb transcriptional output in Figure 3. We did not conduct svbBAC rescue experiments at 25 C as neither the wildtype nor the deletion allele displayed reduced trichome numbers (phenotype output), and the difference between the Ubx intensities (molecular input) around transcription sites of both genotypes was small at this temperature.

– Clarification of exact role of Ubx in T1-T3 regulation, as the conclusions drawn about DG3 and Ubx roles are difficult to know based on the single images shown,

As the reviewers noticed, the role of Ubx in regulating svb, and DG3 specifically, on the ventral surface in segments outside of A1 is more complicated (Figure 1B‐E). DG3 expression in the thoracic segments T1‐T3 overlaps with other ventral svb enhancers and responds to changes in Ubx level less that in the A1 segment. T2 and T3 also show only low levels of expression from DG3 on the ventral surface with wild‐type Ubx expression. This issue potentially introduces many confounding factors for quantitation. We have thus confined ourselves to qualitative descriptions of DG3 properties outside of A1 and A2. We now state this concern at several places in the Results and Discussion.

– The number of data points in Figures 3 and 4 are limited; is there a technical limitation to more extensive sampling of the transcriptional readouts and Ubx intensities?

In the process of doing the additional analysis suggested by the review, we added more data points, and the number of transcription sites and embryos quantified is comparable to the original publication this manuscript is linked to (Tsai et al., 2017). As in the previous publication, colocalization is a relatively rare event, so we observed fewer transcription sites. The number observed for colocalized sites is also similar to our previous publication.

4) In some cases, the actual experimental approach was unclear to the reviewers:

– There was some confusion about whether the DG3 deletion mutants were homozygous, so there would be no wild-type copy of the gene in these embryos – is that indeed the case?

Yes, we selected larvae or embryos homozygous for the Df(X)svb108allele based on the following phenotype in the T1 segment: the lack of trichomes or the lack of svb mRNA expression, respectively. This is a homozygous marker for the deletion allele as the wild‐type svb allele expresses in this segment. This was mentioned in “Deletion of a region including DG3 enhancer causes defects in ventral trichome formation specifically at elevated temperatures” in Results, “Preparing Drosophila embryos for staining and cuticle preps” in Materials and methods and the legends for Figure 2C in our original manuscript (2E in the revised version,). We have now made it explicit in the Results that we use this to select for animals homozygous for the deletion for both counting trichome number and for confocal imaging. It is now also described in both “Cuticle preparations and trichome counting” and “Imaging fixed embryos” in the Materials and methods section.

– Figure 4 shows svb, but not dsRed mRNA expression; is that correct? Imaging of dsRed only used to score a svb locus as "overlapped" vs. "not overlapped"?

Yes, the data analysis in Figure 4 only used only svb mRNA output. Imaging of dsRed transcription site is only used to score colocalization with svb. We displayed image panels for individual nuclei that show a dsRed signal for illustrative purposes. We explicitly stated that we are displaying svb transcription in both the Figure 4E and the legends.

– Choice of pixel size for ROI.

The 40‐pixel ROI is too large and a mistake in our part. The actual ROI size in the previous manuscript was a 4‐pixel square ROI; this has been changed to be a circle with a diameter of 4 pixels (170 nm). We chose this size because it is the resolution limit of the AiryScan images we acquired. We have corrected this and stated our rationale in the revision when we describe the image analysis in “Transcription sites from the DG3‐deletion allele have weaker Ubx microenvironment and lower transcriptional output” in the Results and “Analysis of microenvironment and svb transcription intensity” in the Materials and methods.

– Signal to noise for Ubx across the nucleus, as well as variation in average Ubx from sample to sample.

We used exactly the same antibodies and methodology as reported in (Tsai et al., 2017) to stain for Ubx and the quality of the images acquired were the same. In the previous publication we explored the Ubx cluster characteristics. We now include a new supplemental figure (Figure 3—figure supplement 1) with Ubx variation across the nucleus within embryos, and from sample to sample (there is no significant difference). In contrast, at the sites of active svb transcription there is a significant difference (p < 0.001, two‐tailed t‐test) from randomly sampled locations in the nucleus. This has also been added to the Results “Transcription sites from the DG3‐deletion allele have weaker Ubx microenvironment and lower transcriptional output”
