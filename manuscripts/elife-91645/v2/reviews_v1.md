# Peer review - Round 1

Editors:
- Volker Dötsch, Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91645.2.sa0](https://doi.org/10.7554/eLife.91645.2.sa0)

Antibodies are some of the most important tools in biomedical research. However, their quality and specificity vary significantly. This fundamental study provides guidelines for how the quality of an antibody should be assessed and recorded and provides compelling data on the selected antibodies. This paper will be of interest to researchers working in experimental cell biology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91645.2.sa1](https://doi.org/10.7554/eLife.91645.2.sa1)

The research addresses a key problem in life sciences: While there are millions of commercially available antibodies to human proteins, researchers often find that the reagents do not perform in the assays they are specified for. The consequence is wasted time and research funding, and the publication of misleading results.

Manufacturers' catalogues often contain images of western blots. Researchers are likely to select antibodies that stain a single band at the position expected from the mass of the intended target. However, the good results shown in catalogues are often not reproduced when researchers use the antibody in their own laboratories. A single band is also weak evidence since many proteins have similar mass and because assessment of mass by WB is at best approximate. In addition, results obtained by WB may not predict performance in applications where the antibody is used to recognize folded proteins. Examples include immunoprecipitation (IP) of native proteins in cell lysates and staining of viable or formalin-fixed/permeablized cells for flow cytometry or immunofluorescence microscopy (IF).

The authors of this manuscript are from the Canadian, public interest open-science company YCharos. The company webpage (ycharos.com) explains that they have partnered with many leading manufacturers of research antibodies and that their mission is to characterize commercially available antibody reagents for every human protein.

The authors have developed a standardized pipeline where antibodies are used in WB, IP of native proteins from cell lysates (WB readout) and IF (staining of cell lines that have been fixed with paraformaldehyde and permeabilized with Triton x100). A key component is the use of knockout cell lines as negative controls in WB and IF. Eight cell lines were selected as positive controls on the basis of mRNA expression data that are publicly available in the Expression 22Q1 database.

Reports for antibodies to each protein are made available online at https://ZENODO.org/communities/ycharos/ as images of western blots, and immunofluorescence staining. In addition, reports for each target are available at https://ycharos.com/data/ .

MANUSCRIPT:

The manuscript describes validation criteria and results obtained with 614 commercially available antibodies to 65 proteins relevant for neuroscience A major achievement is the identification of successful renewable antibodies for 50/56 (77%) proteins in WB, 49/65 (75%) for IP and (54%) for IF. There can be little doubt that the approach represents a gold standard in antibody validation. The manuscript therefore represents a guide to a very valuable resource that should be of considerable interest to the scientific community.

While the results are convincing, they could be more accessible. In the current format, researchers have to download reports for each target and look through all images to identify the most useful antibodies from the images. The reports I reviewed did not draw conclusions on performance. A searchable database that returns validated antibodies for each application seems necessary.

It is worth noting that 95% of the tested antibodies were specified by the manufacturer for use in WB. This supports the view that manufacturers use WB as a first-pass test (Nat Methods. 2017 Feb 28;14(3):215) and that most commercial antibodies are developed to recognize epitopes that are exposed in unfolded proteins. Important exceptions are those used for ELISA or staining of viable cells for flow cytometry. 44% of antibodies specified for WB were classified as "successful" meaning a single band that was absent in the negative control (knockout/KO lysate). Another 35% detected the intended target but showed additional bands that were present also in the KO lysate. A key question is to what extent off-target binding was predictable from the WBs provided by the manufacturers. Thus, how often did the authors find multiple bands when the catalogue image showed a single band and vice versa?

The authors correctly point out that manufacturers rarely test their reagents in IP. Thus, there is little information about antibodies capable of binding folded proteins. It is encouraging that as many as 37% of those not specified for IP were able to enrich their targets from cell lysates. Yet it is important to explain that a test that involves readout by WB provides information about on-target binding only. Cross-reactive proteins will generally not be detected when blots are stained with an antibody reactive with a different epitope than the one used for IP. Possible solutions to overcome this limitation such as the use of mass spectrometry as readout should be discussed (Nature Methods volume 12, pages 725-731 2015).

Performance in immunofluorescence microscopy was performed on cells that were fixed in 4% paraformaldehyde and then permeabilized with 0.1% Triton-X100. It seems reasonable to assume that this treatment mainly yields folded proteins wherein some epitopes are masked due to cross-linking. The expectation is therefore that results from IP are more predictive for on-target binding in IF than are WB results (Nature Methods volume 12, pages725-731 2015). It is therefore surprising that IP and WB were found to have similar predictive value for performance in IF (supplemental Fig. 3). It would be useful to know if failure in IF was defined as lack of signal, lack of specificity (i.e. off-target binding) or both. Again, it is important to note the IP/western protocol used here does not test for specificity.

The authors report that recombinant antibodies perform better than standard monoclonals/mAbs or polyclonal antibodies. Again, a key question is to what extent this was predictable from the validation data provided by the manufacturers. It seems possible that the recombinant antibodies submitted by the manufacturers had undergone more extensive validation than standard mAbs and polyclonals.

Overall, the manuscript describes a landmark effort for systematic validation of research antibodies. The results are of great importance for the very large number of researchers who use antibodies in their research. The main limitations are the high cost and low throughput. While thorough testing of 614 antibodies is impressive and important, the feasibility of testing hundreds of thousands of antibodies on the market should be discussed in more detail.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91645.2.sa2](https://doi.org/10.7554/eLife.91645.2.sa2)

The paper nicely demonstrates the extent of the issue with the unreliability of commercial antibodies and describes a highly significant initiative for the robust validation of antibodies and recording this data so that others can benefit. It is a great idea to have all individual antibody characterisation reports available on Zenodo - these reports are comprehensive, clear and available to everyone.

A significant proportion of all life science research conclusions are based on data obtained through the use of antibodies. The quality and specificity of antibodies vary significantly. Until now there has been no uniform generally recognised approach to how to systematically assess and rate antibody specificity and quality. Furthermore, the applications that a particular antibody can be used in including western blot, immunofluorescence or immunoprecipitation are frequently not known. This paper provides important guidelines for how the quality of an antibody should be assessed and recorded and data made freely available via a Zenodo repository. This study will ensure that researchers only use well-validated antibodies for their work. A worrying aspect of this paper is that many poor-quality antibodies that failed validation are reportedly being widely used in the literature. More than 60% of all antibodies recommended for immunofluorescence failed QC. This study will have broad interest. I would recommend that all researchers select their antibodies using the database described in the paper and follow its recommendations for how antibodies should be thoroughly validated before being used in research. Hopefully, other researchers can contribute to this database in the future all widely used antibodies will eventually be well characterized. This should improve the quality and reproducibility of life science research.
