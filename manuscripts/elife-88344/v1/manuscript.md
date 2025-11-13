# A three filament mechanistic model of musculotendon force and impedance

## Authors

- Matthew Millard<sup>1</sup> ([ORCID: 0000-0001-7627-564X](https://orcid.org/0000-0001-7627-564X)) †
- David W Franklin<sup>3</sup> ([ORCID: 0000-0001-9530-0820](https://orcid.org/0000-0001-9530-0820))
- Walter Herzog<sup>6</sup> ([ORCID: 0000-0002-5341-0033](https://orcid.org/0000-0002-5341-0033))

### Affiliations

1. Institute for Sport and Movement Science, University of Stuttgart Stuttgart Germany ([ROR:04vnq7t77](https://ror.org/04vnq7t77))
2. Institute of Engineering and Computational Mechanics, University of Stuttgart Stuttgart Germany ([ROR:04vnq7t77](https://ror.org/04vnq7t77))
3. Neuromuscular Diagnostics, TUM School of Medicine and Health, Technical University of Munich Munich Germany ([ROR:02kkvpp62](https://ror.org/02kkvpp62))
4. Munich School of Robotics and Machine Intelligence (MIRMI), Technical University of Munich Munich Germany ([ROR:02kkvpp62](https://ror.org/02kkvpp62))
5. Munich Data Science Institute (MDSI), Technical University of Munich Munich Germany ([ROR:02kkvpp62](https://ror.org/02kkvpp62))
6. Human Performance Laboratory, University of Calgary Calgary Canada ([ROR:03yjb2x39](https://ror.org/03yjb2x39))

† Corresponding author

## Abstract

The force developed by actively lengthened muscle depends on different structures across different scales of lengthening. For small perturbations, the active response of muscle is well captured by a linear-time-invariant (LTI) system: a stiff spring in parallel with a light damper. The force response of muscle to longer stretches is better represented by a compliant spring that can fix its end when activated. Experimental work has shown that the stiffness and damping (impedance) of muscle in response to small perturbations is of fundamental importance to motor learning and mechanical stability, while the huge forces developed during long active stretches are critical for simulating and predicting injury. Outside of motor learning and injury, muscle is actively lengthened as a part of nearly all terrestrial locomotion. Despite the functional importance of impedance and active lengthening, no single muscle model has all these mechanical properties. In this work, we present the viscoelastic-crossbridge active-titin (VEXAT) model that can replicate the response of muscle to length changes great and small. To evaluate the VEXAT model, we compare its response to biological muscle by simulating experiments that measure the impedance of muscle, and the forces developed during long active stretches. In addition, we have also compared the responses of the VEXAT model to a popular Hill-type muscle model. The VEXAT model more accurately captures the impedance of biological muscle and its responses to long active stretches than a Hill-type model and can still reproduce the force-velocity and force-length relations of muscle. While the comparison between the VEXAT model and biological muscle is favorable, there are some phenomena that can be improved: the low frequency phase response of the model, and a mechanism to support passive force enhancement.

## Introduction

The stiffness and damping of muscle are properties of fundamental importance for motor control, and the accurate simulation of muscle force. The CNS exploits the activation-dependent stiffness and damping (impedance) of muscle when learning new movements (Franklin et al., 2003), and when moving in unstable (Trumbower et al., 2009) or noisy environments (Selen et al., 2009). Reaching experiments using haptic manipulanda show that the CNS uses co-contraction to increase the stiffness of the arm when perturbed by an unstable force field (Burdet et al., 2001). With time and repetition, the force field becomes learned and co-contraction is reduced (Franklin et al., 2003).

The force response of muscle is not uniform, but varies with both the length and time of perturbation. Under constant activation and at a consistent nominal length, Kirsch et al., 1994 were able to show that muscle behaves like a linear-time-invariant (LTI) system in response to small perturbations (see Appendix 9, Note 1): a spring-damper of best fit captured over 90% of the observed variation in muscle force for small perturbations (1–3.8% optimal length) over a wide range of bandwidths (4–90 Hz). When active muscle is stretched appreciably, titin can develop enormous forces (Herzog and Leonard, 2002; Leonard et al., 2010), which may prevent further lengthening and injury. The stiffness that best captures the response of muscle to the small perturbations of Kirsch et al., 1994 is far greater than the stiffness that best captures the response of muscle to large perturbations (Herzog and Leonard, 2002; Leonard et al., 2010). Since everyday movements are often accompanied by both large and small kinematic perturbations, it is important to accurately capture these two processes.

However, there is likely no single muscle model that can replicate the force response of muscle to small (Kirsch et al., 1994) and large perturbations (Herzog and Leonard, 2002; Leonard et al., 2010) while also retaining the capability to reproduce the experiments of Hill, 1938 and Gordon et al., 1966. Unfortunately, this means that simulation studies that depend on an accurate replication of the perturbation response may reach conclusions well justified in simulation but not in reality. In this work, we focus on formulating a mechanistic muscle model (see Appendix 9, Note 2), that can replicate the force response of active muscle to length perturbations both great and small.

There are predominantly three classes of models that are used to simulate musculoskeletal responses: phenomenological models constructed using the famous force-velocity relationship of Hill, 1938, mechanistic Huxley (Huxley, 1957; Huxley and Simmons, 1971; Kosta et al., 2022) models in which individual elastic crossbridges are incorporated, and linearized muscle models (Hogan, 1985; Mussa-Ivaldi et al., 1985) which are accurate for small changes in muscle length. Kirsch et al., 1994 demonstrated that, for small perturbations, the force response of muscle is well represented by an activation-dependent spring and damper that are connected in parallel. Neither Hill nor Huxley models are likely to replicate the experiments of Kirsch et al., 1994 because a Hill muscle model (Zajac, 1989; Millard et al., 2013) does not contain any active spring elements; while a Huxley model lacks an active damping element. Although linearized muscle models can replicate the experiment of Kirsch et al., 1994, these models are only accurate for small changes in length and cannot replicate the nonlinear force-velocity relation of Hill, 1938, nor the nonlinear force-length relation of Gordon et al., 1966. However, there have been significant improvements to the canonical forms of phenomenological, mechanistic, and linearized muscle models that warrant closer inspection.

Several novel muscle models have been proposed to improve upon the accuracy of Hill-type muscle models during large active stretches. Forcinito et al., 1998 modeled the velocity dependence of muscle using a rheological element (see Appendix 9, Note 3) and an elastic rack rather than embedding the force-velocity relationship in equations directly, as is done in a typical Hill model (Zajac, 1989; Millard et al., 2013). This modification allows the model of Forcinito et al., 1998 to more faithfully replicate the force development of active muscle, as compared to a Hill-type model, during ramp length changes of ≈10% (see Appendix 9, Note 4) of the optimal CE length, and across velocities of 4–11% of the maximum contraction velocity (see Appendix 9, Note 5). Tamura and Saito, 2002 extended the work of Forcinito et al., 1998 by formulating a rheological muscle model with two Maxwell elements (a spring-damper in series) where one develops force quickly (high stiffness) and the other develops force slowly (low stiffness). By carefully selecting the dynamics that drive the two elements, the model of Tamura and Saito, 2002 replicated the force-length-velocity relations (Gordon et al., 1966; Hill, 1938) as well as qualitatively reproducing the force and stiffness profiles (Tamura et al., 2005) of force-enhancement and force-depression as measured by Sugi and Tsuchiya, 1988. Haeufle et al., 2014 made use of a serial-parallel network of spring-dampers to allow their model to reproduce the force-velocity relationship of Hill, 1938 mechanistically rather than embedding the experimental curve directly in their model. Günther et al., 2018 evaluated how accurately a variety of spring-damper models were able to reproduce the microscopic increases in crossbridge force in response to small length changes. While each of these models improves upon the force response of the Hill model to ramp length changes, none are likely to reproduce the experiment of Kirsch et al., 1994 because the linearized versions of these models lead to a serial, rather than a parallel, connection of a spring and a damper: Kirsch et al., 1994 specifically showed (see Figure 3 of Kirsch et al., 1994) that a serial connection of a spring-damper fails to reproduce the phase shift between force and length present in their experimental data.

Titin (Maruyama, 1976; Wang et al., 1979) has been more recently investigated to explain how lengthened muscle can develop active force when lengthened both within, and beyond, actin-myosin overlap (Leonard et al., 2010). Titin is a gigantic multi-segmented protein that spans a half-sarcomere, attaching to the Z-line at one end and the middle of the thick filament at the other end (Maruyama et al., 1985). In skeletal muscle, the two sections nearest to the Z-line, the proximal immunoglobulin (IgP) segment and the PEVK segment — rich in the amino acids proline (P), glutamate (E), valine (V) and lysine (K) — are the most compliant (Trombitás et al., 1998b) since the distal immunoglobulin (IgD) segments bind strongly to the thick filament (Houmeida et al., 1995). Titin has proven to be a complex filament, varying in composition and geometry between different muscle types (Tomalka et al., 2019; Boldt et al., 2020), widely between species (Lindstedt and Nishikawa, 2017), and can apply activation dependent forces to actin (Kellermayer and Granzier, 1996). It has proven challenging to determine which interactions dominate between the various segments of titin and the other filaments in a sarcomere. Experimental observations have reported titin-actin interactions at myosin-actin binding sites (Astier et al., 1998; Niederländer et al., 2004), between titin’s PEVK region and actin (Bianco et al., 2007; Nagy et al., 2004), between titin’s N2A region and actin (Dutta et al., 2018), and between the PEVK-IgD regions of titin and myosin (DuVall et al., 2017). This large variety of experimental observations has led to a correspondingly large number of proposed hypotheses and models, most of which involve titin interacting with actin (Rode et al., 2009; Nishikawa et al., 2012; Schappacher-Tilp et al., 2015; Tahir et al., 2018; Heidlauf et al., 2016; Heidlauf et al., 2017), and more recently with myosin (DuVall et al., 2016).

The addition of a titin element to a model will result in more accurate force production during large active length changes, but does not affect the stiffness and damping of muscle at modest sarcomere lengths because of titin’s relatively low stiffness. At sarcomere lengths of $1.62l_{o}^{M}$ or less, the stiffness of the actin-myosin load path with a single attached crossbridge (0.22–1.15pN/nm) equals or exceeds the stiffness of 6 passive titin filaments (0.0348–0.173pN/nm), and our estimated stiffness of 6 active titin filaments (0.0696–0.346pN/nm, see Appendix 1 for further details). When fully activated, the stiffness of the actin-myosin load path (4.05–18.4pN/nm) far exceeds that of both the passive titin (0.0348–0.173pN/nm), and our estimated active titin ($0.0696−0.346pN/nm$) load paths. Since titin-focused models have not made any changes to the modeled myosin-actin interaction beyond a Hill (Zajac, 1989; Millard et al., 2013) or Huxley (Huxley, 1957; Huxley and Simmons, 1971) model, it is unlikely that these models would be able to replicate the experiments of Kirsch et al., 1994.

Although most motor control simulations (Kearney et al., 1997; Perreault et al., 2004; Schouten et al., 2008; Trumbower et al., 2009; Mitrovic et al., 2010) make use of the canonical linearized muscle model, phenomenological muscle models have also been used and modified to include stiffness. Sartori et al., 2015 modeled muscle stiffness by evaluating the partial derivative of the force developed by a Hill-type muscle model with respect to the contractile element (CE) length. Although this approach is mathematically correct, the resulting stiffness is heavily inﬂuenced by the shape of the force-length curve and can lead to inaccurate results: at the optimal CE length this approach would predict an active muscle stiffness of zero since the slope of the force-length curve is zero; on the descending limb this approach would predict a negative active muscle stiffness since the slope of the force-length curve is negative. In contrast, CE stiffness is large and positive near the optimal length (Kirsch et al., 1994), and there is no evidence for negative stiffness on the descending limb of the force-length curve (Herzog and Leonard, 2002). Although the stiffness of the CE can be kept positive by shifting the passive force-length curve, which is at times used in finite-element-models of muscle (Heidlauf et al., 2017), this introduces a new problem: the resulting passive CE stiffness cannot be lowered to match a more ﬂexible muscle. In contrast, De Groote et al., 2017 and De Groote et al., 2018 modeled short-range-stiffness using a stiff spring in parallel with the active force element of a Hill-type muscle model. While the approach developed in De Groote et al., 2017 and De Groote et al., 2018 likely does improve the response of a Hill-type muscle model for small perturbations, there are several drawbacks: the short-range-stiffness of the muscle sharply goes to zero outside of the specified range whereas in reality the stiffness is only reduced (Kirsch et al., 1994, see Figure 9A); the damping of the canonical Hill-model has been left unchanged and likely differs substantially from biological muscle (Kirsch et al., 1994).

In this work, we propose a model that can capture the force development of muscle to perturbations that vary in size and timescale, and yet is described using only a few states making it well suited for large-scale simulations. When active, the response of the model to perturbations within actin-myosin overlap is dominated by a viscoelastic crossbridge element that has different dynamics across time-scales: over brief time-scales the viscoelasticity of the lumped crossbridge dominates the response of the muscle (Kirsch et al., 1994), while over longer time-scales the force-velocity (Hill, 1938) and force-length (Gordon et al., 1966) properties of muscle dominate. To capture the active forces developed by muscle beyond actin-myosin overlap we added an active titin element which, similar to the models of Rode et al., 2009 and (Schappacher-Tilp et al., 2015), features an activation-dependent (see Appendix 9, Note 6) interaction between titin and actin. To ensure that the various parts of the model are bounded by reality, we have estimated the physical properties of the viscoelastic crossbridge element as well as the active titin element using data from the literature.

While our main focus is to develop a more accurate muscle model, we would like the model to be well suited to simulating systems that contain tens to hundreds of muscles. Although Huxley models have been used to simulate whole-body movements such as jumping (van Soest et al., 2019), the memory and processing requirements associated with simulating a single muscle with thousands of states is high. Instead of modeling the force development of individual crossbridges, we lump all of the crossbridges in a muscle together so that we have a small number of states to simulate per muscle.

To evaluate the proposed model, we compare simulations of experiments to original data. We examine the response of active muscle to small perturbations over a wide bandwidth by simulating the stochastic perturbation experiments of Kirsch et al., 1994. The active-lengthening experiments of Herzog and Leonard, 2002 are used to evaluate the response of the model when it is actively lengthened within actin-myosin overlap. Next, we use the active-lengthening experiments of Leonard et al., 2010 to see how the model compares to reality when it is actively lengthened beyond actin-myosin overlap. In addition, we examine how well the model can reproduce the force-velocity experiments of Hill, 1938 and force-length experiments of Gordon et al., 1966. Since Hill-type models are so commonly used, we also replicate all of the simulated experiments using the Hill-type muscle model of Millard et al., 2013 to make the differences between these two types of models clear.

## Model

We begin by treating whole muscle as a scaled half-sarcomere that is pennated at an angle $\alpha$ with respect to a tendon (Figure 1A). The assumption that mechanical properties scale with size is commonly used when modeling muscle (Zajac, 1989) and makes it possible to model vastly different musculotendon units (MTUs) by simply changing the architectural and contraction properties: the maximum isometric force $f_{o}^{M}$, the optimal CE length $l_{o}^{M}$ (at which the CE develops $f_{o}^{M}$), the pennation angle $\alpha_{o}$ of the CE (at a length of $l_{o}^{M}$) with respect to the tendon, the maximum shortening velocity $v_{max}^{M}$ of the CE, and the slack length of the tendon $l_{s}^{T}$. Many properties of sarcomeres scale with $f_{o}^{M}$ and $l_{o}^{M}$: $f_{o}^{M}$ scales with physiological cross-sectional area (Maganaris et al., 2001), the force-length property scales with $l_{o}^{M}$ (Winters et al., 2011), the maximum normalized shortening velocity of different CE types scales with $l_{o}^{M}$ across animals great and small (Rome et al., 1990), and titin’s passive-force-length properties scale from single molecules to myofibrils (Herzog et al., 2012; Prado et al., 2005).

![Figure 1.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig1-v1.jpg)

**Figure 1.:** The name of the VEXAT model comes from the viscoelastic crossbridge and active titin elements (A) in the model. Active tension generated by the lumped crossbridge ﬂows through actin, myosin, and the adjacent sarcomeres to the attached tendon (B). Titin is modeled as two springs of length $l^{1}$ and $l^{2}$ in series with the rigid segments $L^{T12}$ and $L^{IgD}$. Viscous forces act between titin and actin in proportion to the activation of the muscle (C), which reduces to negligible values in a purely passive muscle (D). We modeled actin and myosin as rigid elements; the XE, titin, and the tendon as viscoelastic elements; and the ECM as an elastic element.

The proposed model has several additional properties that we assume scale with $f_{o}^{M}$ and inversely with $l_{o}^{M}$: the maximum active isometric stiffness $k_{o}^{X}$ and damping $\beta_{o}^{X}$, the passive forces due to the extracellular matrix (ECM), and passive forces due to titin. As crossbridge stiffness is well studied (Kaya and Higuchi, 2013), we assume that muscle stiffness due to crossbridges scales such that

$$
k_{o}^{X}=k~_{o}^{X}\frac{f_{o}^{M}}{l_{o}^{M}},
$$

where $k~_{o}^{X}$ is the maximum normalized stiffness. This scaling is just what would be expected when many crossbridges (Kaya and Higuchi, 2013) act in parallel across the cross-sectional area of the muscle, and act in series along the length of the muscle. Although the intrinsic damping properties of crossbridges are not well studied, we assume that the linear increase in damping with activation observed by Kirsch et al., 1994 is due to the intrinsic damping properties of individual crossbridges which will also scale linearly with $f_{o}^{M}$ and inversely with $l_{o}^{M}$

$$
\beta_{o}^{X}=\beta~_{o}^{X}\frac{f_{o}^{M}}{l_{o}^{M}},
$$

where $\beta~_{o}^{X}$ is the maximum normalized damping. For the remainder of the paper, we refer to the proposed model as the VEXAT model due to the viscoelastic (VE) crossbridge (X) and active-titin (AT) elements of the model.

To reduce the number of states needed to simulate the VEXAT model, we lump all of the attached crossbridges into a single lumped crossbridge element (XE) that attaches at $l^{S}$ (Figure 1A) and has intrinsic stiffness and damping properties that vary with the activation and force-length properties of muscle. The active force developed by the XE at the attachment point to actin is transmitted to the main myosin filament, the M-line, and ultimately to the tendon (Figure 1B). In addition, since the stiffness of actin (Higuchi et al., 1995) and myosin filaments (Tajima et al., 1994) greatly exceeds that of crossbridges (Veigel et al., 1998), we treat actin and myosin filaments as rigid to reduce the number of states needed to simulate this model. Similarly, we have lumped the six titin filaments per half-sarcomere (Figure 1A) together to further reduce the number of states needed to simulate this model.

The addition of a titin filament to the model introduces an additional active load-path (Figure 1C) and an additional passive load-path (Figure 1D). As is typical (Zajac, 1989; Millard et al., 2013), we assume that the passive elasticity of these structures scale linearly with $f_{o}^{M}$ and inversely with $l_{o}^{M}$. Since the VEXAT model has two passive load paths (Figure 1D), we further assume that the proportion of the passive force due to the extra-cellular-matrix (ECM) and titin does not follow a scale-dependent pattern, but varies from muscle-to-muscle as observed by Prado et al., 2005.

As previously mentioned, there are several theories to explain how titin interacts with the other filaments in activated muscle. While there is evidence for titin-actin interaction near titin’s N2A region (Dutta et al., 2018), there is also support for a titin-actin interaction occurring near titin’s PEVK region (Bianco et al., 2007; Nagy et al., 2004), and for a titin-myosin interaction near the PEVK-IgD region (DuVall et al., 2017). For the purposes of our model, we will assume a titin-actin interaction because current evidence weighs more heavily towards a titin-actin interaction than a titin-myosin interaction. Next, we assume that the titin-actin interaction takes place somewhere in the PEVK segment for two reasons: first, there is evidence for a titin-actin interaction (Bianco et al., 2007; Nagy et al., 2004) in the PEVK segment; and second, there is evidence supporting an interaction at the proximal end of the PEVK segment (Dutta et al., 2018, N2A-actin interaction). We have left the point within the PEVK segment that attaches to actin as a free variable since there is some uncertainty about what part of the PEVK segment interacts with actin.

The nature of the mechanical interaction between titin and the other filaments in an active sarcomere remains uncertain. Here, we assume that this interaction is not a rigid attachment, but instead is an activation dependent damping to be consistent with the observations of Kellermayer and Granzier, 1996 and Dutta et al., 2018: adding titin filaments and calcium slowed, but did not stop, the progression of actin filaments across a plate covered in active crossbridges (an in vitro motility assay). When activated, we assume that the amount of damping between titin and actin scales linearly with $f_{o}^{M}$ and inversely with $l_{o}^{M}$.

After lumping all of the crossbridges and titin filaments together, we are left with a rigid-tendon MTU model that has two generalized positions

$$
q_^{R}=(l^{S},l^{1})
$$

and an elastic-tendon MTU model that has three generalized positions

$$
q_^{E}=(l^{M},l^{S},l^{1}).
$$

Given these generalized positions, the path length $l^{P}$, and a pennation model, all other lengths in the model can be calculated. Here, we use a constant thickness

$$
H=l_{o}^{M}sin⁡\alpha_{o}
$$

pennation model to evaluate the pennation angle

$$
\alpha=arctan⁡(\frac{H}{l^{P}−l_{s}^{T}})
$$

of a CE with a rigid-tendon, and

$$
\alpha=arcsin⁡(\frac{H}{l^{M}})
$$

to evaluate the pennation angle of a CE with an elastic-tendon. We have added a small compressive element KE (Figure 1A) to prevent the model from reaching the numerical singularity that exists as $l~^{M}$ approaches $l~_{min}^{M}$, the length at which $\alpha→90^{∘}$ in Equation 6 and Equation 7. The tendon length

$$
l^{T}=l^{P}−l^{M}cos⁡\alpha,
$$

of an elastic-tendon model is the difference between the path length and the CE length along the tendon. The length of the XE

$$
l^{X}=\frac{1}{2}l^{M}−(l^{S}+L^{M})
$$

is the difference between the half-sarcomere length and the sum of the average point of attachment $l^{S}$ and the length of the myosin filament $L^{M}$. The length of $l^{2}$, the lumped PEVK-IgD segment, is

$$
l^{2}=\frac{1}{2}l^{M}−(l^{1}+L^{T12}+L^{IgD})
$$

the difference between the half-sarcomere length and the sum of the length from the Z-line to the actin binding site on titin ($l^{1}+L^{T12}$) and the length of the IgD segment that is bound to myosin ($L^{IgD}$). Finally, the length of the extra-cellular-matrix $l^{ECM}$ is simply

$$
l^{ECM}=\frac{1}{2}l^{M}
$$

half the length of the CE since we are modeling a half-sarcomere.

We have some freedom to choose the state vector of the model and the differential equations that define how the muscle responds to length and activation changes. The experiments we hope to replicate depend on phenomena that take place at different time-scales: the stochastic perturbations of Kirsch et al., 1994 evolve over brief time-scales, while all of the other experiments take place at much longer time-scales. Here, we mathematically decouple phenomena that affect brief and long time-scales by making a second-order model that has states of the average point of crossbridge attachment $l^{S}$, and velocity $v^{S}$. When the activation state $a$ and the titin-actin interaction model are included, the resulting rigid-tendon model has a total of four states

$$
x_=(a,v^{S},l^{S},l^{1})
$$

and the elastic-tendon model has

$$
x_=(a,v^{S},l^{S},l^{1},l^{M})
$$

five states. For the purpose of comparison, a Hill-type muscle model with a rigid-tendon has a single state ($a$), while an elastic-tendon model has two states ($a$ and $l^{M}$) (Millard et al., 2013).

Before proceeding, a small note on notation: throughout this work we will use an underbar to indicate a vector, bold font to indicate a curve, a tilde for a normalized quantity, and a capital letter to indicate a constant. Unless indicated otherwise, curves are constructed using $C^{2}$ continuous (see Appendix 9, Note 7) Bézier splines so that the model is compatible with gradient-based optimization. Normalized quantities within the CE follow a specific convention: lengths and velocities are normalized by the optimal CE length $l_{o}^{M}$, forces by the maximum active isometric tension $f_{o}^{M}$, stiffness and damping by $f_{o}^{M}/l_{o}^{M}$. Velocities used as input to the force-velocity relation $f^{V}$ are further normalized by $v_{max}^{M}$ and annotated using a hat: $v^^{M}=v^{M}/v_{max}^{M}$. Tendon lengths and velocities are normalized by $l_{s}^{T}$ tendon slack length, while forces are normalized by $f_{o}^{M}$.

To evaluate the state derivative of the model, we require equations for $a˙$, $v˙^{S}$, $v^{1}$, and $v^{M}$ if the tendon is elastic. For $a˙$ we use of the first order activation dynamics model described in Millard et al., 2013 (see Appendix 9, Note 8) which uses a lumped first-order ordinary-differential-equation (ODE) to describe how a fused tetanus electrical excitation leads to force development in an isometric muscle. We formulated the equation for $v˙^{S}$ with the intention of having the model behave like a spring-damper over small time-scales, but to converge to the tension developed by a Hill-type model

$$
f~^{M}=af^{L}(l~^{M})f^{V}(v~^{M})+f^{PE}(l~^{M})
$$

over longer time-scales, where $f^{L}(⋅)$ is the active-force-length curve (Figure 2A), $f^{PE}(⋅)$ is the passive-force-length curve (Figure 2A), and $f^{V}(⋅)$ is the force-velocity curve (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig2-v1.jpg)

**Figure 2.:** The model relies on Bézier curves to model the nonlinear effects of the active-force-length curve, the passive-force-length curve (A), and the force-velocity curve (B). Since nearly all of the reference experiments used in the ‘Biological benchmark simulations’ section have used cat soleus, we have fit the active-force-length curve ($f^{L}(⋅)$) and passive-force-length curves ($f^{PE}(⋅)$) to the cat soleus data of Herzog and Leonard, 2002. The concentric side of the force-velocity curve ($f^{V}(⋅)$) has been fitted to the cat soleus data of Herzog and Leonard, 1997.

The normalized tension developed by the VEXAT model

$$
f~^{M}=af^{L}(l~^{S}+L~^{M})(k~_{o}^{X}l~^{X}+\beta~_{o}^{X}v~^{X})+f^{2}(l~^{2})+f^{ECM}(l~^{ECM})+\beta~^{ϵ}v~^{M}−\frac{f^{KE}(l~^{M})}{cos⁡\alpha}
$$

differs from that of a Hill model, Equation 14, because it has no explicit dependency on $v~^{M}$, includes four passive terms, and a lumped viscoelastic crossbridge element. The four passive terms come from the ECM element $f^{ECM}(l~^{ECM})$ (Figure 3A), the PEVK-IgD element $f^{2}(l~^{2})$ (Figure 3A and B), the compressive term $f^{KE}(l~^{M})$ (prevents $l~^{M}cos⁡\alpha$ from reaching a length of 0), and a numerical damping term $\beta~^{ϵ}v~^{M}$ (where $\beta~^{ϵ}$ is small). The active force developed by the XE’s lumped crossbridge $k~_{o}^{X}l~^{X}+\beta~_{o}^{X}v~^{X}$ is scaled by the fraction of the XE that is active and attached, $af^{L}(l~^{S}+L~^{M})$, where $f^{L}(⋅)$ is the active-force-length relation (Figure 2A). We evaluate $f^{L}$ using $l~^{S}+L~^{M}$ in Equation 15, rather than $l~^{M}$ as in Equation 14, since actin-myosin overlap is independent of crossbridge strain. With $f~^{M}$ derived, we can proceed to model the acceleration of the CE, $v˙^{S}$, so that it is driven over time by the force imbalance between the XE’s active tension and that of a Hill model.

![Figure 3.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig3-v1.jpg)

**Figure 3.:** The passive force-length curve has been decomposed such that 56% of it comes from the ECM while 44% comes from titin to match the average of ECM-titin passive force distribution (which ranges from 43% to 76%) reported by Prado et al., 2005 (A). The elasticity of the titin segment has been further decomposed into two serially connected sections: the proximal section consisting of the T12, proximal IgP segment and part of the PEVK segment, and the distal section consisting of the remaining PEVK section and the distal Ig segment (B) The stiffness of the IgP and PEVK segments has been chosen so that the model can reproduce the movements of IgP/PEVK and PEVK/IgD boundaries that Trombitás et al., 1998b (C) observed in their experiments. The curves that appear in subplots A and B come from scaling the two-segmented human soleus titin model to cat soleus muscle. The curves that appear in subplot C compare the human soleus titin model’s IgP, PEVK, and IgD force-length relations to the data of Trombitás et al., 1998b (see in Appendix 2 for details).

We set the first term of $v~˙^{S}$ so that, over time, the CE is driven to develop the same active tension as the Hill-type model of Millard et al., 2013 (terms highlighted in blue)

$$
v~˙^{S}=\frac{af^{L}(l~^{S}+L~^{M})(k~_{o}^{X}l~^{X}+\beta~_{o}^{X}v~^{X})−af^{L}(l~^{S}+L~^{M})f^{V}(v^^{S})}{\tau^{S}}−Dv~^{S}+e^{−(a/a_{L})^{2}}(G_{L}l~^{X}+G_{V}v~^{X})
$$

where $\tau^{S}$ is a time constant and $f^{V}(v^^{S})$ is the force-velocity curve (Figure 2B). The rate of adaptation of the model’s tension, to the embedded Hill model, is set by the time constant $\tau^{S}$: as $\tau^{S}$ is decreased the VEXAT model converges more rapidly to a Hill-type model; as $\tau^{S}$ is increased the active force produced by the model will look more like a spring-damper. Our preliminary simulations indicate that there is a trade-off to choosing $\tau^{S}$: when $\tau^{S}$ is large the model will not shorten rapidly enough to replicate Hill’s experiments, while if $\tau^{S}$ is small the low-frequency response of the model is compromised when the experiments of Kirsch et al., 1994 are simulated.

The remaining two terms, $Dv~^{S}$ and $e^{−(a/a_{L})^{2}}(G_{L}l~^{X}+G_{V}v~^{X})$, have been included for numerical reasons specific to this model formulation rather than muscle physiology. We include a term that damps the rate of actin-myosin translation, $Dv~^{S}$, to prevent this second-order system from unrealistically oscillating (see Appendix 9, Note 9). The final term $e^{−(a/a_{L})^{2}}(G_{L}v~^{X}+G_{V}v~^{X})$, where $G_{L}$ and $G_{V}$ are scalar gains, and $a_{L}$ is a low-activation threshold ($a_{L}$ is $0.05$ in this work). This final term has been included as a consequence of the generalized positions we have chosen. When the CE is nearly deactivated (as $a$ approaches $a_{L}$), this term forces $l~^{S}$ and $v~^{S}$ to shadow the location and velocity of the XE attachment point. This ensures that if the XE is suddenly activated, that it attaches with little strain. We had to include this term because we made $l^{S}$ a state variable, rather than $l^{X}$. We chose $l^{S}$ as a state variable, rather than $l^{X}$, so that the states are more equally scaled for numerical integration.

The passive force developed by the CE in Equation 15 is the sum of the elastic forces (Figure 3A) developed by the force-length curves of titin ($f^{1}(l~^{1})$ and $f^{2}(l~^{2})$) and the ECM ($f^{ECM}(l~^{ECM})$). We model titin’s elasticity as being due to two serially connected elastic segments: the first elastic segment $f^{1}(l~^{1})$ is formed by lumping together the IgP segment and a fraction $Q$ of the PEVK segment, while the second elastic segment $f^{2}(l~^{2})$ is formed by lumping together the remaining $(1−Q)$ of the PEVK segment with the free IgD section. Our preliminary simulations of the active lengthening experiment of Herzog and Leonard, 2002 indicate that a $Q$ value of 0.5, positioning the PEVK-actin attachment point that is near the middle of the PEVK segment, allows the model to develop sufficient tension when actively lengthened. The large section of the IgD segment that is bound to myosin is treated as rigid.

The curves that form $f^{ECM}(l~^{ECM})$, $f^{1}(l~^{1})$, and $f^{2}(l~^{2})$ have been carefully constructed to satisfy three experimental observations: that the total passive force-length curve of titin and the ECM match the observed passive force-length curve of the muscle (Figure 2A and Figure 3A) as in the experiments of Prado et al., 2005; that the proportion of the passive force developed by titin and the ECM (Figure 3A) is within experimental observations of Prado et al., 2005; and that the Ig domains and PEVK residues show the same relative elongation (Figure 3C) as observed by Trombitás et al., 1998a. Even though the measurements of Trombitás et al., 1998b come from human soleus titin, we can construct the force-length curves of other titin isoforms if the number of proximal Ig domains, PEVK residues, and distal Ig domains are known (see Appendix 2.4). Since the passive–force-length relation and the results of Trombitás et al., 1998b are at modest lengths, we consider two different extensions to the force-length relation to simulate extreme lengths: first, a simple linear extrapolation; second, we extend the force-length relation of each of titin’s segments to follow a worm-like-chain (WLC) model similar to Trombitás et al., 1998b (see Appendix 2.4 for details on the WLC model). With titin’s passive force-length relations defined, we can next consider what happens to titin in active muscle.

When active muscle is lengthened, it produces an enhanced force that persists long after the lengthening has ceased called residual force enhancement (RFE) (Herzog and Leonard, 2002). For the purposes of the VEXAT model, we assume that RFE is produced by titin. Experiments have demonstrated RFE on both the ascending limb (Peterson et al., 2004) and descending limb of the force-length (Herzog and Leonard, 2002) relation. The amount of RFE depends both on the final length of the stretch (Hisey et al., 2009) and the magnitude of the stretch: on the ascending limb the amount of RFE varies with the final length but not with stretch magnitude, while on the descending limb RFE varies with stretch magnitude.

To develop RFE, we assume that some point of the PEVK segment bonds with actin through an activation-dependent damper. The VEXAT model’s distal segment of titin, $l^{2}$, can contribute to RFE when the titin-actin bond is formed and CE is lengthened beyond $l~_{s}^{M}$, the shortest CE length at which the PEVK-actin bond can form. In this work, we set $l~_{s}^{M}$ to be equal to the slack length of the CE’s force-length relation $l~_{s}^{PE}$ (see Table 1E and H). To incorporate the asymmetric length dependence of RFE observed by Hisey et al., 2009, we introduce a smooth step-up function

$$
u^{S}=\frac{1}{2}+\frac{1}{2}tanh⁡(\frac{l~^{M}−l~_{s}^{M}}{R})
$$

that transitions from zero to one as $l~^{M}$ extends beyond $l~_{s}^{M}$, where the sharpness of the transition is controlled by $R$. Similar to the experimental work of Hisey et al., 2009, active lengthening on the ascending limb will produce similar amounts of RFE since $l~_{s}^{M}<l_{o}^{M}$ and the titin-actin bond is prevented from forming below $l~_{s}^{M}$. In contrast, the amount of RFE on the descending limb increases with increasing stretch magnitudes since the titin-actin bond is able to form across the entire descending limb.

**Table 1.**
 The VEXAT and Hill model’s elastic-tendon cat soleus MTU parameters.The VEXAT model uses all of the Hill model’s parameters which are highlighted in grey. Short forms are used to indicate: length ‘len’, velocity ‘vel’, acceleration ‘acc’, half ‘h’, activation ‘act’, segment ‘seg’, threshold ‘thr’, and stiffness ‘stiff’. The letters ‘R’ or ‘H’ in front of a reference mean the data is from a rabbit or a human, otherwise the data is from cat soleus. References are in brackets and are coded in order of appearance as: ‘H02’ for Herzog and Leonard, 2002, ‘S82’ for Sacks and Roy, 1982, ‘S96’ for Scott et al., 1996, ‘H38’ for Hill, 1938, ‘S95’ for Scott and Loeb, 1995, ‘N96’ for Netti et al., 1996, ‘R99’ for Rassier et al., 1999, ‘K94’ for Kirsch et al., 1994, ‘P05’ for Prado et al., 2005, and ‘T98’ for Trombitás et al., 1998b. The letters following a reference indicate how the data was used to create the parameter: ‘C’ calculated, ‘F’ fit, ‘E’ estimated, or ‘S’ scaled. Most of the VEXAT model’s XE and titin parameters can be used as rough parameter guesses for other muscles because we have expressed these parameters in a normalized space: the values will scale appropriately with changes to $l_{o}^{M}$ and $f_{o}^{M}$. Titin’s force-length curves, however, should be updated if $N^{IgP}$, $N^{PEVK}$, or $N^{IgD}$ differ from the values shown below (see Appendix 2 for details). Note that the rigid-tendon cat soleus parameters differ from the table below because tendon elasticity affects the fitting of $k˜_{o}^{X}$, $\beta˜_{o}^{X}$, $f^{PE}$, $f^{1}(l~^{1})$, and $f^{2}(l~^{2})$. Finally, the parameters related to the compressive element (F), the XE (G), and titin (H and I) can be used as initial values when simulating the MTU’s other mammals. By making use of these defaults, the VEXAT model requires the same number of parameters as a Hill-type muscle model (A—E).


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th></th>
      <th>Value</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">A. Basic parameters</td>
    </tr>
    <tr>
      <td>Max iso force</td>
      <td>foM</td>
      <td>21.5N</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>Opt CE len</td>
      <td>loM</td>
      <td>42.9mm</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>Pen angle</td>
      <td>α</td>
      <td>7.00∘</td>
      <td>(S82)</td>
    </tr>
    <tr>
      <td>Act time const</td>
      <td>τA</td>
      <td>113ms</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>De-act time const</td>
      <td>τD</td>
      <td>142ms</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td colspan="4">B. Force-velocity relation: fV(v^M)</td>
    </tr>
    <tr>
      <td>Max shortening vel</td>
      <td>vmaxM</td>
      <td>4.65loMs</td>
      <td>(S96)F</td>
    </tr>
    <tr>
      <td>fV at −12vmaxM</td>
      <td>f~1V</td>
      <td>0.126foM</td>
      <td>(S96)F</td>
    </tr>
    <tr>
      <td>fV at v^M=+0</td>
      <td>f~2V</td>
      <td>1.40foM</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>fV at vmaxM</td>
      <td>f~3V</td>
      <td>1.55foM</td>
      <td>(H02)E</td>
    </tr>
    <tr>
      <td>vmaxM scaling</td>
      <td>sV</td>
      <td>0.950</td>
      <td>(H38)F</td>
    </tr>
    <tr>
      <td colspan="4">C. Tendon model: fT(l~T), Uk^T(l~T)</td>
    </tr>
    <tr>
      <td>Slack len</td>
      <td>lsT</td>
      <td>30.5mm</td>
      <td>(S95)S</td>
    </tr>
    <tr>
      <td>Stiffness</td>
      <td>k~oT</td>
      <td>30.0foMlsT</td>
      <td>(S95)</td>
    </tr>
    <tr>
      <td>Strain at foM</td>
      <td>eoT</td>
      <td>0.0458</td>
      <td>(S95)</td>
    </tr>
    <tr>
      <td>Toe force</td>
      <td>ftoeT</td>
      <td>23foM</td>
      <td>(S95)E</td>
    </tr>
    <tr>
      <td>Damping</td>
      <td>U</td>
      <td>0.057s</td>
      <td>R(N96)F</td>
    </tr>
    <tr>
      <td colspan="4">D. Active force-length relation: fL(l~M)</td>
    </tr>
    <tr>
      <td>Opt sarcomere len</td>
      <td>L∘M</td>
      <td>2.43μm</td>
      <td>(R99)</td>
    </tr>
    <tr>
      <td>Actin len</td>
      <td>L~A</td>
      <td>0.462loM</td>
      <td>(R99)</td>
    </tr>
    <tr>
      <td>Myosin h-len</td>
      <td>L~M</td>
      <td>0.330loM</td>
      <td>(R99)</td>
    </tr>
    <tr>
      <td>Myosin bare h-len</td>
      <td>L~B</td>
      <td>0.0175loM</td>
      <td>(R99)</td>
    </tr>
    <tr>
      <td>Offset</td>
      <td>ΔL</td>
      <td>−2k~oXloM</td>
      <td>C</td>
    </tr>
    <tr>
      <td colspan="4">E. Passive force-length relation: fPE(l~M)</td>
    </tr>
    <tr>
      <td>Slack len</td>
      <td>l~sPE</td>
      <td>0.872loM</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>Toe len</td>
      <td>l~toePE</td>
      <td>1.39loM</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>Toe force</td>
      <td>f~toePE</td>
      <td>1.00foM</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>Toe stiffness</td>
      <td>k~toePE</td>
      <td>3.88foMloM</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td colspan="4">F. Compressive force-length relation: fKE(l~M)</td>
    </tr>
    <tr>
      <td>Slack len</td>
      <td>l~sPE</td>
      <td>110loM</td>
      <td>E</td>
    </tr>
    <tr>
      <td>Toe len</td>
      <td>l~toePE</td>
      <td>0.00loM</td>
      <td>E</td>
    </tr>
    <tr>
      <td>Toe force</td>
      <td>f~toePE</td>
      <td>1.00foM</td>
      <td>E</td>
    </tr>
    <tr>
      <td colspan="4">G. XE viscoelastic model</td>
    </tr>
    <tr>
      <td>Stiffness</td>
      <td>k~oX</td>
      <td>49.1foMloM</td>
      <td>(K94)F:Figure 12</td>
    </tr>
    <tr>
      <td>Damping</td>
      <td>β~oX</td>
      <td>0.347foMloM/s</td>
      <td>(K94)F:Figure 12</td>
    </tr>
    <tr>
      <td>Acc. time const</td>
      <td>τS</td>
      <td>1.00e-3s</td>
      <td>(K94,H38)E</td>
    </tr>
    <tr>
      <td>Num acc damping</td>
      <td>D</td>
      <td>1.00</td>
      <td>(K94,H39)E</td>
    </tr>
    <tr>
      <td>Low act threshold</td>
      <td>aL</td>
      <td>0.0500</td>
      <td>(K94,H39)E</td>
    </tr>
    <tr>
      <td>Len tracking gain</td>
      <td>GL</td>
      <td>10001s</td>
      <td>(K94,H39)E</td>
    </tr>
    <tr>
      <td>Vel tracking gain</td>
      <td>GV</td>
      <td>1000</td>
      <td>(K94,H39)E</td>
    </tr>
    <tr>
      <td colspan="4">H. Titin &amp; ECM Parameters</td>
    </tr>
    <tr>
      <td>ECM fraction</td>
      <td>P</td>
      <td>56%</td>
      <td>R(P05)</td>
    </tr>
    <tr>
      <td>PEVK attach pt</td>
      <td>Q</td>
      <td>0.625</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>Z-line–T12 len</td>
      <td>L~T12</td>
      <td>0.0412loM</td>
      <td>H(T98)</td>
    </tr>
    <tr>
      <td>IgD rigid h-len</td>
      <td>L~IgD</td>
      <td>L~M</td>
      <td>(R99)</td>
    </tr>
    <tr>
      <td>No IgP domains</td>
      <td>NIgP</td>
      <td>60.5</td>
      <td>H(T98)S</td>
    </tr>
    <tr>
      <td>No PEVK residues</td>
      <td>NPEVK</td>
      <td>1934.7</td>
      <td>H(T98)S</td>
    </tr>
    <tr>
      <td>No IgD domains</td>
      <td>NIgD</td>
      <td>19.5</td>
      <td>H(T98)S</td>
    </tr>
    <tr>
      <td>Active damping</td>
      <td>βAPEVK</td>
      <td>71.9foMloM</td>
      <td>(H02)F</td>
    </tr>
    <tr>
      <td>Passive damping</td>
      <td>βPPEVK</td>
      <td>0.1foMloM</td>
      <td>E</td>
    </tr>
    <tr>
      <td>Length threshold</td>
      <td>l~sM</td>
      <td>12l~sPE</td>
      <td>E</td>
    </tr>
    <tr>
      <td>Act threshold</td>
      <td>A∘</td>
      <td>0.05</td>
      <td>E</td>
    </tr>
    <tr>
      <td>Step transition</td>
      <td>R</td>
      <td>0.01</td>
      <td>E</td>
    </tr>
    <tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td colspan="4">I. Titin’s force-length relations: f1(l~1) &amp; f2(l~2)</td>
    </tr>
    <tr>
      <td>f1(l~1) slack len</td>
      <td>l~S1</td>
      <td>0.0739loM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
    <tr>
      <td>f1(l~1) toe len</td>
      <td>l~toe1</td>
      <td>0.1590loM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
    <tr>
      <td>f1(l~1) toe force</td>
      <td>f~toe1</td>
      <td>(1−P)foM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
    <tr>
      <td>f1(l~1) toe stiff</td>
      <td>k~toe1</td>
      <td>5.17foMloM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
    <tr>
      <td>f2(l~2) slack len</td>
      <td>l~S2</td>
      <td>0.0454loM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
    <tr>
      <td>f2(l~2) toe len</td>
      <td>l~toe2</td>
      <td>0.0977loM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
    <tr>
      <td>f2(l~2) toe force</td>
      <td>f~toe2</td>
      <td>(1−P)foM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
    <tr>
      <td>f2(l~2) toe stiff</td>
      <td>k~toe2</td>
      <td>8.42foMloM</td>
      <td>H(T98)S, (H02)F</td>
    </tr>
  </tbody>
</table>

At very long CE lengths, the modeled titin-actin bond can literally slip off of the end of the actin filament (Figure 1A) when the distance between the Z-line and the bond, $l~^{1}+L~^{T12}$, exceeds the length of the actin filament, $L~^{A}$. To break the titin-actin bond at long CE lengths, we introduce a smooth step-down function

$$
u^{L}=\frac{1}{2}−\frac{1}{2}tanh(\frac{(l~^{1}+L~^{T12})−L~^{A}}{R})
$$

The step-down function $u^{L}$ transitions from one to zero when the titin-actin bond ($l~^{1}+L~^{T12}$) reaches $L~^{A}$, the end of the actin filament.

The strength of the titin-actin bond also appears to vary nonlinearly with activation. Fukutani and Herzog, 2018 observed that the absolute RFE magnitude produced by actively lengthened fibers is similar between normal and reduced contractile force states. Since the experiments of Fukutani and Herzog, 2018 were performed beyond the optimal CE length, titin could be contributing to the observed RFE as previously described. The consistent pattern of absolute RFE values observed by Fukutani and Herzog, 2018 could be produced if the titin-actin bond saturated at its maximum strength even at a reduced contractile force state. To saturate the titin-actin bond, we use a final smooth step function

$$
u^{A}=1−e^{−(\frac{a}{A_{∘}})^{2}}
$$

where $A_{∘}$ is the threshold activation level at which the bond saturates. While we model the strength of the titin-actin bond as being a function of activation, which is proportional Ca2+ concentration (Millar and Homsher, 1990), this is a mathematical convenience. The work of Leonard et al., 2010 makes it clear that both Ca2+ and crossbridge cycling are needed to allow titin to develop enhanced forces during active lengthening: no enhanced forces are observed in the presence of Ca2+ when crossbridge cycling is chemically inhibited. Putting this all together, the active damping acting between the titin and actin filaments is given by the product of $u^{A}u^{S}u^{L}\beta_{A}^{PEVK}$, where $\beta_{A}^{PEVK}$ is the maximum damping coefficient.

With a model of the titin-actin bond derived, we can focus on how the bond location moves in response to applied forces. Since we are ignoring the mass of the titin filament, the PEVK-attachment point is balanced by the forces applied to it and the viscous forces developed between titin and actin

$$
(u^{A}u^{S}u^{L}\beta_{A}^{PEVK}+\beta_{P}^{PEVK})v~^{1}=f^{1}(l~^{1})−f^{2}(l~^{2})
$$

due to the active ($u^{A}u^{S}u^{L}\beta_{A}^{PEVK}$) and a small amount of passive damping ($\beta_{P}^{PEVK}$). Since Equation 20 is linear in $v~^{1}$, we can solve directly for it

$$
v~^{1}=\frac{f^{2}(l~^{2})−f^{1}(l~^{1})}{u^{A}u^{S}u^{L}\beta_{A}^{PEVK}+\beta_{P}^{PEVK}}.
$$

The assumption of whether the tendon is rigid or elastic affects how the state derivative is evaluated and how expensive it is to compute. While all of the position dependent quantities can be evaluated using Equations 6–11 and the generalized positions, evaluating the generalized velocities of a rigid-tendon and elastic-tendon model differ substantially. The CE velocity $v^{M}$ and pennation angular velocity $\alpha˙$ of a rigid-tendon model can be evaluated directly given the path length, velocity, and the time derivatives of Equation 6 and Equation 8. After $v^{1}$ is evaluated using Equation 21, the velocities of the remaining segments can be evaluated using the time derivatives of Equations 9–11.

Evaluating the CE rate of lengthening, $v^{M}$, for an elastic-tendon muscle model is more involved. As is typical of lumped parameter muscle models (Zajac, 1989; Thelen, 2003; Millard et al., 2013), here we assume that difference in tension, $f~^{ϵ}$, between the CE and the tendon

$$
f~^{ϵ}=f~^{M}cos⁡\alpha−f^{T}≈0
$$

is negligible (see Appendix 9, Note 10). During our preliminary simulations, it became clear that treating the tendon as an idealized spring degraded the ability of the model to replicate the experiment of Kirsch et al., 1994 particularly at high frequencies. Kirsch et al., 1994 observed a linear increase in the gain and phase profile between the output force and the input perturbation applied to the muscle. This pattern in gain and phase shift can be accurately reproduced by a spring in parallel with a damper. Due to the way that impedance combines in series (see Appendix 9, Note 11), the models of both the CE and the tendon need to have parallel spring and damper elements so that the entire MTU, when linearized, appears to be a spring in parallel with a damping element. We model tendon force using a nonlinear spring and damper model

$$
f^{T}=f^{T}(l~^{T})+Uk^^{T}(l~^{T})v~^{T}
$$

where the damping coefficient $Uk^^{T}(l~^{T})$, is a linear scaling of the normalized tendon stiffness $k^^{T}$ by $U$, a constant scaling coefficient. We have chosen this specific damping model because it fits the data of Netti et al., 1996 and captures the structural coupling between tendon stiffness and damping (see Appendix 2.2 and Figure 1 for further details).

Now that all the terms in Equation 22 have been explicitly defined, we can use Equation 22 to solve for $v^{M}$. Equation 22 becomes linear in $v^{M}$ after substituting the force models described in Equation 23 and Equation 15, and the kinematic model described in Equation 8, Equation 9 and Equation 11 (along with the time derivatives of Equations 8–11). After some simplification we arrive at

$$
v~^{M}=\frac{(af^{L}(l~^{S}+L~^{M})(k~_{o}^{X}l~^{X}+\beta~_{o}^{X}v~^{S})+f^{2}(l~^{2})+f^{ECM}(l~^{ECM}))cos⁡\alpha−f^{KE}(l~^{M})−f^{T}(l~^{T})−\frac{Uk^^{T}(l~^{T})v^{P}}{l_{s}^{T}}}{\frac{−a\beta~_{o}^{X}f^{L}(l~^{S}+L~^{M})}{2l~^{M}}−\frac{(\beta~^{ϵ}+f^{ECM}(l~^{ECM}))cos⁡\alpha}{2l~^{M}}−\frac{Uk^^{T}(l~^{T})}{l_{s}^{T}cos⁡\alpha}}
$$

allowing us to evaluate the final state derivative in $x˙_$. During simulation the denominator of $v~^{M}$ will always be finite since $\beta~^{ϵ}>0$, and $\alpha<90^{∘}$ due to the compressive element. The evaluation of $x˙_$ in the VEXAT model is free of numerical singularities, giving it an advantage over a conventional Hill-type muscle models (Millard et al., 2013). In addition, the VEXAT’s $x˙_$ does not require iteration to numerically solve a root, giving it an advantage over a singularity-free formulation of the Hill model (Millard et al., 2013). As with previous models, initializing the model’s state is not trivial and required the derivation of a model-specific method (see Appendix 3 for details).

## Biological benchmark simulations

In order to evaluate the model, we have selected three experiments that capture the responses of active muscle to small, medium, and large length changes. The small (1–3.8% $l_{o}^{M}$) stochastic perturbation experiment of Kirsch et al., 1994 demonstrates that the impedance of muscle is well described by a stiff spring in parallel with a damper, and that the spring-damper coefficients vary linearly with active force. The active impedance of muscle is such a fundamental part of motor learning that the amount of impedance, as indicated by co-contraction, is used to define how much learning has actually taken place (Franklin et al., 2003; Franklin et al., 2008): co-contraction is high during initial learning, but decreases over time as a task becomes familiar. The active lengthening experiment of Herzog and Leonard, 2002 shows that modestly stretched (7–21% $l_{o}^{M}$) biological muscle has positive stiffness even on the descending limb of the active force-length curve ($l_{o}^{M}>1$). In contrast, a conventional Hill model (Zajac, 1989; Millard et al., 2013) can have negative stiffness on the descending limb of the active-force-length curve, a property that is both mechanically unstable and unrealistic. The final active lengthening experiment of Leonard et al., 2010 unequivocally demonstrates that the CE continues to develop active forces during extreme lengthening (329% $l_{o}^{M}$) which exceeds actin-myosin overlap. Active force development beyond actin-myosin overlap is made possible by titin, and its activation-dependent interaction with actin (Leonard et al., 2010). The biological benchmark simulations conclude with a replication of the force-velocity experiments of Hill, 1938 and the force-length experiments of Gordon et al., 1966.

The VEXAT model requires the architectural muscle parameters ($f_{o}^{M}$, $l_{o}^{M}$, $\alpha_{o}$, $v_{max}^{M}$, and $l_{s}^{T}$) needed by a conventional Hill-type muscle model as well as additional parameters. The additional parameters are needed for these component models: the compressive element (Equation 15 and Equation 24), the lumped viscoelastic XE (Equation 1 and Equation 2), XE-actin dynamics (Equation 16), the two-segment active titin model (Figure 3), titin-actin dynamics (Equation 21), and the tendon damping model (Equation 23). Fortunately, there is enough experimental data in the literature that values can be found, fitted, or estimated directly for our simulations of experiments on cat soleus (Table 1F.-I.), and rabbit psoas fibrils (see Appendix 2 and Appendix 8 for rabbit psoas fibril model parameters). The parameter values we have established for the cat soleus (Table 1F.-I.) can serve as initial values when modeling other mammalian MTU’s because these parameters have been normalized (by $f_{o}^{M}$, $l_{o}^{M}$, and $l_{s}^{T}$ where appropriate) and will scale appropriately given the architectural properties of a different MTU. By making use of these default values, the VEXAT model can be made to represent another MTU using exactly the same number of parameters as a Hill-type muscle model (Table 1A.-E.).

### Stochastic length perturbation experiments

In the in-situ experiment of Kirsch et al., 1994, the force response of a cat’s soleus muscle under constant stimulation was measured as its length was changed by small amounts. Kirsch et al., 1994 applied stochastic length perturbations (Figure 4A, blue line) to elicit force responses from the muscle (in this case a spring-damper Figure 4A, black line) across a broad range of frequencies (4–90 Hz) and across a range of small length perturbations (1–3.8% $l_{o}^{M}$). The resulting time-domain signals can be quite complicated (Figure 4A) but contain rich measurements of how muscle transforms changes in length into changes in force.

![Figure 4.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig4-v1.jpg)

**Figure 4.:** Evaluating a system’s gain and phase response begins by applying a pseudo-random input signal to the system and measuring its output (A). Both the input and output signals (A) are transformed into the frequency domain by expressing these signals as an equivalent sum of scaled and shifted sinusoids (simple example shown in B and C). Each individual input sinusoid is compared with the output sinusoid of the same frequency to evaluate how the system scales and shifts the input to the output (D). This process is repeated across all sinusoid pairs to produce a function that describes how an input sinusoid is scaled (E) and shifted (F) to an output sinusoid using only the measured data (A).

As long as muscle can be considered to be linear (a sinusoidal change in length produces a sinusoidal change in force), then system identification methods (Oppenheim et al., 1996; Koopmans, 1995) can be applied to extract a relationship between length $x(t)$ and force $y(t)$. We will give a brief overview of system identification methods here to make methods and results clearer. First, the time-domain signals ($x(t)$ and $y(t)$) are transformed into an equivalent representation in the frequency-domain ($X(s)$ and $Y(s)$) as a sum of scaled and shifted sine curves (Figure 4B and C) using a Fourier transform (Oppenheim et al., 1996). In the frequency domain, we identify an LTI system of best fit $H(s)$ that describes how muscle transforms changes in length into changes in force such that $Y(s)=H(s)X(s)$. Next, we evaluate how $H(s)$ scales the magnitude (gain) and shifts the timing (phase) of a sinusoid in $X(s)$ into a sinusoid of the same frequency in $Y(s)$ (Figure 4D). This process is repeated across all frequency-matched pairs of input and output sinusoids to build a function of how muscle scales (Figure 4E) and shifts (Figure 4F) input length sinusoids into output force sinusoids. The resulting transformation turns two complicated time-domain signals (Figure 4A) into a clear relationship in the frequency-domain that describes how muscle transforms length changes into force changes: a very slow (≈0 Hz) length change will result in an output force that is scaled by 4.5 and is in phase (Figure 4E and F), a 35 Hz sinusoidal length change will produce an output force that is scaled by 4.9 and leads the input signal by 24° (Figure 4E and F), and frequencies between 0 Hz and 35 Hz will be between these two signals in terms of scaling and phase. These patterns of gain and phase can be used to identify a network of spring-dampers that is equivalent to the underlying linear system (the system in Figure 4A, E and F is a 4.46 N/mm spring in parallel with a 0.0089 Ns/mm damper). Since experimental measurements often contain noise and small nonlinearities, the mathematical procedure used to estimate $H(s)$ and the corresponding gain and phase profiles is more elaborate than we have described (see Appendix 4 for details).

Kirsch et al., 1994 used system identification methods to identify LTI mechanical systems that best describes how muscle transforms input length waveforms to output force waveforms. The resulting LTI system, however, is only accurate when the relationship between input and output is approximately linear. Kirsch et al., 1994 used the coherence squared, $(C_{xy})^{2}$, between the input and output to evaluate the degree of linearity: $Y(s)$ is a linear transformation of $X(s)$ at frequencies in which $(C_{xy})^{2}$ is near one, while $Y(s)$ cannot be described as a linear function of $X(s)$ at frequencies in which $(C_{xy})^{2}$ approaches zero. By calculating $(C_{xy})^{2}$ between the length perturbation and force waveforms, Kirsch et al., 1994 identified the bandwidth in which the muscle’s response is approximately linear. Kirsch et al., 1994 set the lower frequency of this band to 4 Hz, and Figure 3 of Kirsch et al., 1994 suggests that this corresponds to $(C_{xy})^{2}\geq0.67$ though the threshold for $(C_{xy})^{2}$ is not reported. The upper frequency of this band was set to the cutoff frequency of the low-pass filter applied to the input (15, 35, or 90 Hz). Within this bandwidth, Kirsch et al., 1994 compared the response of the specimen to several candidate models and found that a parallel spring-damper fit the muscle’s frequency response best. Next, Kirsch et al., 1994 evaluated the stiffness and damping coefficients that best fit the muscle’s frequency response. Finally, Kirsch et al., 1994 evaluated how much of the muscle’s time-domain response was captured by the spring-damper of best fit by evaluating the variance-accounted-for (VAF) between the two time-domain signals

$$
VAF(f^{KD},f^{EXP})=\frac{\sigma^{2}(f^{EXP})−\sigma^{2}(f^{KD}−f^{EXP})}{\sigma^{2}(f^{EXP})}.
$$

Astonishingly, Kirsch et al., 1994 found that a spring-damper of best fit has a VAF of between 78% and 99% (see Appendix 9, Note 12) when compared to the experimentally measured forces $f^{EXP}$. By repeating this experiment over a variety of stimulation levels (using both electrical stimulation and the crossed-extension reﬂex) Kirsch et al., 1994 showed that these stiffness and damping coefficients vary linearly with the active force developed by the muscle. Furthermore, Kirsch et al., 1994 repeated the experiment using perturbations that had a variety of lengths (0.4 mm, 0.8 mm, and 1.6 mm) and bandwidths (15 Hz, 35 Hz, and 90 Hz) and observed a peculiar quality of muscle: the damping coefficient of best fit increases as the bandwidth of the perturbation decreases (see Figures 3 and 10 of Kirsch et al., 1994 for details). Here, we simulate the experiment of Kirsch et al., 1994 to determine, first, the VAF of the VEXAT model and the Hill model in comparison to a spring-damper of best fit; second, to compare the gain and phase response of the models to biological muscle; and ﬁnally, to see if the spring-damper coefficients of best ﬁt for both models increase with active force in a manner that is similar to the cat soleus that Kirsch et al., 1994 studied.

To simulate the experiments of Kirsch et al., 1994 we begin by creating the 9 stochastic perturbation waveforms used in the experiment that vary in perturbation amplitude (0.4 mm, 0.8mm, and 1.6 mm) and bandwidth (0–15 Hz, 0–35 Hz, and 0–90 Hz) (see Appendix 9, Note 13). The waveform is created using a vector that is composed of random numbers with a range of [-1,1] that begins and ends with a series of zero-valued padding points. Next, a forward pass of a second-order Butterworth ﬁlter is applied to the waveform and ﬁnally the signal is scaled to the appropriate amplitude (Figure 5). The muscle model is then activated until it develops a constant tension at a length of $l_{o}^{M}$. The musculotendon unit is then simulated as the length is varied using the previously constructed waveforms while activation is held constant. To see how impedance varies with active force, we repeated these simulations at ten evenly spaced tensions from 2.5N to 11.5N. Ninety simulations are required to evaluate the nine different perturbation waveforms at each of the ten tension levels. The time-domain length perturbations and force responses of the modeled muscles are used to evaluate the coherence squared of the signal, gain response, and phase responses of the models in the frequency-domain. Since the response of the models might be more nonlinear than biological muscle, we select a bandwidth that meets $(C_{xy})^{2}>0.67$ but otherwise follows the bandwidths analyzed by Kirsch et al., 1994 (see Appendix 4 for details).

![Figure 5.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig5-v1.jpg)

**Figure 5.:** The perturbation waveforms are constructed by generating a series of pseudo-random numbers, padding the ends with zeros, by ﬁltering the signal using a 2nd order low-pass ﬁlter (wave forms with –3 dB cut-off frequencies of 90 Hz, 35 Hz, and 15 Hz appear in A) and ﬁnally by scaling the range to the desired limit (1.6 mm in A). Although the power spectrum of the resulting signals is highly variable, the ﬁlter ensures that the frequencies beyond the –3 dB point have less than half their original power (B).

When coupled with an elastic-tendon, the 15 Hz perturbations show that neither model can match the VAF of the analysis of Kirsch et al., 1994 (compare Figure 6A to G), while at 90 Hz the VEXAT model reaches a VAF of 89% (Figure 6D) which is within the range of 78–99% reported by Kirsch et al., 1994. In contrast, the Hill model’s VAF at 90 Hz remains low at 58% (Figure 6J). While the VEXAT model has a gain proﬁle in the frequency-domain that closer to the data of Kirsch et al., 1994 than the Hill model (compare Figure 6B to H and E to K), both models have a greater phase shift than the data of Kirsch et al., 1994 at low frequencies (compare Figure 6C to I and F to L). The phase response of the VEXAT model to the 90 Hz perturbation (Figure 6F) shows the consequences of Equation 16: at low frequencies the phase response of the VEXAT model is similar to that of the Hill model, while at higher frequencies the model’s response becomes similar to a spring-damper. This frequency dependent response is a consequence of the ﬁrst term in Equation 16: the value of $\tau^{S}$ causes the response of the model to be similar to a Hill model at lower frequencies and mimic a spring-damper at higher frequencies. Both models show the same perturbation-dependent phase-response, as the damping coefficient of best ﬁt increases as the perturbation bandwidth decreases: compare the damping coefficient of best ﬁt for the 15 Hz and 90 Hz proﬁles for the VEXAT model (listed on Figure 6A. and D.) and the Hill model (listed on Figure 6G. and J., respectively).

![Figure 6.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig6-v1.jpg)

**Figure 6.:** The 15 Hz perturbations show that the VEXAT model’s performance is mixed: in the time-domain (A.) the VAF is lower than the 78–99% analyzed by Kirsch et al., 1994; the gain response (B.) follows the proﬁle in Figure 3 of Kirsch et al., 1994, while the phase response differs (C.). The response of the VEXAT model to the 90 Hz perturbations is much better: a VAF of 91% is reached in the time-domain (D.), the gain response follows the response of the cat soleus analyzed by Kirsch et al., 1994, while the phase-response follows biological muscle closely for frequencies higher than 30 Hz. Although the Hill’s time-domain response to the 15 Hz signal has a higher VAF than the VEXAT model (G.), the RMSE of the Hill model’s gain response (H.) and phase response (I.) shows it to be more in error than the VEXAT model. While the VEXAT model’s response improved in response to the 90 Hz perturbation, the Hill model’s response does not: the VAF of the time-domain response remains low (J.), neither the gain (K.) nor phase responses (L.) follow the data of Kirsch et al., 1994. Note that the Hill model’s 90 Hz response was so nonlinear that the lowest frequency analyzed had to be raised from 4 Hz to 7 Hz to satisfy the criteria that $(C_{xy})^{2}\geq0.67$.

The closeness of each model’s response to the spring-damper of best ﬁt changes when a rigid-tendon is used instead of an elastic-tendon. While the VEXAT model’s response to the 15 Hz and 90 Hz perturbations improves slightly (compare Figure 6A–F to Figure 1A–F in Appendix 6), the response of the Hill model to the 15 Hz perturbation changes dramatically with the time-domain VAF rising from 55% to 85% (compare Figure 6G–L to Figure 1G–L in Appendix 6). Although the Hill model’s VAF in response to the 15 Hz perturbation improved, the frequency response contains mixed results: the rigid-tendon Hill model’s gain response is better (Figure 1H in Appendix 6), while the phase response is worse in comparison to the elastic-tendon Hill model. While the rigid-tendon Hill model produces a better time-domain response to the 15 Hz perturbation than the elastic-tendon Hill model, this improvement has been made with a larger phase shift between force and length than biological muscle (Kirsch et al., 1994).

The gain and phase proﬁles of both models deviate from the spring-damper of best ﬁt due to the presence of nonlinearities, even for small perturbations. Some of the VEXAT model’s nonlinearities in this experiment come from the tendon model (compare Figure 6A–F to Figure 1A–F in Appendix 6), since the response of the VEXAT model with a rigid-tendon stays closer to the spring-damper of best ﬁt. The Hill model’s nonlinearities originate from the underlying expressions for stiffness and damping of the Hill model, which are particularly nonlinear with a rigid-tendon model (Figure 1G–L in Appendix 6). The stiffness of a Hill model’s CE

$$
k^{M}=f_{o}^{M}(a\frac{df^{L}}{dl^{M}}f^{V}+\frac{df^{PE}}{dl^{M}})
$$

is heavily inﬂuenced by the partial derivative of $\frac{df^{L}}{dl^{M}}$ which has a region of negative stiffness. Although $\frac{df^{PE}}{dl^{M}}$ is well approximated as being linear for small length changes, $\frac{df^{L}}{dl^{M}}$ changes sign across $l_{o}^{M}$. The damping of a Hill model’s CE

$$
\beta^{M}=f_{o}^{M}(af^{L}\frac{df^{V}}{dv^{M}})
$$

also suffers from high degrees of nonlinearity for small perturbations about $v^{M}=0$ since the slope of $\frac{df^{V}}{dv^{M}}$ is positive and large when shortening, and positive and small when lengthening (Figure 2B). While Equation 26 and Equation 27 are mathematically correct, the negative stiffness and wide ranging damping values predicted by these equations do not match experimental data (Kirsch et al., 1994). In contrast, the stiffness

$$
k~^{M}=\frac{ak~_{o}^{X}f^{L}(l~^{S}+L~^{M})}{2}+\frac{df^{2}(l~^{2})}{dl^{2}}\frac{1}{2}+\frac{df^{ECM}(l~^{ECM})}{dl^{ECM}}\frac{1}{2}
$$

and damping

$$
\beta~^{M}=af^{L}(l~^{S}+L~^{M})(\beta~_{o}^{X}\frac{dv~^{X}}{dv~^{M}})+\beta~^{ϵ}
$$

of the VEXAT’s CE do not change so drastically because these terms do not depend on the slope of the force-length relation, or the force-velocity relation (see Appendix 2.5 for derivation).

By repeating the stochastic perturbation experiments across a range of isometric forces, Kirsch et al., 1994 were able to show that the stiffness and damping of a muscle varies linearly with the active tension it develops (see Figure 12 of Kirsch et al., 1994). We have repeated our simulations of the experiments of Kirsch et al., 1994 at ten nominal forces (spaced evenly between 2.5 N and 11.5 N) and compared how the VEXAT model and the Hill model’s stiffness and damping coefficients (Figure 7) compare to Figure 12 of Kirsch et al., 1994. The stiffness and damping proﬁle of the VEXAT model deviates a little from the data of Kirsch et al., 1994 because XE’s dynamics at 35 Hz are still inﬂuenced by the Hill model embedded in Equation 16 (see Appendix 2.5). Despite this, the VEXAT model develops similar stiffness and damping proﬁle with either a viscoelastic-tendon (Figure 7A and B) or a rigid-tendon (Figure 7C and D). In contrast, when the Hill model is coupled with an elastic-tendon both its stiffness and damping are larger than what is reported by Kirsch et al., 1994 at the higher tensions (Figure 7A and B). This pattern changes when simulating a Hill model with a rigid-tendon: the model’s stiffness is slightly negative (Figure 7C), while the model’s ﬁnal damping coefficient is nearly three times the value measured by Kirsch et al., 1994 (Figure 7D). Though a negative stiffness may seem surprising, Equation 26 shows a negative stiffness is possible at the nominal CE length of these simulations: just past $l_{o}^{M}$ the slope of the active force-length curve is negative and the slope of the passive force-length curve is negligible. The tendon model also affects the VAF of the Hill model to a large degree: the elastic-tendon Hill model has a low VAF 30–51% (Figure 7A & B) while the rigid-tendon Hill model has a much higher VAF of 86%. Although the VAF of the rigid-tendon Hill model is acceptable, these forces are being generated in a completely different manner than those obtained from biological muscle, as the data of Kirsch et al., 1994 indicate (Figure 7C and D).

![Figure 7.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig7-v1.jpg)

**Figure 7.:** When coupled with an elastic-tendon, the stiffness (A) and damping (B) coefficients of best ﬁt of both the VEXAT model and a Hill model increase with the tension developed by the MTU. However, both the stiffness and damping of the elastic-tendon Hill model are larger than Kirsch et al.’s coefficients (from Figure 12 of Kirsch et al., 1994), particularly at higher tensions. When coupled with rigid-tendon the stiffness (C) and damping (D) coefficients of the VEXAT model remain similar, as the values for $k_{o}^{X}$ and $\beta_{o}^{X}$ have been calculated to take the tendon model into account (see Appendix 2.5 for details). In contrast, the stiffness and damping coefficients of the rigid-tendon Hill model differ dramatically from the elastic-tendon Hill model: while the elastic-tendon Hill model is too stiff and damped, the rigid-tendon Hill model is not stiff enough (compare A. to C.) and far too damped (compare B. to D.). Coupling the Hill model with a rigid-tendon increases the VAF from 30–51% to 86% but this improved accuracy is made using stiffness and damping that deviates from that of biological muscle (Kirsch et al., 1994).

When the VAF of the VEXAT and Hill model is evaluated across a range of nominal tensions (ten values from 2.5 to 11.5 N), frequencies (15 Hz, 35 Hz, and 90 Hz), amplitudes (0.4 mm, 0.8 mm, and 1.6 mm), and tendon types (rigid and elastic) two things are clear: ﬁrst, that the VEXAT model’s 64–100% VAF is close to the 78–99% VAF reported by Kirsch et al., 1994 while the Hill model’s 28–95% VAF differs (Figure 8); and second, that there are systematic variations in VAF, stiffness, and damping across the different perturbation magnitudes and frequencies (see Appendix 5—table 1 and Appendix 5—table 2). Both models produce worse VAF values when coupled with an elastic-tendon (Figure 8A, B and C), although the Hill model is affected most: the mean VAF of the elastic-tendon Hill model is 67% lower than the mean VAF of the rigid-tendon model for the 0.4 mm 15 Hz perturbations (Figure 8A). While the VEXAT model’s lowest VAF occurs in response to the low frequency perturbations (Figure 8A) with both rigid and elastic-tendons, the Hill model’s lowest VAF varies with both tendon type and frequency: the rigid-tendon Hill model has its lowest VAF in response to the 1.6 mm 90 Hz perturbations (Figure 8C) while the elastic-tendon Hill model has its lowest VAF in response to the 0.4 mm 15 Hz perturbations (Figure 8A). It is unclear if biological muscle displays systematic shifts in VAF since Kirsch et al., 1994 did not report the VAF of each trial.

![Figure 8.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig8-v1.jpg)

**Figure 8.:** Kirsch et al., 1994 noted that the spring-damper model of best ﬁt has a VAF of between 78–99% across all experiments. We have repeated the perturbation experiments to evaluate the VAF across a range of conditions: two different tendon models, three perturbation bandwidths (15 Hz, 35 Hz, and 90 Hz), three perturbation magnitudes (0.4 mm, 0.8 mm, and 1.6 mm), and ten nominal force values (spaced evenly between 2.5 N and 11.5 N). Each bar in the plot shows the mean VAF across all 10 nominal force values, with the whiskers extending to the minimum and maximum value that occurred in each set. The mean VAF of the VEXAT model changes by up to 36% depending on the condition, with the lowest mean VAF occurring in response to the 0.4mm 15 Hz perturbation with an elastic-tendon (A), and the highest mean VAF occurring in response to the 90 Hz perturbations with the rigid-tendon (C). In contrast, the mean VAF of the Hill model varies by up to 67% depending on the condition, with the lowest VAF occurring in the 15 Hz 0.4 mm trial with the elastic-tendon (A), and the highest value VAF occurring in the 15 Hz 0.4 mm trial with the rigid-tendon (A).

### Active lengthening on the descending limb

We now turn our attention to the active lengthening in-situ experiments of Herzog and Leonard, 2002. During these experiments, cat soleus muscles were actively lengthened by modest amounts (7–21% $l_{o}^{M}$) starting on the descending limb of the active-force-length curve ($l^{M}/l_{o}^{M}>1$ in Figure 2A). This starting point was chosen speciﬁcally because the stiffness of a Hill model may actually change sign and become negative because of the inﬂuence of the active-force-length curve on $k^{M}$ as shown in Equation 26 as $l^{M}$ extends beyond $l_{o}^{M}$. The experiment of Herzog and Leonard, 2002 is important for showing that biological muscle does not exhibit negative stiffness on the descending limb of the active-force-length curve. In addition, this experiment also highlights the slow recovery of the muscle’s force after stretching has ceased, and the phenomena of passive force enhancement after stimulation is removed. Here we will examine the 9 mm/s ramp experiment in detail because the simulations of the 3 mm/s and 27 mm/s ramp experiments produces similar stereotypical patterns (see Appendix 7 for details).

When the active lengthening experiment of Herzog and Leonard, 2002 is simulated (Figure 9A), both models produce a force transient initially (Figure 9B), but for different reasons. The VEXAT model’s transient is created when the lumped crossbridge spring (the $k~_{o}^{X}l~^{X}$ term in Equation 15) is stretched. In contrast, the Hill model’s transient is produced, not by spring forces, but by damping produced by the force-velocity curve as shown in Equation 26.

![Figure 9.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig9-v1.jpg)

**Figure 9.:** Herzog and Leonard, 2002 actively lengthened (A) cat soleus muscles on the descending limb of the force-length curve (where $l~^{M}>1$ in Figure 2A) and measured the force response of the MTU (B). After the initial transient at 2.4s the Hill model’s output force drops (B) because of the small region of negative stiffness (C) created by the force-length curve. In contrast, the VEXAT model develops steadily increasing forces between 2.4 and 3.4s and has a consistent level of stiffness (C) and damping (D).

After the initial force transient, the response of the two models diverges (Figure 9B): the VEXAT model continues to develop increased tension as it is lengthened, while the Hill model’s tension drops before recovering. The VEXAT model’s continued increase in force is due to the titin model: when activated, a section of titin’s PEVK region remains approximately ﬁxed to the actin element (Figure 1C). As a result, the $l^{2}$ element (composed of part of PEVK segment and the distal Ig segment) continues to stretch and generates higher forces than it would if the muscle were being passively stretched. While both the elastic and rigid-tendon versions of the VEXAT model produce the same stereotypical ramp-lengthening response (Figure 9B), the rigid-tendon model develops slightly more tension because the strain of the MTU is solely borne by the CE.

In contrast, the Hill model develops less force during lengthening when it enters a small region of negative stiffness (Figure 9B and C) because the passive-force-length curve is too compliant to compensate for the negative slope of the active force-length curve. Similarly, the damping coefficient of the Hill model drops substantially during lengthening (Figure 9D). Equation 27 and Figure 2B shows the reason that damping drops during lengthening: $df^{V}/dv^{M}$, the slope of the line in Fig. Figure 2B, is quite large when the muscle is isometric and becomes quite small as the rate of lengthening increases.

After the ramp stretch is completed (at time 3.4 s in Figure 9B), the tension developed by the cat soleus recovers slowly, following a proﬁle that looks strikingly like a ﬁrst-order decay. The large damping coefficient acting between the titin-actin bond slows the force recovery of the VEXAT model. We have tuned the value of $\beta_{A}^{PEVK}$ to $71.9f_{o}^{M}/(l_{o}^{M}/s)$ for the elastic-tendon model, and $77.7f_{o}^{M}/(l_{o}^{M}/s)$ for the rigid-tendon model, to match the rate of force decay of the cat soleus in the data of Herzog and Leonard, 2002. The Hill model, in contrast, recovers to its isometric value quite rapidly. Since the Hill model’s force enhancement during lengthening is a function of the rate of lengthening, when the lengthening ceases, so too does the force enhancement.

Once activation is allowed to return to zero, the data of Herzog and Leonard, 2002 shows that the cat soleus continues to develop a tension that is $Δf_{B}$ above passive levels (Figure 9B for $t>8.5s$). The force $Δf_{B}$ is known as passive force enhancement, and is suspected to be caused by titin binding to actin (Herzog, 2019). Since we model titin-actin forces using an activation-dependent damper, when activation goes to zero our titin model becomes unbound from actin. As such, both our model and a Hill model remain $Δf_{B}$ below the experimental data of Herzog and Leonard (Figure 9B) after lengthening and activation have ceased.

### Active lengthening beyond actin-myosin overlap

One of the great challenges that remains is to decompose how much tension is developed by titin (Figure 1C) separately from myosin (Figure 1B) in an active sarcomere. The active-lengthening experiment of Leonard et al., 2010 provides some insight into this force distribution problem because they recorded active forces both within and far beyond actin-myosin overlap. The data of Leonard et al., 2010 shows that active force continues to develop linearly during lengthening, beyond actin-myosin overlap, until mechanical failure. When activated and lengthened, the myoﬁbrils failed at a length of $3.38l_{o}^{M}$ and force of $5.14f_{o}^{M}$, on average. In contrast, during passive lengthening myoﬁbrils failed at a much shorter length of $2.86l_{o}^{M}$ with a dramatically lower tension of of $1.31f_{o}^{M}$. To show that the extraordinary forces beyond actin-myosin overlap can be ascribed to titin, Leonard et al., 2010 repeated the experiment but deleted titin using trypsin: the titin-deleted myoﬁbrils failed at short lengths and insigniﬁcant stresses. Using the titin model of Equation 20 (Figure 1A) as an interpretive lens, the huge forces developed during active lengthening would be created when titin is bound to actin leaving the distal segment of titin to take up all of the strain. Conversely, our titin model would produce lower forces during passive lengthening because the proximal Ig, PEVK, and distal Ig regions would all be lengthening together (Figure 3A).

Since the experiment of Leonard et al., 2010 was performed on skinned rabbit myoﬁbrils and not on whole muscle, both the VEXAT and Hill models had to be adjusted prior to simulation (see Appendix 8 for parameter values). To simulate a rabbit myoﬁbril we created a force-length curve (Rassier et al., 1999) consistent with the ﬁlament lengths of rabbit skeletal muscle (Higuchi et al., 1995; 1.12 µm actin, 1.63 µm myosin, and 0.07 µm z-line width) and ﬁt the force-length relations of the two titin segments to be consistent with the structure measured by Prado et al., 2005 of rabbit psoas titin consisting of a 70–30% mix of a 3300kD and a 3400kD titin isoform (see Appendix 2.4 for ﬁtting details and Appendix 8 for parameter values). Since this is a simulation of a ﬁbril, we used a rigid-tendon of zero length (equivalent to ignoring the tendon), and set the pennation angle to zero.

As mentioned in the ‘Model’ section, because this experiment includes extreme lengths, we consider two different force-length relations for each segment of titin (Figure 10A): a linear extrapolation, and an extension that follows the WLC model. While both versions of the titin model are identical up to $l~_{toe}^{PE}$, beyond $l~_{toe}^{PE}$ the WLC model continues to develop increasingly large forces until all of the Ig domains and PEVK residues have been unfolded and the segments of titin reach a physical singularity: at this point the Ig domains and PEVK residues cannot be elongated any further without breaking molecular bonds (see Appendix 2.4 for details). Our preliminary simulations indicated that the linear titin model’s titin-actin bond was not strong enough to support large tensions, and so we increased the value of $\beta_{A}^{PEVK}$ from 71.9 to 975 (compare Table 1H and Appendix 8—table 1G).

![Figure 10.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig10-v1.jpg)

**Figure 10.:** We consider two different versions of the force-length relation for each titin segment of the VEXAT model (A): a linear extrapolation, and a WLC model extrapolation. Leonard et al., 2010 observed that active myoﬁbrils continue to develop increasing amounts of tension beyond actin-myosin overlap (B, grey lines with ±1 standard deviation shown). When this experiment is replicated using the VEXAT model (B, blue & magenta lines) and a Hill model (C red lines), only the VEXAT model with the linear extrapolated titin model is able to replicate the experiment with the titin-actin bond slipping off of the actin ﬁlament at 3.38 $l_{o}^{M}$.

The Hill model was similarly modiﬁed, with the pennation angle set to zero and coupled with a rigid-tendon of zero length. Since the Hill model lacks an ECM element the passive-force-length curve was instead ﬁtted to match the passive forces produced in the data of Leonard et al., 2010. No adjustments were made to the active elements of the Hill model.

When the slow active stretch (0.1 µm/sarcomere/s) of the experiment of Leonard et al., 2010 is simulated, only the VEXAT model with the linear titin element can match the experimental data of Leonard et al., 2010 (Figure 10B). The Hill model cannot produce active force for lengths greater than $1.62l_{o}^{M}$ since the active force-length curve goes to zero (Figure 2A and Figure 10B) and the model lacks any element capable of producing force beyond this length. In contrast, the linear titin model continues to develop active force until a length of 3.38 $l_{o}^{M}$ is reached, at which point the titin-actin bond is pulled off the end of the actin ﬁlament and the active force is reduced to its passive value.

The WLC titin model is not able to reach the extreme lengths observed by Leonard et al., 2010. The distal segment of the WLC titin model approaches its contour length early in the simulation and ensures that the the titin-actin bond is dragged off the end of the actin ﬁlament at 1.99 $l_{o}^{M}$ (Figure 10B). After 1.99 $l_{o}^{M}$ (Figure 10B), the tension of the WLC titin model drops to its passive value but continues to increase until the contour lengths of all of the segments of titin are reached at 2.32 $l_{o}^{M}$. Comparing the response of the linear model to the WLC titin model two things are clear: the linear titin model more faithfully follows the data of Leonard et al., 2010, but does so with titin segment lengths that exceed the maximum contour length expected for the isoform of titin in a rabbit myoﬁbril.

This simulation has also uncovered a surprising fact: the myoﬁbrils in the experiments of Leonard et al., 2010 do not fail at 2.32 $l_{o}^{M}$, as would be expected by the WLC model of titin, but instead reach much greater lengths (Figure 10B). Physically, it may be possible for a rabbit myoﬁbril to reach these lengths (without exceeding the contour lengths of the proximal Ig, PEVK, and distal Ig segments) if the bond between the distal segment of titin and myosin breaks down. This would allow the large Ig segment, that is normally bound to myosin, to uncoil and continue to develop the forces observed by Leonard et al., 2010. Unfortunately the mechanism which allowed the samples in Leonard et al.’s experiments to develop tension beyond titin’s contour length remains unknown.

### Force-length and force-velocity

Although the active portion of the Hill model is embedded in Equation 16, it is not clear if the VEXAT model can still replicate force-velocity experiments of Hill, 1938 and the force-length experiments of Gordon et al., 1966. Here, we simulate both of these experiments using the cat soleus model that we have used for the simulations described in the ‘Model’ section (‘Stochastic length perturbation experiments’) and compare the results to the force-length and force-velocity curves that are used in the Hill model and in Equation 16 of the VEXAT model.

The force-velocity experiment of Hill, 1938 is simulated by activating the model, and then by changing its length to follow a shortening ramp and a lengthening ramp. During shortening experiments, the CE shortens from $1.1l_{o}^{M}$ to $0.9l_{o}^{M}$ with the measurement of active muscle force is made at $l_{o}^{M}$. Lengthening experiments are similarly made by measuring muscle force mid-way through a ramp stretch that begins at $0.9l_{o}^{M}$ and ends at $1.1l_{o}^{M}$. When an elastic-tendon model is used, we carefully evaluate initial and terminal path lengths to accommodate for the stretch of the tendon so that the CE still shortens from $1.1l_{o}^{M}$ to $0.9l_{o}^{M}$ and lengthens from $0.9l_{o}^{M}$ to $1.1l_{o}^{M}$.

The VEXAT model produces forces that differ slightly from the $f^{V}$ that is embedded in Equation 16 while the Hill model reproduces the curve (Figure 11). The maximum shortening velocity of the VEXAT model is slightly weaker than the embedded curve due to the series viscoelasticity of the XE element. Although the model can be made to converge to the $f^{V}$ curve more rapidly by decreasing $\tau^{S}$ this has the undesirable consequence of degrading the low-frequency response of the model when simulating the experiments of Kirsch et al., 1994 (particularly Figure 6C., and F.). These small differences can be effectively removed by scaling $v_{max}^{M}$ by $s^{V}$ (Figure 11A has $s^{V}=0.95$) to accommodate for the small decrease in force caused by the viscoelastic XE element.

![Figure 11.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig11-v1.jpg)

**Figure 11.:** When the experiments of Hill, 1938 are simulated (A), the VEXAT model produces a force-velocity proﬁle (blue dots) that approaches zero more rapidly during shortening than the embedded proﬁle $f^{V}(⋅)$ (red lines). By scaling $v_{max}^{M}$ by 0.95 the VEXAT model (magenta squares) is able to closely follow the force-velocity curve of the Hill model. While the force-velocity curves between the two models are similar, the time-domain force response of the two models differs substantially (B). The rigid-tendon Hill model exhibits a sharp nonlinear change in force at the beginning (0.1 s) and ending (0.21 s) of the ramp stretch.

The force-length experiments of Gordon et al., 1966 were simulated by ﬁrst passively lengthening the CE, and next by measuring the active force developed by the CE at a series of ﬁxed lengths. Prior to activation, the passive CE was simulated for a brief period of time in a passive state to reduce any history effects due to the active titin element. To be consistent with the experiment of Gordon et al., 1966, we subtracted off the passive force from the active force before producing the active-force-length proﬁle.

The simulation of Gordon et al., 1966 shows that the VEXAT model (Figure 12A, blue dots) produces a force-length proﬁle that is shifted to the right of the Hill model (Figure 12A, red line) due to the series elasticity introduced by the XE. We can solve for the size of this rightwards shift by noting that Equation 16 will drive the $l~^{S}$ to a length such that the isometric force developed by the XE is equal to that of the embedded Hill model

$$
af^{L}(l~^{S}+L~^{M})k~_{o}^{X}l~^{X}=af^{L}(l~^{S}+L~^{M})
$$

allowing us to solve for

$$
l~^{X}=\frac{1}{k~_{o}^{X}}
$$

the isometric strain of the XE. Since there are two viscoelastic XE elements per CE, the VEXAT model has an active force-length characteristic that shifted to the right of the embedded $f^{L}$ curve by a constant $\frac{2}{k~_{o}^{X}}$. This shift, $Δ^{L}$, can be calibrated out of the model (Figure 12A, magenta squares) by adjusting the $f^{L}(⋅)$ curve so that it is $\frac{2}{k~_{o}^{X}}$ to the left of its normal position. Note that all simulations described in the previous sections made use of the VEXAT model with the calibrated force-length relation and the calibrated force-velocity relation.

![Figure 12.](https://cdn.elifesciences.org/articles/88344/elife-88344-fig12-v1.jpg)

**Figure 12.:** When the passive and active force-length experiments of Gordon et al., 1966 are simulated, the VEXAT model (blue dots) and the Hill model (red lines) produce slightly different force-length curves (A) and force responses in the time-domain (B). The VEXAT model produces a right shifted active force-length curve, when compared to the Hill model due to the series elasticity of the XE element. By shifting the underlying curve by $\frac{2}{k_{o}^{X}}$ to the left the VEXAT model (magenta squares) can be made to exactly match the force-length characteristic of the Hill model.

## Discussion

A muscle model is deﬁned by the experiments it can replicate and the mechanisms it embodies. We have developed the VEXAT muscle model to replicate the force response of muscle to a wide variety of perturbations (Kirsch et al., 1994; Herzog and Leonard, 2002; Leonard et al., 2010) while also retaining the ability to reproduce the force-velocity experiment of Hill, 1938 and the force-length experiment of Gordon et al., 1966. The model we have developed uses two mechanisms to capture the force response of muscle over a large variety of time and length scales: ﬁrst, a viscoelastic crossbridge element that over brief time-scales appears as a spring-damper, and at longer time-scales mimics a Hill-model; second, a titin element that is capable of developing active force during large stretches.

The viscoelastic crossbridge and titin elements we have developed introduce a number of assumptions into the model. While there is evidence that the activation-dependent stiffness of muscle originates primarily from the stiffness of the attached crossbridges (Veigel et al., 1998), the origins of the activation-dependent damping observed by Kirsch et al., 1994 have not yet been established. We assumed that, since the damping observed by Kirsch et al., 1994 varies linearly with activation, the damping originates from the attached crossbridges. Whether this damping is intrinsic or is due to some other factor remains to be established. Next, we have also assumed that the force developed by the XE converges to a Hill model (Millard et al., 2013) given enough time (Equation 16). A recent experiment (see Figure 7 of Tomalka et al., 2021) suggests the force developed by the XE might decrease during lengthening rather than increasing as is typical of a Hill model (Millard et al., 2013). If the observations of Tomalka et al., 2021 can be replicated, the VEXAT model will need to be adjusted so that the XE element develops less force during active lengthening while the active-titin element develops more force. Finally, we have assumed that actin-myosin sliding acceleration (due to crossbridge cycling) occurs when there is a force imbalance between the external force applied to the XE and the internal force developed by the XE as shown in Equation 16. This assumption is a departure from previous models: Hill-type models (Zajac, 1989; Millard et al., 2013) assume that the tension applied to the muscle instantaneously affects the actin-myosin sliding velocity; Huxley models (Huxley, 1957) assume that the actin-myosin sliding velocity directly affects the rate of attachment and detachment of crossbridges.

The active titin model that we have developed makes assumptions similar to Rode et al., 2009 and Schappacher-Tilp et al., 2015: some parts of the PEVK segment bond to actin, and this bond cannot do any positive work on titin. The assumption that the bond between titin and actin cannot do positive work means that titin cannot be actively preloaded: it can only develop force when it is stretched. In contrast, two mechanisms have been proposed that make it possible for titin to be preloaded by crossbridge cycling: the winding ﬁlament theory of Nishikawa et al., 2012 and the titin entanglement hypothesis of DuVall et al., 2016. If titin were signiﬁcantly preloaded by crossbridge cycling, the titin load path would support higher forces and the myosin-actin load path would bear less force. Accordingly, the overall stiffness of the CE would be reduced, affecting our simulations of Kirsch et al., 1994: lower myosin-actin loads mean fewer attached crossbridges, since crossbridges are stiff in comparison to titin, the stiffness of the CE would decrease (see Appendix 1). Hopefully experimental work will clarify if titin can be actively preloaded by crossbridges in the future.

Both the viscoelastic crossbridge and active titin elements include simple myosin-actin and titin-actin bond models that improve accuracy but have limitations. First, the viscoelastic crossbridge element has been made to represent a population of crossbridges in which the contribution of any single crossbridge is negligible. Although it may be possible for the XE model to accurately simulate a maximally activated single sarcomere (which has roughly 20 attached crossbridges per half sarcomere Huxley and Simmons, 1971; Howard, 1997), the accuracy of the model will degrade as the number of attached crossbridges decreases. When only a single crossbridge remains, the XE model’s output will be inaccurate because it can only generate force continuously while a real crossbridge generates force discretely each time it attaches to, and detaches from, actin. Next, we have used two equations, Equation 16 and Equation 21, that assume myosin-actin and titin-actin interactions are temperature-invariant and scale linearly with size ($l_{o}^{M}$ and $f_{o}^{M}$). In contrast, myosin-actin interactions and some titin-actin interactions are temperature-sensitive (Minajeva et al., 2002; Roots et al., 2012) and may not scale linearly with size. In the ‘Active lengthening beyond actin-myosin overlap’ section we had to adjust the active titin damping parameter, $\beta_{A}^{PEVK}$, to simulate the myoﬁbril experiments of Leonard et al., 2010, perhaps because the assumptions of temperature-invariance and size-linearity were not met: the initial value for $\beta_{A}^{PEVK}$ came from ﬁtting to in-situ experimental data (Herzog and Leonard, 2002) from whole muscle that was warmer (35 − 36.5°C vs 20 − 21°C) and larger ($l_{o}^{M}$ of 42.9mm vs. 10 − 15μm) than the myoﬁbrils (Leonard et al., 2010). While the cat soleus XE and titin model parameters (Table 1G, H1) can be used as rough default values, these parameters should be reﬁt to accurately simulate muscle that differs in scale or temperature from cat soleus. Finally, the VEXAT model in its current form ignores phenomena related to submaximal contractions: the shift in the peak of the force-length relation (Stephenson and Wendt, 1984), and the scaling of the maximum shortening velocity (Chow and Darling, 1999). We hope to include these phenomena in a later version of the VEXAT model to more accurately simulate submaximal contractions.

The model we have proposed can replicate phenomena that occur at a wide variety of time and length scales: the experiments of Kirsch et al., 1994 which occur over small time and length scales; and the active lengthening experiments of Herzog and Leonard, 2002 and Leonard et al., 2010 which occur over physiological and supra-physiological length scales. In contrast, we have shown in the ‘Biological benchmark simulations’ section that a Hill-type model compares poorly to biological muscle when the same set of experiments are simulated. We expect that a Huxley model (Huxley, 1957) is also likely to have difficulty reproducing the experiment of Kirsch et al., 1994 because the model lacks an active damping element. Since titin was discovered (Maruyama, 1976) long after Huxley’s model was proposed (Huxley, 1957), a Huxley model will be unable to replicate any experiment that is strongly inﬂuenced by titin such as the experiment of Leonard et al., 2010.

Although there have been several more recent muscle model formulations proposed, none have the properties to simultaneously reproduce the experiments of Kirsch et al., 1994, Herzog and Leonard, 2002, Leonard et al., 2010, Hill, 1938, and Gordon et al., 1966. Linearized impedance models (Hogan, 1985; Mussa-Ivaldi et al., 1985) can reproduce the experiments of Kirsch et al., 1994, but these models lack the nonlinear components needed to reproduce the force-length experiments of Gordon et al., 1966, and the force-velocity experiments of Hill, 1938. The models of Forcinito et al., 1998, and Tahir et al., 2018 have a structure that places a contractile element in series with an elastic-tendon. While this is a commonly used structure, at high frequencies the lack of damping in the tendon will drive the phase shift between length and force to approach zero. The measurements and model of Kirsch et al., 1994, in contrast, indicate that the phase shift between length and force approaches ninety degrees with increasing frequencies. Although the Hill-type models of Haeufle et al., 2014 and Günther et al., 2018 have viscoelastic tendons, these models have no representation of the viscoelasticity of the CE’s attached crossbridges. Similar to the Hill-type muscle model evaluated in this work (Millard et al., 2013), it is likely that models of Haeufle et al., 2014 and Günther et al., 2018 will not be able to match the frequency response of biological muscle. While the model of Tamura and Saito, 2002 is one of the few models that can develop force-enhancement and force-depression (Tamura et al., 2005), it is unlikely that this model will be able to reproduce the frequency response of biological muscle because it uses spring-damping elements in series: Kirsch et al., 1994 showed that the frequency response of spring-damping elements in series poorly fits the response of biological muscle. The models of De Groote et al., 2017 and De Groote et al., 2018 introduced a short-range-stiffness element in parallel to a Hill model to capture the stiffness of biological muscle. While the formulations presented in De Groote et al., 2017 and De Groote et al., 2018 improves upon a Hill model it is unlikely to reproduce the experiement of Kirsch et al., 1994 because we have shown in the ‘Active lengthening beyond actin-myosin overlap’ section that a Hill model has a frequency response that differs from biological muscle. The muscle model of Rode et al., 2009 uses a Hill model for the CE and so we expect that this model will have the same difficulties reproducing the experiment of Kirsch et al., 1994. The model of Schappacher-Tilp et al., 2015 extends a Huxley model (Huxley, 1957) by adding a detailed titin element. Similar to a Huxley model, the model of Schappacher-Tilp et al., 2015 will likely have difficulty reproducing the experiment of Kirsch et al., 1994 because it is missing an active damping element.

While developing this model, we have come across open questions that we hope can be addressed in the future. How does muscle stiffness and damping change across the force-length curve? Does stiffness and damping change with velocity? What are the physical origins of the active damping observed by Kirsch et al., 1994? What are the conditions that affect passive-force enhancement, and its release? In addition to pursuing these questions, we hope that other researchers continue to contribute experiments that are amenable to simulation, and to develop musculotendon models that overcome the limitations of our model. To help others build upon our work, we have made the source code of the model and all simulations presented in this paper available online (see the elife 2023 branch of https://github.com/mjhmilla/Millard2021ImpedanceMuscle; copy archived at Millard, 2024).
