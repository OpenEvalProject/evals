# Author response - Round 1

Authors:
- Hoong Chuin Lim
- Ivan Vladimirovich Surovtsev
- Bruno Gabriel Beltran
- Fang Huang
- Jörg Bewersdorf
- Christine Jacobs-Wagner

## Response text

DOI: [10.7554/eLife.02758.031](https://doi.org/10.7554/eLife.02758.031)

In short, we would like to receive a revised manuscript that addresses the major point raised by Reviewer # 1, to provide additional evidence for elastic dynamics in other regions of the Caulobacter chromosomes and to expand the scope of the modeling, as suggested by Reviewer #2. It will also be useful to provide additional explanations for the scenario raised by Reviewer #2 on how the separation of the parS sites at oriC on the chromosome might affect your model.

Thank you for giving us the opportunity to submit a revised manuscript. We have added experimental evidence for the elastic dynamics of two other chromosomal regions and expanded the scope of the modeling, as requested by Reviewer 1 and 2, respectively. Regarding the multiplicity of parS sites and their separation, please note that in the C. crescentus chromosome, there are only two parS sites and they are separated by only 42 nucleotides. Fully stretched, 42 nucleotides would be at most 14 nm, making the scenario raised by Reviewer 2 unlikely. Nevertheless, we have considered this scenario and shown that it does not alter our conclusions. Please see below for details.

Reviewer #1:

Since elastic dynamics of DNA is proposed to provide chromosome segregational forces and since this is a new dimension introduced to describe DNA segregation, I would like to see if 1-2 other loci (in addition to GroESL) undergo similar elastic dynamics, to further bolster the notion that the Caulobacter chromosome behaves like an elastic filament. I do not know how easy / difficult it would be to generate a strain by integration of LacI into other loci and perform such a study in Caulobacter.

We agree with the reviewer, and have imaged and analyzed the motion of two additional chromosomal loci (139_lac and 165_lac) (Viollier et al., PNAS, 2004). We found that they displayed elastic dynamics similar to the groESL locus. The results have been added to Figure 5 (panel C). The text and figure legend have been modified accordingly.

Reviewer #2:

Intuitively, it seems to me that the modelling would work just as well by a Mizuuchi-like process and that tethering the ParA molecules to DNA provides a matrix on which the polar gradient of ParA can be fixed. It would be interesting to see this alternative scenario modelled.

We apologize for not being more explicit in the original submission, but our ‘diffusion-binding’ model does test a ‘Mizuuchi-like’ process. In that model, a polar gradient of ParA-ATP dimers is fixed on a static DNA matrix exactly as proposed by the reviewer. As shown in Figure 4B and 4C, this diffusion-binding model does not lead to fast or robust segregation. Note that we were, at first, surprised by the results because we had the same intuition as Reviewer 2. In hindsight, the poor performance of the diffusion-binding model should be expected because in this model, the movement of the partition complex is governed by diffusion. There is no force involved and the ParA-ParB interactions only stall the partition complex without productively moving the partition complex in the ‘right’ direction.

There is nothing in this mechanism that prevents the partition complex from diffusing in the wrong direction when the interaction between ParA and ParB is lost (i.e., in the ParA-depleted region away from the ParA gradient). This can be seen in Video 2. As a result, the diffusion-binding model does not perform better than the model in which the partition complex only passively diffuses (no interaction with ParA-ATP dimers). In fact, the diffusion-binding model quantitatively performs worse than the diffusion-alone model because the only thing the ParA/ParB interaction does is to temporally stops the motion of the partition complex, slowing down its ultimate arrival at the opposite cell pole. We found that it was essential to include the elastic dynamics of the underlying DNA (which had not been considered before) to explain the translocation kinetics observed in vivo. We have revised the manuscript to be more explicit.

The new model also does not take account of the fact that each oriC region has multiple ParB molecules bound, and that there are several separated parS sites, each of which could collide with a DNA-bound ParA dimer, facilitating the walk up the ParA gradient towards the cell pole. Perhaps the occasional “stretching” of ParB foci represents simultaneous interactions made by different parS assemblies?

Our modeling does take into account that multiple ParB dimers bind to the parS (ori) region and that the ParB-rich partition complex can interact with more than one DNA-bound ParA-ATP dimer. The interaction radius of the ParB-rich partition complex is 50 nm, which we estimated from our super-resolution images (Figure 1–figure supplement 3). In the model, the 50-nm ParB sphere is allowed to interact with infinite number of DNA-bound ParA-ATP dimers as long as there is an overlap between the ParB sphere and the ParA-ATP dimer sphere (the dimension of which was determined from the crystal structure of a ParA homolog (Leonard et al., EMBO J, 2005)). Multiple interactions between the ParB-rich partition complex and ParA dimers can be clearly seen in Video 3. We agree that this information was not clearly described in the main text of the original submission. The text has been revised to make it clearer.

Regarding the reviewer’s concern about the multiplicity of parS sites and their separation, it is important to note that there are only 2 parS sites in the C. crescentus chromosome and they are separated by only 42 nucleotides, which can be, at most, 14 nm long. Therefore, we believe that there is only one stable ParB/parS assembly complex per chromosome in C. crescentus. This is likely to be the case in most, if not all, plasmid systems.

However, the notion of separated ParB/parS assemblies remains interesting as it may be relevant to the B. subtilis chromosome case in which 10 parS sites are spread across a ∼2 Mb-nucleotide region flanking the origin of replication (Breier and Grossman, Mol Microbiol, 2007). By epifluorescence microscopy, this region appears as a single diffraction-limited spot (Lin et al., PNAS, 1997, Glaser et al., Genes Dev, 1997), indicating that the most distal parS sites are separated by ≤ 250 nm. As suggested by the reviewer, we have expanded the ‘diffusion-binding’ model to consider the cases of two ParB/parS assemblies (two spheres of 35 nm of radius) separated by a flexible linker of varying lengths to simulate the reviewer’s scenario. The reason for using a radius of 35 nm is to make the surface area of the two ParB spheres comparable to the surface area of the single partition complex sphere (50 nm of radius) used in the original model (2·π·352 ≈ π·502). Our simulations show that separating the parS sites by up to 400 nm had little, if any, positive effect on translocation (unpublished result), further supporting the notion that the elastic dynamics of the underlying DNA must be considered to obtain the translocation kinetics observed inside cells. Since the partition complex of C. crescentus is unlikely to form two or more ParB assemblies, we feel that these data do not belong to this manuscript. We would therefore prefer to publish these results elsewhere together with follow-up studies.
