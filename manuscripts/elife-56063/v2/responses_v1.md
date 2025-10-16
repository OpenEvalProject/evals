# Author response - Round 1

Authors:
- Matthieu Genestine
- Daisy Ambriz
- Gregg W Crabtree
- Patrick Dummer
- Anna Molotkova
- Michael Quintero
- Angeliki Mela
- Saptarshi Biswas
- Huijuan Feng
- Chaolin Zhang ([ORCID: 0000-0002-8310-7537](https://orcid.org/0000-0002-8310-7537))
- Peter Canoll
- Gunnar Hargus
- Dritan Agalliu
- Joseph A Gogos
- Edmund Au ([ORCID: 0000-0003-3190-9711](https://orcid.org/0000-0003-3190-9711))

## Response text

DOI: [10.7554/eLife.56063.sa2](https://doi.org/10.7554/eLife.56063.sa2)

Essential revisions:

1. Loss-of-function in vivo studies would be necessary to confidently establish a role for these secreted proteins. While this study provides some very interesting data, the authors have not shown that it is specifically vascular endothelial-derived SPARC and SerpinE1 that regulates interneuron migration and maturation. It is widely appreciated that primary brain endothelial cells rapidly de-differentiate and lose key aspects of their organotypic character when cultured in vitro. As a result, the generalizability of the SPARC and Serpin E1 phenotypes to an in vivo developmental setting cannot be assumed. The authors did not specifically block or delete the function of vascular-derived SPARC and SerpinE1. The authors test the requirement of vascular-derived SPARC and SerpinE1 by inhibiting the ability of endothelial conditioned media to induce migration of interneurons in explants. Unfortunately this experiment does not specifically block vascular-derived SPARC and SerpinE1 as there is evidence that SPARC is expressed by other cell types in the brain (astrocytes Kucukderily et al. 2011, 10.1073/pnas.1104977108, and figure 3A VZ/SVZ and 3B cortical VZ/SVZ). To show the requirement of endothelial SPARC and SerpinE1, the authors could do any of the following experiments: (A) generate conditioned media from mouse primary endothelial cells, deplete CM of SPARC, SerpinE1 or both, and compare if depleted CM induce less migration than intact CM in brain slices. (B) Test if conditional deletion of SPARC or SerpinE1 in endothelial cells prevents or reduces interneuron migration. There are floxed allele mice for SPARC (Ramu 2019, 10.1016/j.ebiom.2019.09.024) and SerpinE1 (Jiang 2017, doi.org/10.1111/acel.12643). (C) Instead strengthening the human work, so that in the end this work can at least advance our ability to accelerate human neuron differentiation process.

We have performed organotypic slice culture migration assays using primary culture endothelial conditioned medium with or without SPARC function-blocking antibody and SK216 Serpin E1 inhibitor (Figure 3H). Here, we found that pEndoCM significant increased the number of interneurons migrating into the cortex and that the biological activity of pEndoCM was attenuated in the presence of function-blocking ab and SK216. We have updated the figure legend, results and discussion to reflect these new data.

2. A clear indication that endothelial cells is the source of the physiological levels of SPARC is needed. SPARC has been studied extensively in astrocytes which could be the source. What is the developmental pattern of expression of SPARC and SerpinE1 in human embryonic development? Do they correspond to the slow rate of interneuronal migration and maturation in human cortex. Publicly available database (e.g. Allen Brain) might have this information, or authors could potentially provide some simple experiments to address this.

We observe robust migration from e14.5 mouse MGE, at which point we assert the effects of SPARC and SerpinE1 has already exerted their effects. This timepoint precedes most of astrogliogenesis and therefore astrocytes are unlikely to be the source for the process we are studying, at least in the case of mice. In human fetal development, astrocytes could be the source since astrocytes (or at least astrocyte progenitors) are detected at 19 pcw (Holst et al., 2019). Although, notably, in this same study, the authors not that the MGE has far fewer astrocyte progenitors than neighboring LGE and CGE.

As for expression of SPARC and SerpinE in human fetal brain, we found evidence in support of increased expression of both SPARC and SerpinE1 late in gestation. From the Allen Institute developmental transcriptomic database (BrainSpan), there is low level expression of SPARC and SerpinE1 in the subpallium at 8 and 9 pcw. In the fetal cortex, expression for both peaks at 37 pcw through to 1 year of age. Further, previous reports find expression of SPARC (Butler et al., 2016; Girard and Springer, 1995; Sage et al., 1989) and SerpinE1 (Canfield et al., 1989) in human endothelial cells. Single cell RNA-seq in mouse indicates that SPARC expression is significantly enriched in brain endothelial cells vs. other endothelial populations (log2-fold increase 3.97) (Hupe et al., 2017). In the same study, SerpinE1 expression increases in mouse brain endothelial cells, peaking at e14.5, which coincides with the timepoint where we observe robust migration in MGE explants. Expression data outlined above has been incorporated into Discussion:

“Our findings support previous studies that have linked angiogenesis to pathfinding during interneuron tangential migration (Barber et al., 2018; Li et al., 2018) and MGE mitosis (Tan et al., 2016). […] In the same study, SerpinE1 expression increases in mouse brain endothelial cells, peaking at e14.5, which coincides with the timepoint where we observe robust migration in MGE explants. Both SPARC (Butler et al., 2016; Girard and Springer, 1995; Sage et al., 1989) and SerpinE1 (Canfield et al., 1989) in human endothelial cells.”

3. Is the amount of SPARC and SerpinE1 used in the treatment of hSC-Ins at physiologically relevant levels (either in the context of mouse or human cortex)?

To try and get a sense of how much SPARC and SerpinE1 are expressed in mouse MGE at e14.5, we analyzed by western blot and found low, but detectable levels. However, much more SPARC and Serpin E1 was detected in EndoCM, pEndoCM and also in when the lane was loaded with the amount of SPARC and SerpinE1 added to hSC-IN organoids.

These results are not particularly surprising. For one vascular cells are a small fraction of the total cells in e14.5 MGE tissue and it would therefore be expected to be detected at low levels in relation to total tissue. Further, it is difficult to calculate the amount of SPARC and SerpinE1 made biologically available in the microenvironment where endothelial cells are signaling immediately adjacent to interneuron progenitors. It is reasonable to assume, however, that a lower level would be needed. This would be especially true of a matricellular protein such as SPARC, which would be interacting with cells in ECM-rich microdomains. Indeed, recent work demonstrates that artificially recapitulating a microdomain environment can greatly enhance the overall effect of a ligand (Raghavendran et al., 2016; Shirure et al., 2017).

In contrast, we added SPARC and Serpin E1 for 14 days into the medium surrounding Matrigel-embedded organoids. In this context, much more SPARC and SerpinE1 would be needed to diffuse through the Matrigel and into the organoids. That said, we thank the reviewer for raising this important point. We have added a passage to the Discussion raising the possibility of recapitulating the vascular/MGE microenvironment for added efficacy in future studies:

“Of note, we found that levels of SPARC and SerpinE1 were detected a low levels in the mouse MGE at e14.5 (data not shown), consistent with in situ hybridization from Allen Institute and GenePaint (Figures 3A and B). […] A number of studies have utilized bioengineering to recapitulate the vascular microenvironment (Raghavendran et al., 2016; Shirure et al., 2017). Employing SPARC and SerpinE1 in such a context could potentially amplify the effects we demonstrated in this study.”

4. The authors do not attempt to explore a mechanism-of-action for the endothelial-derived cues they identify. Which receptors do they interface with to interact with interneurons? Broadly, what intracellular changes do they induce to promote a migratory state? At the very least, discussions of potential answers to these questions are needed for the work to represent a significant scientific advance.

We replaced the paragraph in the Discussion with 3 new paragraphs that addresses potential mechanisms of action for both SPARC and Serpin E1:

“We identified SPARC and SerpinE1 as important proteins that account for most of the activity in EndoCM. […] In future, it will be important to study the molecular basis for how SPARC and SerpinE1 function in regulating interneuron differentiation and migration.”
