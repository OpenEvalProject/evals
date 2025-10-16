# Peer review - Round 1

Editors:
- Birte Forstmann, University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49855.sa1](https://doi.org/10.7554/eLife.49855.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study focuses on a longstanding and important question in the field of diffusion MRI, namely the measurement of axon diameters. Importantly, until now, the accurate estimation of axon diameter mapping with non-invasive techniques such as diffusion MRI has been elusive due to a lack of sensitivity in the signal. The authors provide compelling evidence using sophisticated modeling that axon diameters can be estimated for largest axons when eliminating confounding factors such as extra-axonal water and axonal orientation dispersion. Data of fixed rat brains and optical microscopy of the same specimen are presented showing good quantitative agreement for MR-derived axon diameters. Finally, in vivo data from Connectom 3T scanning is presented which shows the feasibility of mapping axon diameters in healthy subjects. The work is therefore of interest to a broad scientific audience ranging from physicists to cognitive neuroscientists.

Decision letter after peer review:

Thank you for submitting your article "Noninvasive quantification of axon diameter using diffusion MRI' for consideration by eLife. Your article has been reviewed by three peer reviewers, including Birte Forstmann as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen Floris de Lange as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Overall, this manuscript is well written, interesting, timely and will help resolve the debate in the field. We therefore suggest revising the manuscript to address the points raised by the reviewers which are outline below.

Reviewer 1:

This paper introduces an interesting and surprisingly simple method for estimating axon diameter (potentially in vivo). Their approach relies on three key ingredients:

– ensure that the diffusion sensitisation (b value) is high enough to eliminate extra-axonal water

– use powder averaging across diffusion gradient orientations to eliminate confounds due to orientation of axons

– estimate intra-axonal perpendicular diffusivity from a simple power-law formula predicted by the theory

The intra-axonal perpendicular diffusivity is then used to estimate an "effective axonal radius" which describes the tail of the axon radius distribution under certain assumptions.

In general, this is a potentially important contribution. I have the following comments which I am sure the authors will be able to address:

1) Presentation

I found the presentation of the theory unnecessarily dense and difficult to follow. A simple diagram might help. Something like Figure 1 but with a single line showing the prediction from a model with fim as well as Dperp>0 (so with non-zero intercept of the nonlinear part and a negative intercept of the linear part). It would also be helpful to indicate on the same diagram that the slope on the right-hand side depends on Dpara, and that the intercept is fim, but the 'dashed line' intercept is a function of fim and Dperp (and Dpara?). The x-axis could be double-labelled with both 1/b and b. And also it would help to have vertical sections in the graph indicating the b value regimes (e.g. clinically-feasible, vs. Connectom vs. small-bore scanners, vs. low-b regime).

2) Modelling

Having played with the models (i)-(viii) an little, I see lots of degeneracy between fim and Dperp over a wide range of parameter values which is not surprising: unless some curvature is visible in the data (above the noise level), it is difficult to disentangle the contributions of fim and Dperp to the negative intercept. In the data that is shown (e.g. Figure 5), the points fall in a straight line and so there is no curvature to help disentangle fim and Dperp. The authors assumed that fim=0 for the in vivo data, but is this really justified (could there not still be very slow diffusing water that is unmodelled) and what about ex vivo?

In general, some sort of analysis of when the degeneracy breaks down (as a function of the max b value attainable and the other params like Dpara) would be helpful here. For example looking at the full posterior distribution and not just point estimates of the parameters (I don't find AIC values very helpful compared to looking at the full posterior distribution).

3) Axon diameter estimation

It would be helpful if the authors could unpack how they get to reff as a function of Dperp. I can see that the diffusion in a cylinder formula gives rise to a r4 dependence of the log(S) in the regime that the acquisition are made in. But then to go from there to reff (which is the ratio of 6th to 2nd moment) is a stretch for me. Is it simply by doing a Taylor expansion of S=exp(-a*r4) around zero inside the integral in Equation 7? If that is the case then perhaps an appendix would not hurt. Also, it is not clear how accurate it is to use the Taylor expansion.

Also on axon diameters, the authors make it quite clear that they don't like methods that make explicit distributional assumptions on the axon diameter (e.g. AxCaliber) – but I think it would be interesting to compare them with the author's approach. Looking at the histology data that is presented, one wonders how accurate a gamma distribution would be. With a distributional assumption there would be no need for the Taylor expansion above, and everything can be done keeping the exponentials and directly inverting the equations to get the parameters of the gamma distribution. How does this compare to the reff proposed by the authors?

