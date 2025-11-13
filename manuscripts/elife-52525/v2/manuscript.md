# Shape selection and mis-assembly in viral capsid formation by elastic frustration

## Authors

- Carlos I Mendoza<sup>1</sup> ([ORCID: 0000-0001-9769-240X](https://orcid.org/0000-0001-9769-240X)) †
- David Reguera<sup>2</sup> ([ORCID: 0000-0001-6395-6112](https://orcid.org/0000-0001-6395-6112))

### Affiliations

1. Instituto de Investigaciones en Materiales, Universidad Nacional Autónoma de México México Mexico
2. Departament de Física de la Matèria Condensada, Universitat de Barcelona Barcelona Spain
3. Universitat de Barcelona Institute of Complex Systems (UBICS), Universitat de Barcelona Barcelona Spain

† Corresponding author

## Abstract

The successful assembly of a closed protein shell (or capsid) is a key step in the replication of viruses and in the production of artificial viral cages for bio/nanotechnological applications. During self-assembly, the favorable binding energy competes with the energetic cost of the growing edge and the elastic stresses generated due to the curvature of the capsid. As a result, incomplete structures such as open caps, cylindrical or ribbon-shaped shells may emerge, preventing the successful replication of viruses. Using elasticity theory and coarse-grained simulations, we analyze the conditions required for these processes to occur and their significance for empty virus self-assembly. We find that the outcome of the assembly can be recast into a universal phase diagram showing that viruses with high mechanical resistance cannot be self-assembled directly as spherical structures. The results of our study justify the need of a maturation step and suggest promising routes to hinder viral infections by inducing mis-assembly.

## Introduction

Viruses are fascinating biological and nanoscale systems (Douglas and Young, 2006; Wen and Steinmetz, 2016). In the simplest cases, these tiny pathogens are formed by a chain of RNA or DNA encased in a protein shell, also known as capsid, made from multiple copies of a single protein (Flint et al., 2004). Despite this apparent simplicity, viruses are able to perform many complex functions which are essential in their replication cycle. One of the most amazing one is their ability to self-assemble with an unparalleled efficiency and precision.

In vivo, the capsid of most viruses assembles from its basic building blocks, which could be individual capsid proteins, dimers, trimers or capsomers (i.e. clusters of five or six proteins, which constitute the structural and morphological units of the shell). The resulting structure has a precise architecture, which in most cases is spherical with icosahedral symmetry (Roos et al., 2010). Several viruses assemble their capsid before packaging the genetic material. In addition, the proteins of many viruses have the ability to self-assemble in vitro, even in the absence of genetic material, forming empty capsids.

The mechanisms of viral assembly have been the subject of recent and interesting investigations (Hagan and Chandler, 2006; Elrad and Hagan, 2008; Nguyen et al., 2009; Johnston et al., 2010; Perlmutter and Hagan, 2015; Hagan and Zandi, 2016). The assembly of a curved empty shell with a well-defined geometry and precise arrangement of the building blocks is a non-trivial process that resembles 2D crystallization on a curved space (Meng et al., 2014; Gómez et al., 2015). It also shares similarities with the formation of other related structures such as colloidosomes (Meng et al., 2014; Dinsmore et al., 2002; Manoharan et al., 2003), carboxysomes (Perlmutter et al., 2016; Garcia-Alles et al., 2017) or clathrin-coated pits (Mashl and Bruinsma, 1998; Kohyama et al., 2003; Giani et al., 2016). Capsid formation occurs via a nucleation process driven by the favorable binding energy between capsid proteins (Zandi et al., 2006). At the right assembly conditions, thermal fluctuations induce the formation of small partial shells that tend to redissolve unless they reach a minimum critical size. Beyond this size, the shell grows by the progressive binding of subunits. As growth continues, the energy penalty of the naturally curved structure, due to the inescapable presence of the rim and the accumulation of elastic energy, can be larger than the favorable binding energy. This generates a natural self-limiting mechanism for the formation of partial shells of a finite size that do not grow until closing (Grason, 2016). In fact, there are in vitro experimental evidences of apparently stable partial capsids (Law-Hine et al., 2016), that seems to contradict the instability of intermediates that follows from Classical Nucleation Theory (CNT) (Zandi et al., 2006).

Recently, there has been a lot of interest in geometric frustration and crystal growth on spherical templates (Zandi et al., 2004; Luque et al., 2012; Meng et al., 2014; Gómez et al., 2015; Grason, 2016; Azadi and Grason, 2016; Paquay et al., 2017; Li et al., 2018; Panahandeh et al., 2018). Most previous works have focused either on templated growth on the surface of a sphere (Zandi et al., 2004; Luque et al., 2012; Meng et al., 2014; Gómez et al., 2015; Grason, 2016; Li et al., 2018; Panahandeh et al., 2018) or on analyzing the optimal shape of the resulting shell from pure elastic considerations (Paquay et al., 2017; Lidmar et al., 2003; Schneider and Gompper, 2007; Morozov and Bruinsma, 2010; Castelnovo, 2017), ignoring the importance of the delicate interplay of other ingredients such as the line tension, the chemical potential or the preferred curvature on their global stability and their process of formation.

Here, we analyze the conditions and mechanisms leading to mis-assembly of empty viral capsids by elastic frustration, taking into account all these ingredients. We find that the outcome of the assembly depends on three scaled parameters that can be properly tuned to trigger the formation of non-spherical and open shells. Theoretical predictions obtained with the use of Classical Nucleation Theory including elastic contributions are confirmed qualitatively using Brownian Dynamics simulations of a simple coarse-grained model. The results of this work help to better understand viral assembly and might have important implications in: envisaging novel routes to stop viral infections by interfering with their proper assembly; determining the optimal conditions for the assembly of protein cages with the desired geometry and properties for nanotechnological applications (Douglas and Young, 2006); and justifying the potential presence of seemingly stable intermediates that have been observed in recent experiments (Law-Hine et al., 2016).

## Results

### Self-assembly of a curved elastic shell

The continuous description of the assembly of empty spherical viral capsids is based on Classical Nucleation Theory (CNT) (Zandi et al., 2006). In its standard version, the free energy of formation of a partial shell of area $S$ is seen as the competition of an energy gain driving the assembly, and a rim energy penalty, due to the missing contacts at the edge of the shell. Due to the curvature of the shell and the existence of a preferred angle of interaction between capsid proteins there is another ingredient that has to be considered in the energetics of capsid formation: the elastic energy. Accordingly, the free energy of formation of a partial capsid of area $S$ can be modeled as

$$
Δ⁢G=-S⁢\frac{Δ⁢\mu}{a_{1}}+Λ⁢l⁢(S)+G_{e}.
$$

The first term represents the gain in free energy associated with the chemical potential difference $Δ⁢\mu$ between subunits in solution and in the capsid, being $a_{1}$ the area per subunit. (With this definition, a positive $Δ⁢\mu$ is required to promote assembly). The second term is the total line energy of the rim, given by the product of the line tension $Λ$ times its length $l⁢(S)$. Finally, the third term $G_{e}=G_{s}+G_{b}$ is the elastic energy associated with the in-plane stress, $G_{s}$, and the bending, $G_{b}$, energies introduced by the curvature of the shell. Both elastic terms will be modeled using continuum elasticity theory. For the bending energy we will use the generalization of Helfrich’s model for systems with non-zero spontaneous curvature introduced recently by Castelnovo (2017) (see the Appendix). For the in-plane elastic energy, we will use results from continuum elasticity theory for small deformations of thin plates, building up on recent work on the formation and growth of crystal domains of different shapes on curved surfaces (Lidmar et al., 2003; Meng et al., 2014; Seung and Nelson, 1988; Morozov and Bruinsma, 2010; Grason, 2016; Paquay et al., 2017; Köhler et al., 2016; Schneider and Gompper, 2007; Majidi and Fearing, 2008; Castelnovo, 2017). Both stretching and bending terms depend on the particular structure of the growing shell. Four different cases will be analyzed: hexagonally-ordered spherical cap without defects; spherical cap with one or many defects; ribbon and cylinder (see Figure 1). The reason to consider these particular structures is that they represent the most advantageous shapes to release the unfavorable elastic energy. In addition, cylindrical shells also appear frequently as outcome of in vitro assembly experiments. However, it is important to stress that the considered structures do not form a complete set of deformations.

![Figure 1.](https://cdn.elifesciences.org/articles/52525/elife-52525-fig1-v2.jpg)

**Figure 1.:** (a) A hexagonally-ordered spherical cap of radius $R$ and geodesic radius $ρ_{0}$ without defects; (b) a spherical cap with a single disclination at the center (as shown) or multiple disclinations; (c) a rectangular ribbon with length $L$ and width $W$, that it is called belt when the length becomes $L=2⁢\pi⁢R$; and (d) a cylindrical patch with size $L$, that eventually becomes a cylinder of radius $R$. In the bending-dominated regime, $R=R_{0}$.

The relative importance of stretching versus bending contributions is controlled by a single dimensionless parameter: the Föppl-von Kárman number (FvK) defined here as $\gamma≡YR_{0}^{2}/κ$, where $Y$ is the two-dimensional Young’s modulus, $R_{0}$ is the spontaneous radius of curvature and $κ$ is the bending modulus. Most previous studies have focused on the elastic energy and growth of crystals on top of a spherical template of fixed radius $R$. This case resembles the bending-dominated regime discussed below.

### Bending-dominated regime

In the limit $\gamma=Y⁢R_{0}^{2}/κ≪1$, the bending energy dominates over the stretching energy and thus, all structures will adopt their spontaneous curvature, $R=R_{0}$. The situation will be similar to the growth of a crystal on a template of fixed curvature. In the bending-dominated regime, the free energy of formation of all these structures, when properly scaled by the characteristic elastic energy $4⁢\pi⁢R_{0}^{2}⁢Y$, only depends on two parameters: the scaled chemical potential $Δ⁢\mu~≡Δ⁢\mu/(Y⁢a_{1})$ and the scaled line tension $\lambda≡Λ/(R_{0}⁢Y)$. Thus, it is possible to compare them and determine the most stable structure for a given set of conditions. The comparison is performed for different shapes having the same area $S$ , that is having the same number of subunits.

The scaled free energy of formation of a hexagonally-ordered spherical cap of radius $R_{0}$ without defects made of a circular patch of radius $ρ_{0}$ (see Figure 1a) is

$$
Δ⁢g_{c⁢a⁢p}=-\frac{Δ⁢\mu~}{4}⁢x^{2}+\frac{\lambda}{2}⁢x+\frac{1}{1536}⁢x^{6}
$$

where $x≡ρ_{0}/R_{0}$ is the scaled patch size, and the third term is the in-plane elastic energy of a circular domain on a curved spherical surface (Schneider and Gompper, 2007; Meng et al., 2014; Morozov and Bruinsma, 2010). (Equation 2 is an approximation strictly valid for small circular patches with an aperture angle $\theta≪\pi$, since it is assumed that the perimeter of the shell is approximately the same as that of a circular disk, and a flat metric has been used to compute the in-plane elastic energy. However, we have found that a more accurate evaluation of the second and third terms in this equation [Li et al., 2018] does not alter significantly the main results.)

The stretching energy stored in the spherical shell grows fast with the area of the patch, and can be partially released by two different mechanisms: by the introduction of pentagonal defects (see Figure 1b), or by growing anisotropically forming curved ribbon-like crystalline domains (see Figure 1c).

The free energy of formation for a spherical cap with one defect is (Morozov and Bruinsma, 2010; Castelnovo, 2017)

$$
Δ⁢g_{d_{1}}=Δ⁢g_{c⁢a⁢p}+\frac{x^{2}}{1152}⁢(1-\frac{3}{2}⁢x^{2}),
$$

where the last term is the stretching energy due to a pentagonal disclination at the center of the cap. (The energy of an incomplete cap with one defect placed at an arbitrary location is calculated in Li et al., 2018. It is found that the Gaussian curvature attracts the disclination to the center of the cap while the defect self-energy pushes it towards the boundary. The net result is that the minimum energy corresponds to the defect located off the center of the cap. However, we have numerically verified that this approximation introduces only a very small error in our calculations for the scaled energy. This means that not noticeable effect is observed when the exact expression with the off-center defect is considered.) Such mechanism is energetically favorable only if the second term of Equation 3 is negative, that is, if $x\geq\sqrt{2/3}$.

For larger shells, the elastic strain is further released by the introduction of additional disclinations. The free energy of formation of a spherical shell with n 5-fold disclinations is (Grason, 2012; Grason, 2016; Castelnovo, 2017)

$$
Δ⁢g_{d_{n}}=Δ⁢g_{c⁢a⁢p}+g_{s_{1}}+g_{s_{2}}
$$

where $g_{s_{1}}$ is the self-energy of the isolated disclinations, and $g_{s_{2}}$ is their pairwise interaction, whose specific expressions are provided in the Appendix. When more than one defect appears, the minimum of the free energy typically occurs for a closed shell.

An alternative mechanism to alleviate stretching is the anisotropic growth of the originally spherical cap to adopt the shape of a defect-free rectangular curved stripe or ribbon. The free energy of formation of a ribbon of scaled length $l≡L/R_{0}$, width $w≡W/R_{0}$, and area $s=l⁢w=\pi⁢x^{2}$ growing on the surface of a sphere of radius $R_{0}$ is (Schneider and Gompper, 2007; Majidi and Fearing, 2008)

$$
Δ⁢g_{r⁢i⁢b}=-\frac{Δ⁢\mu~}{4}⁢x^{2}+\frac{\lambda}{2}⁢\frac{x^{2}}{w}+\frac{\lambda}{2⁢\pi}⁢w+\frac{9}{20480}⁢x^{2}⁢w^{4}.
$$

Unlike the spherical cap, as the area of the patch increases, the ribbon grows longitudinally without limitation at a nearly fixed optimal width up to the point where $l=2⁢\pi$, where it forms a closed belt with energy

$$
Δ⁢g_{b⁢e⁢l⁢t}=-\frac{Δ⁢\mu~}{4}⁢x^{2}+\lambda+\frac{9}{327680}⁢x^{10}.
$$

The ribbon-like structure with the lowest energy is always a closed belt rather than the open ribbon, so we will focus our comparison with this structure.

Finally, an alternative to the curved belt could be a cylinder with one principal radius of curvature infinitely large and the other $R_{0}$ (see Figure 1d). The cylinder has the advantage of not having any in-plane stretching cost, but it has a bending energy penalty that prevents its formation in the bending-dominated limit (see the Appendix).

Figure 2 shows a comparison of the energy landscape for the different structures for fixed values of $Δ⁢\mu~$ and $\lambda$. The competition between the bulk energy gain, the line tension penalty and the stretching and bending costs will give rise, at the proper conditions, to a barrier that has to be overcome for triggering the formation of these structures. The height of this nucleation barrier and its location, corresponding to the critical cluster size, are mostly controlled by the bulk and line energy contributions, since the critical size typically occurs at small values of x. In terms of shell nucleation, the barrier for the formation of a spherical cap is always the smallest, since the line energy of a circular edge is always smaller than for a rectangular stripe of the same area. Accordingly, the initial embryo of all these structures will be a small spherical cap (Paquay et al., 2017). Neglecting the elastic terms, the critical size for the formation of a spherical shell will be $x^{*}≈\lambda/Δ⁢\mu~$, corresponding to a barrier height for nucleation of $Δ⁢g_{c⁢a⁢p}^{*}≈\lambda^{2}/(4⁢Δ⁢\mu~)$. But rather than on the critical cluster for shell formation, we will be mostly interested in what is the most stable final structure for a given set of conditions.

![Figure 2.](https://cdn.elifesciences.org/articles/52525/elife-52525-fig2-v2.jpg)

**Figure 2.:** Free energy of formation $Δ⁢g$ versus the radius of the patch x in the bending-dominated regime for a defectless spherical shell (blue line), a spherical shell with defects (green), and a ribbon/belt (orange) for $\lambda=0.0001$ and $Δ⁢\mu~=0.001$. The optimal structure is the one with the minimum energy, which is the belt in this case. The dashed line represents the unfrustrated decrease of energy expected by the classical nucleation picture for the defectless spherical cap in the absence of elastic stresses. The inset zooms the nucleation barrier located at small patch sizes.

Since the free energies of formation only depend on $\lambda$ and $Δ⁢\mu~$ we can draw a universal phase diagram describing what is the structure (i.e. cap with or without defects, ribbon, or belt) with the lowest free energy in its stable size in terms of these two parameters. The term universal is intended to mean that the phase diagram is independent of the details of the capsomer-capsomer interactions such as range, preferred angle between capsomeres, bending rigidity, etc, as we corroborate with a coarse-grained simulation in the next section. Figure 3a shows the phase diagram in the bending-dominated limit, corresponding to $\gamma=0$. As can be seen, belts are the most stable structure at low line tension $\lambda$ and chemical potential differences $Δ⁢\mu~$. Closed shells with disclinations are the preferred structure for large values of $Δ⁢\mu~$ or $\lambda$. The frontier between the belt zone and the cap with disclinations is approximately independent of $\lambda$ and located at $Δ⁢\mu~≃0.0020$. Additionally, a small triangular region where the most stable structure is a frustrated cap with only one disclination is also apparent. As shown in the Appendix, a stable defectless cap only appears as metastable structure, since it has always a larger energy than a belt, and it is thus non competitive as stable structure, even though it may have lower energies as intermediate in the assembly process.

![Figure 3.](https://cdn.elifesciences.org/articles/52525/elife-52525-fig3-v2.jpg)

**Figure 3.:** Phase diagrams of the most stable structures in terms of the scaled chemical potential $Δ⁢\mu~$ and the scaled line tension $\lambda$ for different values of the FvK number: a) $\gamma=0$, corresponding to the bending-dominated regime, (b) $\gamma=80$, (c) $\gamma=200$, and d) $\gamma=250$. Three possible equilibrium regions are present: belts (i.e. closed ribbons, in orange), frustrated capsids with one defect (red), closed shells with defects (green), and cylinders (purple). Additionally, a region corresponding to a metastable spherical cap without defects (blue) is shown only in (a). In the white region, the equilibrium state corresponds to disaggregated individual capsomers.

### General case of arbitrary FvK number

Most small viral shells form without any underlying spherical template fixing their curvature. Therefore, it is very interesting to analyze shell formation at arbitrary FvK number, beyond the bending-dominated limit, and without the aid of an auxiliar template. In this general case, we have to consider the bending energy and the fact that the radius of the structures, $R$, may deviate from the spontaneous one, $R_{0}$, since it would be now dictated by the competition between stretching, bending, and rim energies. Using the expressions for the bending energy of a sphere and a cylinder of radius $R$ (see the Appendix), the free energy of formation of all structures analyzed in the previous section can be derived. Explicitly, the free energy of formation of a defectless spherical cap of radius $R$ becomes

$$
Δ⁢g_{c⁢a⁢p}⁢(\gamma)=-\frac{Δ⁢\mu~}{4}⁢x^{2}+\frac{\lambda}{2}⁢x+\frac{1}{1536}⁢\frac{x^{6}}{r^{4}}+\frac{1}{4⁢\gamma}⁢x^{2}⁢(\frac{1}{r}-1)^{2},
$$

where $r≡R/R_{0}$, and the optimal radius of the shell is given by

$$
r^{2}⁢(r-1)-\frac{\gamma}{192}⁢x^{4}=0.
$$

Deviations from the spontaneous radius (i.e $r=1$) are only expected for large domain sizes or large FvK numbers.

As the domain size increases, it becomes more favorable to release the elastic stress by the introduction of one or many 5-fold disclinations. The free energy of formation of a spherical shell with one central defect is

$$
Δ⁢g_{d_{1}}⁢(\gamma)=Δ⁢g_{c⁢a⁢p}⁢(\gamma)+\frac{x^{2}}{1152}⁢(1-\frac{3}{2}⁢\frac{x^{2}}{r^{2}}),
$$

which becomes favorable over the defectless case when $x/r\geq\sqrt{2/3}$. The formation energy of a spherical shell with $n$-defects is

$$
Δ⁢g_{d_{n}}⁢(\gamma)=Δ⁢g_{c⁢a⁢p}⁢(\gamma)+g_{s_{1}}⁢(r)+g_{s_{2}}
$$

where the specific expressions for $g_{s_{1}}⁢(r)$ and $g_{s_{2}}$ are written in the Appendix. Finally, the free energies of a closed belt and a cylinder (which are the ribbon-like and cylindrical-patch-like structures with the lowest energy) are

$$
Δ⁢g_{b⁢e⁢l⁢t}⁢(\gamma)=-\frac{Δ⁢\mu~}{4}⁢x^{2}+\lambda⁢r+\frac{9}{327680}⁢\frac{x^{10}}{r^{8}}+\frac{1}{4⁢\gamma}⁢x^{2}⁢(\frac{1}{r}-1)^{2},
$$

and

$$
Δ⁢g_{c⁢y⁢l}⁢(\gamma)=-\frac{Δ⁢\mu~}{4}⁢x^{2}+\lambda⁢r+\frac{1}{8⁢\gamma}⁢x^{2}⁢(1+(\frac{1}{r}-1)^{2}),
$$

respectively.

Remarkably, the free energy of formation of all these structures only depends on three scaled parameters: the chemical potential $Δ⁢\mu~$, the line tension $\lambda$, and the FvK number $\gamma$. Thus, it is possible to compare them and draw a universal phase diagram for the most stable structure in terms of these three parameters, to contrast with the scenario for the bending-dominated limit. Figure 3 shows phase diagrams for different values of the FvK number, showing the structure with the lowest free energy as a function of the normalized line tension $\lambda$ and chemical potential $Δ⁢\mu~$. For small values of FvK, that is $\gamma≲100$, the phase diagram is essentially the same as in the bending-dominated case. As the FvK number increases, the region where belts are formed occupy a larger domain, while the region with closed caps with disclinations reduces its size. However, the most relevant change is the appearance of a zone at $Δ⁢\mu~>1/(2⁢\gamma)$, where the cylinder is the optimal structure. This region progressively invades the other structures as the FvK number is increased. Roughly for $\gamma≃250$ only cylinders and belts are expected to be stable structures. This is a very important result since it shows that spherical capsids cannot be self-assembled directly as stable structures at large FvK numbers.

The reason why cylinders dominate at large FvK numbers, corresponding to the regime where stretching dominates over bending, is because they have the advantage of not having any stretching energy cost (i.e. a flat sheet of hexamers can be bent into a cylinder without any stretching). A cylindrical structure having a radius equal to the spontaneous radius $R_{0}$, that is $r=1$, will minimize the bending penalty and will have a free energy of formation, according to Equation 12, that decreases unboundedly with size when $Δ⁢\mu~>1/(2⁢\gamma)$. In other words, once the formation of a cylinder becomes more favorable than free capsomers, it will continue growing without limit decreasing indefinitely its free energy of formation without paying any stretching cost, thus overcoming the energetic gain of any finite sized structure. This will be the case when $Δ⁢\mu~>1/(2⁢\gamma)$. The larger the $\gamma$ (FvK), the smaller the $Δ⁢\mu~$ required for this to occur and therefore, regions where finite sized structures where preferred start to be devoured by the region where cylinders dominate (purple regions in Figure 3). Making use of the definition of the scaled variables, the condition for the appearance of the cylindrical phase can be recast as $Δ\mu\geqa_{1}κ/(2R_{0}^{2})$. In other words, cylinders appear more easily (smaller $Δ⁢\mu$ required) for larger values of $R_{0}$, in agreement with previous results by Castelnovo (2017) predicting that cylinders should dominate for small spontaneous curvatures (large $R_{0}$).

### Simulation

A minimal coarse-grained model has been recently proposed to analyze the assembly of empty viral shells (Aznar and Reguera, 2016; Aznar et al., 2018) and other protein cages (Garcia-Alles et al., 2017). The model can successfully reproduce the assembly of the lowest spherical shell structures using capsomers, that is, pentamers and hexamers, as basic assembly units. Capsomers are coarse-grained at low resolution as effective spheres and their interaction is modelled using three contributions capturing the essential ingredients (see Materials and methods): a Mie-like potential describing the attraction driving the assembly and the excluded volume interaction between a pair of capsomers; an angular term accounting for the preferred orientation of the interaction between proteins; and a torsion term, included to distinguish the inner and outer surfaces of the capsomers, and to favor the formation of closed shells. The model has been implemented in a Brownian Dynamics simulation as described in Materials and methods.

One of the advantages of this simple model is that the parameters of the interaction can be related to the elastic constants (Aznar and Reguera, 2016) (see Materials and methods). In terms of these, the three relevant parameters controlling the assembly become $\gamma≡\frac{Y⁢R_{0}^{2}}{κ}=\frac{4⁢n⁢m⁢\alpha^{2}}{9⁢cos^{2}⁡ν}$, $\lambda≡\frac{Λ}{Y⁢R_{0}}=\frac{2⁢cos⁡ν}{n⁢m}$, and $Δ⁢\mu~≡\frac{Δ⁢\mu}{a_{1}⁢Y}=\frac{2⁢\sqrt{3}}{\pi⁢n⁢m}⁢\frac{Δ⁢\mu}{ϵ_{0}}=\frac{2⁢\sqrt{3}}{\pi⁢n⁢m}⁢\frac{k_{B}⁢T⁢ln⁡c_{1}/c^{*}}{ϵ_{0}}.$

Thus, by changing the parameters of the model (mainly the exponents $n$ and $m$ controlling the range of the interaction, the preferred angle of interaction between capsomers $ν$, the local bending rigitidy $\alpha$, and the concentration $c_{1}$ which controls the effective chemical potential $Δ⁢\mu$) we can explore the universality and the different scenarios of assembly discussed in the previous section.

Figure 4 shows the results of simulations using different sets of parameters represented in scaled units and contrasted with the theoretical phase diagram for $\gamma=80$. For $\lambda=0.00084$, that is a relatively large line tension, at low concentration of capsomers, the seed dissolves and no nucleation or growth occurs. As the capsomer concentration is progressively increased, a metastable defectless shell and a closed spherical shell with typically 12 defects form, as expected by the theory. At very high concentrations, nucleation occurs simultaneously at many sites, and the final outcome of the simulation are many fragments of spherical capsids that cannot grow any further due to the depletion of free capsomers in solution. That would correspond to kinetic trapping, which is an interesting alternative mechanism to prevent the correct capsid assembly, that will be analyzed in a future work. For $\lambda=0.000585$, as the concentration is increased we obtained the expected sequence of: seed disolution; formation of a stable cap with a single 5-fold defect in a very narrow range of concentrations; and the formation of closed caps with many defects. Finally for $\lambda=0.000372$, that is a relatively small line tension, as the capsomer concentration is increased we go from no assembly, to the formation of ribbon-like stripes, to the growth of spherical shells with many defects. As naively expected, as $\lambda$ increases, higher scaled chemical potentials are needed to nucleate the structures. Finally, by increasing the parameter $\alpha$, the bending rigidity is reduced and assembly at higher FvK can be analyzed. The results of the simulations show that as the FvK number is increased, the formation of spherical shells is overriden by the formation of cylindrical bodies, as shown in Figure 4c, that also competes with other elongated structures such as spherocylinders or even conical shapes (see Appendix 1—figure 3). Remarkably, simulations that have been performed for widely different values of the interaction parameters, when properly scaled, all fall into the predicted picture. Therefore, the simulation results nicely confirm almost quantitatively the universality of the fate of the assembly and the potential scenarios discussed in the theory. A precise quantitative comparison between the theory and the simulations has not been performed, since they are done at slightly different conditions. While theory assumes a reservoir of capsomers, the simulations are done at fixed total number of subunits. This implies that, as the assembly proceeds, the concentration of the remaining free particles, and consequently the chemical potential, decreases. For this reason, we have not intended to reproduce with precision the borders of the phase diagram using the simulations. The fact that the chemical potential is not strictly constant in the simulations due to the depletion of free subunits may cause quantitative discrepancies when comparing with theory, but does not alter the relative stability of the different shapes analyzed.

![Figure 4.](https://cdn.elifesciences.org/articles/52525/elife-52525-fig4-v2.jpg)

**Figure 4.:** (a) Phase diagram of the most stable structure in terms of the scaled chemical potential $Δ⁢\mu~$ and the scaled line tension $\lambda$ for $\gamma=80$. Snapshots of the final outcome of the simulation for different initial capsomer concentrations for: b) $\lambda=0.00037$, obtained with $ν=1.45$ and a $m=36$, $n=18$ potential. By increasing the concentration of capsomers one goes from a dissassembled state to the formation of a ribbon to a spherical shell with defects. (The ribbon and spherical shell are not closed in the snapshots due to the limited number of capsomers and finite simulation time). (c) $\lambda=0.000525$, obtained with $ν=1.38$ and a $m=36$, $n=18$ potential. As concentration increases, one goes from a shell with one defect to a complete shell with many defects. By increasing the FvK number to $\gamma=1280$ (by setting $\alpha=0.4$), the simulations clearly forms cylindrical tubes. (d) $\lambda=0.00084$, obtained with $ν=1.45$ and a $m=24$, $n=12$ potential. In this case, the sequence is: disagreggated, metastable defectless shell, and closed spherical shell with many defects (a partial shell is shown). The simulation results agree qualitatively with the predictions from the theoretical phase diagram.

## Discussion

We have provided a comprehensive analysis of non-templated assembly of curved elastic shells, taking into account all relevant ingredients (i.e. chemical potential, line tension, spontaneous curvature, and elastic contributions) and the potential formation of non-spherical shapes. The importance of accounting for all these ingredients becomes evident, for instance, in the study of the stability of the defectless spherical cap, which turns out to be always metastable, its global stability hindered by the introduction of defects (at high line tensions) or the formation of ribbons (at low line tensions). Our analysis also shows that the outcome of the assembly not only depends on elastic considerations, but also on the assembly conditions, represented here by the scaled chemical potential. Hence, either belts or closed spherical shells or cylinders may be obtained as the most stable structure for fixed interaction parameters, depending on the concentration of assembly units. When assembly takes place at conditions near the vicinity of a phase boundary, a mixture of the two phases, or a structure resulting from their combination (e.g. a spherocylinder) may form. This may justify the observation of coexisting tubes and spherical capsids in the in vitro assembly of viruses such as SV40 (Kanesashi et al., 2003).

Although, for the sake of simplicity, our theoretical analysis has been performed using the continuous and small curvature approximations, we have verified that releasing these approximations does not alter significantly the results. The exact expression of the perimeter of the growing edge (Zandi et al., 2006; Gómez et al., 2015) influences the height and location of the nucleation barrier, but has a minor impact on the properties of the final stable structure. The accurate evaluation of the in-plane elastic cost of defects taking into account their spatial distribution (Li et al., 2018), modifies the energies of the growing shell, but does not modify significantly the stability of the final structure.

Simulations of a coarse-grained model made using widely different values for the parameters and interaction range confirm that the outcome of the assembly only depends on three scaled parameters: the scaled chemical potential $Δ⁢\mu~$, line tension $\lambda$, and FvK number $\gamma$. Thus, the assembly phase diagram is universal, and different protein shells, interaction potentials and coarse-grained models can be recast into a unifying picture of assembly, that could guide the efficient production of artificial viral cages. For instance, our analysis indicates that relatively long-range interactions are desirable to increase the line tension, decrease the FvK number and facilitate the assembly of closed spherical shells. In fact, spherical shells with icosahedral symmetry and triangulation number T > 7 could be successfully assembled in simulations without any template or scaffolding protein, provided that the line tension and FvK number are adequate. Alternatively, chemical or physical modifications that increase the FvK number or reduce the line tension or the effective concentration may become a potential therapeutic target to prevent viral replication by inducing the formation of open, and presumably non-infective, cylindrical or belt-like structures. Experimentally, the chemical potential can be tuned by the total protein concentration or by the addition of crowding agents. The line tension (which depends on the strength of the binding interaction), could be modified by the temperature, the pH and the salt concentration. The bending rigidity and spontaneous radius of curvature are also presumably controlled by pH and the presence, concentration and nature of ions or auxiliary proteins in solution. Further experimental and theoretical investigations are required to make a precise quantitative connection between the physical parameters controlling the assembly and experiments.

Triggering the formation of closed spherical shells with an incorrect radius, triangulation number (Caspar and Klug, 1962), or arrangement of proteins could also be an alternative to interfere with the assembly of the right viral capsid. But in our study, we have focused on mechanisms interferring with the closing of the shell by elastic frustration, rather than classifying the specific radius and triangulation number of the resulting spherical structure. In addition, we do not consider the situation in which the capsomers interact with cargo. Such interactions are crucial for viruses that co-assemble with their genetic material or a cargo, but this is beyond the scope of the present study.

A very important conclusion of our analysis is that spherical capsids cannot be self-assembled directly as stable structures at large FvK numbers. This may explain why some viruses that require high mechanical resistance, for instance many dsDNA bacteriophages such as lambda, HK97 and P22, first assemble a relatively soft spherical procapsid before suffering a maturation transition (Roos et al., 2012; Johnson, 2010) that flattens out their faces, which is a clear signature of a high FvK number (Lidmar et al., 2003). The results of our work indicate that a one-step assembly of a spherical shell with the high elastic resistance and Fvk number of the final structure is not viable. Table 1 compares the estimated elastic properties of different empty capsids of real viruses. The table clearly shows that viruses like CCMV or SV40 that assemble easily in vitro as spherical shells, have estimated values of the scaled line tension and FvK in the region where these structures are expected to be stable outcomes of the assembly. Contrarily, the high FvK number of the mature bacteriophage lambda will prevent its direct assembly. However, its procapsid, which is the first structure that is assembled, has a larger scaled line tension and smaller FvK that would facilitate a successful assembly. (The FvK number of lambda procapsid listed in Table 1 is probably overestimated, given its noticeable spherical shell. In addition, we have found in our simulations that even though the theoretical threshold for the disappearance of spherical shells as stable structures is around $\gamma=250$, in practice larger FvK numbers are typically required to obtain cylindrical structures since the nucleation barrier for their formation is larger than for the metastable spherical shell).

**Table 1.**
 Estimates of the main geometric and elastic properties of different non-enveloped empty viral capsids.The Young’s modulus $E$ has been evaluated from AFM nanoindentation experiments (Mateu, 2012; Michel et al., 2006; Ivanovska et al., 2007; Sae-Ueng et al., 2014) and, for SV40, from the experimental spring constant (van Rosmalen et al., 2018) using the standard thin shell formula $k=2.25⁢E⁢h^{2}/R$ (Ivanovska et al., 2004). The 2D Young’s Modulus was calculated as $Y=E⁢h$; the effective diameter of the capsomers as (Santolaria, 2011) $\sigma=R/\sqrt{\frac{5⁢\sqrt{3}}{\pi}}⁢(T+\frac{1}{\sqrt{3}}⁢c⁢o⁢t⁢(\frac{\pi}{5})-1)$, where $T$ is the triangulation number; the line tension as (Luque et al., 2012) $\lambda=\frac{2⁢ϵ_{0}}{\sqrt{3}⁢\sigma}$ considering a typical binding energy $ϵ_{0}≈10⁢k_{B}⁢T$; and the FvK number as $\gamma=12(1−ν_{p}^{2})(R/h)^{2}$, with $ν_{p}=0.3$ (Buenemann and Lenz, 2008).


<table>
  <thead>
    <tr>
      <th>Virus</th>
      <th>T-number</th>
      <th>Diameter (nm)</th>
      <th>Thickness h (nm)</th>
      <th>E (Gpa)</th>
      <th>Y (N/m)</th>
      <th>σ (nm)</th>
      <th>Scaled line tension λ</th>
      <th>Föppl-von Karman γ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CCMV</td>
      <td>3</td>
      <td>28</td>
      <td>3.8</td>
      <td>0.14</td>
      <td>0.53</td>
      <td>5.9</td>
      <td>0.00107</td>
      <td>148</td>
    </tr>
    <tr>
      <td>λ Procapsid</td>
      <td>7</td>
      <td>50</td>
      <td>4.0</td>
      <td>0.16</td>
      <td>0.64</td>
      <td>6.8</td>
      <td>0.000436</td>
      <td>427</td>
    </tr>
    <tr>
      <td>λ Capsid</td>
      <td>7</td>
      <td>63</td>
      <td>1.8</td>
      <td>1.0</td>
      <td>1.8</td>
      <td>8.6</td>
      <td>0.0000976</td>
      <td>3344</td>
    </tr>
    <tr>
      <td>SV40</td>
      <td>7</td>
      <td>45</td>
      <td>6.0</td>
      <td>0.033</td>
      <td>0.2</td>
      <td>6.1</td>
      <td>0.00174</td>
      <td>152</td>
    </tr>
  </tbody>
</table>

In summary, we have seen that the fate of the assembly is controlled by a universal phase diagram in terms of three scaled parameters: line tension, chemical potential and FvK number. The phase diagrams shed light on the physics controlling the assembly of curved shells, and could guide assembly experiments to achieve either an efficient assembly of artificial viral shells of desired geometry and mechanical properties or, alternatively, to envisage the conditions needed to impede viral infections by arresting viral assembly or inducing missasembly into a non-infective structure.

## Materials and methods

### Coarse-grained model and simulation details

The simulation model, introduced in Aznar and Reguera (2016); Aznar et al. (2018), is coarse-grained at the level of capsomers which are represented as effective spheres of two different diameters: $\sigma_{h}$ and $\sigma_{p}$, reflecting the fact that hexamers and pentamers are made of a different number of proteins (six and five, respectively). The interaction between capsomers, $V=V_{L⁢J}⋅V_{a}⋅V_{t⁢o⁢r}$, is modeled using three contributions: a Mie-like, an angular, and a torsion potential. The Mie-like potential

$$
V_{L⁢J}⁢(𝐫_{i⁢j})=ϵ_{i⁢j}⁢\frac{n}{m-n}⁢[(\frac{\sigma_{i⁢j}}{r})^{m}-\frac{m}{n}⁢(\frac{\sigma_{i⁢j}}{r})^{n}],
$$

describes the binding and the excluded volume interaction between a pair of capsomers in terms of their relative distance, $r_{ij}$ is the equilibrium distance corresponding to the minimum of the potential, r is the distance between capsomers centers, $ϵ_{ij}$ is the binding energy between capsomers, and m and n represent the power of the repulsive and attractive interaction terms, respectively, which set the range of the interaction potential. The angular contribution is given by

$$
V_{a}⁢(𝐫_{i⁢j},𝛀_{i},𝛀_{j})=exp⁡(-\frac{(\theta_{i⁢j}-ν)^{2}}{2⁢\alpha^{2}})⁢exp⁡(-\frac{(\theta_{j⁢i}-ν)^{2}}{2⁢\alpha^{2}}),
$$

where $\theta_{i⁢j}$ is the angle between the vector $Ω_{i}$, describing the spatial orientation of the capsomer, and the unit vector $𝐫_{i⁢j}$. The parameter $ν$ is the preferred angle of interaction between proteins of different capsomers, and the parameter $\alpha$ controls the local bending stiffness, that is, the energy cost required to bend two capsomers out of their preferred angle of interaction. The torsion term is given by

$$
V_{t⁢o⁢r}⁢(𝛀_{i},𝛀_{j})=exp⁡(-k_{t}⁢\frac{(1-cos⁡ξ)}{2}),
$$

where $k_{t}$ is the torsion constant and $ξ$ is the angle between the planes defined by the unit vector $𝐫_{i⁢j}$ and both orientation vectors.

The elastic properties of a shell can be related to the main parameters of the interaction. In particular the Young’s modulus is approximately given by $Y=\frac{2⁢n⁢m}{\sqrt{3}}⁢\frac{ϵ_{0}}{\sigma^{2}},$ the bending rigidity is $κ=\frac{3⁢\sqrt{3}}{8}⁢\frac{ϵ_{0}}{\alpha^{2}},$ and the preferred radius of curvature is $R_{0}=-\frac{\sigma}{2⁢cos⁡ν}.$ The line tension of a partially formed cap can be approximated by Luque et al. (2012) $\lambda=\frac{2⁢ϵ_{0}}{\sqrt{3}⁢\sigma},$ and the chemical potential difference that controls the assembly is given by $Δ⁢\mu=k_{B}⁢T⁢ln⁡(c_{1}/c^{*}),$ where $c_{1}$ is the concentration of free capsomers and $c^{*}$ is the critical concentration (Zandi et al., 2006).

The model has been implemented in a Brownian Dynamics simulation code using a simple stochastic Euler’s integration algorithm, as described in Aznar et al. (2018). Simulations were made with only one type of capsomers. We worked using reduced units in terms of the diameter of the basic building blocks $\sigma$, their diffusion coefficient $D$, and the binding energy $ϵ_{0}$. In these reduced units, the parameters used in the simulation are: torsion constant $k_{t}=1.5$, reduced temperature $T=0.1$, corresponding to a binding energy between capsomers of $10⁢k_{B}⁢T$, representing the typical order of magnitude of the strength of interactions between viral capsid proteins.

Since, in all cases, the critical nucleus is a partial spherical cap, all simulations were started using a small spherical cap of 19 units with the spontaneous curvature as initial seed. The remaining capsomers up to a total of $N=200-400$ were initially placed randomly inside a cubic box with periodic boundary conditions. The simulations run for a total of 2 × 109 steps and the final structures were analyzed. To verify the universality of the phase diagram, we performed an extensive set of simulations with different interaction parameters. More specifically, the interaction range was varied from $m=12,n=6$ to $m=48,n=24$; the spontaneous angle in the range $1.24<ν<1.45$; the bending stiffness in the range $0.05<\alpha<0.4$; and the concentration of capsomers was varied from $ρ=0.005$ to $ρ=0.05$.
