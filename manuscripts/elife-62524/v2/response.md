# Author response - Round 1

Authors:
- Ashwin Nandagiri ([ORCID: 0000-0001-7328-9288](https://orcid.org/0000-0001-7328-9288))
- Avinash Satish Gaikwad ([ORCID: 0000-0002-7379-6383](https://orcid.org/0000-0002-7379-6383))
- David L Potter
- Reza Nosrati ([ORCID: 0000-0002-1461-229X](https://orcid.org/0000-0002-1461-229X))
- Julio Soria ([ORCID: 0000-0002-7089-9686](https://orcid.org/0000-0002-7089-9686))
- Moira K O'Bryan ([ORCID: 0000-0001-7298-4940](https://orcid.org/0000-0001-7298-4940))
- Sameer Jadhav ([ORCID: 0000-0002-4207-3393](https://orcid.org/0000-0002-4207-3393))
- Ranganathan Prabhakar ([ORCID: 0000-0001-7357-4222](https://orcid.org/0000-0001-7357-4222))

## Response text

DOI: [10.7554/eLife.62524.sa2](https://doi.org/10.7554/eLife.62524.sa2)

Essential revisions:

1. It is not completely clear from the manuscript what the configuration of the sperm is with respect to the glass slide where the head is tethered. What is the orientation of the cells with respect to the slide, and in which plane are the deformations measured? (from above or from the side?) We would expect that different configurations may lead to slightly different waveforms. In particular, we are surprised that the mean shapes shown in figure 2(a) have a net asymmetry which is observed in nearly all the cells: could this have to do with the relative configuration of the flagellum with respect to the surface?

Rodent sperm heads are flat and have falciform (hook-like) shapes. In our experiments with mouse sperm, the heads are tethered on one of their flat sides to the glass slide at the bottom of the imaging chamber. Imaging is done from above the sperm cell. The tethering renders the sperm head nearly immobile. As explained further below, the plane of the flagellar beat is approximately planar and parallel to the glass slide surface. Our calculations are restricted to the head, mid-piece and principal piece as these can be clearly resolved in the images. The end-piece (the distal 15% of the cell body) is neglected.

Intrinsic net asymmetry in flagellar beating is well known in sperm in many mammalian species, even when uncapacitated. Our observation that the mean shape is curved with a anti-hook (ventral) concave shape is consistent with the observations of Woolley (2003) that, in mouse sperm, the flagellum bends at the neck more on the ventral side than on the other.

Revisions

a. A new paragraph has been inserted in the “Tethering and imaging” subsection in the Materials and methods that summarizes the comments above on how the orientation of the cell relative to the microscope.

b. A figure is also included in a supplementary Appendix that shows a schematic of the side-view of the sperm beating plane parallel to the glass slide.

c. The comments above on the asymmetry of the mean shape have been inserted at the end of the second paragraph in the subsection, “POD enables identification of beat cycles”, in Results.

2. The experiments are done with flagella very near a no-slip surface, since the cells are chemically adhered to the chamber boundary. Yet, the authors use resistive force theory for filaments in free space, without any reference to the nearby no-slip surface. As the rate of energy dissipation near the surface will be considerably larger than estimated by RFT, it is possible that some (or much, or perhaps all) of the additional dissipation found by the authors is actually within the fluid and simply not accounted for by RFT. Thus, all of the calculations must be redone with the appropriate Blake tensor for stokeslets near a no-slip wall before the results can be considered definitive. The paper must also more carefully illustrate and quantify the proximity of the flagella to the surface in order to make these calculations precise. Absent this analysis, the claims of the paper do not stand up to scrutiny.

We acknowledge that the proximity to the wall is an important issue and address this comment in detail below. All the results presented in the revised manuscript are now with the distance from the wall taken into account. We find that this revised calculation does not alter the primary conclusions in our paper that internal dissipation – either due to passive internal friction or due to a mechanism associated with the motors – could be significant in sperm.

In our detailed response below, we discuss (a) the evidence from literature on which our estimate of the distance from the wall is based, (b) the RFT calculation with the wall distance taken into account and the resulting changes in the friction coefficients, and (c) how these changes leave our primary conclusions unaffected.

a. Wall distance. If the bottom of the sperm body were to be in direct contact with the wall everywhere, hydrodynamic frictional resistance will be very large. In that extreme case, flagellar beating would be expected to be significantly attenuated compared to the beating of freely swimming observed away from the wall. However, in all our samples where cells are tethered at their heads, the sperm continue to

beat their flagella freely.

A detailed study by Woolley (2003) showed that freely swimming mouse sperm exhibit “preferential capture” by walls. They are hydrodynamically drawn to walls and then stabilize with the left sides of their flat heads held against the surface. If a sperm arrives at a wall with its right-side next to the surface, it quickly moves away from the wall after a few flagellar beats and will be eventually captured in its stable orientation. Sperm following this “left-side rule” exhibit planar beating in a plane that is parallel to the wall. This beating is clearly resolvable within the focal width of the microscope. On the other hand, those that approach the wall with the right sides of their heads parallel to the wall exhibit considerable motion out of the focal plane. Scanning electron microscopy further revealed that the plane of the left-side of the flat head makes an angle less than 180°◦ with the flagellum at the neck. This appears to enable sperm following the left-side rule to stabilize planar beating parallel to the wall.

In our samples, the heads are chemically tethered to the wall. While we did observe a few cells adhere on their right sides, these cells exhibited non-planar beating out of the focal plane. Author response image 1 (a) and (b) sketch the expected geometry of the mouse sperm cell with its intrinsic head-tail angle at the neck, when the left side of its head is tethered to the wall. In this orientation, the flagellum beats in a plane parallel to the wall and its centreline is at a distance equal to the neck radius, h = an, from the wall, where an is the radius of the neck. The head-neck angle is the same as the angle made by the head axis with the wall, θ ≈ aN/ℓH, where ℓH is the length of the head. From literature measurements of mouse sperm dimensions, aN ≈ 0.6 µm and ℓH≈ 5 μm, which gives θ ≈ 0.1 rad or 6°.

We note here that, in the process of recalculating the wall effect, we discovered that we had previously mistakenly used the width of 2.7 µm of the basal region of the head as the neck radius and a radius at the tail end of 0.65 µm. The correct value of the neck radius, an, is 0.57 µm, and the radius of the filament at the tail end, at, is the axonemal radius, 0.18 µm.

b. Resistive Force Theory with wall distance Katz et al. (1975) obtained the following Resistive Force Theory (RFT) approximations for the tangential and normal friction coefficients for planar motion of a slender body parallel to a wall, at a distance of h from the wall are(1)ζtwall=2πμln2h/a;ζnwall=4πμln2h/a

These coefficients have previously been used in a number of studies, notably by J´’ulicher and co-workers (Riedel-Kruse et al., 2007a) for analyzing experimental data on wall-tethered sperm and, more recently, by Mondal et al. (2020), for tethered axonemes isolated from cilia. We have now used these coefficients in all calculations along with h = an = 0.6 µm, and the linear radial taper,(2)a(s)=(aN−aT)L−sl−sN+aTwhere an is the radius at s = sn at the neck and at = 0.65 µm is the radius of the axoneme at s = L at the tip of the tail.

In the original manuscript, we had used the following RFT coefficients for motion in bulk fluid well away from a wall (Lighthill, 1976):(3)ζtbulk=2πμln2q/a;ζnbulk=4πμln2q/a+1/2 where q = 0.09λ, λ is the wavelength which can be approximated the flagellar length, L = 120 µm. As noted above, we had also calculated the friction coefficients with an = 2.7 µm. Author response image 2 compares the ratios of the friction coefficients near the wall and in the bulk(4)Wt=ζtwallζtbulk=ln(0.18L/a′)ln(2H/a);Wt=ζnwallζnbulk=ln (0.18L/a′)=1/2ln(2H/a) where a0 is the radius profile used in the original submission. Further, the ratio of the normal coefficient to the tangential coefficient, γ = ζn/ζt is 2 for all s in the case of the Wall-RFT coefficients. With the bulk RFT coefficients in the original manuscript, this ratio is close to 1.8 and only varies weakly with s. Hence, the change in γ with the Wall-RFT coefficients is relatively smaller than the change in ζt.

c. Changes to results The changes in the RFT coefficients directly impact the calculation of the hydrodynamic dissipation density,

phd=ζt(vt2+ζvn2), (5)

from the experimentally measured velocity components, vt and vn. The change in ph is mostly due to the change in ζt, since the change in γ is relatively small. In the calculation of the total instantaneous hydrodynamic power dissipation, phd=∫ststphdds,and its cycle-average, the changes in ζt are weighted more strongly by the squares of the larger velocities towards the tail end. The revised values for the total hydrodynamic dissipation are about 2.5 times as large as before for all the samples (Author response image 3).

The change in phd affects the calculation of the active power density, pa, directly:(6)pa=∈̇−ps−phd−pid

Here, the densities of elastic storage rate, ˙, and the internal dissipation rate, pid, are unaffected by the changes in the RFT coefficients. The rate of mechanical work done by the passive material stress across the cross section,

ps=∂(v•F)∂s+∂(w•M)∂a. (7)

In this equation, only F depends on the RFT coefficients, since(8)F(s,t)=∫sLfh(s,t)ds′=∫SLζt(vt+γvn)ds′

A scaling analysis can be used to understand the relative contributions of the different terms in the energy balance that we use to determine pa. The elastic terms scale as κn ℓ2w k4, where κn is the elastic stiffness at the neck, ℓ is the beat amplitude and w and k are, respectively, the angular frequency and wavenumber corresponding to the travelling bending wave in the flagellum. If internal dissipation due to bending friction is included, those terms scale as ηn ℓ2w2k4, where ηn is the internal friction coefficient at the neck. The hydrodynamic contribution scales as ζt,n ℓ2w2. The relative magnitudes of the elastic and internal frictional contributions over the hydrodynamic contributions in the energy balance thus scale as κnk4/(ζt,nw) and ηnk4/ζt,n, respectively.

With ζt,n = 4π µ/ln(4hn/an) when Wall-RFT is used, and with κn = 7 × 104 Pa µm4, , ηn = 103 Pa s µm4, µ = 10−3 Pa s, a beat frequency of f = 7 Hz, and a wavelength of about L = 100 µm, the elastic and internal friction contributions in the energy balance are, respectively, 2.7 and 1.7 times larger than the contribution from hydrodynamic power. Since these terms dominating the energy balance remain unaffected by any changes in the RFT coefficients, pa is less sensitive to changes in the RFT coefficients than the hydrodynamic dissipation itself. The motor dissipation and motor power input are determined from pa, and these are also not strongly influenced by the changes (Author response image 3).

As a result, while the numerical values of our results in Figures 3, 4–B and C, and 5 of the manuscript have changed, the key original conclusions still stand: that, in either the WT or Crisp2 KO mouse lines we have studied, (i) there is significant motor dissipation within the axoneme, and (ii) the total internal dissipation within the flagellum is significantly larger than the external hydrodynamic dissipation.

Revisions

a. The Wall-RFT coefficients have been included in the Theoretical Modeling section in the paper, along with literature references.

b. The correct values of the neck radius, an, is 0.57 µm , and the radius of the filament at the tail end, at, is the axonemal radius, 0.18 µmhave been specified in the paragraph before the Results section.

c. All data in Figures3, 4 and 5 in the revised manuscript are with Wall RFT. The discussion on lines 359–382 associated with Figure 5 (C) of the relative magnitudes of the different dissipations has taken into account the increased hydrodynamic dissipation.

d. The second paragraph in the “Tethering and imaging” subsection in the Materials and methods section summarizes the discussion of tethering of the left-side of the heads in (a) in the response above.

e. A supplementary Appendix now includes the discussion in (a) in the response above as a separate section titled “Planar beating of tethered moue sperm”. A figure similar to Author response image 1 is also included. This figure shows the head shape when viewed with the left-side attached to the wall, the neck diameter, the schematic of the cell viewed side-on, showing the distance of the beating plane from the wall and the angle at the neck that enables beating parallel to the wall when the left-side of the head is tethered to the wall.

A related point is the need to understand the effect of tethering the cell on its kinematics and energetics? In other words, do the conclusions still hold for freely swimming cells?

We firstly note that our observations with tethered sperm are relevant for in their own right. Mammalian sperm, in vivo, are known to swim close to the oviductal wall. Uncapacitated sperm (such as the samples in our work) are known to also bind tightly at their heads to the oviductal epithelia while continuing to beat with their flagella oriented away from the wall (Ardon et al., 2016). While freely swimming in bulk fluids is more common in aquatic species that fertilize by broadcast spawning, in mammalian species, sperm localized near a wall is closer to physiological conditions. From the applied perspective understanding the behaviour of sperm near walls is also of considerable interest for developing artificial reproduction technologies that use microfluidic devices for sorting and separating sperm.

The reviewers have already pointed out the increased strength and anisotropy of the hydrodynamic resistance near a wall. The tethering constraint results in an additional force and torque being imposed at the head. We can certainly expect that these different external loading conditions will cause the kinematics of tethered sperm to be different from those of free swimmers , either at a wall or in bulk fluid. Nevertheless, we expect that our conclusions that most of the dynein power input is actually spent to overcome internal dissipation within the motors and the rest of the passive material will still be valid for free swimmers. We discuss the reasons for this in detail below in our responses to the reviewers’ queries (in Comments 7 and 8) on how our work relates to current theoretical understanding of sperm waveforms and the effect of increasing medium viscosity on the waveforms.

Revisions

The effect of tethering is discussed in the Discussion section in the revised manuscript along with the effects of fluid viscosity and wall proximity.

3. Is there any evidence of 3D dynamics? Some recent experiments with human sperm have suggested that sperm beats can take place in 3D (Gadelha et al., Science Advances 2020). As the model in the paper is 2D, this could also affect the energy balance.

We firstly note that there have been other studies that have used imaging of tethered sperm and cilia to understand axonemal dynamics (Mondal et al., 2020; RiedelKruse et al., 2007b). We have also taken advantage of the nearly planar beating that many mammalian sperm exhibit near walls. In our experiments, out-of-plane excursions in the resolved portion of the tail appear limited to less that 2 µm. Nearly planar beating of the mid-piece and principal piece is evidenced by the fact that these portions of the flagellum remained in focus at all times in our samples. The

total depth of field(9)dtot=λnNA2+neMNAis 1.2 µm in our microscope, where λ = 0.7 µm is the mean wavelength of the incident light, n = 1 is the refractive index of the air medium between the coverslip and the objective lens, M = 20 is the lateral magnification, NA = 0.7 is the numerical aperture of the objective, and e = 0.65 µm is the resolution of the detector in the image plane. After taking into account uncertainties due to the spread in incident wavelengths and other factors, we estimate that the depth of field cannot be larger than 2 µm. We have verified this independently in calibration experiments using 5 µm diameter spherical particles adhered to the bottom surface.

A maximum vertical deviation of around 2 µm is about 10% of the mean amplitude of the in-plane beating of around 20 µm. Therefore, neglecting such deviations can be expected to contribute errors of around 10% in the velocity components, curvature and rate of curvature. These errors propagate quadratically when calculating energetic quantities. The resulting error due to non-planarity in beating cannot therefore be larger than 1%, which is considerably smaller than the natural fluctuations in the beating patterns within a single sample and the sample-to-sample variations.

Revisions

a. The subsection on Tethering and Imaging in Materials and methods now includes as statement that out of plane deviations are less than 2 µm.

b. The discussion above of the near planarity of the beating is now included in a

supplementary Appendix.

4. The authors should examine the work of K.E. Machin ["The control and synchronization of flagellar movement"], Proc. Roy. Soc. B 158, 88 (1963), which provided the first theoretical formalism to study active moment generation within beating flagella based on examining the difference between known force contributions from viscous dissipation and elastic bending. It seems that this same kind of analysis could be done here to identify directly the non-viscous contribution, rather than having to postulate a particular form.

Stated another way: Why not try to estimate the active power density directly from the active moment density, which could be calculated from the moment balance of equation (4) where all the other terms are known? This would provide a direct estimate of the active power. The force balance could then be used to estimate the internal friction, which would then no longer rely on an assumed value for the internal friction coefficient. In fact, this could be used to obtain an estimate for that coefficient.

We missed citing Machin’s seminal work on flagellar waveforms and have corrected this oversight in the revised manuscript. However, estimating both the unknown internal friction coefficient and the unknown active power distribution (or the active moment density, ma) from the same set of data is problematic.

In the Kirchhoff model, the force F in the linear momentum equation (i.e the force balance) is the Lagrangian multiplier enforcing the inextensibility and nonshearability constraints. Since the net active force at any cross section is zero and there are no non-hydrodynamic external forces acting on the flagellum, the force balance for the tail region is:(10)fh+∂F∂s=0

The hydrodynamic force density , fh, is calculated from the observed kinematics using RFT. We therefore integrate this equation to calculate F at any cross section

in the filament as:(11)F (s,t)=∫slfh(s,,t)ds′

In other words, F is completely known from fh, and it cannot provide any further information on internal friction.

It is, in principle, possible to use Eqn. 4 for the conservation of angular momentum to calculate the active moment density, ma. The hydrodynamic moment, mh, is negligible relative to other terms and there are no non-hydrodynamic external moments, me, that act on the tail. Splitting the passive internal moment M into elastic and dissipative contributions, the angular momentum equation for the flagellum reduces

to:(12)ma+t × F+ ∂Mel∂s+ ∂Mid∂s=0

In this equation, the tangent vector t is known from experiments. We also have the curvature and curvature rates to be used in the constitutive equations for Mel and Mid, and as well as an estimate for the elastic stiffness, κn, for mouse sperm from literature. We can use F determined from the previous equation.

However, both the active moment, ma, as well as the internal friction coefficient, ηn, are unknown. It is not possible to use the same equation to determine these independently of each other. We have the same situation even while using the energy balance. We have, therefore, performed a parameter-sweep in ηn, with values ranging from 0 to well above the scaling estimate of 103. In the Discussion, we have pointed out the need for performing independent experiments for microrheological characterization of the flagellar material.

Revisions

In the Introduction, the start of the fourth paragraph discussing extracting forces and energetics from the measured beat patterns explicitly states: “Our approach for calculating forces and energetics from the measured beating patterns stems from ideas discussed originally by Machin….”

5. The paper addresses in detail the use of Chebyshev fitting methods for the filaments, but does not appear to address the physical boundary conditions one would expect on elastic objects (particularly at the free end), involving the vanishing of moments and forces. Unlike, for example, the biharmonic eigenfunctions of simple elastic filament dynamics which are tailored to those boundary conditions [see, e.g. Goldstein, Powers, Wiggins, PRL 80, 5232 (1998)], it is not clear how the Chebyshev functions satisfy those conditions. Some explanation is needed.

We thank the reviewers for bringing these interesting eigenfunctions of the hyperdiffusive operator for elastica to our attention and will explore using them in future.

Here, however, we have a composite body with free ends. The head region is treated as a rigid body, rotating about the tether point. The tail region is flexible and viscoelastic. Chebyshev polynomials are fitted only to through the tail region. Internal stresses are expected to be non-zero and continuous across the neck junction.

We do not apply the dynamical force- and torque-free conditions at the head and tail ends when fitting a smooth curve through the raw pixel data for the centerlines. Instead, we only place geometric and kinematic constraints. We ensure that, in the head region, the fitted tangent angle function satisfies rigid-body rotational kinematics. For the Chebyshev fits through the tail at any time instant, we ensure C2-continuity of the tangent angle profile across the neck. We have used the method of undetermined coefficients to impose these continuity constraints on the Chebyshev polynomial coefficients. The procedure is described in the subsection on Data Processing in Materials and methods.

The tail region is further complicated by the fact that the distal end of the tail often fades in and out of optical resolution because it is moving fast and is also very thin. We only have reliable data for what we refer to as the imaged-tail region, s ∈ [sn,st], where st ≈ 0.85L. We therefore do not enforce any boundary conditions at the imaged-tail end (st = 0.85L). We find that enforcing a zero elastic moment (i.e. zero curvature) at st 6 = L produces unsatisfactory curve-fits to the experimental centerlines. Such curves tend to be too flat at the tail end.

We do, however, account for the force- and torque-free conditions at the free head and tail ends when developing the equations for extracting the internal dynamics and energetics from the measured kinematics. Firstly, the passive internal force in the tail is formally calculated from the hydrodynamic force distribution as(13)f (s,t)=∫sLfh(s′,t)ds′

This satisfies the condition that F(L,t) = 0. However, since we do not have motion data for s > st, we neglect the contribution to the hydrodynamic forces from s > st. This effectively amounts to applying the force-free condition at s = st.

Secondly, the force- and torque-free conditions at the head end are applied when calculating the instantaneous power dissipated against the hydrodynamic and tethering forces on the head. The point-wise energy balance for the rigid head region (which cannot elastically deform to store energy) is:(14)0=phd+pe+pswhere phd and pe are the hydrodynamic dissipation and tethering power densities and ps = ∂/∂s(v · F + ω M). Integrating this over the head-region at any time, and applying the boundary conditions at the free end, gives:(15)pHhd= pHe=(vo ∙ F0+ ω0M0)− (vN ∙ Fn+ ωNMN)= −(vN ∙ FN+ ωNMN)

Since stresses are continuous across the neck junction, we equate FN and MN in the equation above to those calculated with Eqn. (13) for F earlier and with the viscoelastic constitutive equation for M in the tail region. The C2-continuity of the fitted tangent angle profile at the neck ensures that the velocities, vN and ωN, are uniquely defined at sn.

Thirdly, the force- and torque-free conditions at the tail end are applied to calculate the instantaneous power balance across the entire tail region. For the (untethered and viscoelastic) tail, the point-wise energy balance is:

∈̇=pa+phd+pid+ps. (16)

Integrating over the tail region, we obtain,(17)Ė=pa+phd+pid+(vL•FL+ωLML)−(vN•FN+ωNMN)

The free-end boundary condition is used to set FL = 0 and ML = 0. Using Eqn. (15) earlier, the neck contribution can be replaced in terms of the total power dissipation by the head, Phd = Phhd + Phe. Further, we split the integral of pa into contributions from its negative and positive parts by defining the motor dissipation and motor input as follows:(18)pmd(t)=∫sNLmin(pa,0)ds;pmi(t)=∫sNLmax(pa,0)ds.

Substituting these in Eqn. (17) and rearranging, we obtain (noting that dissipations are negative in our sign convention)(19)pmi=Ė−phd−pid−pmd−pHd

In other words, the motor input provided is either used for elastic storage or to overcome all the contributions to dissipation.

This shows that the energy balance equations we have used in our calculations are formally consistent with the free-end conditions. It also shows that we have effectively neglected contributions from the non-imaged tail end. We do not, however, expect significant qualitative changes due to this approximation.

Revisions

a. Key details of our approach to determining the energetics from the measured kinematics have been brought forward from the Materials and methods section into the Theoretical Modeling section and described more clearly. The description also discusses how the boundary conditions are incorporated into the equations for the energetics.

b. The section on conservation equations in a supplementary Appendix has been augmented with the equations for the head and tail region.

6. If indeed internal dissipation dominates, that would suggest that essentially all prior theoretical approaches to calculating sperm waveforms must be quantitatively in error by very large factors. It would be very appropriate for the authors to examine some of those theoretical works to determine if this is the case.

We have now considerably revised the Discussion section to consider observations in the light of the current theoretical understanding of axonemal dynamics and sperm waveforms.

Several ideas have been presented in the past for the generation of the beating patterns by the axoneme. In a landmark study, Riedel-Kruse et al. (2007b) compared the predictions of many of these with experimental observations of planar beating in bull sperm that were either head-tethered or swimming freely in circles for long adjacent to a glass-slide wall. It was shown that the best agreement with experiments is obtained with the sliding-control model of Ju¨licher and co-workers (Camalet et al., 1999; Camalet and Ju¨licher, 2000). In this model (in the notation of the current paper), the active moment is related to the local internal shear and shear rate through an equation of the form ma = K γ + λ∂γ/∂t where γ is the local shear strain. In the parlance of control theory, this model proposes that motors are regulated by the location deformation through a mechanism that follows a proportionalderivative control logic. More recently, Mondal et al. (2020) suggested a variant with proportional-integral control logic instead i.e where ma + β ∂ma/∂t = K γ.

In either case, when the equation for regulation of the active moment is coupled with the equations for the rest of the passive material of the flagellum, an oscillatory instability emerges in certain ranges of the controller constants. This triggers a travelling wave that propagates down the filament and beating patterns similar to experimental data are obtained. It is further found with these models that the controller constants to achieve oscillations are negative, indicating that the active moment exerted by the dynein motors is down-regulated by the load exerted back on the motors due to the local shear deformation in the filament and its time rate of change. This also appears to be consistent with the recent experimental finding that dynein motors are always primed to deliver forces on microtubules but are inhibited when a curvature wave passes through their location (Lin and Nicastro, 2018).

It is possible that regulation of ma could more generally described by an equation of the form, ma + β ∂ma/∂t = K γ + λ∂γ/∂t, which corresponds to proportional-integral-derivative (PID) control. Such regulation of ma immediately means that, when stable travelling waves are generated, the local rotation rate, ω (which is proportional to ∂γ/∂t) will be systematically out of phase with ma, as is indeed observed in Figure 6. There will necessarily, therefore, be phases in each cycle when the two variables will be of opposite sign and pa = maω will always be negative in those phases.

The mechanical work done back on the motors during such phases by the passive elements of the filament must be quickly dissipated in some form, since the motors cannot store the energy that is received nor reconvert it back to ATP. What, then, is the internal mechanism behind this additional dissipation? Riedel-Kruse et al. pointed out that the sliding-control model had to allow for relative sliding between microtubules at the basal end to obtain experimental agreement and that frictional resistance to basal shearing is important for the model to predict stable oscillations. Mondal et al. analyzed axonemes isolated by demembranating Chlamydomonas cilia and found that external hydrodynamic friction is too small to explain the stable beating pattern observed. They then showed that their sliding-control model predicts stable oscillations when coupled with equations that include passive filament elasticity and internal frictional resistance to the shear deformation rate. These sources of internal friction are not modeled in the present study, where we have treated the flagellum as an unshearable Kirchhoff rod. As Figure 5 (A) in the manuscript shows, we find that, if internal friction is absent or insufficient, then the observed motion would mean that, for a significant duration of the mean cycle, the filament may as a whole be driving the motors backward. While this unphysical picture is eliminated when a sufficiently high internal friction coefficient is used, we still observe motor dissipation due to ma and ω being out of phase with one another.

The key point is that, while some or all of these different frictional contributions may be necessary for an internally-driven filament to oscillate stably, if the local regulation of the active moment in general follows PID logic, then the out-of-phase moment and local deformation rate will lead to phases of negative active power, irrespective of the nature of internal or external friction. This points to the existence of a separate dissipative mechanism associated with the dynein motors themselves.

There is already evidence that dyneins can dissipate energy locally. It is known that dynein motors can cycle through conformational changes driven by ATP binding and hydrolysis even when not driving microtubule sliding (Kon et al., 2005). Opticaltweezer experiments on dyneins bound to static microtubules have further shown that dyneins can steadily be driven in the reverse along the microtubule by an external load by forces larger than the stall force for these motors (Gennerich et al., 2007). The force required is more than that required to move unbound motors at the same velocity. This work done to drive the motors backward must be dissipated locally by a mechanism other than just the hydrodynamic frictional resistance of the motors to motion. Our results show that such motor dissipation can be a large part of the energy budget within the flagellum.

Revisions

The revised Discussion includes the response above, along with Figure 6.

7. The authors note in the Discussion that the beating waveform changes dramatically in fluid with higher viscosity. Yet, if external dissipation plays such a small role how can this be rationalized?

As noted in our response to the previous comment, even close to a wall, viscous dissipation appears to play a minor role in our experiments as well as those conducted with demembranated cilia (Mondal et al., 2020), in aqueous media. As pointed out in the original manuscript, if the kinematics remain unchanged, an increase in viscosity increases in a proportional increase in the hydrodynamic dissipation. However, as discussed above, the flagellar waveform emerges from the tight coupling of the active-viscoelastic axonemal dynamics to the passive viscoelasticity of the rest filament. Therefore, any change to the external mechanical environment – whether it be due to viscosity, or the presence of bounding surfaces, or the exertion of nonhydrodynamic tethering forces or moments – can lead to non-trivial changes in the emergent waveform.

For instance, Mondal et al. have shown that, when external hydrodynamic friction is negligible and internal resistance to shear deformation is taken into account, the governing equations for the passive material are diffusive in nature. When the external viscosity is large enough that hydrodynamic effects are not negligible, the equations governing the dynamics have a hyperdiffusive character. Therefore, one can expect that, the system may transition from one kind of qualitative behaviour to another with an increase in viscosity.

Revisions

The revised Discussion includes most of the comments above. We have not included the last paragraph above on the change in the nature of equations in the model of Mondal et al.
