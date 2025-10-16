# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69181.sa0](https://doi.org/10.7554/eLife.69181.sa0)

There has been a lively debate recently concerning the multiplicity of reported observations of phase-separated compartments inside of cells. Specifically, some claims of phase separation have been challenged, and an alternative model has been put forward that explains clustering of observed particles as resulting from colocalization of binding sites with no phase separation. The current study does an admirable job of proposing and analyzing ways of distinguishing these two scenarios.


---

# Peer review - Round 1

Editors:
- Agnese Seminara, University of Genoa Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69181.sa1](https://doi.org/10.7554/eLife.69181.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Physical observables to determine the nature of membrane-less cellular sub-compartments" for consideration by eLife. Your article has been reviewed by 3 peer reviewers; this evaluation has been overseen by Agnese Seminara as Reviewing Editor and José Faraldo-Gómez as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Pierre Ronceray (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers believe the work is suitable for eLife but also believe the manuscript could be improved upon – as noted below. Please consider their concerns and recommendations and implement the suggested changes whenever possible.

Reviewer #1:

The authors propose several ways of leveraging single-particle tracking experiments to distinguish between intracellular phase separation and an alternative model of clustered binding sites. The first proposed scheme is particularly intuitively appealing: in the binding site scenario, the local density of binding sites both increases particle density and slows effective particle diffusion, leading to a definite relationship between these two quantities, while the phase separation scenario would not necessarily couple these two quantities. The additional schemes based on particle movement near a cluster boundary, angles between consecutive steps, and search times add to the arsenal of potential analysis tools. Overall, the work is timely, rigorous, and generally clearly presented and given the growing list of reported observations of phase separation, will appeal to a broad audience.

1. The authors don't explicitly address the effects of crowding that might occur inside a cluster of binding sites. Crowding can change both the free density and the free diffusion coefficient of the particles in the cluster. How would such crowding affect the relation between observed particle density and observed diffusion, particularly if crowding scales with density of binding sites?

2. I found the discussion of the angles between consecutive steps hard to follow at points. In particular, what do the authors have in mind by the statement that binding sites can "reflect" the motion of tracked molecules (line 219)? I also wasn't sure what the final sentence of that section was meant to convey – some more guidance on the conditions under which this approach is useful would help.

3. The paper is well written but could use some additional proofreading for spelling, e.g. "dropblet", "membranelss", "rapide", "displacememnt", "mimick".

Reviewer #2:

Heltberg et al., investigate two possible mechanisms for the formation of nuclear foci and how these mechanisms can be distinguished experimentally, based on single-particle tracking of molecules that are up-concentrated in the focus. First, liquid-liquid phase separation (here: Liquid Phase Model, LPM) is treated as one of the major mechanisms currently hypothesized. Second, as an alternative mechanism, a polymer-bridging model (PBM) is investigated, in which the focus is held together by polymer bridges and contains binding sites, which can lead to local enrichment, appearing as a focus.

The theory is presented in a clean way, and while the Langevin equation for single molecules in a phase-separated liquid comes without derivation, it is plausible, and in fact backed up by our own calculations. A similar Langevin equation is found for the PBM and it is subsequently shown that both models can lead to very similar displacement distributions, thus showing that this simple observable cannot always distinguish between PBM and LPM.

Subsequently, the authors derive an effective description of the PBM, based on the experimental observation that potential binding sites on the DNA (proxied by Rfa1, a DNA-binding protein) diffuse much more slowly than a typical repair factor (represented by Rad52). Thus there is a separation of time scales between the two relevant diffusion processes, which is used to constrain the possible parameter combinations for the PBM. Based on these constraints, the authors shown that PBM is incompatible with their previous experimental results.

The remainder of the paper deals with a number of interesting observables, such as the angular distribution of displacements and search time to find a repair target, which can also be used to distinguish PBM and LPM with an ideal setup.

Strengths:

Heltberg et al., present a clean way to distinguish LPM on the one hand, and a realization of PBM on the other hand, based on theory. This is validated by comparison to data they obtained in previous work. The theory is rigorous and the data analysis is well carried out, save for minor ambiguities, which can likely be eliminated during revision. The paper draws its main strength from its interdisciplinarity.

Conclusions and Discussion:

The authors have achieved their goal of distinguishing LPM and PBM. The corresponding theory will be of great use for everyone in the field aiming to make this distinction based on single molecule tracking, a strategy that has been attempted numerous times, but eventually always failed due to the lack of an appropriate theoretical framework. Heltberg et al., have gone on to show a striking difference between experimentally constrained PBM realizations and the experimental measurements themselves, rendering the PBM much less likely than the LPM.

The manuscript could use some additional proofreading for grammar/typos.

Regarding the references to Miné-Hattab et al., 2021 we were uncertain with regard to two points:

1. Figure 4b shows a striking agreement between the focus size and the minimum in the time-to-find-a-target function. Measuring the focus radius of 120 nm with such a high accuracy requires exquisite microscope resolution, while we believe that this is in principle possible with PALM, we couldn't find any supporting data for this resolution in the original paper, would it be possible to point us either to the right place in the manuscript or to general references that make clear that this is a standard resolution for live-PALM the way it was used in Miné-Hattab et al.?

2. Please point us to the measurements of inverse partitioning (pout/pin). We weren't able to immediately find them in the previous paper.

Abstract/Intro:

Foci as a word works, however, in particular in the intro condensate and foci need more of distinction. A nucleolus (as a very prominent example of a nuclear condensate) wouldn't be called focus in the literature.

The abstract seems to be missing a key point of the paper, namely that based on the available observables/data a call can be made that yeast repair foci are more likely LPM, rather than PBM.

L48: The references seem to be a mix of reviews and primary research, we believe this strong statement calls for only primary references.

L54: What did Miné-Hattab et al., find? How did you make the call in your previous paper?

Results:

L73: maybe 'by the Boltzmann factor' is a bit easier to google for the uninitiated reader, rather than 'Boltzmann's law', which isn't really a thing.

L76: 'While this description is general' is unclear, but could simply be left out.

L80ff: Motivate why this potential is a good way to model binding sites? In the PMB model, the diffusion model for the binding sites ends up being very similar to the one used for LPM. Is it then fair to claim that this model is more "microscopic"? It seems that PBM is more microscopic only in words and not really in the modeling. One might say that the binding sites are just themselves following diffusion in an LPM. Then the difference between the two models is more about the fact that for LPM the tracer molecule diffuses in the LPM and in the other case the tracers do not feel directly the LPM but just bind to molecules (or binding sites) that are diffusing in the LPM. In this respect, the distinction between the two models does not contain much information on whether the foci are formed by phase separation or not. In view of the importance of this distinction and the ongoing controversies, the authors should clearly discuss this issue. To have a more microscopic model it might be useful to adopt a polymer model description, rather than a simple potential.

L92: Why exclude potential? Relevant for confinement, shape of droplet boundary (which might be a significant part of the droplet, for such small droplets). Also, six isn't much worse than five parameters.

L105: Maybe say that parameter values are mentioned in Figure legend.

L109: Why just the simple Gaussian of free diffusion? Shouldn't there be confinement effects for small droplets?

L116: Would be good to have references for k- in yeast. At least ballpark. Otherwise also look at other k-.

L120: Does Rad52 ever appear in groups, e.g. dimers or multiple times within the same repair site?

L127ff: This entire section is a bit less clear than the rest. Maybe a slightly longer, more systematic exposition could help?

L131: Rebinding description is a bit vague, maybe elaborate a bit? Can this be connected to appendix 1?

Equation 7: Shouldn't the second ∝ be an equal sign?

141: How realistic is this limit? Doesn't it imply also fast diffusion? In other words, it seems like equation 6 gives many constraints on what your rate can be. Please comment. How well does the time scale separation hold? If it doesn't, many of the conclusions would have to be modified.

L152: Recall the definition of δ r. Is average from equation 10 removed?

L161: Not sure about D0, according to table this is only part of LPM? Also not mentioned in L93.

L164: Typo in unit for rho.

L167: Is this shown? Is this Figure 2d?

L181 and equation 13: Inconsistent use of δ vs d.

Equation 13: In measuring this in 3C, is the average r as a function of r computed from displacements starting at r or arriving at r?

L164: Is it obvious that dr cannot be negative? What are the consequences of this? Is it true at the focus boundary?

L195: Why underestimate and how is this seen? Underestimate with respect to what ground truth? Overall the discussion of 3C, D should be extended and made clearer. It is one of the main signatures used to tell PBM from LPM so it should be very clearly discussed.

L197: Didn't you say above it was never negative? Now only for this value?

L199: Can you expand this a bit for a clearer picture?

L210: Without confinement in shouldn't it be uniform in any dimension?

L250: Can you comment more on the Burger Purcell limit? How relevant is the discussion in the present context? If it is relevant, it should be expanded.

L263: Missing 'of'.

L269ff: This seems quite weak as a test, compared to the previous results (in particular 2H). The PBM clearly also has a minimum, how different are these for different parameter ranges? It also seems very hard to control focus size in vivo.

L297: Using 'condensates' as a verb required rereading this sentence for clarification, maybe rephrase.

Figures:

General: It would be helpful to have bold one-sentence figure caption summaries. Please make sure to always mention the equations that each panel refers to in the figure caption.

1: Panel B: might be good to also have shading for the background of the nucleus. Otherwise the boundary could be mistaken for a nuclear membrane happened to us at first glance (also compare Figure 4b).

2: Panel D: caption: are (bottom) and (top) reversed?

Panel F: Caption: please clarify 'using displacement histograms'.

Panel G: Displacement is misleading for the x-axis label, how about 'r' or something like 'dist. from nucleus'.

Panel H: reorder legend, otherwise data point 'experimental observation' looks like legend.

X axis has D0, shouldn't this be D~? Same in caption for H.

To us this panel has the strongest evidence that the model of choice should be LPM,

is this true? If yes, please clarify in text.

Caption for H: Could you refer to the figures/sections in Miné-Hattab where the

partitioning is calculated? After a quick skim we weren't able to find it.

3: Panel B: What do the error bars refer to?

Panel C: Why the dip in the bottom panel? Equation 13 is said to never be negative? Is only Db varied between the bottom and top panels? If D~ is kept constant, shouldn't the plateaus be the same?

Panel D: Caption: black instead of blue line?

Are these plots purely based on equation (13)? Same as in C, how can this be negative?

Reviewer #3:

Membraneless condensates have recently become a central focus of the molecular and cellular biophysics communities. While the dominant paradigm for their formation, liquid-liquid phase separation (LLPS), has been well established in a number of cases for large, optically resolved droplets, there are significant concerns regarding the generality of this mechanism for smaller foci or puncta, and other mechanisms have been proposed to explain their formation. The problem is that it is very difficult to distinguish experimentally between these mechanisms for sub-optical resolution condensates. In this article, Heltberg et al., propose a novel method, based on the analysis of single molecule tracks, that allows discriminating between the liquid phase model (LPM) and one of the challenger mechanisms, the "polymer bridging model" (PBM). This method relies on the statistics of individual displacements – diffusion, radial displacements, angular changes – which are showed theoretically to exhibit different signatures for the two models. With realistic data this is sufficient to discriminate between the models: for instance in the case of double strand break foci (DSB), building on a recent work by some of the same authors, this article convincingly rules out the PBM in favor of the LPM. The author also investigate the influence on these two models on the search time to reach a specific small target – a commonly invoked role of condensates – and show that only the LPM substantially accelerates this, which could provide additional means to experimentally discriminate between the mechanisms, on top of the intrinsic interest of this finding.

This article is a welcome addition to the literature in this field, as it will help clarify the nature of these condensates, in particular below the optical resolution. It is well-written, interesting and the conclusions are justified. I particularly appreciate the effort to employ simulated data that are realistic for actual experiments, which strengthens the claims of applicability. Some aspects of the data analysis and of the modeling, however, are insufficiently discussed and would need to be precised / expanded.

1) The modeling is made under the assumption of thermal equilibrium, without further discussion. The authors should comment on why this is reasonable, in particular in view of the presence of active fluctuations and of chemical reactions in these condensates.

2) How is the diffusivity measured? Are these measures corrected for experimental error (e.g. using three-point estimators)?

3) The conditioning of the averages should be discussed, e.g. in Equation 13: I assume that it is in the Ito convention? Similarly for the angle changes.
