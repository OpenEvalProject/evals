# Peer review - Round 1

Editors:
- Ariel Amir, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78743.sa0](https://doi.org/10.7554/eLife.78743.sa0)

This study provides new experimental data and detailed modeling of the partitioning of low copy plasmids under the control of the ParABS system in bacteria. The dynamics of the partition complex is tracked over many generations, providing valuable data to constrain the models. The authors propose a compelling model which can manifest either regular positioning or oscillations depending on the model parameters. The research will be of interest to biologists and biophysicists interested in cellular dynamics and internal organization in bacteria.


---

# Peer review - Round 1

Editors:
- Ariel Amir, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78743.sa1](https://doi.org/10.7554/eLife.78743.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "High-throughput imaging and quantitative analysis uncovers the nature of plasmid positioning by ParABS" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers believe that the paper has the potential to be published in eLife, but have substantive comments that should be addressed, as detailed below and in their reviews. Please note that both reviewers did not hinge the publication on additional experiments.

(1) Not all claims are fully supported by the presented data, in particular the claim of the role of ParA hopping/diffusion.

(2) Limited analysis of the control parameters.

(3) Unsatisfactory analysis on the origin of the difference between F1 and pB147 plasmids dynamics.

(4) More careful comparison/analysis to previously published model of ParA and ParA-like systems is an essential element needed to make this work impactful.

(5) (Optional) Providing information on the ParA distribution would be a very strong addition.

Reviewer #1 (Recommendations for the authors):

Using "hopping" as a substitute for the ParA diffusion over the chromosome and then stating that it was "primary determinant of the geometry sensing" (abstract) might be misleading. What the authors did – they considered ParA diffusion in the model. And that apparent diffusion over the chromosome might be result of at least two non-exclusive scenarios – repeated cycles of binding/unbinding of ParA dimer intermittent by the diffusion of the unbound ParA dimer or direct hopping of chromosome-bound ParA from one chromosome locus to another when they come into contact upon their intrinsic fluctuations.

Along the same line, stating in the Abstract that "we identify ParA hopping on the nucleoid as the primary determinant of this geometry-sensing" is not correct as neither the hopping was explicitly considered in the model nor the author really tested whether this statement would be correct even for ParA diffusion. The only test involved was analysis of the motion in the short cells vs long cells, without perturbation of diffusion per se. Moreover, the authors observed that in case of pB171 plasmid mode of motion was different, yet it is not clear whether the difference could be explained by the model as due to a difference in diffusion coefficient or kd or something else. This reviewer believes that "identify" requires a little bit more that being able to reproduce observed behavior by changing a parameter in the model.

"Lack of quantitative experiments" mentioned several times by the authors might not be exactly the case. While previous experiments/analysis was not the same what the authors did, several groups measured different experimental metrics (just a few examples, far from exhaustive, – Li et al. 2004 Mol.Microbiol, Surovtsev et al. PNAS 2016, Le Gall et al. Nat.Commun. 2016)

The authors compare their model to "diffusive" and "superdiffusive" models (Figure 1 Figure Sup 2A), but details on how they were modeled are lacking.

p.5 ln 1-3 The authors report characteristic timescale, τ, at which elastic fluctuations act to be about 120 s using fitting of the velocity vs position data, and then they report that the same τ is ~ 170 s using velocity and position autocorrelation functions fitting, concluding the values are comparable. That seems to this reviewer as quite a difference, warranting at least some comment on the potential origin of the difference.

Regarding velocity autocorrelation function and positional dependence, it would be really helpful and reassuring to calculate them from the higher temporal resolution (dt=1s mentioned for MSD and D calculations) since the authors already have the data.

p.5 ln 33 …have previously shown that regular positioning can theoretically be achieved, independently of the particular mechanism of force generation, through the balancing of the diffusive fluxes. Given that the force is what really defines where the cargo moves, I don't think the positioning mechanism can be dissected from the mechanism of force generation, once one tries to conclude what specific mechanism operates for a given experimental system. For example, in the model the authors simulated here the force is not directly dependent on the flux of the ParA on the plasmid, rather it depends on the local distribution of ParA. While it is not necessarily negates the authors reasonings, it does require an additional explanation on how these reasonings relates to the simulated model…

p.6 Figure 2 (A) When s ≪ L/2 (i), where L is the nucleoid length, a disparity in the flux only exists very close to the poles (blue region). This seems somewhat counterintuitive, as this regions actually many s away from the sink of ParA (i.e. plasmid)…

p.7 30-33 Imaging studies in several Par systems, especially those that position non-DNA cargos, have observed that ParA fluorescence can be higher at the plasmid than elsewhere (Roberts et al., 2012; Schumacher et al., 2017). This is in somewhat disagreement with the canonical picture of the ParB coated cargo acting as a sink for ParA-ATP. This is not a real conundrum, as previous models showed this effect (Surovtsev et al. Biophys.J. 2016, Hu et al.Biophys.J. 2021)

Figure 3I What is the color code? It is actually described deep in the methods, but it would be really useful to have it in the main text or figure legend.

Figure 3 Sup.Figure -2B what is the color code?

In image analysis description, the authors do not provide any details beyond referring to the general Segger description and MotherSegger code on the most important part – cell segmentation and defining position of the plasmid. This reviewer believes that some short description should be readily available within the text for the reader to understand potential limitations. For example, beyond just finding position in the image, how it was used for the analysis – was it position in image coordinate or relative to the cell coordinate, and how change in the coordinate, without motion due to cell growth was taken into account.

It seems that the number of ParA and spring constant values are not specified for the model.

Reviewer #2 (Recommendations for the authors):

The paper claims that they are the only paper to have a model that shows regular positioning of the ParABS system and that models without substrate hopping on the nucleoid only admit oscillations. This is not true. Jindal and Emberly (2019) showed that regular positioning of plasmids could occur in a model that did not allow for any diffusion of substrate in the nucleoid and that oscillations would emerge due to relaxing of confinement or potentially the liberation of substrate resources due to the addition of plasmids. Indeed the phenomena observed in these experiments (regular positioning, transitioning to oscillations, and back to regular positioning) was predicted in that paper. Have the authors fully explored the parameter space of their model? If they set kh = 0, (i.e. no hopping), are there any values of n_A, and on/off rates that allow for regular positioning that transitions to oscillations as the cell lengthens? For regular positioning, it requires a broad wake that is balanced between left and right. On longer cells, the confinement is relieved and the complex can oscillate. It would be interesting to know if the stochastic formulation of the model does not allow for any regular positioning if kh=0. If it does, are the parameters values such that they are completely inconsistent with measured kinetic parameters, thus necessitating hopping for the given system.

A few other comments/questions:

I'm assuming Figure 6 is from experimental data, but there are no reported cell numbers for the various distributions and statistics.

it would have been nice to have seen data from > 2 plasmids. Do the authors ever see oscillations in 2 plasmids switching to regular positioning once 3 plasmids are present (i.e. Figure 7F with a column for 3 plasmids). Presumably yes as there are around ~20% of the 2 plasmid systems oscillating, and when 3 are present, regular positioning likely follows. Do they ever get filamentous cells, and what are the dynamics like in those cells?

I am intrigued by the difference in dynamics for the F-plasmid and pB171 plasmid. Their experimental results for the 1b system show it is more likely to oscillate. Why? Is it due to a smaller s? The paper claims that it is due to smaller s, but no real discussion/evidence is given.

I could find no details of how varying n_A affects results. As in most other published models, this also has a huge effect on dynamics, similar to their parameter, λ. Could some of their observations be due to cell-to-cell heterogeneities in n_A? Also dilution would have an effect, which it is not clear if it is taken into account here. Do they use n_A=500 for all simulated cell lengths? Could differences in the total amount of ParA explain the different dynamics between the F plasmid and pB171 (see my comment above)?

Have they done lineage tracking? Do they see correlations in the likelihood to do regular positioning or oscillations? If so, especially for the case with 1-plasmid oscillations, is it due to length differences in the daughter? or could oscillations be arising from some other unmeasured system parameter?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "High-throughput imaging and quantitative analysis uncovers the nature of plasmid positioning by ParABS" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor. Please take note of the points below and address them in the final version submitted.

Reviewer #2 (Recommendations for the authors):

Summary:

This work focuses on how subcellular objects (plasmids) can sense spatial dimensions of the cell and how they are transported to the specific targeted positions. The authors expand previously proposed 'DNA-relay' mechanism of the intracellular transport in which plasmid are actively driven by chromosome fluctuations. By adding diffusion of chromosome-bound ParA, a protein that 'links' the plasmid to fluctuating chromosome, to the model, they show that this expanded model can reproduce full range of observed experimental dynamics including plasmids oscillations and direct motion to the mid-cell. This work reconciles some apparent differences between previously published models on ParA-dependent intracellular transport and expand our understanding of the chromatin-fluctuation-driven intracellular patterning.

Review:

Kohler and Murray present high-throughput image-based measurements of how low-copy F plasmids move (segregate) inside E. coli cell. This active segregation ensures that each daughter cell inherit equal share of the plasmids. Previous work by different labs have shown that faithful F-plasmid segregation (as well as segregation of many other low-copy plasmids, segregation of chromosomes in many bacterial species and segregation of come supramolecular complexes) requires ParA and ParB proteins (or proteins similar to them) and is achieved by an active transport mechanism. ParB is known to bind to the cargo (plasmid) and ParA forms a dimer upon ATP binding that binds to DNA (chromosome) non-specifically, and also can bind to ParB (associated with cargo). After ATP hydrolysis (stimulated by the interaction with ParB), ParA dimer dissociates to monomers and from ParB and the chromosome. While different mechanisms of the ParA-dependent active transport had been proposed, recently two mechanisms become most popular – one based on the elastic dynamics of the chromatin (Lim et al. eLife 2014, Surovtsev PNAS 2016, Hu et al. Biophys.J 2017, Schumaher Dev.Cell 2017) and the other based on a theoretically-derived "chemophoretic" force (Sugawara and Kaneko Biophysics 2011, Walter et al. Phys.Rev.Lett. 2017).

Measuring motion of F plasmid in large number of cells with one or two plasmids allowed authors to overcome inherently stochastic nature of the motion and to analyze plasmid spatial distribution, plasmid displacement (i.e. velocity) as a function of their relative position, and autocorrelations of the position and the displacement. They concluded that these metrics are consistent with 'true positioning' (i.e. average plasmid displacement is biased toward the target position – center for one plasmid and 1/4 and 3/4 positions for two plasmids) but not with 'approximate positioning' (i.e. when plasmid moves around target position, for example, in near-oscillatory fashion). This 'true positioning' can be described as a particle moving on the over-dampened spring. They reproduce this behavior by expanding previous model for 'DNA-relay' mechanism (Lim et al. eLife 2014, Surovtsev PNAS 2016), in which plasmid is actively moved by the elastic force from the chromosome and ParA serves to transmit this force from the chromosome to the plasmid. Now, the authors explicitly consider in the model that the chromosome-bound ParA can diffuse and this allows the model to achieve 'true plasmid positioning' for some combination of model parameters in addition to oscillatory dynamics reported in the original model.

Based on their computational model, the authors proposed that two parameters: (1) diffusion scale of ParA, i.e. typical length diffused by ParA before dissociation, λ = 2(2Dh/kd)1/2/L (here, Dh is diffusion rate of DNA-bound ParA, kd is ParB-independent hydrolysis rate, i.e. lifetime of DNA-bound ParA); and (2) ratio of ParB-dependent and -independent hydrolysis rates epsilon = kh/kd; are key control parameters defining what qualitative behavior is observed. By varying these parameters (via changing ~30- and ~200-fold Dh and kh) they showed that their model encompasses all observed dynamic behaviors – random diffusion, near-oscillatory behavior, or overdamped spring ('true positioning'), and illustrated how dynamics of the system changes between these 3 modes of motion. The parameter analysis includes also changing other parameters such as ParA number, elastic spring of the chromosome, etc. for some selected initial combinations of the λ and epsilon.

The authors also show by simulations that overdamped spring dynamics can transition into oscillatory behavior when λ decreases, for example by cell growth. Indeed, they observed more oscillatory behavior when they compared single-plasmid dynamics in the longer cells compared to the shorter cells. This was not the case in double-plasmid cells, in perfect agreement with their analysis. The authors concluded that the system operates close but below (perhaps, "above" should be used as it refers to bigger λ) the threshold to oscillatory regime. The authors also calculated ATP consumption in the model and found that oscillatory regime minimizes ATP consumption.

I think the major impact of the paper is that the expanded model and analysis presented here shows how various dynamics (observed experimentally) can be achieved within the same mechanism in which an intracellular cargo is moved by the fluctuating chromosome via ParA-mediated attachments. While original "bare-bone" DNA-relay model could explain active transport of the plasmid cargo, taking into account diffusion of DNA-bound ParA dimer (and in appropriate value range) was essential to achieve "true positioning" observed for F-plasmids. Importantly, parameters analysis shows how the expanded model encompasses, depending on combinations of control parameters, previously modelled 'oscillations' (Surovtsev PNAS 2016), 'local excursions' (Hu et al. Biophys.J 2017) and 'true positioning' (Schumaher Dev.Cell 2017).

Overall, I think, the revised manuscript unifies previous modelling efforts on ParA/ParB and similar (PomXYZ) systems and clarifies role of ParA diffusion in the dynamic behavior. It advances our general understanding of how out-of-equilibrium dynamics of ParA ATP cycle allows to achieve various modes of intracellular dynamics depending on parameters combination. In a broader perspective, it advances our general knowledge of intracellular organization and of DNA segregation.

Suggestions/Questions:

While the revised manuscript now really helps the reader to understand how ParA/ParB system works, thanks to explicit comparison to earlier models, here are a few things that could be addressed by the authors (in this reviewer opinion).

Again, there is no doubt that λ is an important parameter of the model, however I found the authors explanation (Figure 2) confusing (at least for me). They argue about importance of the parameter based on the importance of the balancing ParA fluxes to the plasmid. But these fluxes would be there and would be balanced only in the center (for one plasmid) no matter how big a nucleoid is relative to the ParA diffusion scale… Moreover, the plasmid interacts with ParA bound mostly within few σ (range of chromosome fluctuations), so argument about "information" also does not work out… Also, the authors did not really test whether λ (but not Dh alone) governs dynamics. The authors varied λ and epsilon independently by changing Dh and kh, but does plasmid dynamics look exactly the same if we say change instead Dh, kd, kh and L such that λ and epsilon do not change? Other parameters sweeps that were added to the manuscript are very appreciated, but they do not answer this question. Along the same line, a bit more expanded discussion on underlying nature of the transition to different dynamics during these sweeps may help reader to understand interplay between different parameters in determining dynamics qualitatively. I found description of results of these sweep too brief (so not very insightful).

Along the same line, it might be a bit counter-intuitive that the system behavior almost does not depend on number of ParA. For example, the authors argued for the importance of λ based on ParA-fluxes, but value of the fluxes should strongly depend on the amount of ParA in the system. Additionally, the authors report that the plasmid velocity strongly depends on the ParA amount associated with it (Figure 3—figure supplement 2 B) (perhaps, on overall amount of ParA as well). One might think that the velocity would play a role whether we observe a strongly dampened spring or a decaying oscillator. Maybe it is a naïve thinking, but, perhaps, this warrants some explanation in the manuscript. And, while for relatively high ParA number the dependence might be saturating, Figure 3—figure supplement 3 top-left and Figure 3—figure supplement 4D suggest that lowering ParA may drive switch to different dynamics.

Additional comment on parameter sweeping. Since ParA diffusion is an "effective" description of some underlaying dynamics, effective Dh might depend on other parameters, i.e. cannot be varied independently. For example, in a potential "binding-unbinding-bulk_diffusion-binding" scenario, Dh depends on k_dis, ka and D_bulk. In an alternative scenario, where ParA hopes (without unbinding) to a new DNA position, Dh depends on σ and Da. While ideally these scenarios should be modelled explicitly to test how changes in these parameters affect apparent Dh and plasmid dynamics, such a limitation, perhaps, should be mentioned in the manuscript (since it will make the model more complex and also there is only so much we can do at once).

Regarding pB171 plasmids, having a plot similar to Figure 1E and F would be nice, as they were used as an evidence for 'true positioning' regime. And still some potential explanation of what might be different between F and pB171 plasmids – D, kd(?) – would be a nice addition as it might prompt someone to test it in the experiment.

On presentation:

I found the title of the paper too vague, as "nature of plasmid positioning" could be interpreted very differently (and thus whether the work "uncovers" it or not).

I would suggest adding to the abstract what were the key ingredients of the authors model to succeed in achieving full range and transition between different modes of the plasmid dynamics.

Still in this reviewer opinion, "lack of quantitative measurements of plasmid dynamics" (used several times through the paper) might be misleading as the authors measured from microscopy exactly the same thing – position vs time – as earlier works. The strength of the work is not in a measuring experimentally a new thing, but having a great statistics (high-throughput imaging!) that enabled a new analysis (meaningful beyond inherent stochastic noise) – velocity vs position and velocity and position autocorrelation functions. I would emphasize this achievement instead.

Figure 1E referred before any other panels, and similar happens with some other panels through the manuscript.

Table1: I do not think Weber et al. 2010, or Javer et al. 2014 reported any chromosomal spring constants (or σ) as both studies focused on subdiffusion of the loci motion.

Not sure if this comment to the authors or to eLife: having only pdf with tracked changes made task of evaluating manuscript unnecessary hard, as reading it and finding right version of figures become cumbersome.
