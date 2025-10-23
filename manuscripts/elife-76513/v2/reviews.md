# Peer review - Round 1

Editors:
- Karine A Gibbs, https://ror.org/01an7q238 University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76513.sa0](https://doi.org/10.7554/eLife.76513.sa0)

This paper nicely considers how the biofilm matrix impacts the organism's moving within that environment, connecting prior analyses of cell movements on/within abiotic substrates to those within a "living" substrate. Though there are instinctive descriptions for this motility, the strength of this manuscript is the development and implementation of a statistical model that quantifies critical parameters and incorporates interactions with the biofilm matrix itself. While the manuscript measures the differences between morphologically distinct bacteria, a long-term possibility is to achieve predictable and reliable delivery of antimicrobials (delivered by bacteria or an abiotic object) into the biofilm's center, thereby reducing a biofilm's recalcitrant responses to biocontrol chemicals.


---

# Peer review - Round 1

Editors:
- Karine A Gibbs, https://ror.org/01an7q238 University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76513.sa1](https://doi.org/10.7554/eLife.76513.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Inferring characteristics of bacterial swimming in biofilm matrix from time-lapse confocal laser scanning microscopy" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Iago Grobas (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Overall, the presented data support the conclusions and provide insights into bacterial motility. However, there are concerns about the model (assumptions and extensions), the limited discussion/application of bacterial motility and morphology, and aspects of the experimental design. If you choose to revise this manuscript, please address the following items:

1) In its current form, the paper lacks a characterization of the swimming motility of the bacteria in a Newtonian fluid, an important aspect to rationalize the impact of the biofilm.

2) Clearly communicate how this model would help characterize bacteria motility in exogeneous biofilms (instead of performing microscopy).

3) The discussion of cell morphology and potential impacts on motility within the biofilm is inadequate. Cell morphology should also be considered when characterizing swimming motility in a Newtonian fluid.

See the detailed comments for specific concerns regarding each of these items.Reviewer #1 (Recommendations for the authors):

This manuscript by Ravel and colleagues connects prior analysis of bacterial movements on/within abiotic substrates to those within a "living" substrate. The primary outcome is developing a methodology to examine the overall swimming of a bacterial population within another bacterium's biofilm. Implementing these methods would allow for differentiation among bacterial species, identifying microbes that can travel more deeply within an existing biofilm. The authors consider that in the long-term, one could potentially use microbes to reliably deliver antimicrobials (or similar) into the heart of a biofilm, thereby hopefully reducing the biofilm's recalcitrant responses to these biocontrol chemicals.

Strengths

– These scientists develop an inference model and supportive methods to ascertain traits of the population of swimming cells. While similar methods and models exist, the specific examination within a "living" biofilm is intriguing and foundational for developing drug delivery methods or interpreting how cells of any type, e.g., immune cells, might penetrate these bacterial communities. These results also raise questions about the role of cell shape, size, and motility in infiltrating already formed colonies, and conversely, how the composition of the extracellular matrix and cell stacking could protect biofilms from invasion.

– The scientists sequentially test their inference model with and without experimental data. Similar results emerge, suggesting that the inference model could provide an initial step to evaluate different bacterial strains with various biofilm conditions rapidly.

– The authors do a good job of clearly explaining each variable's definition and directly addressing many of the assumptions and constraints of these experiments.

Overall, the presented data support the conclusions, except for the discussion about bacterial shape and motility.

Weaknesses

– An underlying thread is that the difference in shape and flagella size/motility contributes to how each Bacillus strain can navigate the S. aureus biofilm. Yet, the discussion of these contributions is not until the end and relies on abstract assertions of potential behavioral differences. This analysis could be more robust if it included analysis of each species' motility in the absence of biofilm so as to establish if and how these species swim differently from one another. As such, lines 416 – 419 are not strongly supported by the data in this manuscript or the current literature.

– There is a potential bias in the data due to the constraints of the experimental set-up: only focal planes near the well's edge are included in the analysis. The biofilm in these zones could have a distinct physical structure (due to the well's wall) than the remainder of the biofilm. While the datasets presented here are self-contained for analysis, any conclusions about the general/overall biofilm are more narrow (or should be taken with a caveat).

– The time-scale of 30 minutes at 30{degree sign}C could permit bacterial growth while cells are moving. The inference measurements appear to be reasonably robust against these potential impacts (perhaps incorporated as part of the "noise" variable). The possible cell growth is worth also considering if attributing differential swimming behaviors to cell morphology or flagella size/location.

I have included all of my scientific comments in the public review. A couple of typographical errors alter a sentence's meaning. The critical ones are as follows:

