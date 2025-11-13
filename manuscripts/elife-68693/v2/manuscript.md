# Rolling controls sperm navigation in response to the dynamic rheological properties of the environment

## Authors

- Meisam Zaferani<sup>1</sup>
- Farhad Javi<sup>1</sup>
- Amir Mokhtare<sup>1</sup>
- Peilong Li<sup>1</sup>
- Alireza Abbaspourrad<sup>1</sup> ([ORCID: 0000-0001-5617-9220](https://orcid.org/0000-0001-5617-9220)) †

### Affiliations

1. Department of Food Science, College of Agriculture and Life Sciences, Cornell University Ithaca United States

† Corresponding author

## Abstract

Mammalian sperm rolling around their longitudinal axes is a long-observed component of motility, but its function in the fertilization process, and more specifically in sperm migration within the female reproductive tract, remains elusive. While investigating bovine sperm motion under simple shear flow and in a quiescent microfluidic reservoir and developing theoretical and computational models, we found that rolling regulates sperm navigation in response to the rheological properties of the sperm environment. In other words, rolling enables a sperm to swim progressively even if the flagellum beats asymmetrically. Therefore, a rolling sperm swims stably along the nearby walls (wall-dependent navigation) and efficiently upstream under an external fluid flow (rheotaxis). By contrast, an increase in ambient viscosity and viscoelasticity suppresses rolling, consequently, non-rolling sperm are less susceptible to nearby walls and external fluid flow and swim in two-dimensional diffusive circular paths (surface exploration). This surface exploration mode of swimming is caused by the intrinsic asymmetry in flagellar beating such that the curvature of a sperm’s circular path is proportional to the level of asymmetry. We found that the suppression of rolling is reversible and occurs in sperm with lower asymmetry in their beating pattern at higher ambient viscosity and viscoelasticity. Consequently, the rolling component of motility may function as a regulatory tool allowing sperm to navigate according to the rheological properties of the functional region within the female reproductive tract.

## Introduction

In mammals, sperm must migrate through the female reproductive tract to fertilize an egg (Suarez and Pacey, 2006; Suarez, 2016). During this migration, sperm require navigational mechanisms to swim in the correct direction (Eisenbach and Giojalas, 2006; Kaupp et al., 2008). These navigational mechanisms rely on external and dynamic biochemical and biophysical cues that are present in the female reproductive tract (Kaupp et al., 2008; Bahat et al., 2003; Tung et al., 2015a). Although the role of biochemical cues in mammalian sperm navigation remains poorly understood (Kaupp et al., 2008; Suarez, 2008), in vitro and in vivo studies have provided evidence for two navigational mechanisms that rely on external biophysical cues, namely rheotaxis (Miki and Clapham, 2013; Kantsler et al., 2014; Bukatin et al., 2015; Tung et al., 2015b) and wall-dependent navigation (Guidobaldi et al., 2014; Nosrati et al., 2016; Denissenko et al., 2012; Zaferani et al., 2019; Wang and Larina, 2018). Rheotaxis, as an upstream swimming in response to an external fluid flow, has been observed and quantitatively studied for bovine, human, and mouse sperm (Miki and Clapham, 2013; Kantsler et al., 2014). Wall-dependent navigation, as sperm response to the nearby physical boundaries such as walls of the female reproductive tract, has also been observed and characterized for bovine and human sperm (Tung et al., 2015a; Denissenko et al., 2012).

Although wall-dependent navigation combined with rheotaxis may characterize regulatory mechanisms of sperm navigation within the complex geometry of the female reproductive tract and under dynamic fluid flow, it remains unclear how sperm rolling contributes to these navigational mechanisms (Gadadhar et al., 2021; Miller et al., 2018; Drake, 1974; Babcock et al., 2014; Schiffer et al., 2020). Furthermore, the dynamic biophysical factors of the female reproductive tract are not limited to its complex geometry and the varying flow of the mucus within it. The rheological properties of the mucus also change according to the functional region within the female reproductive tract (Suarez and Pacey, 2006; Carlstedt and Sheehan, 1984; Tung et al., 2017). It also remains poorly understood how the rheology of the environment influences sperm swimming behavior, and in particular, rheotaxis and wall-dependent navigation.

To address these questions, we investigated bovine sperm motion in a microfluidic device to identify how the rolling component of its motility contributes to navigation under simple shear flow and within a quiescent reservoir. To avoid errors arising from studying sperm motility under external fluid flow, such as experimental inaccuracies caused by decoupling the effect of flow on sperm motion from active swimming, we employed a multi-step approach. In this approach, we first isolated sperm within a quiescent reservoir using a rheotaxis-based method to ensure that sperm within the reservoir could swim upstream before entering the reservoir (Zaferani et al., 2018). We then characterized the components of sperm motility, including flagellar beating and rolling, in viscous and viscoelastic media, in the absence of external flow. Finally, we studied wall-dependent navigation within the reservoir and, by tracking the sperm prior to their entry into the reservoir, we evaluated rheotaxis to identify the function of rolling in sperm navigation under fluid flow.

We found that rolling enables sperm to swim progressively even when the sperm flagellar beating pattern is intrinsically asymmetric, which subsequently promotes rheotaxis and wall-dependent navigation. Sperm that lack rolling swim along two-dimensional (2D) diffusive circular paths and are less susceptible to being influenced by the nearby walls and external flow. We observed that the suppression of rolling occurs by increasing ambient viscosity or viscoelasticity, such that an increase in ambient rheological properties transitions progressive motion into 2D diffusive circular surface exploration. Such diffusive circular surface exploration is caused by the intrinsic asymmetry of flagellation and the curvature of the circular path is proportional to the level of asymmetry. We noticed that suppression of rolling was reversible, as a decrease in ambient viscosity or viscoelasticity resulted in reactivation of rolling. Furthermore, we found out that the level of flagellar asymmetry in a sperm population forms a continuum, and suppression of rolling in sperm with lower flagellar asymmetry occurs at higher viscosity or viscoelasticity.

Sperm swimming behavior transitions between progressive and diffusive circular motions after each incidence of suppression or reactivation of rolling. Since the suppression or reactivation of rolling relies on changes in the viscosity or viscoelasticity of the media, sperm swimming behavior manifests differently in response to the rheological properties of the environment. Because the characteristics of these swimming behaviors (circular versus progressive) are different and the viscosity and viscoelasticity of the mucus in the female reproductive tract varies according to functional regions (Suarez and Pacey, 2006; Tung et al., 2017; Ishimoto and Gaffney, 2018; Ishimoto and Gaffney, 2016; Gaffney et al., 2011), our results suggest that rolling potentially enables sperm to regulate its navigation in response to the dynamic rheological properties of the mucus in the tract.

## Results

To select sperm based on their rheotactic behavior and to isolate them inside the quiescent reservoir, we used a microfluidic corral system. Within the reservoir filled with standard Tyrode’s albumin lactate pyruvate medium (TALP), a sub-population of sperm (<5%) exhibited an in-plane 2D asymmetric flagellar beating pattern, where the midpiece of each flagellum was consistently bent more significantly to one side (Figure 1A and Video 1). This asymmetric beating pattern results in circular swimming at an angular velocity of $Ω$, whereas other sperm within the population swim progressively (Figure 1B). Unlike circular motion, progressive motion is not just produced by 2D in-plane symmetric flagellation, rather frequent but irregular rollings contribute to sperm motility (Figure 1C and Video 2). The rolling component was detected when a change in the light intensity of the sperm heads was visualized under a phase contrast microscope (Figure 1C). Rollings occur rapidly and discontinuously (Drake, 1974; Babcock et al., 2014), such that the elapsed time between two consecutive rolling events $T_{SR}$ is not constant. While tracking the sperm within the reservoir and under the flow prior to their entry into the reservoir, we found that progressive motility included the rolling component, both under the flow and within the quiescent reservoir, whereas sperm exhibiting a circular motion did not exhibit rolling under either condition (Figure 1D). Although rolling occurs independently of external fluid flow, it does depend on the rheological properties of the medium, as the percentage of rolling sperm decreases with an increase in the viscosity and viscoelasticity of the medium (Figure 1E, Video 3). Our results indicate that the suppression of rolling is more sensitive to viscoelasticity than to viscosity. We used varying concentrations of polyvinylpyrrolidone (PVP) and polyacrylamide (PAM) to prepare viscous and viscoelastic solutions (Tung et al., 2017), the rheological characteristics of which are presented in Section I of Appendix 1.

![Figure 1.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig1-v2.jpg)

**Figure 1.:** (A) Flagellar asymmetric beating. The midpiece of the flagellum consistently bends more prominently in one direction. (B) The circular motion caused by the asymmetric beating. A least-squares fitting algorithm was used to fit a circle into the sperm trajectory. (C) Rolling under a phase-contrast microscope. (D) All progressively motile sperm exhibit frequent rolling under flow and within the quiescent reservoir. (E) Increasing viscosity and viscoelasticity suppresses rolling and increases circular motion within the population (p>0.05). (F) An increase in viscosity results in a decrease in rolling frequency in rolling sperm while an increase in viscoelasticity does not change the frequency of rolling in rolling sperm. (G) Propulsive velocity of non-rolling sperm in 4% polyvinylpyrrolidone (PVP) is significantly lower than that of 1% polyacrylamide (PAM). (H) Suppression of rolling for sperm exhibiting less asymmetry in their flagellation occurs at higher viscoelasticity. (I) Infrequent rolling changes the direction of motion from CW to CCW or vice versa. (J) Sperm rotating around the tethering point upon adhesion to the glass surface. Progressive motion before tethering was generated by frequent rolling. (K) Reversible transition between progressive and circular motions through suppression and reactivation of rolling. Trajectories in Tyrode’s albumin lactate pyruvate medium (TALP) and 1% PAM were obtained with 0.08 s intervals. Intervals in 4% PVP were 0.16 s. (L) Distribution of sperm angular velocity $Ω$ for both tethered and untethered sperm. **p>0.05, **p<0.01. The p-values were obtained from two-tailed t-tests, with adjustments for multiple comparisons (Bonferroni correction). The concentrations are reported in weight percent.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig1-figsupp1-v2.jpg)

![Video 1.](https://cdn.elifesciences.org/articles/68693/elife-68693-video1.mp4.jpg)

![Video 2.](https://cdn.elifesciences.org/articles/68693/elife-68693-video2.mp4.jpg)

![Video 3.](https://cdn.elifesciences.org/articles/68693/elife-68693-video3.mp4.jpg)

We observed that, in all the solutions we used, rolling sperm swam progressively, whereas non-rolling sperm exhibited 2D asymmetric flagellar beatings and swam in circles, such that the curvature of the circular path was found to be proportional to the asymmetry level of flagellar beating. Furthermore, an increase in viscosity decreased the frequency of rolling $\omega_{SR}=\frac{1}{T_{SR}}$ in rolling sperm (Figure 1F) as well as their progressive velocities, such that rolling sperm continue to swim progressively but slowly, with rolling occurring at lower frequency in a viscous solution. An increase in viscoelasticity did not, however, change the frequency of rolling and the average path velocity of rolling sperm (Figure 1F). We also observed that suppression of rolling in the viscous solution (4% PVP) occurred with a significant decrease in the propulsive velocity of non-rolling sperm, whereas rolling suppression in the viscoelastic solution (1% PAM) did not result in a decrease in the propulsive velocity of non-rolling sperm (Figure 1G). Considering that viscosity of 1% PAM solution is an order of magnitude higher than that of 4% PVP solution (Appendix I, Section I), these results seem to contradict our claim that an increase of viscosity leads to suppression of rolling as well as decrease in the propulsive velocity. However, we stress that the storage modulus $G^{'}$ of 1% PAM solution which represents the elastic properties of the fluid was two orders of magnitude higher than that of 4% PVP solution (SI, Section I). The higher elasticity of 1% PAM indicates that this increase contributed significantly to the suppression of rolling, while it did not result in decrease of the sperm propulsive velocity.

We also noticed that the range of curvature $κ$ of the circular path in the non-rolling sperm population depended on ambient viscoelasticity (Figure 1H). As shown in Figure 1H, the suppression of rolling in sperm with a higher degree of asymmetry in their beating pattern occurred at lower ambient viscoelasticity, whereas higher ambient viscoelasticity was needed to suppress the rolling of sperm that exhibited lower asymmetry in their beating patterns. Similar behavior was observed when we increased the viscosity of the solution.

In TALP + 1% and 2% PVP solutions, some sperm exhibiting circular motion (<10%) also exhibited infrequent rollings, such that $ΩT_{SR}>2\pi$. Such infrequent rollings changed the direction of the circular motion (Figure 1I and Video 4) and resulted in abrupt relocations of the circular path’s center without significantly changing the curvature of the path.

![Video 4.](https://cdn.elifesciences.org/articles/68693/elife-68693-video4.mp4.jpg)

Although our results indicate that rolling is a key contributor to progressive motility, more evidence is needed to validate the hypothesis. Therefore, we decreased the concentration of bovine serum albumin to 0.5% in TALP and tethered sperm heads to the glass surface upon their entry into the reservoir (Saggiorato et al., 2017). Tethering the sperm heads to the glass surface suppressed the rolling component, and the 2D flagellar beating pattern was observed separately from rolling. We observed that, without rolling, flagellation was not necessarily symmetric and >80% of the sperm began rotating around the sperm head upon tethering, although their motion was progressive prior to the surface binding (Figure 1J, Videos 5 and 6).

![Video 5.](https://cdn.elifesciences.org/articles/68693/elife-68693-video5.mp4.jpg)

![Video 6.](https://cdn.elifesciences.org/articles/68693/elife-68693-video6.mp4.jpg)

Another piece of evidence that validates our hypothesis was observed by tracking single sperm migrating between TALP and 1% PAM or 4% PVP solutions (Figure 1K). The representative sperm trajectories shown in Figure 1K indicate that suppression of rolling upon exiting TALP and entering into the viscous or viscoelastic solutions (blue trajectories) resulted in an instantaneous transition in sperm swimming behavior from progressive to circular. The transition in sperm swimming behavior was found to be reversible, as reactivation of rolling upon exiting the viscous or viscoelastic solutions and entering into TALP (red trajectories) caused sperm to start swimming progressively. This reversible transition was observed in more than 95% of sperm cells (total count = 109) migrating between TALP and 1% PAM or 4% PVP solutions. This finding agrees with the results shown in Figure 1G, as sperm velocity of average path for the blue and red trajectories was measured to be (70 ± 5) µms−1 in TALP, (45 ± 5) µms−1 in 4% PVP, and (70 ± 5) µms−1 in 1% PAM solutions.

We measured the angular velocities of all tethered sperm and compared them with that of untethered sperm, which were swimming freely in circles (Figure 1L). Consistent with Figure 1H, tethered sperm exhibited lower angular velocities than untethered sperm. Thus, rolling sperm exhibit lower asymmetry than their non-rolling counterparts and, accordingly, higher ambient viscosity and viscoelasticity is needed to suppress the rolling motion of sperm with lower asymmetry in flagellation and vice versa.

### Rolling and progressive motion

To quantify the relationship between rolling and progressive motion, we first characterized asymmetry in the flagellar beating pattern. In agreement with Friedrich et al., 2010, measuring bending in the midpiece of the flagellum in time (Figure 2A) and the corresponding normalized fast Fourier transform $(P^{*}t)$ revealed the presence of a zeroth harmonic within the frequency domain of flagellation (Figure 2B). Note that the constant offset in the normalized power spectrum is white noise in our measurement system. Furthermore, the experimental noise coming from our measurement system (e.g., image processing) is also included in the peak width around the first harmonic frequency. That is, the peak width centered at $\omega$ includes the intrinsic noise originated from flagellar sources, as well as the noise associated with our measurement system.

![Figure 2.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig2-v2.jpg)

**Figure 2.:** (A) Bending in the midpiece ($y(t)$). (B) The Fourier transform of $y(t)$, $P^{∗}(\omega)$. (C) The average angle that the sperm sweeps in each beat, $Δ\theta$ and the corresponding $a_{0}¯$. (D) The normalized curvature of the path $LΩV_{p}^{-1}$ versus the normalized amplitude of the zeroth harmonic $a_{0}L^{-1}$ measured in Tyrode’s albumin lactate pyruvate medium (TALP), TALP + 4% polyvinylpyrrolidone (PVP), and TALP + 1% polyacrylamide (PAM). (E) Mean square displacement of the circular path’s center and (F) distribution of the center’s speed for two sperm swimming in circles. (G) The plot of head light intensity (HLI) versus time and the corresponding $Π(t)$. (H) The distribution of $T_{SR}$ for a single progressively swimming sperm with rolling. The distribution has mean and standard deviation of $\mu_{SR}$ and $\sigma_{SR}$, respectively. (I) A single sperm with arbitrary $Ω$ and frequent rollings swims progressively. The direction of progressive motion has a similar distribution to that of the frequent rolling, with mean and standard deviation of 0 and $\sqrt{n_{SR}}\sigma_{SR}Ω~$, respectively. See the effect of $Ω$ in the inset plot.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The $ϕ_{0}=2\pi$ situation corresponds to symmetric beating, and thus to absolute progressive motility. As $ϕ_{0}$ decreases, asymmetry in beating emerges and motility includes a circular motion ($x^{*}$ and $y^{*}$ are normalized $x$ and $y$ axes as sperm motion can be described using the 2D Cartesian system).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** At $ϕ_{0}=2\pi$, the beating pattern has a single 20 Hz frequency. As asymmetry emerges during beating, the main frequency shifts and higher harmonics along with the zeroth harmonic appear in the spectrum ($a^{*}$ is the normalized amplitude of the harmonics).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig2-figsupp3-v2.jpg)

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Dependence of sperm trajectory on $ΩT_{SR}~$.(A) Sperm pathways for varying values of $ΩT_{SR}~$. At low values of $ΩT_{SR}~$, the sperm swims progressively, whereas at higher values the sperm swims in circles, subject to relocations. (B) Experimental measurements of $ΩT_{SR}~$ for both progressive and circular motions. Data for circular motion without infrequent self-rolling are not presented. (C) Sperm velocity of the average path with respect to $ΩT_{SR}~$, showing that, when $ΩT_{SR}~$ approaches 0, $V-$ approaches $V_{p}$.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** (A) Sperm orientation with respect to the fluid stream decreases with rolling. (B) Rolling alters the direction of the perpendicular velocity produced by asymmetrical beating and thus, increases the upstream component of motion.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** Unlike frequently rolling sperm, those without rolling exhibit inefficient upstream motion. x and y axes are in µm, and the time between two consecutive points is 0.08 s. External flow rate is 1.2 µL/h.

Writing the flagellar beating pattern in Fourier series ansatz (Equation 1) and further modeling the flagellar beating pattern (SI, Section II), we found that $\sigma=\frac{a_{1}-a_{0}}{a_{1}}$ approximately presents the asymmetry level in the beating pattern. That is, $\sigma=1$ presents symmetric beating whereas lower values correspond to higher asymmetry in the beating pattern:

$$
y(x,t)=\sumn=0a_{n}cos⁡(n\omegat−kx).
$$

In Equation 1, the $x$ axis was set parallel to the flagellum at its straight-line form, $k=\frac{2\pi}{\lambda}$ (with $\lambda≈L$) is the wave number, $\omega$ is the main frequency, and $a_{n}$ is the amplitude of the nth harmonic. Note that the amplitude and frequencies of beating include delta-correlated Gaussian noise that can be described as $a_{n}=a~_{n}1+η_{n}(t)$ and $\omega_{n}=\omega~_{n}1+ξ(t)$, respectively, with $η_{n}(t)=ξ(t)=0$, $η_{n}(t)η_{n^{'}}(t')=D_{n}\delta_{nn^{'}}\delta(t-t')$, and $ξ(t)ξ(t')=D_{\omega}\delta(t-t')$. The tilde sign above a quantity represents its time average value. Following Saggiorato et al., 2017; Friedrich et al., 2010; Elgeti et al., 2015, we applied small amplitude (i.e., $∀n→a_{n}≪L$) and length preservation constraints and used resistive force theory (SI, Sections II–IV), to find that the zeroth harmonic in the beating pattern yields a toque as follows:

$$
\tau_{f}=(ξ_{N}−ξ_{T})\omegakLa_{0}\sumn=0na~_{n}^{2}.
$$

Note that $ξ_{T}$ and $ξ_{N}$ are drag coefficients in the tangential and normal directions, respectively, and $L$ is the sperm length. Although the propulsive force produced by the flagellum correlates with the characteristics of the first and higher harmonics, the amplitude of the zeroth harmonic is involved solely in the torque produced (Equation 2). Applying the zero net torque and force constraints, we found that propulsive $V~_{P}$ and angular $Ω~$ velocities were related through $a_{0}$:

$$
Ω~∝\frac{ξ_{T}}{ξ_{N}}(\frac{a_{0}}{L^{2}}V~_{P}).
$$

To verify Equation 3, we measured the angular velocity of the sperm and plotted a normalized path curvature $LΩV_{P}^{-1}$ with respect to the normalized amplitude of the zeroth harmonic $a_{0}L^{-1}$ in TALP, TALP + 4% PVP (viscous), and TALP + 1% PAM (viscoelastic) solutions (Figure 2C and D). The linear correlation between $LΩV_{P}^{-1}$ and $a_{0}L^{-1}$ is consistent with our mathematical arguments (Equations 1–3), confirming that $a_{0}$ modulates the curvature of the non-rolling sperm path. Furthermore, the linear relationship between $LΩV_{P}^{-1}$ and $a_{0}L^{-1}$ predicted by the resistive force theory is preserved for sperm motion in a viscoelastic solution whereas the slope differs from that observed for sperm motion in standard and viscous solutions (Zhang and Goldman, 2014; Teran et al., 2010; Li and Ardekani, 2015; Riley and Lauga, 2017; Spagnolie et al., 2013).

The resistive force theory, as a mean field approach, cannot explain the observed inconsistency in the circular path. The inconsistency in the circular path, however, can be characterized by quantifying the random fluctuations at the center of the circular path (Ma et al., 2014). We noticed that fluctuations at the center, and thus circular motion, are diffusive in character as the mean square displacement (MSD) of the center is proportional to the elapsed time: $MSD~t$ (Figure 2E). This diffusive motion can be quantified by the diffusion coefficient of the center determined by the intercept of MSD, or alternatively, the center’s speed distribution (Figure 2F).

We measured the head light intensity (HLI) of the sperm over time to characterize rollings during progressive motility (Figure 2G). HLI is a pulse-type quantity, with the pulse duration shorter than the time that elapses between two consecutive pulses, $T_{SR}$. Therefore, we defined the edge-sensitive function $Π(t)$ with $Π0=1$, such that $Π(t)$ is multiplied by −1 at each positive edge of HLI (Figure 2G). Note that $Π(t)$ captures the rolling component as a rapid switch in the direction of asymmetry (Figure 1I); rolling can therefore be incorporated into Equation 1 with $Π(t)$:

$$
y(x,t)=\sumn=0Π(t)a_{n}cos⁡(n\omegat−kx).
$$

Solving the equations of motion using Equation 4, we found that, depending on $ΩT_{SR}~$, sperm swim along varying pathways with average progressive velocity of:

$$
V−=V~_{P}\frac{2sin⁡(\frac{ΩT_{SR}~}{2})}{ΩT_{SR}~}
$$

(Figure 2—figure supplement 4A and B). At the frequent rolling limit $ΩT_{SR}~→0$, $V-$ approaches $V~_{P}$, which means that frequent rolling asymptotically yields progressive motion with the average path velocity equal to the propulsive velocity even though $Ω~\neq0$. Our experimental measurements are consistent with this finding because $ΩT_{SR}~$ is less than $2\pi$ for rolling sperm, whereas for circular motion with infrequent rolling it is greater than $2\pi$ (Figure 2—figure supplement 4C). Note that for non-rolling sperm, $ΩT_{SR}~→∞$.

Even though $ΩT_{SR}~$ determines the average path, how do deviations of $T_{SR}$ from the mean during motion influence the trajectory? Our measurements of $T_{SR}$ for one rolling sperm for ~40 s indicate that the mean and standard deviation of this random variable are $T~_{SR}≈0.11 s,\sigma_{SR}≈0.02 s$, respectively (Figure 2H). Combining arbitrary values for $Ω~$ with $T_{SR}$ distribution, we found that the direction of the average path obeys a similar distribution with mean of 0 and standard deviation of $\sqrt{n_{SR}}\sigma_{SR}Ω~$ (Figure 2I), in which $n_{SR}$ is the number of rolling occurrences.

Considering rolling as a switch in the direction of asymmetry, we investigated how rolling influenced sperm rheotaxis. The sperm-rheotactic behavior and angular velocity of upstream orientation is modeled using an Adler-type Equation 10:

$$
Ω_{RH}=−A\gammasin⁡\theta,
$$

in which $\gamma$ is the shear rate, $A$ is a constant, and $\theta$ is the relative orientation of the sperm with respect to the external fluid stream. For sperm with intrinsic angular velocity $(Ω)$, the net angular velocity under fluid flow is $Ω_{RH}+Ω$, which orients the sperm with respect to the flow during upstream motion $\theta_{UP}$:

$$
\theta_{UP}=sin^{−1}⁡(\frac{Ω}{A\gamma}).
$$

Including the rolling component in Equation 7 using $Πt$, the average orientation of the sperm with respect to flow during upstream motion is:

$$
\theta~_{UP}=⟨sin^{−1}⁡(\frac{ΩΠ(t)}{A\gamma})⟩=Π(t)~sin^{−1}⁡(\frac{Ω}{A\gamma})≪sin^{−1}⁡(\frac{Ω}{A\gamma}).
$$

Notably, $Π(t)~≪1$. Equation 8 predicts that rollings result in significant decay in $\theta~_{UP}$. Consequently, Equations 9 and 10 respectively present sperm net velocity in the upstream direction ($V~_{UP}$) in the presence or absence of frequent rollings:

$$
V~_{UP}=V_{P}cos⁡(\theta~_{UP})−V_{F}≈V_{P}−V_{F}
$$



$$
V~_{UP}≈V_{P}−V_{F}−(V_{N}\frac{Ω}{A\gamma}+\frac{1}{2}V_{P}(\frac{Ω}{A\gamma})^{2}).
$$

In Equations 9 and 10, $V_{P}$ and $V_{N}$ are sperm propulsive and perpendicular velocities (corresponding to the angular velocity), respectively, whereas $V_{F}$ is the external flow velocity (SI, Section V). To experimentally confirm the prediction obtained from Equations 9 and 10, we back-tracked and analyzed sperm motion under flow prior to their entry into the quiescent zone. We observed that $\theta~_{UP}$ is greater for non-rolling sperm $\theta~_{UP}=40°\pm10°$ than for those exhibiting the rolling motion $\theta~_{UP}=10°\pm5°$. Furthermore, the average upstream velocity of rolling sperm was much higher $(V~_{UP}=60\pm10 \mum/s)$ than that of non-rolling sperm $(V~_{UP}=30\pm10 \mum/s)$ (SI, Section V). These results indicate that, even though the rolling component is not required for sperm rheotaxis, it facilitates rheotactic behavior by minimizing the angle between sperm orientation and the external fluid flow, thus maximizing the upstream component of their motion.

### Sperm surface exploration

Non-rolling sperm swim along diffusive circular paths and explore the surface (Ma et al., 2014). To characterize the diffusivity in circular motion (Figure 2E and F), we overlayed consecutive images of one sperm with 0.08 s intervals over different times (Figure 3A). The thickness of the combined circular paths $\delta_{1-4}$ increases over time in all directions, $\delta_{1-4}∝\sqrt{t}$ (Figure 3B) as predicted by the MSD of the circular path’s center (Figure 2E and F). For any sperm that diffused more rapidly, cell tracking followed by circle fitting was used to characterize the motion of circular path’s center (Figure 3C).

![Figure 3.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig3-v2.jpg)

**Figure 3.:** (A) Overlayed consecutive images of a single sperm. Intervals: 0.08 s. (B) Diffusive motion increases $\delta_{1-4}$ in time. (C) Manual tracking of the sperm and the corresponding circular path’s center. (D) Trajectories of the sperm’s circular motion obtained by solving equations of motion. The signal-to-noise ratio (SNR) value is inversely correlated with the diffusion coefficient of the center. (E) Normalized mean step size obtained from experimental data and (F) from results shown in (D). (G) Infrequent rolling results in relocation of the center. (H) Two-phase intermittent search caused by infrequent rolling. (I) Experimental tracking of a sperm exhibiting intermittent search.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Average thickness increases with $~t^{0.5}$ and can be modeled with a normal diffusion process.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig3-figsupp3-v2.jpg)

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** This two-phase motion is an intermittent search process.

To identify the flagellar source of the center’s diffusion, we solved equations of motion where the amplitude and phase of all harmonics included white Gaussian noises, as described in Equation 1 (the results are shown in Figure 3D). Our simulations suggest that noise in the amplitudes and the phases of first and higher harmonics yielded a noisy $V_{P}$ without resulting in fluctuations of the center (SI, Section VI). By contrast, the noise in the amplitude of the zeroth harmonic yielded a similar noise in $Ω$ but not in $V_{P}$. Therefore, $Ω$ and $κ$ can be expressed as $Ω(t)=Ω~(1+η_{0}(t))$ and $κ(t)=κ~(1+η_{0}(t))$, respectively, such that lower signal-to-noise ratios $SNR=\frac{κ~^{2}}{κ^{2}-κ~^{2}}$ for identical mean curvatures yielded faster diffusion, whereas higher SNRs yielded more consistent pathways (Figure 3D). We measured the normalized mean step size $\delta^{2}κ^{2}$ and the corresponding SNR and found that our experimental data were consistent with the simulation-based results, except for a constant as shown in Figure 3E and F. That is, as suggested by simulations, the normalized mean step size was found to be inversely correlated with the SNRs: $\delta^{2}κ^{2}∝SNR^{-1}$.

As previously published (Ma et al., 2014; Goldstein et al., 2009), these fluctuations in the circular path’s center correspond to non-thermal noise in the sperm flagellar beating, rather than thermally driven fluctuations. Approximating sperm as a rod with length of ∼80 µm and diameter of ∼5 µm, the rotational diffusion caused by thermal fluctuations is in the other of 10−6s−1, which yields a $SNR~10^{7}$ for $κ~~(5\times10^{-3})\mum^{-1}$. This order of $SNR$ estimated for thermal fluctuations are far greater than our measured values and the experimental resolution; therefore, the contribution of thermal noise to the sperm diffusive circular motion is negligible.

Diffusive circular motion might be abruptly interrupted by infrequent rollings (Figure 1I, Figure 3G and H). In this case, the center of the circular path not only diffuses in time but also relocates ballistically upon rolling in a random direction with $V_{r}$ (Figure 3H,I), such that $\frac{D}{V_{r}}$∼10−6 −1 µm (SI, Section VII). This two-phase motion is an intermittent search, with greater efficiency in surface exploration than with normal diffusion (Bénichou et al., 2011). This increase in the efficiency of exploration may be interpreted as a decrease in the probability of revisiting previously swept spots. More precisely, the average area swept by the sperm through diffusion is proportional to the square root of diffusion time $A(t)∝\sqrt{t}$. Assuming that $T_{i}$ is the time frame between the (i−1)th and ith relocations, the areas swept with and without relocation are proportional to $\sumi\sqrt{T_{i}}$ and $\sqrt{\sumiT_{i}}$, respectively. Because $\sqrt{\sumiT_{i}}\leq\sumi\sqrt{T_{i}}$, infrequent rolling increases the area swept by the sperm (see SI, Section VII).

### Rolling and wall-dependent navigation

In addition to active swimming and external flow, the surrounding walls contribute to sperm motion (Elgeti et al., 2010). For a sperm that is positioned away from the walls (distance from the wall > the sperm length), the wall’s effect on the swimmer is known to be a drift velocity that can be either attractive or repulsive depending on the swimmer’s angle with respect to the wall (Elgeti et al., 2010). The model proposed for studying this drift velocity is based on positing the swimmer as a force dipole that includes the propulsive force provided by the flagellum as well as the corresponding drag force (Elgeti et al., 2010). However, this model can be used when the sperm exhibits fully symmetric flagellation. We therefore developed a new swimmer model that includes the torque caused by asymmetric beating. The proposed model is depicted in Figure 4—figure supplement 1A, in which $f$ is the propulsive force, $f^{''}$ is the perpendicular force corresponding to the torque, and $f^{'}$ is the drag force required for the torque-free condition. We then carried out finite element method simulations in a cylindrical domain, like our microfluidic quiescent reservoir, and solved the Stokes and mass conservation equations for our model to find the velocity field imposed by the sperm active swimming.

The velocity field imposed by flagellar beating for $Δ\theta~=0−15^{∘}$ is shown in Figure 4—figure supplement 1B. Integrating net flow in the y direction imposed on the sperm body that is caused by no-slip walls, we calculated the drift velocity toward the wall (Figure 4—figure supplement 1C). The simulation results indicated that the motion of the microswimmer is influenced to a lesser degree by nearby boundaries as the circular component emerges in the motility (SI, Section VIII). This decay in the drift velocity caused by the circular component of motion was also predicted by the analytical solution derived from a Stokeslet (Ardekani and Stocker, 2010; Li and Ardekani, 2014) description (SI, Section IX). The attraction of the sperm toward the wall in the presence of circular behavior can be described by the following equation:

$$
U_{w}=U_{w}^{p}(1−\frac{3}{2}sin(2Δ\theta~)),
$$

where $U_{w}$ and $U_{w}^{p}$ are the drift velocities with and without the circular motion. Calculating the average far-field drift velocity imposed on the sperm during one round of circulation, we found that the average magnitude of the drift velocity in one round (<1 µm/s) is much smaller than random fluctuations ((>540 µm/s) of the circular path’s center (Figure 4—figure supplement 1D and SI, Section X); therefore, the sperm’s circular motion is more strictly controlled by the level of asymmetry in its flagellum and diffusivity than by distant walls.

Frequent rollings, however, negate the contribution of circular components of the motion, producing a drift velocity as if the flagellation is symmetric and the sperm behaves like a dipole swimmer,

$$
U_{w}~=U_{w}^{p}(1−\frac{3}{2}Π(t)~sin(2Δ\theta~))≈U_{w}^{p}.
$$

We reiterate that $Π(t)~≪1$. Equation 12 states that frequent rollings make the sperm more readily disposed to physical boundaries at the far field.

Sperm near-field interactions with its nearby walls fit in one of the four categories shown in Figure 4A. A rolling sperm reorients upon wall contact and swims along the wall ($S_{1}$, Video 7), whereas with a non-rolling sperm, depending on $Ω$ and the location of the circular path’s center at the contact point, three other behaviors were observed. At a high magnitude of $Ω$, the sperm do not contact the wall, maintaining their circular motion ($S_{2}$, Video 8). At lower magnitudes of $Ω$, the sperm contact the wall and, depending on the location of the path’s center relative to the contact point, either swim near the wall temporarily and detach ($S_{3}$, Video 9) or swim more slowly along the wall (compared with $S_{1}$) with a tilted orientation with respect to the wall ($S_{4}$, Video 10). We compared these four types of sperm–wall interactions quantitatively using the time of sperm detention on the wall ($T_{D}$, Figure 4B), sperm velocity on the wall divided by its velocity before wall contact ($V^{*}$, Figure 4C), and the normalized length of detention $ρ^{*}$ (Figure 4D,E). Based on the measurements shown in Figure 4B–E, we found that the $S_{1}$ and $S_{3}$ categories yield similar $V^{*}$ values (close to 1), whereas for $S_{4}$, $V^{*}$ is smaller than 1 and for $Ω>1.5 s^{−1}$ the sperm do not migrate along the wall. Furthermore, $S_{1}$ and $S_{4}$ yield similar $ρ^{*}$ values, close to 1, whereas for $S_{3}$, $ρ^{*}$ is much smaller than 1, indicating temporary detention on the wall. A simple yet insightful approach to understanding these four categories involves surface contact force analysis (Marion, 2013), where the sperm contact with the wall can be modeled by a positive force that is perpendicular to the surface $N$.

![Figure 4.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig4-v2.jpg)

**Figure 4.:** (A) Sperm–wall interaction categories. Rolling sperm rotate and align with the wall upon contact to swim stably along it $S_{1}$. Non-rolling sperm exhibiting circular motion either do not contact the wall ($S_{2}$), detach from the wall after temporarily swimming along it $S_{3}$, or swim slowly along the wall $S_{4}$ depending on the magnitude and direction of angular velocity. (B) Sperm detention time on the wall, that is, $T_{D}$. (C) Sperm normalized velocity on the wall, that is, $V^{*}$. (D) A schematic to illustrate the definition of $ρ^{*}$. (E) $ρ^{*}$ versus $Ω$. (F) Free body diagram for the $S_{3}$, (G) $S_{4}$, and (H) $S_{1}$ categories. (I) Rolling results in alterations between $S_{3}$ and $S_{4}$, forming $S_{1}$. (J) The phase curves describing the dynamics of the angle between the sperm and wall after contact. Filled dots are stable points. Note that negative and positive $\beta_{S}$ values correspond to the $S_{3}$ and $S_{4}$ categories, respectively. (K) Rolling can be modeled as a transition between two-phase curves obtained for $\pmΩ$. A frequent transition between $\pmΩ$ results in $\beta_{S}~≪\beta_{S}^{*}$. (L) The phase curve for a rolling sperm. The final angle between the sperm and wall is ∼10°. (M) The phase curve for a non-rolling sperm. The final angle between the sperm and wall is ∼30°. (N) The distribution of $\beta_{S}~$ for 20 rolling sperm. $\beta_{S}~$ is linearly related to $\frac{Ω}{V}$ for non-rolling sperm (inset plot).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Proposed swimmer model, including the terms corresponding to circular motion. (B) The velocity field imposed by active swimming of the swimmer at varying $\Delta\theta$. (C) The drift velocity imposed by the wall for varying $V_{p}$ and $\Delta\theta$. (D) The model acquired to calculate average drift velocity imposed on the sperm in one circulation. The average $U_{w}$ is less than 1 µm/s; thus, the far-field influence of the wall on sperm motion is much weaker than fluctuations in the circular path’s center.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) The flow produced by the propulsive component of motility and its corresponding drag. (B) The flow produced by the circular components of motility and their corresponding drags $\Delta\theta$, ranging from 3° to 15°. The arrows are the normalized direction, whereas colors represent the magnitude of the velocity field.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig4-figsupp3-v2.jpg)

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig4-figsupp4-v2.jpg)

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig4-figsupp5-v2.jpg)

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig4-figsupp6-v2.jpg)

![Video 7.](https://cdn.elifesciences.org/articles/68693/elife-68693-video7.mp4.jpg)

![Video 8.](https://cdn.elifesciences.org/articles/68693/elife-68693-video8.mp4.jpg)

**Video 8.:** Non-rolling sperm with high $Ω_{in}$ does not contact the wall (S2).

![Video 9.](https://cdn.elifesciences.org/articles/68693/elife-68693-video9.mp4.jpg)

![Video 10.](https://cdn.elifesciences.org/articles/68693/elife-68693-video10.mp4.jpg)

Suppose that a sperm swims along a wall at an angle $\beta$ (Figure 4F). Under a zero net force constraint, the normal surface force becomes $N=F_{T}sin⁡(\beta)−F_{N}cos⁡(\beta)$, where $F_{T}$ and $F_{N}$ are the propulsive and perpendicular forces produced by the sperm, respectively. The threshold angle ($\beta_{th}$) that corresponds to the $N=0$ situation is equal to $tan^{-1}⁡\gamma$, where $\gamma=\frac{F_{N}}{F_{T}}$. For $\beta<\beta_{th}$, $N$ becomes negative and no contact occurs ($S_{2}$). Because an increase in $\gamma$ leads to higher $\beta_{th}$, sperm with greater $\gamma$ values are less likely to contact and follow the wall. For $\beta$ values greater than $\beta_{th}$, where sperm–wall contact occurs, greater $F_{N}$ yields a smaller $N$ and leads to easier detachment from the wall ($S_{3}$). When the direction of the sperm perpendicular force at the contact point is against the wall $(N=F_{T}sin⁡(\beta)+F_{N}cos⁡(\beta_{s}))$, a greater surface force is exerted, yielding a stronger attachment to the wall (Figure 4G). In this configuration, however, the parallel-to-the-wall components of the perpendicular and propulsive forces thwart each other and cause slower sperm motion along the wall. Therefore, asymmetric flagellation perturbs sperm motion along the wall by decreasing either its detention time ($S_{3}$) or velocity ($S_{4}$) on the wall. However, the rolling component functions as a switch between $S_{3}$ and $S_{4}$, and not only guarantees longer detention but also increases sperm velocity along the wall (Figure 4H,I).

Based on previous theoretical and computational studies on hydrodynamic interactions of a sperm (or a bacteria) with a wall (Drescher et al., 2011; Schaar et al., 2015; Elgeti and Gompper, 2013; Rode et al., 2019; Elgeti and Gompper, 2016), we developed a simple hydrodynamic model of sperm–wall interaction at the lubrication limit. Solving Stokes and mass conservation equations (SI, Section XI), we plotted the phase curve $(\beta˙vs\beta)$ of sperm dynamics after contacting the wall (Figure 4J). Note that $\beta˙$ is the effect of the wall superimposed with intrinsic $Ω$. For $Ω=0$, stability ($\beta˙=0$) occurs at $\beta_{S}=0$, implying that the final orientation of a symmetrically beating sperm with respect to the wall is 0. For $Ω>0$, corresponding to $S_{4}$, $\beta_{S}>0$ is the final angle between the sperm and the wall. For $Ω<0$, corresponding to $S_{3}$, $\beta_{S}<0$ and $\frac{d\beta}{dt}>0$ at $\beta=0$, suggesting that swimming parallel to the wall is unstable, and the sperm detaches from the wall with $\beta_{S}$. Figure 4J shows that the instability that occurs at $\beta_{U}=\frac{\pi}{2}$ (for $Ω=0$) changes with $Ω$ as well.

To include the contribution of rolling in sperm dynamics after wall contact, we modeled rollings as transitions between two curves in the phase space with positive and negative values of $Ω$ (Figure 4K). We then can rewrite $\beta˙$ and include $Πt$ such that:

$$
\beta˙=g(\beta)+Π(t)Ω.
$$

Note that $g\beta$ is the curve in the phase space that corresponds to $Ω=0$. Insofar as stability occurs at $\beta˙=0$,

$$
\beta_{S}^{∗}(t)=g^{−1}(−Π(t)Ω)=Π(t)g^{−1}(−Ω)=Π(t)\beta_{S},
$$

in which $\beta_{S}^{*}$ and $\beta_{S}$ are the stable points with and without taking rolling into account. Because $Π(t)~≪1$, the average of $\beta_{S}^{*}(t)$ is:

$$
\beta_{S}^{∗}~=Π(t)~\beta_{S}≪\beta_{S}.
$$

Equation 15 suggests that, at the frequent rolling limit where $Π(t)~$ approaches 0, $\beta_{S}^{∗}~$ approaches 0 as well. Consequently, frequent rollings mitigate the destructive role of $Ω$ in sperm motion along the wall, thereby yielding faster and longer-lasting swimming along the wall (SI, Section XII). Because at the frequent rolling limit $\beta_{S}^{∗}~$ is close to 0, we posit that $g(\beta_{S}^{∗}~)≈0$, and thus $\beta˙$ near the stable point can be written as:

$$
\beta˙=g(\beta_{S}^{∗}~)+Π(t)Ω≈Π(t)Ω.
$$

Based on Equation 16, $\betat$ is a triangular function near the stable point in the form of:

$$
\beta(t)≈Λ(t)Ω+\beta_{S}^{∗}~.
$$

We measured $\beta˙$ experimentally to verify the results obtained from the lubrication theory (Figure 4J). The net rotation ($\beta˙$) with respect to the angle between the sperm and wall ($\beta$) that corresponds to $S_{1}$ and $S_{4}$ is consistent with the results obtained from our model (Figure 4J,L,M). Furthermore, the frequent rollings observed in the $S_{1}$ category decreased $\beta_{S}~$ significantly to ∼10° (Figure 4N) in comparison with $\beta_{S}~$ for $S_{4}$, which was greater and linearly correlated with $\frac{Ω}{V}$ (Figure 4N, inset plot). This measurement supports our prediction that rolling enables the sperm to swim stably along the wall by decreasing $\beta_{s}~$. Measuring $\betat$ during stable swimming along the wall for 25 sperm that belong to the $S_{1}$ category, we found that $\betat$ is indeed a triangular function near the stable point, as predicted by Equation 17 (SI, Section XII).

A unified picture of sperm motion within the quiescent reservoir can be obtained by developing a state diagram and identifying the transitions between the $S_{1-4}$ states, possibly through the diffusivity of the circular motion and rolling. Suppose that, within the quiescent reservoir (radius of $R$), the non-rolling sperm swims in circle (with a radius of $R^{′}$), such that the distance between the centers of the two circles is $d(t)$, which evolves through diffusion (Figure 5A). Defining $s(t)=\frac{1}{2}(R^{2}+R^{′2}−d(t)^{2})$, the circular path does not intersect the reservoir for $s(t)>RR'$ (category $S_{2}$), whereas for $0<s(t)\leqRR^{′}$ the angle between the two circles at the intersection point (sperm incidence angle) is greater than $\beta_{u}$ (category $S_{3}$); for $s<0$, the angle at the intersection point is less than $\beta_{u}$ (category $S_{4}$). Assuming that at $t=0$ and the sperm is in the $S_{2}$ state, the circular path starts to diffuse over time, which leads to transitions between the $S_{2}$ and $S_{3}$ states. The average time for the first occurrence of a transition is $⟨T⟩=\frac{(R−R^{′})^{2}}{2D}$ (Figure 5B). One might expect the diffusion process to continue until $st$ becomes negative and the transition to $S_{4}$ occurs (Figure 5B). However, the angle at which the sperm detaches from the wall after the first contact $(\beta_{s})$ depends on $Ω$ rather than the location and angle at which contact occurs (Figure 5C). Therefore, after first contact, the sperm returns to the wall at an incidence angle that is identical to the angle at which it detaches from the wall $\beta_{s})$. Therefore, the transition from $S_{3}$ to $S_{4}$ occurs if $\beta_{s}>\beta_{u}$. Given that $\beta_{s}≈\frac{Ω}{|g^{′}(0)|}$, $\beta_{u}≈\frac{\pi}{2}+\frac{Ω}{g^{'}\frac{\pi}{2}}$, and $|g^{′}(0)|≪g^{′}(\frac{\pi}{2})$, the condition of such a transition reduces to:

$$
Ω>\frac{\pi}{2}\frac{|g^{′}(0)|g^{′}(\frac{\pi}{2})}{g^{′}(\frac{\pi}{2})−|g^{′}(0)|}≈\frac{\pi}{2}|g^{′}(0)|.
$$

![Figure 5.](https://cdn.elifesciences.org/articles/68693/elife-68693-fig5-v2.jpg)

**Figure 5.:** (A) The circular path does not intersect with the reservoir for $s>RR'$, whereas $0<s<RR'$ corresponds to $S_{3}$ and $s<0$ corresponds to $S_{4}$. (B) Diffusivity in circular motion results in the evolution of $st$, after which $T$$S_{2}$ transforms into $S_{3}$. (C) The angle at which the sperm detaches from the wall $\beta_{S})$ is independent of the incidence angle at the contact point. After the first contact and detachment, the sperm returns to the wall with $\beta_{S}$. (D) State diagram of non-rolling sperm–wall interactions. (E) At the frequent rollings limit, the time average of $s(t)$ approaches 0, where $s~≈0$, which corresponds to $S_{1}$. (F) Frequent rollings convert all the states into the $S_{1}$ state, whereas infrequent rollings result in reversible transitions between $S_{2},S_{3}$, and $S_{4}$, as needed for an efficient surface exploration.

The prime indicates derivative with respect to $\beta$. The corresponding curvature that satisfies Equation 18 is κ ∼ 0.1 µm−1, which is much greater than the experimentally observed values. The state diagram of non-rolling sperm–wall interactions and the possible transitions are summarized in Figure 5D.

For rolling sperm, the state diagram shown in Figure 5D alters significantly. First, infrequent rollings result in abrupt changes in $d(t)$ and thus $s(t)$, causing reversible transitions between $S_{2}$, $S_{3}$, and $S_{4}$ (Figure 5F). Second, at the frequent rollings limit, one may write $st≈Π(t)s$, so that $s(t)~$ approaches 0 (Figure 5E). Consequently, in the presence of frequent rollings, all states transition to $S_{1}$, where the sperm swims stably along the wall (Figure 5F).

## Discussion

In summary, rolling is a component of mammalian sperm motility that is sensitive to ambient viscosity and viscoelasticity. In a solution with low viscosity and viscoelasticity, most sperm exhibit a rolling and progressive motion that is susceptible to external fluid flow (rheotaxis) and rigid physical boundaries (wall-dependent navigation). As ambient viscosity or viscoelasticity increases, the rolling component becomes suppressed and subsequently the sperm swim in diffusive circular paths (surface exploration), a type of motion that is less susceptible to being influenced by external fluid flow or nearby walls. Suppression of rolling was found to be reversible, as sperm migrate into medium with low viscosity or viscoelasticity, rolling reactivates, and thus sperm swimming transitions from surface exploration to progressive motion. Furthermore, we demonstrated that the suppression of rolling in sperm with lower asymmetry in their flagellar beating pattern occurs at higher viscosity or viscoelasticity. Therefore, the suppression of rolling, and thus the onset of surface exploration, depends on both ambient rheological properties and the level of asymmetry in sperm flagellation.

Our results evidenced sperm flagellar beating is intrinsically asymmetric, but frequent rolling counteracts this asymmetric flagellation by alternating the direction of asymmetry, and results in a progressive motion. This progressive motion resulted from frequent rollings found to be key to the sperm rheotaxis and wall-dependent navigations. But why is susceptibility to external fluid flow and nearby walls under dynamic conditions not controlled solely by the level of asymmetry in flagellation so that maximum susceptibility appears with the fully symmetric beating pattern?

We argue that while fully symmetric beating pattern yields an efficient wall-dependent navigation, it does not result in an efficient rheotaxis, because the tilted orientation of the sperm (caused by rolling) with respect to the surface is needed for efficient rheotaxis, as demonstrated previously (Kantsler et al., 2014). More importantly, it is possible that, unlike the asymmetric beating pattern that is modulated by chemical factors (Suarez, 2008; Quill et al., 2003; Ramírez-Gómez et al., 2020), rolling depends on the ambient viscosity and viscoelasticity of the medium alone (Schiffer et al., 2020). Because the viscosity and viscoelasticity of the fluid within the female reproductive tract varies across functional regions, the tract possibly regulates sperm navigation by independently controlling: (1) the rolling component through regulating the rheology of the environment and (2) the asymmetry level in the flagellar beating pattern through secreting chemical factors. To show how regulating of asymmetrical beating caused by chemical factors works together with rolling, which is impacted by ambient viscosity and viscoelasticity, more studies regulating both aspects are needed.

Our results also demonstrate that the transition found between fast progressive and slow diffusive circular motions is reversible and occurs through suppression or reactivation of rolling. This finding, in particular, suggests that sperm motion during migration within the female reproductive tract is possibly bimodal. The fast progressive mode is an appropriate swimming behavior for sperm to migrate long distances between different functional regions within the female reproductive tract. This mode of motion may be regulated by the tract through rheotaxis and wall-dependent navigation. Whereas the slow diffusive motion is an appropriate swimming behavior for exploring the functional regions within the female reproductive tract to possibly receive physiological signals from these regions that are essential for the fertilization process. These physiological signals may include specific ligands secreted by the tract (Chang and Suarez, 2010), or pH of the functional region (Marquez and Suarez, 2007).

Our findings also suggest that elastic properties of the swimming media are key to the suppression of rolling and thus sperm motion. Characterizing the rheological properties of our viscous (4% PVP) and viscoelastic (1% PAM) solutions, we noticed that viscosity of 1% PAM is two orders of magnitude greater than that of 4% PVP solution. Rolling suppression in 1% PAM occurred without a loss in sperm propulsive velocity, whereas rolling suppression in the 4% PVP occurred with a significant loss in the propulsive velocity. Since the storage modulus of 1% PAM solution was two orders of magnitude greater than that of 4% PVP, we, therefore, conclude that the absence of a loss in the sperm propulsive velocity was due to the elastic properties of the solution. Accordingly, the elasticity of the swimming media is a key contributing factor to the sperm navigation within the female reproductive tract.

Our findings revealed the potential role of sperm rolling in mammalian fertilization, which results in a holistic and fundamental understanding of the fertilization process. Furthermore, these results are useful for more practical purposes such as designing technologies to improve fertility in cattle industry, as well as diagnosing and treating human male infertility. Furthermore, our results can be used to design new types of synthetic microswimmers that are responsive to dynamic physical environments, and thus more sensitive while exploring confined spaces.

## Materials and methods

### Sperm sample and culture media preparation

Commercially available cryopreserved bovine semen samples taken from two mature black and white Holstein bulls (5.5 and 6 years of age) were kindly donated by Genex Cooperative (Ithaca, NY) in milk and egg yolk–based extender in plastic straws. The ejaculate concentration was 2.9 and 3 billion cells/mL, respectively, and had a pre-freeze motility of 65%. The semen was thawed at 37°C in a water bath and diluted in a 1:4 ratio with TALP. After dilution, the viscosity of the samples was ~5 mPas. The initial sperm concentration in the thawed semen samples was ~200 million/mL, which was diluted to ~40 million/mL with TALP. The motility of the semen sample after dilution decreased to 20–30%. We used 10 separate semen samples in both the milk and egg yolk–based extender. At least three replicates were performed for each experiment to validate the accuracy of data and obtain a valid value for error bars.

TALP was prepared as follows: NaCl (110 mM), KCl (2.68 mM), NaH2PO4 (0.36 mM), NaHCO3 (25 mM), MgCl2 (0.49 mM), CaCl2 (2.4 mM), HEPES buffer (25 mM), glucose (5.56 mM), pyruvic acid (1.0 mM), penicillin G (0.006% or 3 mg/500 mL), and bovine serum albumin (20 mg/mL). To tether the sperm head to the glass surface, we reduced the concentration of bovine serum albumin to 5 mg/mL. To increase the viscosity and viscoelasticity of TALP, we added 1–4% of PVP (weight percent) and 0.25–1% PAM (weight percent).

### Rheological measurements

Dynamic rheological measurements were performed with a rheometer (MCR 501, Anton Paar, Stuttgart, Germany) with a 50 mm parallel plate at a gap of 0.5 mm. The amplitude sweep was conducted from 0.01% to 100% strain with a 1 Hz angular frequency to identify the linear viscoelastic region. The frequency sweep was performed from 1 to 100 s−1 (Tung et al., 2017) with a constant 1% strain (within the linear viscoelastic region). The viscosity was measured using the steady shear mode with the shear rate from 0.01 to 100 s−1. Samples were characterized at 37°C.

### Microfabrication and semen injection

The microfluidic device was made of polydimethylsiloxane using a standard soft lithography protocol. The diameter of the circular quiescent zone was 500 µm and the height of the chamber was 25 µm. Diluted semen was injected into the microfluidic device using gravity and the flow generated in the channel was controlled by changing the height of the semen container. Because sperm rheotaxis occurs under a very low shear rate (0.6 s−1), using gravity instead of conventional syringe pumps is more efficient for obtaining and controlling low flow rates.

### Rheotaxis-based sperm isolation and phase-contrast microscopy

To isolate motile bovine sperm inside the quiescent reservoir, we used a microfluidic corral system that isolated motile swimmers based on their ability to move upstream. As we injected the sample at an injection rate of 1.2 µLh−1, sperm with motilities higher than 53.2 µms−1 could swim upstream and enter the quiescent zone, which was filled with TALP, allowing us to study sperm movement with minimal fluid mechanical noise. Sperm movement was observed with a Nikon Eclipse TE300 inverted phase-contrast microscope (20× and 40× magnifications) and recorded with an Andor Zyla 5.5 sCMOS camera (25 and 50 frames/s).

### Cell tracking and zeroth harmonic measurement

Sperm trajectories and other motility-related characteristics were analyzed using ImageJ and MATLAB. To identify the harmonics of midpiece bending, we first removed noise and background using Gaussian filter and image subtraction. We then binarized the images taken from the sperm at 25 frames/s and measured the deviation of the midpiece (i.e., the segment located at 10 ± 1 µm from the head) from the centerline using the optical flow Flareback method. Taking the fast Fourier transform of the bending, we identified the zeroth, first, and second harmonics of the bending signal. A simple method for measuring the amplitude of the zeroth harmonic involves measuring the maximum bending toward the left $y_{L}$ and right $y_{R}$ sides of the swimmer. Therefore, the magnitude of the zeroth harmonic can be calculated using the following equation:

$$
a_{0}=\frac{|y_{L}−y_{R}|}{2}.
$$

The main advantage of our method is its simplicity, as tracking the whole flagellum was not required for measurement of zeroth harmonic.

### Numerical simulation

#### Beating pattern

To model the beating pattern of a sperm, we posited that the flagellation in one beat could be described by a sine wave at a temporal interval of $\pi-ϕ_{0},ϕ_{0}$, such that $ϕ_{0}\in\pi,2\pi$. $ϕ_{0}$ determines the level of asymmetry in the beating pattern. Thereafter, by evenly extending the function, we obtained the beating patterns, where $ϕ_{0}$ determined the asymmetry in the beating. For example, $ϕ_{0}=2\pi$ corresponds to $\sigma=1,$ and thus symmetric beating, whereas $ϕ_{0}<2\pi$ results in $\sigma<1$, and thus asymmetric beating. We then applied a fast Fourier transform on the beating patterns to determine their temporal frequencies. These steps were performed using MATLAB (version R2017a).

#### Finite element method simulations

To obtain the velocity field imposed by the swimmer model shown in Figure 4—figure supplement 1 and determine the far-field hydrodynamic interactions, we first imported the cylindrical structure of the quiescent zone to the COMSOL MULTIPHYSICS (version 5.2) platform. Two orthogonal Gaussian pulse functions (defined in the $x$ and $y$ directions) were used to define each point force in the swimmer model. The mathematical form of the pulse is a 2D Gaussian distribution, as follows:

$$
f\delta(x−x_{0})\delta(y−y_{0})=\frac{f}{2\pi\sigma_{x}\sigma_{y}}e^{\frac{−(x−x_{0})^{2}}{2\sigma_{x}^{2}}}e^{\frac{−(y−y_{0})^{2}}{2\sigma_{y}^{2}}}.
$$

We used $x_{0}$,$y_{0}$ to move and $\sigma_{x}$, $\sigma_{y}$ to focus the point forces arbitrarily. This strategy was chosen to lower the computational cost and avoid issues related to using small volumetric forces and their associated meshing problems in the finite element method. Finally, assuming that sperm swim in a quasi-2D plane that is located 5 μm below and parallel to the top surface, we solved the Stokes (Equation 21) and mass conservation equations for varying $Δ\theta$ values:

$$
∇p−\mu∇^{2}v=\sumf_{i}\delta(r−r_{i}).
$$

In Equation 21, p is the pressure, μ is the dynamic viscosity of the TALP medium ($3.2 mPas$), v is the fluid velocity, r is the position, $r_{i}$ is the position of the point force $f_{i}$, and $\delta$ is the Dirac delta function. The results obtained from this section are demonstrated in Figure 4—figure supplement 1B. Then, by integrating the velocity field imposed by the sperm, we obtained the drift velocity toward the wall, as shown in Figure 4—figure supplement 1C.

To find the torque imposed on the sperm in near-field conditions through lubrication approximation, we used a finite element method to solve Stokes and mass conservation equations for the configuration shown in Appendix 1. Given that the contribution of pressure in the stress tensor dominates that of viscous stress (SI, Section XI) ($pI≫\mu(\nablav+\nablav^{T})$), we extracted the pressure exerted on the sperm (Figure 4—figure supplement 5) at varying incident angles ($-90°<\beta<90°$) for a constant progressive velocity ($V_{p}=80\mum/s$). The torque exerted on the sperm from the wall and the corresponding angular velocity was then calculated:

$$
\beta˙=\frac{d\beta}{dt}=\frac{\alpha}{ξ_{N}}\frac{\int_{0}^{L}p(x−x_{cm})dx}{\int_{0}^{L}(x−x_{cm})^{2}dx}.
$$

In Equation 22, $p$ is pressure, $x_{cm}$ is the coordinate of the sperm center of mass, $L$ is the sperm length, and $\alpha$ is a fitting parameter. Note that $\beta˙$ is linearly correlated to $V_{p}$.
