# Flagellar energetics from high-resolution imaging of beating patterns in tethered mouse sperm

## Authors

- Ashwin Nandagiri<sup>1</sup> ([ORCID: 0000-0001-7328-9288](https://orcid.org/0000-0001-7328-9288))
- Avinash Satish Gaikwad<sup>4</sup> ([ORCID: 0000-0002-7379-6383](https://orcid.org/0000-0002-7379-6383))
- David L Potter<sup>5</sup>
- Reza Nosrati<sup>3</sup> ([ORCID: 0000-0002-1461-229X](https://orcid.org/0000-0002-1461-229X))
- Julio Soria<sup>3</sup> ([ORCID: 0000-0002-7089-9686](https://orcid.org/0000-0002-7089-9686))
- Moira K O'Bryan<sup>6</sup> ([ORCID: 0000-0001-7298-4940](https://orcid.org/0000-0001-7298-4940))
- Sameer Jadhav<sup>2</sup> ([ORCID: 0000-0002-4207-3393](https://orcid.org/0000-0002-4207-3393))
- Ranganathan Prabhakar<sup>3</sup> ([ORCID: 0000-0001-7357-4222](https://orcid.org/0000-0001-7357-4222)) †

### Affiliations

1. IITB-Monash Research Academy Mumbai India
2. Department of Chemical Engineering, Indian Institute of Technology Bombay Mumbai India
3. Department of Mechanical and Aerospace Engineering, Monash University Clayton Australia
4. School of BioSciences, University of Melbourne Parkville Australia
5. Monash Micro-Imaging, Monash University Clayton Australia
6. School of BioSciences, University of Melbourne Parkville Australia

† Corresponding author

## Abstract

We demonstrate a technique for investigating the energetics of flagella or cilia. We record the planar beating of tethered mouse sperm at high resolution. Beating waveforms are reconstructed using proper orthogonal decomposition of the centerline tangent-angle profiles. Energy conservation is employed to obtain the mechanical power exerted by the dynein motors from the observed kinematics. A large proportion of the mechanical power exerted by the dynein motors is dissipated internally by the motors themselves. There could also be significant dissipation within the passive structures of the flagellum. The total internal dissipation is considerably greater than the hydrodynamic dissipation in the aqueous medium outside. The net power input from the dynein motors in sperm from Crisp2-knockout mice is significantly smaller than in wildtype samples, indicating that ion-channel regulation by cysteine-rich secretory proteins controls energy flows powering the axoneme.

## Introduction

In their journey towards the oocyte, sperm propel themselves by beating a whip-like flagellum. This motility is essential for successful fertilization and is fundamental to reproduction. Understanding sperm motility is essential for improving male infertility treatments, animal breeding, and wildlife conservation (Gaffney et al., 2011). Despite the vast body of work on the structure and function of different parts of the axoneme – the internal ‘engine’ powering the flagellum (Brokaw and Kamiya, 1987; Okagaki and Kamiya, 1986; Yagi et al., 2005) – and other accessory structures that surround the axoneme, such as the outer dense fibers (Zhao et al., 2018) and the fibrous sheath (Eddy et al., 2003), the mechanisms that control the complex beating patterns observed in flagella remain poorly understood (Brokaw, 2009; Lehti and Sironen, 2017; Lindemann and Lesich, 2016; Lin and Nicastro, 2018). It is, however, recognized that mechanical properties of the flagellum and its surroundings play a crucial role in determining sperm motility (Gaffney et al., 2011). Measurements of the mechanical behavior of single flagella in living sperm have however remained a critical bottleneck.

We demonstrate here a set of powerful new tools that enable detailed calculation of the mechanical energetics of single sperm flagella from high-resolution optical microscopy. Automated image-analysis tools have long been used to study sperm movement (Katz et al., 1975; Katz and Overstreet, 1981; Overstreet et al., 1979). Computer-aided sperm analysis systems are today used extensively in clinical settings to rapidly assess the viability of samples containing hundreds of cells in a single field of view (FOV) (Amann and Waberski, 2014). These high-throughput techniques, however, do not resolve flagellar motion. Improvements in digital imaging and storage have now placed within reach the high-speed, high-resolution, and long-exposure imaging that researchers of flagellar propulsion have long sought (Gray, 1955; Gray, 1958; Brokaw, 1966; Rikmenspoel et al., 1960). A wide range of digital image processing algorithms are now available (Gonzalez et al., 2004) that can be combined with high-performance parallel computing to analyze thousands of video frames with little manual intervention (Baba and Mogami, 1985; Riedel-Kruse et al., 2007; Saggiorato et al., 2017; Hansen et al., 2018; Sartori et al., 2016). We have implemented these image-analysis techniques to automatically extract centerlines of sperm flagella in every video frame.

To quantitatively analyze beat patterns in a statistically meaningful way, we need to image swimming sperm over several beat cycles. While rapid progress is being made on full three-dimensional tracking (Muschol et al., 2018; Dardikman-Yoffe et al., 2020; Gadêlha et al., 2019), it is unlikely that sufficient beat cycles can be reliably recorded with freely swimming sperm that can quickly move out of focal plane or the FOV (Mondal et al., 2020). Instead, we image flagella beating freely in the focal plane in cells tethered chemically at their heads to a glass slide. Our tethered-cell assay, in principle, permits imaging single cells until they stop beating. We report here results obtained by analyzing large numbers of (∼50) beat cycles in single tethered sperm in freshly prepared samples when they are most vigorous (Gaikwad et al., 2020).

Beating patterns in sperm flagella have been studied previously to investigate changes induced by environmental factors (Bukatin et al., 2015; Smith et al., 2009; Saggiorato et al., 2017) or by gene mutations (Krähling et al., 2013; Lim et al., 2019). We build here on the suggestion that the technique of proper orthogonal decomposition (POD) can be applied on the time-resolved tangent-angle profiles of flagellar centerlines to analyze their kinematics (Ma et al., 2014; Werner et al., 2014; Saggiorato et al., 2017). POD is widely applied in the analysis of turbulent flows (Lumley, 1967; Holmes et al., 2012) and other fields (Baumberg and Hogg, 1994; Jolliffe, 2002) to reduce complexity of spatiotemporal patterns and represent them with a much smaller set of numbers, while still retaining accuracy. To objectively compare flagellar beating patterns, we apply POD to unambiguously identify the mean beat cycle of each sperm from the time series of the tangent-angle profiles of its flagellar centerline. We can compute average cycles of any kinematic or dynamic quantity derived from the tangent-angle profiles. We further introduce a technique to consistently represent the POD shape modes with smooth Chebyshev polynomials to ensure that the tangent-angle profile is sufficiently smooth and its spatial derivatives can be computed without spurious artifacts. The tangent-angle profile obtained thus is consistent with the rigid-body kinematics of the stiff head region. This Chebyshev-POD (C-POD) technique allows for efficient calculation of geometric quantities such as the local curvature and kinematic quantities such as the velocity components, at any material point on the centerline.

Our approach for calculating forces and energetics from the measured beating patterns stems from ideas discussed originally by Machin, 1963. We use the geometric and kinematic data to determine the hydrodynamic resistance offered by the external fluid medium using resistive force theory (RFT) (Gray and Hancock, 1955; Lighthill, 1976) and further calculate internal forces by applying conservation principles. This requires a model for the mechanical behavior for the flagellar body. Several models have been proposed that consider the flagellum to be an ‘active’ material (Camalet et al., 1999; Camalet and Jülicher, 2000; Lindemann, 1994a; Lindemann, 1994b; Sartori et al., 2016; Chakrabarti and Saintillan, 2019). These are based on different models for motor forcing in the axoneme and the regulation of their kinetics. We propose instead a different approach that is agnostic to the nature of motor activity and avoids invoking the assumption that the flagellar material is active. We consider the motion of the non-motor passive material of the flagellum under the action of the unknown forces exerted by the axonemal motors. This allows us to use well-established principles for the continuum material stress in the passive flagellar material. The resulting Soft-Internally -Driven-Kirchhoff-Rod (SIDKR) model leads to an energy balance across the flagellum, which we then use to determine the spatiotemporal distribution of motor power across the flagellum over its mean cycle.

We have used this approach to analyze flagellar beating patterns of sperm from wildtype (WT) and Crisp2 knockout (KO) mice. The cysteine-rich secretory proteins (CRISPs) are a group of proteins that are predominantly expressed in the male reproductive tract (Gaikwad et al., in preparation). Crisp2 is incorporated into the sperm acrosome, connecting piece and the outer dense fibers of the sperm tail. It is known that the deletion of Crisp2 in mice leads to compromised sperm function, including altered sperm motility (Hu et al., 2018; Lim et al., 2019). The precise effect on flagellar function, however, is unknown.

Our observations with these sperm reveal intriguing new information: there is considerable intracellular friction within the flagellum. This challenges the widely held view that the hydrodynamic resistance offered by the viscous fluid medium outside is the sole dissipative sink that must be overcome by the continual driving provided by the dynein motors. Further, the flagellar filament is also conventionally regarded as an elastic body that perfectly stores energy temporarily by bending. Our findings suggest instead that internal friction within the passive structures of the flagellum, and within the motors themselves, may be as large as the external hydrodynamic friction. These are in line with recent observations also made in algal cilia (Mondal et al., 2020). These sources of internal dissipation could therefore play a significant role in determining beating patterns in sperm (Camalet and Jülicher, 2000). This insight could be vital for understanding dramatic changes in flagellar beating patterns induced by changes in the medium (Smith et al., 2009) or the proximity of surfaces (Nosrati et al., 2015; Denissenko et al., 2012).

### Theoretical model

#### The soft, internally driven Kirchhoff rod model

Flagellar motion is driven internally by the action of dynein motors distributed within the axoneme. The sperm body is treated as a slender, flexible filament immersed in a viscous fluid (Figure 1). It is assumed that the passive material of the sperm body is a Kirchhoff rod (Audoly and Pomeau, 2010; Malvern, 1969; O’Reilly, 2017), that is, it is inextensible and each of its material cross-sections remains rigid and planar, while rotating with respect to each other about the rod axis as it bends and twists. The passive Kirchhoff rod has external as well as internal surfaces. It is driven by axonemal motors acting on its internal surfaces and the resulting motion is resisted by the hydrodynamic forces that act on its external surface (Figure 1) as well as the stresses that arise to resist material deformation as the rod bends.

![Figure 1.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig1-v2.jpg)

**Figure 1.:** (A) Geometric variables defined along the centerline. (B) An arbitrary control volume used for deriving the equations of the model: the volume consists of the passive flagellar material; hydrodynamic forces act on the external surface while axonemal motors act on the internal surfaces. The passive material adjacent to the cross-sectional faces at either end exerts stresses on those faces.

The instantaneous space curve of the axial centerline of the filament, $𝐫⁢(s,t)$, is parameterized by its arc length variable, $s$, defined such that $s=0$ at the tip of the head, and $s=L$ at the tail end. A local material frame is attached to each cross-sectional plane and is specified by a triad of unit vectors, $𝐝_{k}$, where $k=1,2,3$. In general, the smooth variation of these vectors with $s$ at any instant of time, $t$, is specified in terms of the Darboux vector, $𝛀$, where $∂d_{k}/∂s=Ω\timesd_{k}$. The components $Ω_{k}$ of the Darboux vector are the generalized curvatures. Since we shall only consider motion of the rod in the $x-y$ plane, we align the material frame at each cross-section with the Frenet–Serret frame associated with each point on the axial curve. For this choice, $𝐝_{1}=𝐭=\partial⁡𝐫/\partial⁡s$, the unit tangent vector to axial curve. The other two vectors, $𝐝_{2}=𝐧$ and $𝐝_{3}=𝐛$, are the normal and binormal vectors, which span the cross-sectional plane. The Darboux vector for the Frenet–Serret frame is $𝛀=T⁢(s,t)⁢𝐝_{1}+C⁢(s,t)⁢𝐝_{3}$, where $C$ and $T$ are the curvature and torsion profiles at any time. For planar motion, $𝐛=𝐞_{z}$ (pointing out of the plane of the page) is a constant; hence, $T=0$. The geometry of a planar Kirchhoff rod at any instant is thus fully specified by the curvature, $C$. The velocity of a point on the centerline, $𝐯⁢(s,t)=\partial⁡𝐫/\partial⁡t$. Cross-sectional planes can rotate relative to each other. Then, $∂d_{k}/∂t=\omega\timesd_{k}$, where $𝝎⁢(s,t)$ is the instantaneous angular velocity of a cross-sectional plane at $s$. It can further be shown that $𝝎$ and $𝛀$ satisfy the compatibility relation (Powers, 2010),

$$
\frac{\partial⁡𝝎}{\partial⁡s}=\sumi=13\frac{\partial⁡Ω_{i}}{\partial⁡t}⁢𝐝_{i}.
$$

For planar motion, where $𝝎=\omega⁢𝐞_{z}$,

$$
\frac{\partial⁡\omega}{\partial⁡s}=\frac{\partial⁡C}{\partial⁡t}.
$$

For inertialess rods, consideration of the conservation of linear momentum for a segment of the rod where $s\in[s_{1},s_{2}]$ formally yields the following equation (see Appendix 1):

$$
𝐟^{a}+𝐟^{h}+𝐟^{e}+\frac{\partial⁡𝐅}{\partial⁡s}= 0,
$$

where $𝐟^{a}⁢(s,t)$ and $𝐟^{h}⁢(s,t)$ are the force distributions per unit length on the cross-section at any $s$ due to the surface tractions exerted by internal motor activity and the external hydrodynamic resistance, respectively. Other external forces, such as the force exerted by a tethering traction at a wall, are accounted for by the distribution $𝐟^{e}⁢(s,t)$. The passive stress in the Kirchhoff rod results in a force, $𝐅$, exerted on a cross-section by the material on its aft side. The gradient with respect to $s$ of $𝐅$ in the momentum balance thus describes the net restoring force per unit length on a cross-section due to passive internal stresses resisting deformation. From conservation of angular momentum, we obtain (Appendix 1):

$$
𝐦^{a}+𝐦^{h}+𝐦^{e}+𝐭\times𝐅+\frac{\partial⁡𝐌}{\partial⁡s}= 0,
$$

where $𝐦^{a}⁢(s,t)$ and $𝐦^{h}⁢(s,t)$ are the torques per unit length exerted by the surface tractions due to the internal motors and the external viscous hydrodynamic resistance; $𝐦^{e}$ is the torque distribution due to other external forces. The torque on a cross-section exerted by the passive material stresses on its aft side is $𝐌$, and its gradient in the equation above is the net restoring torque distribution. Energy conservation further shows that at any cross-section, in general,

$$
\frac{\partial⁡ϵ}{\partial⁡t}+\frac{\partial⁡u}{\partial⁡t}=p^{a}+p^{hd}+p^{e}+p^{s}-q,
$$

where $ϵ⁢(s,t)$ is the local elastic energy per unit length (i.e., the elastic storage density) of the rod and $u⁢(s,t)$ is the thermal internal energy density. On the right-hand side, $q$ is the net rate of heat removal per unit length of the rod by the surroundings, while each of the remaining terms is, respectively, the mechanical power per unit length delivered into the rod cross-section by the action of the motors, the hydrodynamic and non-hydrodynamic external forces, and the passive material stress. The motor power distribution, $p^{a}$, is the key unknown in our study. The hydrodynamic power distribution is related to the corresponding force and torques distributions: 

$$
p^{hd}=𝐯⋅𝐟^{h}+𝝎⋅𝐦^{h}.
$$

The other external mechanical power $p^{e}$ is similarly related to the external force and moment distributions, $𝐟^{e}$ and $𝐦^{e}$. The net rate of work done on a cross-section by the action of the local stress gradient is

$$
p^{s}=\frac{\partial⁡(𝐯⋅𝐅)}{\partial⁡s}+\frac{\partial⁡(𝝎⋅𝐌)}{\partial⁡s}.
$$

The sign convention used here is that mechanical power due to work done on a cross-section of the rod and tending to increase the local internal energy storage is positive whereas the power due to work done by that cross-section to overcome resistances leading to a decrease in stored energy is negative. Due to its purely dissipative nature, $p^{hd}$ is therefore always negative at any $s$ and $t$. In our study, the external force and moment due to the tethering constraint exerted on the head cannot be measured directly. The mechanics of this tether could be complex and, at any instant of time, $p^{e}$ may be positive or negative. However, over a full cycle, we expect net work to be done by the cell against the tethering constraint. The key advantage in treating the motor contribution as a forcing that is external to the passive material of the Kirchhoff rod is that we can treat the active forcing as an unknown to be extracted from experimental data in a model agnostic manner while applying well-established concepts to treat passive material stresses within the Kirchhoff rod. The passive stress tensor can be formally split into an elastic part and a part that provides internal dissipation, so that the total material torque, $𝐌=𝐌^{el}+𝐌^{id}$. It can be shown that Equation (62) is satisfied when the elastic torque arising from the passive material stress is such that

$$
\frac{\partial⁡ϵ}{\partial⁡t}=𝐌^{el}⋅\frac{\partial⁡𝝎}{\partial⁡s}=𝐌^{el}⋅\frac{\partial⁡𝛀}{\partial⁡t},
$$

and the dissipative part of the material stress is such that

$$
\frac{\partial⁡u}{\partial⁡t}=𝐌^{id}⋅\frac{\partial⁡𝝎}{\partial⁡s}-q=-p^{id}-q,
$$

where $p^{id}$ denotes the rate of internal frictional dissipation per unit length. Since the material of the Kirchhoff rod is passive, the Second Law of Thermodynamics requires that $p^{id}\leq0$ everywhere (Chaikin and Lubensky, 1995). Since the dynein motors are excluded from the control volume in the analysis above, $p^{id}$ does not include any dissipation that occurs within the motors themselves. We shall later discuss how we separately obtain the motor dissipation.

#### Constitutive relations

Although presented in the context of a sperm body, the equations above are generally valid of any inertialess, internally driven Kirchhoff rod. To proceed further, we make several constitutive assumptions that are specific to the case of a sperm cell tethered at its head. The sperm body is assumed to be composed of a head region, $s\in[0,s_{N}]$, and a flagellar tail region, $s\in(s_{N},L)$, with $s_{N}$ denoting the location of the neck junction between the two regions. We assume that the head is a rigid body. In our experiments, cells are further tethered at a point in the head region, and the head can rotate rigidly about this tether point. Therefore, although the angular velocity $𝝎\neq$ in the head region, rigid-body kinematics dictates that $\partial⁡𝝎/\partial⁡s= 0$ everywhere in the head region. Hence, from Equation (48), $\partial⁡Ω_{k}/\partial⁡t=0$ across the head. Therefore, for planar beating, $\partial⁡\omega/\partial⁡s=\partial⁡C/\partial⁡t=0$ across the head. The flagellar tail is flexible and not subject to the kinematic constraints above.

The head does not contain internal motors, which are all distributed only along the tail region. Therefore, $f^{a}$, $m^{a}$, and $p^{a}$ are all zero for $s\in[0,s_{N}]$. In the flagellar tail, each dynein motor is assumed to act on the internal surfaces of a cross-section such that the forces exerted at its two ends are of equal magnitude but in opposite directions. Therefore, $𝐟^{a}=$. However, the net torque they exert is not zero, and therefore $𝐦^{a}\neq$, which serves to drive the filament’s motion. The external hydrodynamic force distribution is given by RFT (Gray and Hancock, 1955; Lighthill, 1976):

$$
f^{h}=−[ζ_{t}tt+ζ_{n}(\delta−tt)]⋅v,
$$

where the tangential and normal hydrodynamic friction coefficients in an infinite fluid medium of viscosity, μ, are $ζ_{t}=2⁢\pi⁢\mu/ln⁡(2⁢L/a)$ and $ζ_{n}=4⁢\pi⁢\mu/[ln⁡(2⁢L/a)+1/2]$, respectively. For sperm tethered to a glass slide, the no-slip condition at the slide surface creates an additional resistance to fluid flow. Katz et al., 1975 obtained the following RFT approximations for the friction coefficients for motion of a slender body in a plane parallel to a wall and at a distance of $h$ from it:

$$
ζ_{t}=\frac{2\pi\mu}{ln⁡2h/a};ζ_{n}=\frac{4\pi\mu}{ln⁡2h/a}.
$$

These coefficients have previously been used in a number of studies, notably by Jülicher and co-workers (Riedel-Kruse et al., 2007) for analyzing experimental data on wall-tethered sperm and, more recently, by Mondal et al., 2020, for tethered axonemes isolated from cilia. The cross-sectional radius of the cylindrical filament, $a$, is further not constant along the sperm body. For our calculations here, only the variation of the radius in the tail region is relevant. We assume a linear taper along the flagellum, that is, for $s\geqs_{N}$,

$$
a(s)=(a_{N}−a_{T})\frac{L−s}{L−s_{N}}+a_{T}.
$$

where $a_{N}$ and $a_{T}$ are the radii at the neck and the tail tip. When a sperm tethered at its head beats in a plane parallel to the wall, $h=a_{N}$, is constant (Appendix 2).

The rigid head region requires no further constitutive assumptions. The tail region can deform and therefore requires a constitutive model that relates its material stresses to its deformation. The simplest constitutive model for the elastic stress in a passive material is the Hookean model, which leads to a linear relation between the elastic material torque and the local curvature. The corresponding elastic energy distribution must be consistent with Equation (8). Thus, in the tail region,

$$
M_{i}^{el}=\sumi=13κ_{i}Ω_{i}d_{i};ϵ=\sumi=13\frac{κ_{i}Ω_{i}^{2}}{2}.
$$

where $κ_{i}$ is an elastic stiffness coefficient. The simplest constitutive model for the dissipative stress that satisfies the condition imposed by the Second Law that the dissipation rate is always positive leads to the following expression for the dissipative part of the internal torque:

$$
M^{id}=η\frac{∂\omega}{∂s},
$$

where $η>0$ is the internal friction coefficient per unit length. Taken together, the constitutive equations above are equivalent to modeling the Kirchhoff rod as a passive viscoelastic Kelvin–Voigt solid (Bird et al., 1987). For the linear taper assumed in the tail region, the elastic stiffness and internal friction coefficients can be shown to vary with the radius as $a^{4}$. That is,

$$
κ(s)=κ_{N}(\frac{a(s)}{a_{N}})^{4}η(s)=η_{N}(\frac{a(s)}{a_{N}})^{4}
$$

where $κ_{N}$ and $η_{N}$ are the values of the elastic stiffness and frictional coefficients at the neck. For planar motion, $𝐌=M⁢𝐞_{z}$, and the relations above reduce to

$$
M^{el}(s,t)=κ(s)C;ϵ(s,t)=κ(s)\frac{C^{2}}{2};M^{id}(s,t)=η(s)\frac{∂\omega}{∂s}.
$$

We make a few other simplifying assumptions. The head and tail ends are free; $𝐅$ and $𝐌$ are, therefore, zero at the two ends. The external surface traction due to tethering at the wall acts at a single location, $s_{E}$, on the head and is zero elsewhere, that is,$f^{e}=F^{e}\delta(s−s_{E})$ and $m^{e}=M^{e}\delta(s−s_{E})$. The system is further isothermal and changes in the internal thermal energy of the body are negligible, that is, $\partial⁡u/\partial⁡t=0$ in Equation (62) and Equation (9). This means that any internal frictional heat generation is, therefore, instantaneously balanced by, $q$, the heat removal from the passive flagellar material to its surroundings. Further, the ratio of the contributions from the external hydrodynamic moment, $𝐦^{h}$, and the hydrodynamic force, $𝐟^{h}$, to the total hydrodynamic power, that is, the ratio $|𝝎⋅𝐦^{h}|/|𝐯⋅𝐟^{h}|$, is expected to scale as $a/L≪1$. The contribution of $𝐦^{h}$ in Equation (60) to the hydrodynamic dissipation is, therefore, neglected. The momentum and energy balance equations for the rigid, passive, head region on which the external tether force acts, and the viscoelastic, untethered, internally driven tail region are summarized in Appendix 1. We next describe our approach to quantifying the kinematics of the beating patterns recorded in experiments and then using these along with the momentum and energy balances to obtain the dynamics and energetics of sperm.

#### Kinematics from image analysis and POD

In Materials and methods, we describe in detail the image-analysis and data-processing algorithms used to obtain power distributions from microscope videos of tethered sperm samples from WT and Crisp2 KO mice. Briefly, the image-analysis algorithm is used to process videos of single sperm cells tethered to a glass surface and beating in the focal plane of the microscope and extract centerlines of sperm bodies in every video frame. This raw data is first analyzed for head region separately to determine its motion as a rigid body. Twentieth-order Chebyshev polynomials are fitted through these centerlines to construct smooth tangent-angle profiles (see Figure 1A) of the flagellar tail region. These Chebyshev polynomials are designed to be consistent with the rigid-body kinematics of the head region.

In general, the POD is an order-reduction technique that optimally approximates spatiotemporally varying data. In our C-POD approach, we apply POD on the time-dependent Chebyshev coefficients to represent the deviation of $ψ⁢(s,t)$, the time-resolved tangent-angle profile of the centerline from its time average, $ψ_{0}⁢(s)$, as a weighted sum of $M$ orthogonal shape modes (see C-POD of the tail region). In other words,

$$
ψ⁢(s,t)=ψ_{0}⁢(s)+\summ=1MB_{m}⁢(t)⁢ψ_{m}⁢(s).
$$

The set of ‘shape modes’, $ψ_{m}$, $m= 1⁢…⁢M$, is optimal in the sense that, for any given $M$, the approximation above is guaranteed to deviate least from the original data than any other expansion in terms of another set of $M$ mutually orthogonal basis functions (Holmes et al., 2012; Werner et al., 2014). We describe, in Materials and methods, the C-POD method to obtain the shape modes, each of which is a 20th order, Chebyshev polynomial that is consistent with the head region executing rigid-body rotation. The corresponding time-dependent weights of the shape modes are referred to as ‘shape coefficients’. With the smooth C-POD tangent profiles, we can efficiently compute at any $s$ and $t$, geometric and kinematic quantities in the beating plane, such as the curvature $C$ and its derivatives with respect to $s$ or $t$, the flagellar velocity $𝐯$, and the cross-sectional angular rotation rate, $𝝎$.

#### Dynamics and energetics from measured kinematics

The hydrodynamic force distribution, $𝐟^{h}$, is first calculated using Equation (10) and the expressions for the tangential and normal friction coefficients. Using Equation 3 together with the boundary condition that $𝐅⁢(L,t)= 0$ at the tail tip, we then obtain

$$
F(s,t)=\int_{s}^{L}f^{h}(s^{′},t)ds^{′},
$$

for all $s$ in the tail region. The moments, $M^{el}$ and $M^{id}$, and the elastic energy density $ϵ$ are calculated using the constitutive Equations (13) and (14) and the elastic stiffness and internal dissipation profiles, $κ⁢(s)$ and $η⁢(s)$, in Equation (15) along with the values of the parameters, $κ_{n}$ and $η_{n}$. The total bending moment, $M=M^{el}+M^{id}$.

The energetic variables are then calculated as follows. In the tail region, the rate of change of the elastic storage density, $ϵ$, and the power dissipated due to internal friction per unit length are (from Equations 8 and 9), respectively,

$$
\frac{∂ϵ}{∂t}=κ(s)C\frac{∂C}{∂t};p^{id}=−η(s)(\frac{∂\omega}{∂s})^{2}.
$$

We henceforth denote the rate of elastic storage density as $ϵ˙$. The external hydrodynamic dissipation due to flagellar motion, $p^{hd}$, is calculated using $𝐯$ and $𝐟^{h}$ in Equations (60). Consistent with their dissipative natures, $p^{hd}$ and $p^{id}$ are always negative. The gradient in the mechanical power due to the internal force and bending moment, $p^{s}$, is obtained using Equation (61). There are no other external forces acting on the freely beating tail. The external power distribution, $p^{e}$, is therefore zero at all points in the tail region. The energy balance, Equation (62), can be rearranged as follows for the tail region:

$$
p^{a}(s,t)=ϵ˙−p^{s}−p^{hd}−p^{id}.
$$

The active power distribution along the tail can be obtained with all the terms on the right-hand side determined from centerline kinematics as described above.

The integrals of each term in the equation over the entire tail region give the instantaneous net rates of change of the energetic variables. For instance, the net instantaneous storage rate, $E˙(t)=\int_{s_{N}}^{L}ϵ˙ds$. The instantaneous total hydrodynamic and passive internal frictional dissipation rates, $P^{hd}$ and $P^{id}$, and the net active power, $P^{a}$, are similarly calculated by integrating the distributions $p^{hd}$, $p^{id}$, and $p^{a}$ over the tail region, respectively. We can similarly obtain rates over just the mid-piece or over the principal piece alone. We further define and calculate

$$
P^{md}(t)=\int_{s_{N}}^{L}min(p^{a},0)ds;P^{mi}(t)=\int_{s_{N}}^{L}max(p^{a},0)ds.
$$

As we shall show later, the active power distribution is not always positive, and $P^{md}$, the integral of $p^{a}$ over its negative values is the total rate at which energy is dissipated within the dynein motors themselves. We will show below that, $P^{mi}$, the integral over the positive values of $p^{a}$ is the actual instantaneous power input from the dynein motors into the filament that is necessary to overcome all the different sources of dissipation. We shall refer to $P^{md}$ and $P^{mi}$ as the motor dissipation and the motor input, respectively.

Besides the various sources of energy dissipation in the tail region, there is also dissipation against the hydrodynamic and tethering forces acting across the head region. Since the head is modeled as a rigid, passive body, there is no elastic storage or internal dissipation in that region, nor is there any active motor power. Thus the work required to move the head against the hydrodynamic and tethering forces must come from the force, $F_{N}$, and the moment $M_{N}$, exerted by the flagellum on the head at the neck junction. Hence, the instantaneous power dissipated by the head against the hydrodynamic and external tethering forces,

$$
P_{H}^{hd}+P_{H}^{e}=P_{H}^{d}=−(v_{N}⋅F_{N}+\omega_{N}M_{N}),
$$

the power delivered on to head by the force acting on the neck junction. Since $𝐅$ and $𝐌$ must be continuous across the neck junction, $F_{N}=F(s_{N},t)$ using Equation (70) and $M_{N}=M^{el}(s_{N},t)+M^{id}(s_{N},t)$ calculated using Equation (16).

The physical boundary conditions at the tail end of the flagellum are $𝐅⁢(L,t)= 0$ and $M⁢(L,t)=0$. Integrating Equation (71) over the entire tail region with these boundary conditions at the tail end, and Equation (66) at the head end, and noting that $P^{a}=P^{md}+P^{mi}$, we obtain, at any $t$,

$$
P^{mi}=E˙−P_{H}^{d}−P^{hd}−P^{id}−P^{md}.
$$

The time averages of these instantaneous power functions over a single cycle are referred to as their ‘cycle-means’. These cycle-means are denoted by an overline. Since the motion of the flagellum is periodic but noisy, there is no net storage of elastic storage in the flagellum over many cycles, that is, the average of the cycle-mean, $E˙¯$, over several cycles must be zero. The cycle-means of the dissipation rates are, however, not zero. Therefore, neglecting the fluctuations due to $E˙¯$, we calculate the cycle-mean of the motor input as the power input required to balance the dissipations due to head motion, external hydrodynamic resistance and internal friction, and the dissipation within the motors:

$$
P¯^{mi}=−(P¯_{H}^{d}+P¯^{hd}+P¯^{id}+P¯^{md}).
$$

The average of the cycle-means over all beat cycles is identically equal to the time average over the entire duration of observation and will be referred to as such and denoted by a double overline (e.g., $P¯¯^{hd}$) .

In Results, we compare the relative magnitudes of these different dissipations. The results are obtained with the medium viscosity, $\mu=10^{−3}$ Pa s. The radius at the neck and at the tail end are $a_{n}= 0.57$ μm and $a_{t}= 0.18$ μm, respectively (Gu et al., 2019). The total body length $L$ for each sample is taken to be the maximum observed length in the sample video and is around 120 μm. There are few measurements of the bending stiffness for sperm flagella in the literature. The stiffness of flagella in mouse sperm is reported to be between that of bull (1.5 × 103 Pa μm4) and rat (3 $\times10^{4}$ Pa μm4) sperm (Lindemann and Lesich, 2016). We use their geometric mean $7\times10^{4}$ Pa μm4 as the value for $κ_{N}$ in calculations here. There are, however, no clear measurements yet of the internal bending friction coefficient, $η_{N}$. We report below the results obtained for flagellar energetics with both $η_{N}=0$ and 103 Pa s μm4 and discuss the reasons why the latter value may be realistic.

## Results

### POD enables identification of beat cycles

Figure 2 summarizes generic observations on the C-POD shape modes and their coefficients. In all the results presented here, the arc-length coordinate $s$ along the centerline is normalized by the maximum observable length of the whole flagellum in the entire duration of a sample video. The mid-piece region corresponds approximately to values of $s$ in the range 0.1–0.3, and the principal piece extends from $s=0.3$ to $s=0.85$.

![Figure 2.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig2-v2.jpg)

**Figure 2.:** (A) Time-averaged tangent-angle profiles for five wildtype (WT) (continuous curves) and five knockout (KO) (dashed curves) samples. (B) First (top) and second (bottom) C-POD shape modes for WT (continuous curves) and KO (dashed curves) samples; the colors are as in (A). (C) Cumulative accuracy of the C-POD representation for WT and KO samples; the colors are as in (A). A representation using the first four modes captures 95% or more of the observed centerline shapes for all samples. (D) Five shape cycles for a single WT sample in the parameter space defined by the time-dependent coefficients of the first two C-POD shape modes. The zero-crossing of the second modal coefficient marks the start of a new cycle. (E) Contributions of the first four modes to the tangent angle at the midpoint of the sperm body in the five tangent-angle cycles in (D): the horizontal line in the top plot is the time-averaged tangent angle for this WT sample. The starting time of the $i$ th cycle is denoted as $t_{i}^{0}$, and its duration (i.e., cycle time) is $T_{i}$.

Mouse sperm heads have distinctive falciform (hook) shapes (Woolley, 2003). In the image-processing protocol we have followed, all video frames are initially digitally rotated or reflected such that the head is on the left end of the body with the hook facing concave downward. For most of the WT and KO samples, the time-averaged tangent angles ($ψ_{0}⁢(s)$) are observed in Figure 2A to consistently first increase with $s$ around the mid-piece region before decreasing in the principal piece. Since the local curvature $C=\partial⁡ψ/\partial⁡s$, the gradient of the tangent angle with respect to $s$, Figure 2A shows that the time-averaged shape for these samples is curved such that it is concave in the anti-hook direction in the mid-piece and concave in the pro-hook direction in the principal piece. The mean shapes thus show that the asymmetric spatial bias in the beating pattern over time is not uniform across the flagellum. In the one outlier KO sample (KO-5) in Figure 2A, however, the mean shape is anti-hook concave throughout. Intrinsic net asymmetry in flagellar beating is well known in sperm in many mammalian species, even when uncapacitated. Our observation that the mean shape is curved with an anti-hook (ventral) concave shape is consistent with the observations of Woolley, 2003 that, in mouse sperm, the flagellum bends at the neck more on the ventral side than on the other.

The periodic beating of the flagellum about the mean shape is described by the C-POD shape modes and their time-dependent coefficients. The shapes of the first two shape modes ($ψ_{1}⁢(s)$ and $ψ_{2}⁢(s)$) in Figure 2B are qualitatively similar across the WT and KO samples. The key advantage of using the POD method to represent beating patterns is its optimality: a significant proportion of the beating pattern can be studied and understood by considering just a few shape modes. Figure 2C plots the cumulative contribution of the shape modes to the overall accuracy in capturing the full centerlines. Just the first two modes achieve a capture efficiency greater than 92% for all the WT samples, and for three out of the five KO samples. Even for the other two KO samples these dominant shape modes account for more than 85% of the observed beating patterns. Across all samples, the first four modes describe at least 95% of the beating patterns. We therefore calculate all kinematic, dynamic, and energetic quantities using the first four shape modes and their time-dependent coefficients.

As pointed out by Werner et al., 2014 and Ma et al., 2014, the periodicity in the beating pattern is clearly brought out by plotting the coefficients $B_{1}⁢(t)$ and $B_{2}⁢(t)$ of the two dominant modes against one another. For any sperm sample, the trajectory traced out in B1-B2 phase space consists of loops, one for each beat cycle (e.g., Figure 2D). We choose here to demarcate the start and end time for each beat cycle as the time at which the polar angle in the $B_{1}$-$B_{2}$ phase space crosses zero. This choice means that, in each sperm sample, the shape at the start of a beat cycle always corresponds mostly to the shape of the first dominant mode (with minor contributions from modes higher than the second; Figure 2E). Thus, the overall time series for any quantity can be split into individual beat cycles, as demonstrated in Figure 2E. Although Figure 2D, E shows only a few cycles for clarity, the C-POD technique applied to tethered sperm makes it possible to systematically accumulate data for large numbers of beat cycles and quantitatively compare, in a statistically meaningful sense, individual sperm samples within a genotypical population and also compare one genotypical population with another.

### Active power distribution provides evidence for energy dissipation by dynein motors

We first present the spatiotemporal variations typically observed in all our samples in the energetic quantities. Figure 3 plots the kymographs for the different energetic contributions obtained with the scaling estimate of the internal friction coefficient, $η_{n}= 10^{3}$ Pa s μm4, over several beat cycles for one of the WT samples. Similar results are obtained for all the other samples. The banded structures in these kymographs provide a visual confirmation of the spatiotemporal periodicity of the energy variables corresponding to the periodic beating of the flagellum.

![Figure 3.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig3-v2.jpg)

**Figure 3.:** The data in (C) and (D) have been obtained using the scaling value of 103 Pa s μm4 for the internal friction coefficient.

In Figure 3A, the hydrodynamic power distribution, $p^{hd}$, is always negative: that is, every part of the flagellum is at all times working against the hydrodynamic forces exerted externally by the viscous environment provided by the ambient fluid. This work done on the fluid is dissipated away by fluid friction. The elastic storage rate per unit length, $ϵ˙$ at any location $s$, however, alternates between positive (red) and negative (blue) values in Figure 3B. As a bending wave propagates through that location, the local curvature at that $s$ increases, leading to potential energy being stored elastically and a positive rate of $ϵ˙$ at that location. As the filament begins to relax and straighten out, the stored elastic energy is released and begins decreasing, leading to negative $ϵ˙$ values there. The filament then proceeds to bend in the other direction at that point, leading to a second positive growth of $ϵ˙$ within the same beat cycle, followed by a negative phase in $ϵ˙$ as the filament relaxes back towards being undeformed and straight at that location. Thus, at any $s$ in Figure 3B, each beat cycle consists of two successive positive and negative growth rate phases in $ϵ˙$.

Comparing the bands in Figure 3B with those in Figure 3A, it is clear that every single planar wave that propagates down the filament is associated with a pair of hydrodynamic dissipation peaks: the contribution of any single location to the hydrodynamic dissipation peaks as the filament moves quickly while bending and relaxing back on one side, and then again, on the other side. These bands are mirrored in Figure 3C, which plots $p^{id}$, the distribution of power dissipated due to internal friction. This frictional dissipation, calculated with $η_{n}= 10^{3}$ Pa s μm4, is due to relative motion between adjacent cross-sectional planes of the flagellar material, which also peaks at a location when a bend towards one side or the other propagates past that point.

The external and internal dissipations and temporary elastic storage of energy must together be supported by the mechanical power input provided by the dynein motors acting on the microtubule surfaces of the flagellum. Figure 3D plots the distribution of the net active power density $p^{a}$, across the filament. Interestingly, we find that the $p^{a}$ distribution displays clear negative bands that repeatedly occur in all beating periods and are spread throughout the filament. The positive domains (red) of the $p^{a}$ kymograph in Figure 3D represent mechanical power being delivered on the passive parts of the filament by the motors. In those regions, the motors cause relative sliding of microtubule doublets to rotate the local cross-sectional planes in the same sense as the torques they exert, that is, since $p^{a}=𝝎⋅m^{a}$, $p^{a}$ is positive at a cross-section when both the rotational velocity of that plane, ω, and the torque per unit length, $m^{a}$, exerted by the dynein motors in that plane have the same sign. On the other hand, where $p^{a}$ is negative (blue) in Figure 3D, ω and $m^{a}$ are opposite in sign. At any such point, work is being done by the rest of the flagellar material on the axonemal motors, driving them back against the torque they continue to exert. We observe this behavior consistently in all beat cycles and for all WT and KO samples.

The energy transferred back as mechanical work on the motors can neither be stored either within the dyneins nor converted back to chemical free energy (i.e., ATP): it must be therefore quickly dissipated locally within the axoneme itself. This axonemal motor dissipation is measured by the negative domains of $p^{a}$ and is denoted here as $p^{md}$. This is a second source of dissipation within the flagellum and is distinct from the dissipation, $p^{id}$, that is due to internal friction arising from the relative motions of all the other structures in the flagellum that surround the axonemal motors, such as the microtubules, the outer dense fibers, etc. By adding together the $p^{a}$ distribution over all the locations where it is negative, we can calculate, $P^{md}$, the instantaneous rate of energy dissipation due to the dynein motors themselves. The sum of $P^{md}$ and $P^{id}$ is the total mechanical power dissipated within the whole flagellum.

### POD enables statistics of beating patterns and energetic variables

The qualitative features of the distributions of the key energetic variables discussed above are common to both WT and KO samples. Before identifying significant differences between the beating patterns and energetics of the genotypes, it is worth examining the sample-to-sample variability within each population. Figure 4A shows the mean cycle of the beating pattern in physical $x$-$y$ space for each sperm sample in our study. Flagellar centerlines at the same value of the fractional duration of the mean beat cycle have the same color in Figure 4A. This fractional duration of the mean cycle is referred to as the time phase and is denoted as τ. To obtain the mean centerline shape at a particular value of τ, we collect, at that τ, the $x$ and $y$ coordinates obtained (using Equation 44) for all the beat cycles, and then calculate their mean values. The bands in Figure 4A around the mean centerlines are the standard errors in the mean (SEM) $y$ coordinates at each $s$. Our procedure for identifying the start and end of each beat cycle thus enables calculation and comparison of average beating patterns.

![Figure 4.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig4-v2.jpg)

**Figure 4.:** (A) Each colored curve shows the mean shape at a particular phase of the mean cycle for the five wildtype (WT) (top row) and knockout (KO) (bottom row) samples. The color bands around each curve indicate the standard error in the mean component. (B) Mean cycles for the magnitudes of the net elastic storage (yellow), hydrodynamic dissipation (black), internal frictional dissipation (magenta), and active power (red) in WT (top panel) and KO (bottom panel) sperm samples corresponding to those in (A). Bands show standard errors in means. (C) Statistical distributions of cycle times and dissipation rates in each of the WT (top panel) and KO (bottom panel) samples. The box-plots present the median (red line), the first and third quartile (bottom and top box edges), and minimum and maximum (lower and upper whiskers) values for 40–60 cycles. Outliers that are more than 1.5 times the interquartile range away from the top or bottom of the box are indicated by red crosses. The notch extremes correspond to $q_{2}\pm1.57(q_{3}−q_{1})/\sqrt{n}$, where q1, q2, and q3 are the first, second (median), and third quartiles, respectively, and $n$ is the number of observations (McGill et al., 1978).

The difference between the mean beat patterns of the WT and Crisp2 KO samples is striking. The KO samples exhibit a smaller amplitude across the entire flagellar tail. In Figure 4B, C, we apply the idea of calculating mean cycles to the energetic variables calculated from the four-mode C-POD of the tangent-angle profiles. Figure 4B compares the mean cycles in the net rates of elastic storage, ($E˙$; yellow), hydrodynamic ($P^{hd}$; black) and internal frictional ($P^{id}$; magenta) dissipations, and the net rate of motor power input ($P^{a}$; red curves). At each time phase, τ, in a beat cycle, these mean rates are calculated by collecting the values of $E˙$, $P^{hd}$, $P^{id}$, and $P^{a}$ from all the cycles and averaging those values. No distinctive common patterns are immediately apparent across the WT or KO samples in Figure 4B. In 7 of the 10 samples, the minimum value in $P^{a}$ ($P_{min}^{a}$; black symbols in Figure 4B) occurs close to the beginning or end of the cycle, when the first shape mode is dominant, suggesting that the first shape mode could be associated with a state of minimum power input. In two of the KO samples (KO-1 and KO-5), however, the net motor power remains nearly constant over the entire cycle.

It is visually apparent from Figure 4B that the mean cycles of the energy flows vary considerably from sample to sample. We plot the distributions of cycle times for each of the WT (Figure 4C; top panel, i) and KO (bottom panel, i) samples. Also shown as box-plots are the statistical distributions of the magnitudes of the cycle-averaged hydrodynamic, passive internal friction and motor dissipation powers. The cycle power in any single cycle is calculated by integrating an instantaneous power with respect to time over that cycle and dividing by the cycle time for that cycle. In the following sections, we use this data to answer two questions. Firstly, how large are the internal dissipations due to passive and motor friction relative to the external hydrodynamic dissipation? Secondly, what is the effect of the Crisp2 gene deletion on flagellar energetics?

### Internal dissipation is larger than external hydrodynamic dissipation

The novel finding in Figure 4B, C is that, for any WT or KO sample, the magnitudes of the internal frictional and motor dissipations are comparable to or larger than the dissipation in the external fluid. Before we examine this further, it must be reiterated that the results in Figure 4 for these dissipation rates depend on the values of the material parameters $κ_{n}$ and $η_{n}$. As previously mentioned, we have used here $κ_{n}= 7\times10^{4}$ Pa μm4 based on experimental measurements elsewhere (Lindemann and Lesich, 2016). While the existence of internal friction in the fluid-filled region around the axoneme is expected (Riedel-Kruse et al., 2007; Mondal et al., 2020), direct measurements of the value of $η_{n}$ are not available.

For the same sperm motion quantified by the tangent-angle C-POD, we have calculated the energetics with different values of $η_{n}$, ranging from zero to values well above the scaling estimate of 103 Pa s μm4. For any value of $η_{n}$, we robustly find negative domains in the active power distribution, $p^{a}$. However, as Figure 5A shows, for the 10 sperm samples studied, the minimum value of the net motor power delivered in a mean cycle, $P_{min}^{a}$, has a strongly negative value when $η_{n}$ is much smaller than 103 Pa s μm4. For such values of $η_{n}$, there is a significant portion of the mean cycle when $P^{a}$ is negative. This would mean that, in that phase of the mean cycle, the axoneme does not drive the motion of the flagellum, but rather, the majority of the motors are being driven backward. The overall motion of the flagellum during that phase of the cycle is powered mostly by the release of the potential energy stored elastically in the body of the flagellum. This appears to be physically unrealistic. On the other hand, Figure 5A shows that, above $η_{n}= 10^{3}$, although $p^{a}$ has negative domains, the net instantaneous power is always positive since its minimum value in the mean cycle, $P_{min}^{a}$, is positive. With a value of $η_{n}> 10^{3}$, the motion of the flagellum is always driven by the power input from the axoneme at all times during the beat cycle.

![Figure 5.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig5-v2.jpg)

**Figure 5.:** (A) Effect of the value of internal friction coefficient, $η_{N}$, on the minimum value of the net active power required to overcome dissipation for wildtype (WT) (blue) and knockout (KO) (red) samples. At each $η_{N}$, and for each sample, the minimum in the mean cycle of the net active power, $P_{min}$, is normalized by the time average of the motor input, $P¯¯^{mi}$, over all cycles. The vertical line is the scaling value of 103 Pa s μm4. (B) Correlation of time averages of the hydrodynamic dissipation and net active power for $η_{N}=10^{3}$ Pa s μm4 (top) and 0 (bottom). The lines are linear fits through data for both species. (C) Comparison of the external hydrodynamic dissipation (black) with the motor (blue) and passive internal frictional (magenta) dissipations obtained with $η_{N}=10^{3}$ Pa s μm4 (left) and 0 (right). The bars represent the averages of the cycle-means of dissipations pooled from all the five sperm samples in each genotype; the error bars represent 1 standard deviation in each direction in the set of pooled cycle-means. (D) Statistical distributions of the cycle-means of powers from the WT (dark color boxes) and KO (light color boxes) samples pooled together over the entire tail (left), mid-piece (middle), and principal piece (right). The top and bottom panels are for $η_{N}=10^{3}$ Pa s μm4 and 0, respectively. In (C) and (D), unpaired two-tailed t-tests are used to compare population means; **** refers to a significance level of $p\leq10^{-4}$ , *** $p\leq10^{-3}$, ** $p\leq10^{-3}$, *$p\leq0.05$. Differences are not significant (n.s.) when $p>0.05$.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Comparison of population means of time-averaged dissipations obtained with the five wildtype and Crisp2 knockout mice sperm samples obtained with (A) $η_{N}$=103  Pa.s.m4 and (B) $η_{N}$ = 0 Pa.s.m.Error bars shown correspond to 1 standard deviation in the set of samples. Unpaired two-tailed t-tests are used to compare population means; ** $p\leq10^{−3}$, *$p\leq0.05$. Differences are not significant (n.s.) when $p>0.05$.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Comparison across genotypes of population means of time-averaged powers obtained with the five wildtype and Crisp2 knockout mice sperm samples o $η_{n}$=103  Pa.s.m4 is shown in A and $η_{n}$ = 0 Pa.s.m4 in B.Error bars shown correspond to 1 standard deviation in the set of samples. Unpaired two-tailed t-tests are used to compare population means; **$p\leq10^{-3}$, *$p\leq0.05$. Differences are not significant (n.s.) when $p>0.05$.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Comparison of pooled averages of the cycle-means of hydrodynamic dissipation in the tail (black) and dissipation at head due to hydrodynamic and tethering resistances (purple): $p\leq10^{-3}$, *$p\leq0.05$. $η_{n}$=103  Pa.s.m4 is shown in A and $η_{n}$ = 0 Pa.s.m4 in B.Differences are not significant (n.s.) when $p>0.05$.

In Figure 5B, D, we plot results for the energetic variables obtained with $η_{n}=0$ and 103 Pa s μm4. With either value of $η_{n}$, Figure 5B shows that time averages, $P¯¯^{mi}$, of the net motor power input (Equation 73), calculated across all beat cycles in each sample, appear positively and linearly correlated with time averages, $P¯¯^{hd}$, of the hydrodynamic dissipation rate. This suggests that average hydrodynamic dissipation, which only needs the application of RFT, can be used as an indicator of the average motor input, which requires a more involved calculation. We find that the dissipation at the head against hydrodynamic and tethering forces is just a small fraction of the hydrodynamic dissipation across the tail region (Figure 5). Therefore, the excess of the time-averaged motor power input above the hydrodynamic dissipation is required to primarily overcome the different sources of internal dissipation in the tail.

Two different statistical approaches are possible for comparing the different kinds of dissipations within a genotypical population and for comparing the energetics across the WT and KO mice sperm. In the first approach, we can compare the population means of the time averages of samples. We recall that, for any single sperm sample, the arithmetic mean of the cycle-means of a quantity over all the cycles of that sample is the same as the time average for that sample. Within each genotype, a one-way ANOVA reveals that, for all the different energetic quantities, the time-average values of the individual sperm samples are distinctly different from the overall population mean for that genotype obtained by pooling all the cycles from the samples together ($p≪10^{-4}$; Appendix 2). In other words, there is significant sample-to-sample variation in the time averages of the energetic quantities. Due to the large sample-to-sample variation within each population, the standard deviations are large and although differences between the levels of the different sources of dissipation appear visually apparent, they are statistically not significant due to the small number of sperm samples (Figure 5). We, therefore, need to take the second approach and pool together all the individual cycles from each sample in a genotype to create a much larger set of individual time cycles for each genotype. With this approach, a clear picture emerges with statistical significance judged by unpaired, two-tailed Student's $t$-tests ($p≪10^{-4}$; Appendix 2). We observe in Figure 5C that motor dissipation is substantial when compared with the hydrodynamic dissipation. In the WT samples, with either value of $η_{n}$, the motor dissipation (135 fW) is clearly larger than the hydrodynamic dissipation (89.1 fW). In the KO samples, the motor dissipation (48.7 fW) is smaller than the hydrodynamic dissipation (66.3 fW), but of comparable magnitude. As discussed earlier, $η_{n}=10^{3}$ Pa s μm4 is the critical value in Figure 5A that is required to achieve a beat pattern wherein motors deliver net positive power across the whole beat cycle. Figure 5C shows that, at this value of $η_{n}$, dissipation due to internal friction (magenta) dominates above either motor (blue) or hydrodynamic dissipation (black bars) in either WT or KO samples. The data in Figure 5C thus leads us to conclude that, in wall-tethered WT as well as Crisp2 KO mice sperm beating in an aqueous medium, the total internal dissipation due to motor and internal friction is considerably larger than the external hydrodynamic dissipation.

The box-plots in Figure 5D summarize the statistics of the entire pool of cycle-averaged powers for each genotype obtained with $η_{n}=10^{3}$ Pa s μm4 (top panel) and with zero internal friction (bottom panel). We find that the net input from the dynein motors in sperm from Crisp2 KO mice is significantly smaller than the power input in the corresponding WTs. This is observed over the entire tail. We further find that each kind of dissipation – hydrodynamic, motor, or internal friction – is smaller in sperm from Crisp2 KO mice. These observations in Figure 5D are consistent with those in Figure 4A that the Crisp2 KO samples have smaller beating amplitudes over the entire flagellum. The rapidity of the beating, that is, the mean beat frequency, could also be an important factor in determining the rate of energy dissipation. In the samples studied here, however, due to the large variability in cycle times, we do not find a significant difference ($p>0.01$ in a Student's $t$-test; Appendix 2) between the population means of the cycle times (0.16 s and 0.18 s for WT and KO, respectively) or their reciprocals (7.19 Hz and 7.2 Hz, respectively) even after pooling the cycle times from the samples from each genotype together.

Further analysis of the spatial distribution of the dissipations between the mid-piece and principal piece is shown in Figure 5D and Table S-3. In both genotypes, the hydrodynamic dissipation occurs primarily due to the motion of the principal piece as expected. In contrast, most of the motor dissipation appears to occur in the mid-piece region in the WT population (average of 110 fW compared to 25.1 fW in the principal piece). In the KO samples, on the other hand, motor dissipation in both mid-piece and principal piece is similar (averages of 29.1 and 19.5 fW, respectively). With $η_{n}=10^{3}$ Pa s μm4, the average internal dissipation in the WT population in the mid-piece (108 fW) is similar to that over the entire principal piece (131 fW). However, in the KO population, the internal dissipation in the mid-piece (32.4 fW) is much lower than in the principal piece (168 fW) . This latter value is also higher than average internal dissipation in the KO samples, despite their more vigorous motion. The physical significance of this spatial distribution of the motor dissipations or the variations between the WT and KO species are not clear at this stage and require further detailed investigation.

## Discussion

In recent years, a number of studies have used image analysis of flagellar or ciliary waveforms to quantify beating patterns (Brumley et al., 2014; Sartori et al., 2016). Particle tracking (Guasto et al., 2010) or particle image velocimetry (Drescher et al., 2010) techniques have further provided a detailed picture of the dynamic velocity fields around beating filaments. These measurements have provided rich information on the nature of the beating patterns themselves (Ma et al., 2014; Werner et al., 2014; Wan et al., 2014) and on hydrodynamic quantities, such as the total hydrodynamic dissipation and flow features such as hydrodynamic singularities, vortices, etc. (Ishimoto et al., 2017; Brumley et al., 2014; Gallagher et al., 2019). Such measurements have further been used to test and refine models of axonemal dynamics (Riedel-Kruse et al., 2007; Mondal et al., 2020).

Our study contributes further to this body of work. Firstly, we have used the cycles in the phase space of POD shape coefficients to unambiguously split the data into individual time cycles. This enables the collection of data over several cycles and the calculation of mean cycles for all variables associated with flagellar beating. When used with tethered sperm, we can collect sufficient data to make statistically significant observations despite the large variability in beating patterns. Secondly, while studies have thus far focused on external hydrodynamics and internal forces, we have shown that energy flows within sperm flagella can be extracted using standard conservation principles. The Chebyshev-POD technique proposed here provides the smooth shape modes required for the calculation of the spatial derivatives that appear in the equations. We have shown that we can use these methods to compare, in a statistically meaningful manner, the energetics of different sperm populations.

This could potentially be used to systematically explore the effect of genetic mutations on sperm energetics. Here, we have demonstrated such comparison between sperm of WT and Crisp2 KO genotypes. The CRISPs are the sub-clade of the CAP superfamily proteins that are expressed in the male reproductive tract. Crisp2 is further known to be incorporated internally into the sperm flagellum (O'Bryan et al., 1998) and is expected to act by regulating ion channels on the cell or organelle membranes (Lim et al., 2019). Although CRISPs are not essential for fertility (Hu et al., 2018; Lim et al., 2019; Da Ros et al., 2008), we see here that a lack of Crisp2 significantly reduces the mechanical power input from the axoneme in sperm, which in turn appears to be responsible for slower beating with smaller amplitude.

Our results also reveal some fascinating new features of flagellar energetics that appear to be shared by all of our samples. We firstly see that along the filament there exist distinct phases during each cycle where dynein motors in the axoneme are driven back against the torques they exert by the motion of the rest of the flagellar body. It is known that dynein motors are regulated to create a traveling wave of forces, and hence turning moments, that propagates down the flagellum (Lin and Nicastro, 2018). Since the active power density $p^{a}=m^{a}⁢\omega$, the periodic occurrence of positive and negative domains in the active power distribution in Figure 3D shows that at any location along the tail $m^{a}$ and ω are in the same direction (i.e., of the same sign) in some parts of a beat cycle and in opposite directions (i.e., of opposite sign) in other parts of the cycle. In other words, the rotational velocity and the moment exerted by the dyneins are out of phase with one another, as shown in Figure 6.

![Figure 6.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig6-v2.jpg)

**Figure 6.:** Out-of-phase mean beat cycles of active moment density and angular rotation rate at $s=0.5$ in (A) wildtype (WT)-1 and (B) knockout (KO)-1 samples.

This is in line with current thinking on axonemal dynamics. Several ideas have been presented in the past for the generation of the beating patterns by the axoneme. In a landmark study, Riedel-Kruse et al., 2007 compared the predictions of many of these with experimental observations of planar beating in bull sperm that were either head-tethered or swimming freely in circles for long adjacent to a glass-slide wall. It was shown that the best agreement with experiments is obtained with the sliding-control model of Jülicher and co-workers (Camalet et al., 1999; Camalet and Jülicher, 2000). In this model (in the notation of the current paper), the active moment is related to the local internal shear and shear rate through an equation of the form $m^{a}=K⁢\gamma+\lambda⁢\partial⁡\gamma/\partial⁡t$, where γ is the local shear strain. In the parlance of control theory, this model proposes that motors are regulated by the location deformation through a mechanism that follows a proportional-derivative control logic. More recently, Mondal et al., 2020 suggested a variant with proportional-integral control logic instead, that is, where $m^{a}+\beta⁢\partial⁡m^{a}/\partial⁡t=K⁢\gamma$. In either case, when the equation for regulation of the active moment is coupled with the equations for the rest of the passive material of the flagellum, an oscillatory instability emerges in certain ranges of the controller constants. This triggers a traveling wave that propagates down the filament, leading to beating patterns that are similar to those observed experimentally . It is further found with these models that the controller constants to achieve oscillations are negative, indicating that the active moment exerted by the dynein motors is down-regulated by the load exerted back on the motors due to the local shear deformation in the filament and its time rate of change. This also appears to be consistent with the recent experimental finding that dynein motors are always primed to deliver forces on microtubules but are inhibited when a curvature wave passes through their location (Lin and Nicastro, 2018).

It is possible that regulation of $m^{a}$ could more generally be described by an equation of the form, $m^{a}+\beta⁢\partial⁡m^{a}/\partial⁡t=K⁢\gamma+\lambda⁢\partial⁡\gamma/\partial⁡t$, which corresponds to proportional-integral-derivative (PID) control. Such regulation of $m^{a}$ immediately means that, when stable traveling waves are generated, the local rotation rate, ω, (which is proportional to $\partial⁡\gamma/\partial⁡t$) will be systematically out of phase with $m^{a}$, as is indeed observed in Figure 6. There will necessarily, therefore, be phases in each cycle when the two variables will be of opposite sign and $p^{a}=m^{a}⁢\omega$ will always be negative in those phases.

The mechanical work done back on the motors during such phases by the passive elements of the filament must be quickly dissipated in some form since the motors cannot store the energy that is received nor reconvert it back to ATP. What, then, is the internal mechanism behind this additional dissipation? Riedel-Kruse et al. pointed out that the sliding-control model had to allow for relative sliding between microtubules at the basal end to obtain experimental agreement and that frictional resistance to basal shearing is important for the model to predict stable oscillations. Mondal et al. analyzed axonemes isolated by demembranating Chlamydomonas cilia and found that external hydrodynamic friction is too small to explain the stable beating pattern observed. They then showed that their sliding-control model predicts stable oscillations when coupled with equations that include passive filament elasticity and internal frictional resistance to the shear deformation rate. These sources of internal friction are not modeled in the present study, where we have treated the flagellum as an unshearable Kirchhoff rod. As Figure 5A shows, we find that, if internal friction is absent or insufficient, then the observed motion would mean that, for a significant duration of the mean cycle, the filament may as a whole be driving the motors backward. While this unphysical picture is eliminated when a sufficiently high internal friction coefficient is used, we still observe motor dissipation due to $m^{a}$ and ω being out of phase with one another.

The key point is that, while some or all of these different frictional contributions may be necessary for an internally driven filament to oscillate stably, if the local regulation of the active moment in general follows PID logic, then the out-of-phase moment and local deformation rate will lead to phases of negative active power, irrespective of the nature of internal or external friction. This points to the existence of a separate dissipative mechanism associated with the dynein motors themselves. There is already evidence that dyneins can dissipate energy locally. It is known that dynein motors can cycle through conformational changes driven by ATP binding and hydrolysis even when not driving microtubule sliding (Kon et al., 2005). Optical-tweezer experiments on dyneins bound to static microtubules have further shown that dyneins can steadily be driven in the reverse along the microtubule by an external load by forces larger than the stall force for these motors (Gennerich et al., 2007). The force required is more than that required to move unbound motors at the same velocity. This work done to drive the motors backward must be dissipated locally by a mechanism other than just the hydrodynamic frictional resistance of the motors to motion. Our results show that such motor dissipation can be a large part of the energy budget within the flagellum.

As pointed out above, our results in Figure 5 indicate that bending friction in the accessory structures surrounding the axoneme could also be significant. While most current models of flagella or cilia assume that the flagellum is a purely elastic filament, it is beginning to be recognized that internal friction plays an important role in flagella and cilia (Riedel-Kruse et al., 2007; Mondal et al., 2020; Klindt et al., 2016). An internal friction coefficient of $η_{n}=10^{3}$ Pa s μm4 is the minimum required to obtain physically realistic axonemal power input. It is possible that the internal coefficient is larger than this value. The ratio $η_{n}/κ_{n}$ represents a characteristic internal viscoelastic time scale for the passive flagellar material. If internal friction dominates the dynamics, we should expect to see the observed mean frequency of a beat cycle, $f¯∼κ_{n}/η_{n}$. The observed beat frequency of 7 Hz and $κ_{n}= 7\times10^{4}$ Pa μm4 suggests $η_{n}∼10^{4}$ Pa s μm4. Systematic measurements of the bending and other internal friction coefficients in flagella and cilia through single-cell microrheological techniques are therefore essential for a better understanding of their dynamics.

Our experiments were conducted with an aqueous buffer with cells beating close to a wall. It is natural to ask, therefore, how the results here would change with either medium viscosity or in the absence of the greater and more anisotropic hydrodynamic resistance due to wall. If the kinematics of the beating pattern remain unchanged, changes in medium viscosity or the distance from the wall would trivially result in changes in the magnitude of the hydrodynamic friction coefficients, and proportional changes in the contribution of hydrodynamic dissipation. However, the response to changes in the viscous resistance may be considerably more complex. It is known that the beating pattern changes dramatically with an increase in medium viscosity (Smith et al., 2009; Kirkman-Brown and Smith, 2011). Well away from a wall, the beating is non-planar, with helical traveling waves, and as sperm approach a wall, the beating becomes planar and cells appear to ‘slither’ quickly across the surface (Nosrati et al., 2015). Although the mechanisms behind these qualitative changes in beating waveforms are still unknown, it is likely that they are the result of the strong coupling of the motor regulation and the viscoelasto-hydrodynamics of the passive filament. With such changes in the waveform, the internal frictional and motor dissipation can also be expected to change appreciably. A related question pertains to the effect of the tethering constraint at the head. The constraint results in an additional force and torque being imposed at the head. Removing the constraint will alter the external loading on the cell and may result in a qualitatively different beating pattern and energetics. We nonetheless expect that, even in freely swimming sperm, motor dissipation and internal friction will be important.

Moreover, our observations of the effect of the Crisp2 mutation on the waveform and energetics are also likely to be independent of the effect of the tethering. The smaller beating amplitudes result in a smaller motor dissipation in the KO samples that is similar in magnitude with the smaller hydrodynamic dissipation in those samples, whereas in the WT samples, the motor dissipation is clearly larger than the hydrodynamic dissipation. The approach presented here can similarly be used to systematically explore the role played by other proteins and signaling agents on the internal dynamics and energetics of flagellar beating.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>Crisp2</td>
      <td>Lim et al., 2019</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>C57BL/6N</td>
      <td>Lim et al., 2019</td>
      <td>PMID:30759213</td>
      <td>Mice produced through the Australian Phenomics Network</td>
    </tr>
    <tr>
      <td>Biological sample (Mus musculus)</td>
      <td>Sperm</td>
      <td>Lim et al., 2019</td>
      <td>-</td>
      <td>Collected from the cauda epididymis and vas deferens using the backflushing method</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TYH medium with 0.3 mg/ml BSA</td>
      <td>Lim et al., 2019</td>
      <td>-</td>
      <td>Buffer media for sperm</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB, MATLAB Image Processing Toolbox, Fiji</td>
      <td></td>
      <td>SCR 001622,SCR 002285</td>
      <td>Code (Nandagiri, 2021) and original videos (Nandagiri et al., 2020) available for public access</td>
    </tr>
  </tbody>
</table>

### Sperm sample preparation

Generation of KO mouse models and all animal procedures were approved by the Monash University Animal Experimentation Ethics Committee. The mouse KO line were maintained on a C57/BL6N background. Sperm were collected from cauda epididymis and vas deferens using the back-flushing method (Lim et al., 2019) in modified TYH medium (135 mM NaCl, 4.8 mM KCl, 2 mM CaCl2, 1.2 mM KH2PO4, 1 mM MgSO4, 5.6 mM glucose, 0.5 mM Na-pyruvate, 10 mM L-lactate, 10 mM HEPES, pH 7.4). The samples were stored in dark at 37 °C until imaging. Sperm samples WT-1 and -2 were from the same individual, WT-3 and -4 were from another individual, and WT-5 was from a third individual mouse. All the five KO samples were from separate individuals.

### Tethering and imaging

Sperm motility was investigated in a custom-made observation chamber. Briefly, two strips of double-sided tape (90 μm nominal thickness) were affixed to a glass slide 16 mm apart. A drop of 40 μl of sperm suspension was placed between the two strips and sealed against evaporation with 17 mm square coverslips (Thermo Fisher Scientific, No. 1.5).

Mouse sperm have flat falciform (hook-shaped) heads. A detailed study by Woolley, 2003 showed that freely swimming mouse sperm are hydrodynamically drawn to walls and mostly stabilize with the left sides of their flat heads held against the surface. It was also found that the plane of the left side of the flat head makes an angle less than 180° with the flagellum at the neck. This enables sperm following the left-side rule to stabilize to beating in a plane parallel to the wall.

We have taken advantage of this nearly planar beating close to walls to design our experiments. In our experiments, the TYH medium was supplemented with 0.3 mg/ml of BSA, which causes sperm swimming at the wall to adhere to the glass slide at the bottom of the imaging chamber. The out-of-plane excursions in the resolved portion of the tail appear limited to less than 2 μm (Appendix 2). This beating is clearly resolvable within the depth of field of the microscope. Sperm tethered at their heads with flagella beating freely within the focal plane were chosen for video imaging and subsequent analysis. Imaging is done from above the sperm cell.

An Olympus AX-70 upright microscope equipped with a U-DFA 18 mm internal diameter dark-field annulus, an 20 × 0.7 NA objective (UPlanAPO, Olympus, Japan), and incandescent illumination served as the platform for the imaging system. All extraneous optical elements were removed from the detection light paths to maximize system light efficiency. An ORCA-Flash4.0 v2+ (C11440-22CU) sCMOS camera (Hamamatsu, Japan) was used for capturing images. This system leverages a high frame rate for motion capture, an exceptional 82% QE for the low level of light and the small 6.5 μm pixel size to increase system spatial resolution (Stuurman and Vale, 2016; Beier and Ibey, 2014; Saurabh et al., 2012).

The optical lateral resolution was 0.479 μm at a reference wavelength of 550 nm. With the 6.5 μm pixel size of the ORCA sCMOS and the system magnification factor of 20, the best-case lateral resolution of 0.650 μm (0.325 μm/pixel) at the Nyquist–Shannon sampling was sufficient to spatially resolve the tip of the sperm tail. A 512 × 512 pixel region of interest therefore corresponded to an experimental sample FOV of 166.4 × 166.4 μm, which was sufficient for most of the experiments reported here. Occasionally, sperm with stiffer flagella required an FOV increase with a reduction of approximately 0.8 frames per second (fps) for each pixel increase.

Image data was free-streamed to a Xeon E5-2667 computer (with a 12-core CPU running at 2.9 GHz supplemented by 64 GB of DDR3 RAM and 1 TB SSD hard drive in a RAID0 configuration) via a dedicated Firebird PCIe3 bus 1xCLD Camera Link frame-grabber card (Active Silicon, UK) at the 8.389 MB/s memory buffer speed of the camera. This resulted in a capture frame rate of approximately 400 fps. The best-case blur-free motion capture of the system at this frame rate corresponds to element point velocities of 130 μm/s. The Fiji image-processing package was used for image capture control along with the Micro-Manger Studio plugin (version 1.4.23) for multidimensional acquisition (Beier and Ibey, 2014) set to 4000 time points, zero time point interval, a 2.0 ms exposure time. The data was written as an image stack.

Camera resolution can be increased to exceed optical resolution by replacing the 180 mm tube lens with a 250 mm tube lens. The region of interest would then increase to 714 × 714 pixels, with the capture frame rate being reduced to approximately 286 fps. Frame exposure can be likewise increased to 3.25 ms to allow for a superior signal-to-noise ratio.

### Image analysis and skeletonization

The videos of the sperm samples are available for public access (Nandagiri et al., 2020). The mean of the grayscale intensity at each pixel location across all the frames was used to construct a background image. This was then subtracted from each frame to remove the background. The contrast was then adjusted to enhance the foreground grayscale intensity. Median filters of different sizes were applied to remove noise. The grayscale image was then smoothened with a Gaussian filter before binarization at a threshold computed by Otsu’s method (Otsu, 1979). Connected components in the binarized image were then located and classified according to size and eccentricity. The sperm body is expected to have the largest size among the objects in the frame. An oval (i.e., an ellipse) is fitted around each body. The eccentricity is a measure of the deviation of the oval from a perfect circle. An oval fitted around the whole sperm body will be highly elongated and will have a high eccentricity. These two criteria were used to automatically identify the sperm body in each frame and remove other extraneous objects. Morphological thinning was then applied to the segmented image to extract a skeleton of the sperm tail. Spurious branches on the skeleton were automatically identified and removed to give an unbranched skeleton. The skeleton at this stage is rough, with noisy burrs that are then smoothed out using low-pass filtering. The resulting smoothed curve representing the sperm body is henceforth referred to as the centerline (Figure 7). Since the algorithm treats each frame independently of all others, frames were processed on separate processors on a high-performance computational cluster.

![Figure 7.](https://cdn.elifesciences.org/articles/62524/elife-62524-fig7-v2.jpg)

**Figure 7.:** A. The original frame B. Enhanced and filtered C. Thresholded frame D. Segmented E. Skeletonized frame F. Smoothed centreline.

The arc length between each adjacent pair of points was calculated and the overall contour length of the centerline in each frame was obtained. Motion of the sperm body out of the plane of focus leads to blurring and loss of contrast and intensity of the image, which in turn increases errors in the automated processing of the images. This is particularly problematic at the tail end of the flagellum. As a result, the skeleton obtained is truncated at the tail end, resulting in a loss of total contour length of the captured skeleton. Videos with significant loss of length were discarded, and only videos showing largely in-plane beating, with deviations smaller than 10% from the mean contour length, were considered for further analysis. In each of the samples selected for further analysis, the maximum contour length across all the video frames is taken to be the cell body length, $L$.

For each video, the time-averaged end-to-end straight line was first determined. Sperm centerlines in every frame were rotated by an angle to align this line with the horizontal $x$-axis. The centerlines in a video were reflected about the horizontal axis if necessary to orient the head-hook concave downwards in all videos. At this stage, the pixel points on the centerline were not uniformly distributed along the length of the sperm body. That is, the arc length between each adjacent pair of points is not the same along the centerline. The $x$ and $y$ coordinates for each centerline point were linearly interpolated to obtain a large number of points (∼200) distributed uniformly with the same difference in the arc length $s$ between adjacent points. Frames were also not always equally spaced in time since poor-quality frames were discarded. Linear interpolation in time was applied across the two frames on either side of a missing frame to compute the centerline in the missing frame. Tangent angles to the horizontal were computed at each $s$ in every frame. A Butterworth low-pass filter was used to spatially smoothen the tangent-angle-versus-$s$ data in each frame. The values of $s$ in each frame are normalized by the body length, $L$.

### Data processing

The head and imaged-tail regions are defined as $s\in[0,s_{N}]$ and $s\in[s_{n},s_{t}]$, where $s_{n}= 0.1⁢L$, and $s_{T}$ is the maximum value of $s$ for which pixel data is available for every time sample (typically, $s_{T}=0.85L$). Since the data for $s>s_{T}$ is not available at all time steps, this data is neglected.

When working with Chebyshev polynomials in the tail region, we define a rescaled variable that maps the domain $[s_{N},s_{T}]$ onto $[-1,1]$:

$$
ξ=2(\frac{s−s_{N}}{s_{T}−s_{N}})−1.
$$

The inner product of a pair of functions $f$ and $g$ with respect to the Chebyshev weighting function $w(ξ),= 1/\sqrt{1-ξ^{2}}$ is defined as $(f,g)=\int_{-1}^{1}f⁢(ξ)⁢g⁢(ξ)⁢w⁢(ξ)⁢𝑑ξ$ . The norm of $f$, $∥f∥=\sqrt{(f,f)}$. We further denote time averages, $t_{m⁢a⁢x}^{-1}⁢\int_{0}^{t_{max}}…⁢𝑑t$ as $⟨…⟩$.

There are four stages in calculating flagella energetics, starting from the raw tangent-angle data obtained from the centerlines after image processing. This original tangent-angle function is denoted as $ψ^$.

Each of these stages is described further below.

#### Intermediate tangent-angle profile

The raw centerline data $ψ^$ in the head region does not satisfy the rigid-body motion conditions since the large and diffuse image of the head leads to errors during skeletonization in identifying its centerline consistently. The sufficient condition that the head region rotates about a single point as a rigid body is that $\partial⁡C/\partial⁡t=\partial⁡\omega/\partial⁡s=0$. To impose this, the time-averaged tangent-angle profile $ψ~_{0}⁢(s)=⟨ψ^⁢(s,t)⟩$ is first calculated from the raw data in this domain. Then, the tangent-angle profile in this domain is set to the following to ensure the rigid-body conditions:

$$
ψ~⁢(s,t)=ψ~_{0}⁢(s)+B~_{0}⁢(t),
$$

where

$$
B~_{0}⁢(t)=ψ^⁢(s_{n},t)-ψ~⁢(s_{n}).
$$

The time average of B0 is thus zero. The rotation rate, $\omega=\partial⁡ψ~/\partial⁡t=B~_{0}/d⁢t$, is uniform and non-zero for the whole head region. With this profile, the tangent values at the neck are given by $ψ_{n}⁢(t)=ψ~_{0}⁢(s_{n})+B~_{0}⁢(t)$. The time-independent $s$-derivatives, $ψ_{n}^{′}$ and $ψ_{n}^{′′}$ are determined from the values of $ψ~_{0}$ adjacent to the neck in second-order backward-difference formulae.

A Chebyshev polynomial,

$$
ψ~⁢(ξ,t)=\sumk= 0Pa_{k}⁢(t)⁢T_{k}⁢(ξ),
$$

of order $P=20$ is fitted to the data in the imaged tail region at each time, $t$. Here, $T_{k}$ is the $k$ th Chebyshev polynomial of the first kind (Hildebrand, 1987). The fitted Chebyshev polynomial must also satisfy boundary conditions at $ξ=-1$ so that it is $C^{2}$-continuous with the tangent profile of the rigid head region across the neck. No boundary conditions are imposed at the other boundary at $ξ= 1$ since that end of the imaged region is not the physical end of the tail. (The physical boundary conditions at the tail tip are accounted for through the energy balance [Equation 73], as discussed earlier.)

To ensure $C^{2}$-continuity across the neck, we must have at $ξ=-1$,

$$
ψ~⁢(-1,t)=ψ~_{n}⁢(t);\frac{\partial⁡ψ~}{\partial⁡ξ}|_{ξ=-1}=\frac{(s_{t}-s_{n})}{2}⁢ψ~_{n}^{′}⁢(t);\frac{\partial^{2}⁡ψ~}{\partial⁡ξ^{2}}|_{ξ=-1}=(\frac{s_{t}-s_{n}}{2})^{2}⁢ψ~_{n}^{′′}⁢(t),
$$

where $ψ~_{n}$, $ψ~_{n}^{′}$, and $ψ~_{n}^{′′}$ are the values of the tangent angle and its first two $s$-derivatives at the neck, respectively. These values at the neck are determined from the motion of the rigid head, as discussed above.

We determine the set of coefficients ak as those that minimize $S=∥ψ^-ψ~∥^{2}$, the mean square error between the raw data, $ψ^$, and the Chebyshev polynomial, $ψ~$, while also satisfying the boundary conditions at $ξ=-1$ in Equation (29). Using the properties of Chebyshev polynomials and Lagrange’s method of undetermined coefficients, and using standard methods and Gaussian quadrature to approximate integrals, we obtain

$$
a_{k}⁢(t)=a_{k}^{∗}⁢(t)+\frac{K_{1}}{2⁢\gamma_{k}}⁢(-1)^{k+1}+\frac{K_{2}}{2⁢\gamma_{k}}⁢(-1)^{k}⁢k^{2}+\frac{K_{3}}{2⁢\gamma_{k}}⁢(-1)^{k+1}⁢(\frac{k^{4}-k^{3}}{3}),
$$

where $\gamma_{k}=(1+\delta_{0,k})/(2⁢(P+1))$, $\delta_{i,j}$ is the Kronecker δ-function, K1, K2, and K3 are the Lagrange multipliers. The $k$ th unconstrained Chebyshev coefficient,

$$
a_{k}^{∗}⁢(t)=\frac{1}{\gamma_{k}}⁢\sumi=0Pψ^⁢(ξ_{i},t)⁢T_{k}⁢(ξ_{i}),
$$

where $ξ_{i}$ is the $i$ th root of the $P+1$ th Chebyshev polynomial (Hildebrand, 1987). The values of $T_{k}⁢(ξ_{i})$ can be calculated using standard recursion relations (Hildebrand, 1987). Substituting from Equation (30) in the boundary conditions into Equation (29) results in a system of linear equations that can be solved for the Lagrange multipliers. Inserting these values back into Equation (30) gives the Chebyshev coefficients in the imaged tail region. The resulting $ψ~$ is consistent with boundary conditions at the neck.

#### C-POD of the tail region

The C-POD provides advantages over the ‘empirical’ POD used previously for sperm (Werner et al., 2014; Ma et al., 2014). The empirical POD is applied directly on the discrete data to produce shape modes that are numeric vectors. The discrete nature of the modes makes high-order spatial derivatives computed from them susceptible to noise. The C-POD approach here allows derivatives to be computed without noisy artifacts. Further, specific restrictions on the shape at the boundaries can be conveniently imposed.

We first recall key aspects of the general POD technique to obtain the optimal mutually orthogonal basis functions. The Chebyshev polynomials $T_{k}$ themselves constitute a set of mutually orthogonal basis functions. At any $t$, $ψ~$ is a polynomial of order $P$ that is expanded in terms of $P+1$ Chebyshev polynomials. Given a small number $M<P+1$, say $M=2$, any linear combination of $M$ of the Chebyshev polynomials can be expected to be a poor approximation of the full $P$ th-order polynomial, $ψ~$. The technique of POD allows us to find a set, ${ψ_{m}}$, of $M$ unique orthogonal functions different from $T_{k}$ such that a linear combination of these provides the best approximation of $ψ~$ possible, given the choice of $M$. The gain is that we need to track only the set of $M$ coefficients ${B_{m}}$ as functions of time rather than the larger set of all the $P+1$ time-dependent Chebyshev coefficients, ${a_{k}}$.

The time-averaged profile in the imaged-tail region is $ψ_{0}⁢(ξ)=⟨ψ~⁢(ξ,t)⟩$. The deviation of the original function $ψ~⁢(ξ,t)$ from this time average is

$$
χ~⁢(ξ,t)=ψ~⁢(ξ,t)-ψ~_{0}⁢(ξ),
$$

and the spatial two-point cross-correlation of $χ~$ is

$$
C⁢(ξ,\mu)=⟨χ~⁢(ξ,t)⁢χ~⁢(\mu,t)⟩.
$$

It can be shown that the set of optimal basis functions for the POD are the eigenfunctions of this two-point cross-correlation (Lumley, 1967; Holmes et al., 2012). That is, an optimal shape mode, $ψ_{m}$, is such that

$$
(C⁢(ξ,\mu),ψ_{m}⁢(\mu))=\lambda_{m}⁢ψ_{m}⁢(ξ),
$$

where $\lambda_{m}>0$ is the corresponding eigenvalue. These eigenfunctions are mutually orthogonal, that is,$(ψ_{m},ψ_{n})=\delta_{m,n}$. The coefficient of the $m$ th shape mode is then obtained by projection as

$$
B_{m}⁢(t)=(χ~⁢(ξ,t),ψ_{m}⁢(ξ,t)).
$$

These coefficients are themselves orthogonal in time, that is, $⟨B_{m}⁢(t)⁢B_{n}⁢(t)⟩=\delta_{m,n}⁢\lambda_{m}$. The matrix algorithm for obtaining the time-independent Chebyshev coefficients of the shape modes is as follows. The Chebyshev polynomials are first normalized as follows:

$$
\tau_{m}⁢(ξ)=\frac{1}{\sqrt{\gamma_{m}}}⁢T_{m}⁢(ξ)
$$

so that the inner product (with the Chebyshev weighting function) $(\tau_{m},\tau_{n})=\delta_{m,n}$. The Chebyshev coefficients ak of $ψ~$ are correspondingly rescaled as $\alpha_{k}=\sqrt{\gamma_{k}}⁢a_{k}$, so that $ψ~⁢(t,ξ)=\sum_{k=0}^{P}\alpha_{k}⁢(t)⁢\tau_{k}⁢(ξ)$. The Chebyshev coefficients of the time-averaged tangent-angle profile, $ψ_{0}⁢(ξ)$, and the deviation from the mean, $χ~$, are then $⟨\alpha_{k}⁢(t)⟩$ and $Δ⁢\alpha_{k}⁢(t)=\alpha_{k}⁢(t)-⟨\alpha_{k}⁢(t)⟩$, respectively. From Equation (34), the cross-correlation, $C⁢(ξ,\mu)=\sum_{l=0}^{P}\sum_{k= 0}^{P}\tau_{k}⁢(ξ)⁢A_{k⁢l}⁢\tau_{l}⁢(\mu)$, where

$$
A_{k⁢l}=⟨Δ⁢\alpha_{k}⁢(t)⁢Δ⁢\alpha_{l}⁢(t)⟩.
$$

The symmetric matrix $𝐀$ composed of $A_{k⁢l}$ is equivalent to the cross-correlation matrix. Diagonalizing the matrix $𝐀=𝐕⋅𝚲⋅𝐕^{T}$ yields the $P+1$ eigenvalues, ${\lambda_{m}}$, of the correlation operator as the diagonal elements of the matrix, $𝚲$. The $m$ th column of $𝐕$ is the $m$ th eigenvector of $𝐀$. Its elements are the Chebyshev coefficients of the $m$ th shape mode:

$$
ψ_{m}⁢(ξ)=\sumk= 0PV_{k⁢m}⁢\tau_{k}⁢(ξ).
$$

The corresponding shape coefficient can be obtained from the equation above and from Equation (35) as

$$
B_{m}⁢(t)=\sumk= 0PΔ⁢\alpha_{k}⁢(t)⁢V_{k⁢m}.
$$

With $ψ_{m},$ and $B_{m}$ thus determined from the original cross-correlation of $χ~$, we can obtain the C-POD approximation, ψ, given by Equation (17) for any choice of $M\leqP+1$. The deviation of the C-POD approximation from the mean,

$$
χ=ψ-ψ_{0}=\summ=1MB_{m}⁢(t)⁢ψ_{m}⁢(ξ),
$$

is an approximation of the original $χ~$. The approximation improves with increasing $M$ and when $M=P+1$, $χ=χ~$ exactly, since the full set of $P+1$ eigenfunctions ${ψ_{m}}$ spans the same function space that is spanned by the set of $P+1$ Chebyshev polynomials, ${T_{k}}$. Further, using the orthogonality of the shape modes, it can be shown that

$$
⟨∥χ~∥^{2}⟩=\summ=1P+1\lambda_{m};⟨∥χ∥^{2}⟩=\summ=1M\lambda_{m}.
$$

Therefore, the mean-squared error in the approximation when $M<P+1$,

$$
⟨∥ψ-ψ~∥^{2}⟩=⟨∥χ-χ~∥^{2}⟩=\summ=1P+1\lambda_{m}-\summ=1M\lambda_{m}=⟨∥χ~∥^{2}⟩-⟨∥χ∥^{2}⟩.
$$

We can, therefore, use the ratio of the cumulative sum of the eigenvalues for any $M$, normalized by the sum of all the $P+1$ eigenvalues,

$$
Γ_{M}=\frac{\sum_{m=1}^{M}\lambda_{m}}{\sum_{m=1}^{P+1}\lambda_{m}}= 1-\frac{⟨||χ-χ~||^{2}⟩}{⟨||χ~||^{2}⟩}.
$$

as a measure of the accuracy of the $M$ th order C-POD representation: the closer $Γ_{M}$ is to 1, the better ψ captures $ψ~$. As discussed earlier, $ψ~$ is constructed to be consistent with the neck boundary conditions (in Equation 29) at all times. The C-POD basis functions, $ψ_{m}⁢(ξ)$, that span this function space, therefore, also satisfy the same neck boundary conditions.

#### Calculation of flagellar kinematics and dynamics

The equations in the section on The soft, internally driven Kirchhoff rod model are used to calculate the active power distribution in the following manner:

#### Mean beat cycles

The time-dependent coefficients of the dominant shape modes, B1 and B2, are plotted against one another. Individual beat cycles are identified from the times at which the polar angle of a point in this B1–B2 space is zero. In other words, a beat cycle starts when the flagellar shape is a scaled version of the first shape mode, $ψ_{1}$. The time phase within the $i$ th beat cycle is then calculated as

$$
\tau=\frac{(t-t_{i}^{0})}{T_{i}},
$$

where $t_{i}^{0}$ is the starting time of the $i$ th cycle and $T_{i}=t_{i+1}^{0}-t_{i}^{0}$ is the time period of that cycle.

Functions such as $p^{a}⁢(s,t)$ and $P^{a}⁢(t)$ are split into individual beat cycles and, in each cycle, expressed as functions of the time phase, τ. The mean of that function over the set of its cycles is computed at each τ, as is the SEM. Between 40 and 60 beat cycles were captured for each sperm sample. These beat cycles are used for statistical analysis either for each sample, or for each genotypical population, as required. The mean beat cycles of beating patterns and their shaded error bands in Figure 4B have been obtained in this manner and by applying the graphing tools provided in Campbell, 2020. The averaged powers, $P¯¯_{h}^{d}$, $P¯¯^{hd}$, $P¯¯^{id}$, $P¯¯^{md}$, and $P¯¯^{mi}$, are computed as the averages of the corresponding cycle-means over all beat cycles in either the set of samples or the set of pooled cycles, as required.