– line 96, dies --> dyes

– line 198, γ --> β (?)

Further, please clarify that in Table 1 that the video duration is in minutes.

Reviewer #2 (Recommendations for the authors):

This work aims to create a workflow to elucidate how the biofilm matrix affect the trajectories of exogeneous swimming bacteria. In principle, this could potentially be interesting to study biofilm spatial organization and also to characterize transport of synthetic particles such as nanoparticles or colloids carrying biocides into the biofilm. However, the statistical model presented here does not consider the surface interactions between the particles and the porous media which makes the model quite specific to the bacteria-biofilm interaction and, therefore, difficult to extend to other particles and porous materials.

The article is mainly focused on the statistical model which quantifies the key parameters of the bacteria swimming motility affecting their trajectory within the biofilm matrix. The main parameters studied are the acceleration, swimming speed, net displacement in the swimming trajectory and the area covered by the bacteria during the trajectory. The variables in the biofilm matrix that can affect those parameters are the local differences in cell density within the biofilm and the cell density itself. In this regard, the authors found a good agreement between the trajectories inferred by the model and the real trajectories, validating their model for the strains tested. The model allows to decipher how the different bacteria species adapt to the biofilm matrix. Nevertheless, I fail to understand how the model provides an advantage with respect to just observing the trajectories under the microscope. Following the bacteria with microscopy could identify when they slow down or speed up depending on the density of the host biofilm matrix as the model does.

Finally, the authors connect the bacteria morphology of the three species studied to the kinematic descriptors of the bacteria trajectories. The morphological features logically agree with what their model predicts, meaning that, long bacteria are slower in the biofilm matrix and bacteria with lower aspect ratio finds easier to go through the porous biofilm matrix. I find this like a nice way of checking that the model works but at the same time I wonder how useful this model can be since the mentioned morphological features and their impact in the bacteria trajectories could be inferred without the model, just by using microscopy. On the same line, the authors suggest that a brush-like group of thin flagella make changing directions easier but I do not see how this is checked experimentally.

In summary, the parameters affecting the model and the correlation between the kinematic variables of the swimming trajectories and the local conditions in the biofilm are thoroughly checked. However, my concern is that I do not see how this model can widen our knowledge about how bacteria navigate biofilm matrix since tracking bacteria in a biofilm matrix would give similar information. Furthermore, I do not know how limited this model is in terms of the surface chemistry interaction between the biofilm and the bacteria, or the particles in general, that are introduced in the biofilm. This surface chemistry interaction could totally change the trajectory of the swimmers independently on the parameters studied in this article which limits the model to bacteria swimming in a host biofilm and does not allow the extension of the model to synthetic particles or other porous media.

I do not understand very well Figure 1a. There are red bacteria (guest bacteria) in the last frame that do not appear in previous timestamps. Specifically, the trajectory at the bottom right has its origin in an area that is visible for all timepoints and I do not manage to see any bacteria in there in any of the timestamps.

I have also a problem with Figure 1b. I guess that in the caption, 'distance' refers to the shortest distance between the initial and final point of the trajectory. But this is what the authors seem to be drawing in the figure for 'displacement' which is defined as 'the total length of the trajectory path'. So I think these two should be swapped. Actually, I think the correct representation according to the capture is as drawn in Figure 1d.

In table 1, could the units of time interval be specified?

In Figure 2, is the whole set of trajectories for each species displayed for 1 batch or for the 3 batches? I think Figure 2, would be easier to follow if the order of the bacteria in (a) matches the order in (b). I think it would also benefit from a rough y axis in the first graph of the upper panel of (b). What are the units in the x axis? If the magnitudes are dimensionless because they are normalized, I think this should be said in the caption, also because dimensionless magnitudes are referred as V* and A* in the main text. The legend in the bottom panel (b) containing the names of the bacteria should be in italics and 'B' separated from the rest of the name. There is a mistake in the caption (2b), the magnitude 'Area' is not mentioned in the caption.

Do the authors know why the distributions in Figure 2 look quite similar for B. pumilus and B. cereus but different to B. sphaericus? It seems to me that this might be an artefact coming from the fact that less trajectories are plotted for B. sphaericus. I think it would be informative if they put a label with the number of total trajectories displayed in this panel.

I do not see very well the added value of the bottom panel in Figure 2b. I have read the Results section just looking at the 50% line, I don't think the others present much more additional data.

I think the penalization coefficient 'γ' being inversely proportional to the relaxation time should be further explained.

In line 316 says that B. pumilus shows the highest v0 value, indicating a higher ability to swim fast in low density. But v0 was defined as the speed at the highest density, so this means that B. pumilus swims fast at high density. Which one is right?

