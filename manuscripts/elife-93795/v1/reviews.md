# Peer review - Round 1

Editors:
- Stephen A Baccus, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93795.3.sa0](https://doi.org/10.7554/eLife.93795.3.sa0)

This paper provides an important method that uses a computational model to predict photoreceptor currents in mammalian photoreceptors. By inverting the model, visual stimuli can be constructed to produce desired photoreceptor current responses. The authors provide compelling evidence that this approach can disentangle the effects of photoreceptor nonlinearities including light adaptation from downstream nonlinear processing, thus facilitating future studies of the higher visual system.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93795.3.sa1](https://doi.org/10.7554/eLife.93795.3.sa1)

Summary:

This manuscript aims at a quantitative model of how visual stimuli, given as time-dependent light intensity signals, are transduced into electrical currents in photoreceptors of macaque and mouse retina. Based on prior knowledge on the fundamental biophysical steps of the transduction cascade and a relatively small number of free parameters, the resulting model is found to fairly accurately capture measured photoreceptor currents under a range of diverse visual stimuli and with parameters that are (mostly) identical for photoreceptors of the same type.

Furthermore, as the model is invertible, the authors show that it can be used to derive visual stimuli that result in a desired, predetermined photoreceptor response. As demonstrated with several examples, this can be used to probe how the dynamics of phototransduction affect downstream signals in retinal ganglion cells, for example, by manipulating the visual stimuli in such a way that photoreceptor signals are linear or have reduced or altered adaptation. This innovative approach had already previously been used by the same lab to probe the contribution of photoreceptor adaptation to differences between On and Off parasol cells (Yu et al, eLife 2022), but the present paper extends this by describing and testing the photoreceptor model more generally and in both macaque and mouse as well as for both rods and cones.

Strengths:

The presentation of the model is thorough and convincing, and the ability to capture responses to stimuli as different as white noise with varying mean intensity and flashes with a common set of model parameters across cells is impressive. Also, the suggested approach of applying the model to modify visual stimuli that effectively alter photoreceptor signal processing is thought-provoking and should be a powerful tool for future investigations of retinal circuit function. The examples of how this approach can be applied are convincing and corroborate, for example, previous findings that adaptation to ambient light in the primate retina, as measured by responses to light flashes, mostly originates in photoreceptors. Application of the approach by other labs is facilitated by the clear exposition and the listing of obtained optimal parameter values.

Weaknesses:

The model is impressive, but not perfect, including some small systematic differences between model predictions and measurements from held-out cells. The deviations likely (partly) reflect differences between cells used for parameter optimization and test cells, as stated in the text (though this is not fully proven), which has to be kept in mind when applying the model, in particular with the listed parameters.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93795.3.sa2](https://doi.org/10.7554/eLife.93795.3.sa2)

Summary:

This manuscript proposes a modeling approach to capture nonlinear processes of photocurrents in mammalian (mouse, primate) rod and cone photoreceptors. The ultimate goal is to separate these nonlinearities at the level of photocurrent from subsequent nonlinear processing that occurs in retinal circuitry. The authors devised a strategy to generate stimuli that cancel the major nonlinearities in photocurrents. For example, modified stimuli would generate genuine sinusoidal modulation of the photocurrent, whereas a sinusoidal stimulus would not (i.e., because of asymmetries in the photocurrent to light vs. dark phases of a sinusoidal stimulus); and modified stimuli that could cancel the effects of light adaptation at the photocurrent level. Using these modified stimuli, one could record downstream neurons, knowing that any nonlinearities that emerge must happen beyond the stage of the photocurrent. This could be a useful method for separating nonlinear mechanisms across different stages of retinal processing and may be useful in vivo.

Strengths:

(1) This is a very quantitative and thoughtful approach and addresses a long-standing problem in the field: determining the location of nonlinearities within a complex circuit, including asymmetric responses to different polarities of contrast, adaptation, etc.

(2) The study presents data for two primary models of mammalian retina, mouse and primate, and shows that the basic strategy works in each case.

(3) Ideally, the present results would generalize to the work in other labs and possibly other sensory systems. The authors do provide evidence that a photocurrent model constructed from data in one set of cells can be used in a second set of cells.

Weaknesses:

(1) The model is limited to describing photoreceptor responses at the level of photocurrents, as opposed to the output of the cell, which takes into account voltage-dependent mechanisms, horizontal cell feedback, etc., as the authors acknowledge. It could be interesting to expand the model in the future to include factors that affect photoreceptor output beyond the stage of the photocurrent.

(2). It will be interesting to eventually test the impact of this work for in vivo experiments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93795.3.sa3](https://doi.org/10.7554/eLife.93795.3.sa3)

Summary:

The authors propose to invert a mechanistic model of phototransduction in mouse and rod photoreceptors to derive stimuli that compensate for nonlinearities in these cells. They fit the model to a large set of photoreceptor recordings, and show in additional data that the compensation works. This can allow to exclude photoreceptors as a source of nonlinear computation in the retina, as desired to pinpoint nonlinearties in retinal computation. The recordings made by the authors are impressive and I appreciate the simplicity and elegance of the idea. The data support the authors conclusions.

Strengths:

- The authors collected an impressive set of recordings from mouse and primate photoreceptors, which is very challenging to obtain.

- The other proposes to exploit mechanistic mathematical models of a well understood phototransduction to design light stimuli which compensate for nonlinearities.

- The authors demonstrate through additional experiments that their proposed approach works and is useful for offering insights into retinal computation.

- The biophysical modeling approach is well described.