4) Are the results biologically sound?

Generally, I found that there was not enough in terms of showing results that indicate the technique actually works well, e.g. in Figure 8: is there a way to show a similar map from histology?. Or in general show that inter-areas variation in radius from histo correlate with inter-area variation from MR in the ex vivo data. The only comparison between the two modalities is done in Figure 7 in a single region.

Similarly for the in vivo data: Figure 10: is there any evidence that the intervoxel variation is meaningful? There are zones of reduced radius in the lateral frontal lobes near the cortex – are those meaningful?

5) Exchange

The authors present an interesting extra source of information, in that an exchange model makes a different prediction at high b values and they found evidence for exchange in GM. Can you convince the reader that this is not just partial volume effects (e.g. multiple pools of water with different diffusion coefficients and no exchange?) would that for example induce a curve with the opposite convexity? As GM is likely to have more partial volume issues I think this is a valid question that needs addressing.

Also on exchange: My understanding of the Karger model is that it assumes that exchange happens in situ (a molecule would change its behaviour from e.g. slow to fast diffusion with some probability instantaneously). But in reality exchange happens at the membrane. Does that invalidate the equations? Can the equations be derived here in an appendix?

6) Presentation of the data

Single voxel data is never shown and so it is difficult to tell how noisy the signal vs. 1/sqrt(b) curves actually are.

7) Data sharing

The authors are to be commended on sharing their data. However the way they have done it is not optimal in that they only provide raw data with no particular documentation or curation. The shared data set would strongly benefit if you would add the following:

– include preprocessed data not just raw data (including the Dperp and reff maps) – or at least provide code to generate the maps and do the preprocessing

– match data format between human and rodent

– include documentation

– avoid lsm format as it is proprietary – maybe use tiff instead?

– include processed histo data?

Reviewer 2:

This study focuses on a longstanding and important question in the field of diffusion MRI, namely the measurement of axon diameters. Importantly, until now, the accurate estimation of axon diameter mapping with non-invasive techniques such as diffusion MRI has been elusive due to a lack of sensitivity in the signal. The authors provide compelling evidence using sophisticated modeling that axon diameters can be estimated for largest axons when eliminating confounding factors such as extra-axonal water and axonal orientation dispersion. Data of fixed rat brains and optical microscopy of the same specimen are presented showing good quantitative agreement for MR-derived axon diameters. Finally, in vivo data from Connectom 3T scanning is presented which shows the feasibility of mapping axon diameters in healthy subjects.

Major comments:

Generalizability of the data:

My main concern is that the MRI-based axon diameter modeling was only evaluated in the corpus callosum. It would be important to see whether the modeling also holds in other fiber tracts, e.g., fronto-occipital fasciculus.

This is something that the authors should ideally address, but in case this is not feasible, at least comment on.

Reviewer 3:

This is an impressive work combining well-thought out theory with experimental data only recently available, particularly for the human studies, using the Connectom system to provide gradient strengths some 4 times larger than available on commercial scanners. The mix of pre-clinical data with rat CC for which histological distributions of axon diameters was measured, with human data (using somewhat less gradient strength than available on the animal system) and only literature histology is justified and actually adds strength to the comparison of experimental with theoretical considerations. The lack of any attempt to measure the "dot" component in humans is less justifiable in my view though that might have significantly added to the scan time and further comments on this might be appreciated. The authors recognize the limitations of their assessment in having to rely upon a rather "weighted" version of the distribution which gives an output index well into the tail of the distribution, the larger axons, but at least the measures are getting closer to the actual size of the median axon values than those reported in the past with more standard gradient strengths and perhaps dubious modeling. It also would be helpful to perhaps add to Figure 1 or another figure the curves that would be anticipated theoretically from the exchange model of Equation 4 at such high b values, emphasizing the difference between concave and convex theoretical curves that the authors, I assume, deem to eliminate the latter model given the experimental data. Finally as a major point, in the Data Analysis section the authors explain reff or rMR from the data but this description is difficult to follow. For example, in Equation 2, how are the O(b2) taken into account if they are. Then, assume we now have Da(perpendicular) how does one use that with Equations 5 and 9 to get reff. This must be clarified. People should be able to replicate this calculation from what is in this text.