I do not know if it can be argued that B. sphaericus presents no difference between v0 and v1 as it is written in the main text. It seems that the v0 is extremely low, almost 0, indicating that it cannot swim at high cell density. However, this strain has the highest v1 mean.

Appendix 1: In Figure 1. I think the red channel's brightness should be increased. When the authors say 'rescalled biofilm density map'? what do they mean? Is it just the first image of the biofilm for a certain condition? Or do they alter the image in any way? In this same Figure 1, there is a white space in the gray frame enclosing the 'swimmer trajectories in normalized biofilm'.

I would put figure 6 in an appendix. I do not think it adds much value to the aim of the paper.

Not sure about Fig7. I think it's better to put a square in the zoomed in regions instead of the dashed line. For example, in the middle panel, the zoomed in version of B. pumilus seems like there are two bacterial bodies attached to each other. However, this is very difficult to see in the zoomed out version. I think this would be clearer if instead of a dashed line there was a dashed square around the region.

Why is there a huge change in the epsilon coefficient depending on the species? I thought random noise would affect roughly the same to all species.

I think in general, the paper would benefit if the figure 7 was changed to figure 1. I would motivate the paper by saying that there are three species with different hydrodynamic properties because of shape, number/type of flagella, etc. and this leads to the hypothesis that the behaviour would be different in the porous biofilm matrix. For example, the longer body of B. sphaericus would be an impediment when navigating the biofilm and therefore they expect lower motility, etc. As the paper is structured now, the whole story seems to be around checking whether their model is correct.

I do not understand the calculation of the visited area. What is the parameter k and ns? Why do they have those values? Why was the visited area not calculated using the trajectory multiplied by the size of the particle?

Reviewer #3 (Recommendations for the authors):

Ravel et al., investigate the swimming behavior of three different Bacillus species in the biofilm formed by Staphylococcus aureus. The biofilm structure and the swimmers' behavior are experimentally characterized using time-lapse confocal microscopy. The swimmers' behavior is described by several parameters measured from tracking their positions in time, including acceleration and speed. The biofilm structure is described in terms of the density of the biomass. The data highlight differences in the shape of the trajectories, speed distributions, and tendency to visit high-density areas of the biofilm in the three different species. These observations are reproduced using a generative model of the data and tentatively explained in terms of bacterial morphology. The model could, in principle, be used to predict the motility of other bacterial species in biofilms.

The conclusions of this paper are supported by the data and the model. Still, the explanation of the former in terms of bacterial motility and morphology needs to be extended and some aspects of the model need to be clarified.

1) The authors explain the different swimming behavior observed in the biofilm in terms of different bacterial morphology, i.e. shape and number of flagella. However, the impact of these differences in a Newtonian fluid should be evaluated and used to better understand the adaptation strategies to the biofilm. In addition, the observations should be commented in light of the literature studying bacterial motility in non-Newtonian fluids (Phys. Rev. Fluids, 5, 073103 (2020); Nat. Phys, 15, 554-558, (2019); Sci. Rep., 5, 15761 (2015); PNAS, 111, 17771-17776 (2014)), where the impact of the flagellar shape and motility are discussed.

2) While a lot of attention is dedicated to describing how bacterial motility is quantified, very few details are given about the measurement of biofilm density and the possible error sources. Since this is a primary ingredient for the interpretation of the results, I would recommend commenting on the procedure and the sensitivity of density measurement.

3) The authors suggest that bacterial motility could help create channels into the biofilm, affecting transport. Is this effect observed in the experiments? This aspect should be clarified and commented on.

4) The purpose of the model and its pros and cons should be discussed more clearly for a general audience. In particular, the authors should clarify the added value of the model with respect to the experiments.

5) Do these bacteria perform a run-and-tumble or a run-and-reverse type of motion in water? Could a back-and-forth trajectory be described as a run-and-reverse?

6) Table 1: The units are missing.

7) Line 125: It would be helpful if some numbers were given in the text to quantify the "large swimming distances" or the "widest swimming distribution".

8) Figure 1: The biofilm density map should be added in panel a. I would recommend avoiding the superimposition of the distributions of ||A||, ||V||,dist, disp and area in panel b.

9) Line 136: Could the term "few" be quantified? From Figure 1a the exceptions seem to be several.

10) Line 192: The bio-readership may not find clear the term "basal" used to identify the simulations. The same applies to "ground truth" in the following. These terms should be defined to improve clarity.

11) Line 303-306: The conclusion on the variability of the outputs should be clarified. Is it a positive feature or is the model missing something?
