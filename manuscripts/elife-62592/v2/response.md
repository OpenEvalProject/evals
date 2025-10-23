# Author response - Round 1

Authors:
- Joanna L Gillis
- Josephine A Hinneh
- Natalie K Ryan
- Swati Irani
- Max Moldovan
- Lake-Ee Quek
- Raj K Shrestha
- Adrienne R Hanson
- Jianling Xie
- Andrew J Hoy ([ORCID: 0000-0003-3922-1137](https://orcid.org/0000-0003-3922-1137))
- Jeff Holst ([ORCID: 0000-0002-0377-9318](https://orcid.org/0000-0002-0377-9318))
- Margaret M Centenera
- Ian G Mills
- David J Lynn
- Luke A Selth ([ORCID: 0000-0002-4686-1418](https://orcid.org/0000-0002-4686-1418))
- Lisa M Butler ([ORCID: 0000-0003-2698-3220](https://orcid.org/0000-0003-2698-3220))

## Response text

DOI: [10.7554/eLife.62592.sa2](https://doi.org/10.7554/eLife.62592.sa2)

Essential revisions:

1. Although previous literature show this in breast and liver cancer cell lines, the authors should conduct ChIP-qPCR in the cell lines they are studying (LNCaP and VCaP) to confirm that SREBP1 is associated with the 6PGD promoter in prostate cancer. If SREBP1 binding to this promoter is observed, does it increase as a result of AR induction and/or decrease with AR inhibition?

We have spent some time attempting to perform SREBP1 ChIP but have faced a number of challenges outside of our control. Most notably, the validated ChIP antibody for SREBP1 from Santa Cruz Biotechnology (sc-8984), which was used in the ENCODE ChIP-seq studies mentioned by the Reviewers, is no longer commercially available. This led us to try an alternative antibody (Santa Cruz monoclonal anti-SREBP1 2A4). However, despite optimising our experimental conditions to ensure that we selected timepoints for DHT treatment that robustly activated SREBP1 (Author response image 1A), we could not demonstrate robust binding of SREBP1 to known target sites at the SCD and LDLR genes that we used as positive controls (Author response image 1B).

(A) LNCaP cells were cultured in the absence or presence of DHT (10nM) for varying timepoints up to 48 hours. Nuclear and cytoplasmic protein extracts were evaluated for the active (cleaved) form of SREBP1. (B) DHT-induced recruitment of AR or SREBP1 to canonical AR/SREBP1 binding sites after 4 or 16 hrs culture.

This could not be explained by a problem with the DHT or our ChIP-qPCR protocol, as we showed the expected 40-60-fold recruitment of AR to the KLK3 enhancer in the same experiment. Collectively these results are consistent with the SREBP antibody being unsuitable for ChIP and, as mentioned, the ChIP-validated antibody is unfortunately no longer available.

2. More mechanistic evidence regarding how AR controls 6PGD levels and subsequently, how 6PGD impacts on AR abundance would improve the study. The authors show that an SREBP inhibitor affects 6PGD levels, but considering potential issues with specificity of inhibitors, SREBP depletion by CRISPR or siRNA should be tested for the ability to attenuate DHT-induced 6PGD expression.

The Reviewers raise an important point about inhibitor specificity, and we now show that siRNA-mediated SREBP1 knockdown also attenuates the DHT-induced protein levels of 6PGD. These new data further strengthen the association between SREBP1 and PGD expression and have been incorporated into the revised manuscript (new Figure 2D).

Similarly, the experiments using 6PGD inhibitors (Figures 4 and 5) should be complemented by orthogonal genetic approaches.

In response to the Reviewers’ suggestion, we have repeated key functional experiments from Figures 4 and 5 using genetic knockdown via siPGD to block 6PGD signalling, instead of the S3 and Physcion inhibitors. Specifically, we have now performed growth, death and ROS assays in the absence or presence of siPGD in 2 additional cell lines (V16D and MR49F), and shown very similar effects to our results using the inhibitors; namely, reduced cell growth and induction of cell death and ROS production. These new data strengthen our conclusions and have been incorporated into the revised manuscript (new Figures 3A, 3B and 3G). We also now include new Western blot data showing that, as we observed using S3, siPGD leads to inhibition of ACC1 and mTOR signalling (new Figure 5—figure supplement 1.).

3. It is not clear how and at which level 6PGD may affect AR levels. Experiments using transcriptional, translational and proteasome inhibitors to address the level at which 6PGD regulates AR are required to strengthen this part of the study. As a related point, the authors should investigate whether overexpression of 6PCG lead to an increase in AR levels.

As suggested by the Reviewers, we exploited transcriptional (actinomycin D), translational (cycloheximide) and proteasome (MG132) inhibitors in our experiments with the 6PGD inhibitor, S3, and assessed the effects on AR RNA (for actinomycin D) or protein (for cycloheximide and MG132) levels. Actinomycin D and cycloheximide did not influence the effect of S3 on AR. Conversely, our experiments with MG132 provide strong evidence that S3 leads to enhanced turnover of AR by the ubiquitin proteasome system. Specifically, we immunoprecipitated AR from LNCaP cells cultured with S3 in the absence and presence of MG132. Importantly, in the presence of MG132, ubiquitinylated AR accumulated in a dose-responsive manner with S3. Accordingly, we can now confidently conclude that S3 is affecting AR at the level of protein turnover, and these new data have been incorporated into the revised manuscript (new Figure 6D).

To address whether overexpression of 6PGD influences AR protein levels, we generated a LNCaP cell line stably overexpressing 6PGD via lentiviral transduction. Over multiple passages in culture, the 6PGD overexpressing line maintained similar AR levels to the control vector-transduced line (Author response image 2). This finding provides further evidence that 6PGD is affecting AR protein stability rather than its protein synthesis.

4. It remains unclear whether the effects of AR on cell survival are dependent on 6PGD. Would enforced expression of 6PCG in the context of AR depletion improve cell viability through engagement of the PPP?

Thank you for this suggestion; to address the dependency of AR depletion on 6PGD, we used the LNCaP cell line stably overexpressing 6PGD (Author response image 2) and compared its sensitivity to siAR knockdown with that of the control (empty vector-transduced) line. Author response image 3 shows that both the control and the 6PGD-overexpressing lines were equally sensitive to siAR, indicating that 6PGD alone is not responsible for the growth-inhibitory effects of AR depletion. It is, however, likely that while inhibition or knockdown of 6PGD can block the PPP to influence cell viability, selective overexpression of a single member of the PPP may not sufficiently activate this pathway in a setting where one or more other pathway factors may be limiting. Additionally, AR has many functions in prostate cancer growth beyond regulation of the PPP, and it is therefore not surprising that over-expression of 6PGD alone could not rescue loss of AR.

Cells stably transduced with control or 6PGD-overexpressing vectors were transfected with siCon or siAR and viable cell number measured after 6 days in culture. **** P<0.001 c.f. siCon.

5. A deeper investigation of the effects on PPP is warranted. Although the levels of 6-PG (the substrate of the reaction) have been measured (Figure 3C), levels of the PPP intermediates/products (ribulose-5-phosphate or NADPH) or a final product of the pathway (e.g. ribose-5-phosphate) should be included. Isotopic tracing of 13-C glucose through the PPP following modulation of AR/SEBP1/6PGD would provide more direct evidence that PPP is indeed being affected.

We agree with the need to more directly relate our effects on PGD modulation to PPP activity in prostate cancer cells. Accordingly, we have followed the suggestion to perform isotopic tracing with 1,2-13C glucose after knockdown of AR/SREBP1/6PGD. PPP flux was estimated over a period of 15 minutes by measuring the incorporation of 13C into the immediate product of 6PGD catalytic activity, ribulose-5-phosphate (Ru-5-P). Our new data conclusively show that flux through the oxidative (irreversible) branch of the PPP (i.e. through 6PGD) significantly decreased with knockdown of 6PGD, AR or SREBP1 (included in the revised manuscript as Figures 3D-G, and Figure 3—figure supplement 2C). Interestingly, knockdown of AR and SREBP1 (but not 6PGD) also had a significant impact on flux through the non-oxidative (reversible) branch of the PPP, as determined by evaluating m2 (doubly labelled) Ru5P production via F6P/GAP (Figures 3F-G). Collectively, these glucose tracing data show that targeting 6PGD significantly suppresses PPP activity through the oxidative pathway, an effect that is also evident when targeting the upstream signalling factors AR and SREBP1. We thank the Reviewers for this suggestion, which has markedly strengthened our manuscript’s conclusions.
