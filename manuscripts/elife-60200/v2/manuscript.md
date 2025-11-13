# Emergence and propagation of epistasis in metabolic networks

## Authors

- Sergey Kryazhimskiy<sup>1</sup> ([ORCID: 0000-0001-9128-8705](https://orcid.org/0000-0001-9128-8705)) †

### Affiliations

1. Division of Biological Sciences, University of California, San Diego La Jolla United States

† Corresponding author

## Abstract

Epistasis is often used to probe functional relationships between genes, and it plays an important role in evolution. However, we lack theory to understand how functional relationships at the molecular level translate into epistasis at the level of whole-organism phenotypes, such as fitness. Here, I derive two rules for how epistasis between mutations with small effects propagates from lower- to higher-level phenotypes in a hierarchical metabolic network with first-order kinetics and how such epistasis depends on topology. Most importantly, weak epistasis at a lower level may be distorted as it propagates to higher levels. Computational analyses show that epistasis in more realistic models likely follows similar, albeit more complex, patterns. These results suggest that pairwise inter-gene epistasis should be common, and it should generically depend on the genetic background and environment. Furthermore, the epistasis coefficients measured for high-level phenotypes may not be sufficient to fully infer the underlying functional relationships.

## Introduction

Life emerges from an orchestrated performance of complex regulatory and metabolic networks within cells. The blueprint for these networks is encoded in the genome. Mutations alter the genome. Some of them, once decoded by the cell, perturb cellular networks and thereby change the phenotypes important for life. Understanding how mutations affect the function of cellular networks is key to solving many practical and fundamental problems, such as finding mechanistic causes of genetic disorders (Hu et al., 2011; Fang et al., 2019), deciphering the architecture of complex traits (Zuk et al., 2012; Mackay, 2014; Wei et al., 2014), building artificial cells (Hutchison et al., 2016), explaining past, and predicting future evolution (Blount et al., 2008; Wiser et al., 2013; de Visser and Krug, 2014; Harms and Thornton, 2014; Kryazhimskiy et al., 2014; Sailer and Harms, 2017a; Sohail et al., 2017). Conversely, mutations can help us learn how cellular networks are organized (Phillips, 2008; van Opijnen and Camilli, 2013).

To infer the wiring diagram of a cellular network that produces a certain phenotype, one approach in genetics is to measure the pairwise and higher-order genetic interactions (or ‘epistasis’) between mutations that perturb it (Phillips, 2008). Much effort has been devoted in the past 20 years to a systematic collection of such genetic interaction data for several model organisms and cell lines (Kelley and Ideker, 2005; Lehner et al., 2006; Jasnos and Korona, 2007; Collins et al., 2007; St Onge et al., 2007; Typas et al., 2008; Roguev et al., 2008; Costanzo et al., 2010; Szappanos et al., 2011; Huang et al., 2012; Roguev et al., 2013; Bassik et al., 2013; Babu et al., 2014; Costanzo et al., 2016; van Leeuwen et al., 2016; Skwark et al., 2017; Du et al., 2017; Heigwer et al., 2018; Horlbeck et al., 2018; Norman et al., 2019; Liu et al., 2019; Kuzmin et al., 2018; New and Lehner, 2019; Celaj et al., 2020). This approach is particulary powerful when the phenotypic effect of one mutation changes qualitatively depending on the presence or absence of a second mutation in another gene, for example when a mutation has no effect on the phenotype in the wildtype background, but abolishes the phenotype when introduced together with another mutation, such as synthetic lethality (Tong et al., 2001). Such qualitative genetic interactions can often be directly interpreted in terms of a functional relationship between gene products (Tong et al., 2001; Davierwala et al., 2005; Phillips, 2008).

Most pairs of mutations do not exhibit qualitative genetic interactions. Instead, the phenotypic effect of a mutation may change measurably but not qualitatively depending on the presence or absence of other mutations in the genome (Babu et al., 2014; Costanzo et al., 2016). The genetic interactions can in this case be quantified with one of several metrics that are termed ‘epistasis coefficients’ (Wagner et al., 1998; Hansen and Wagner, 2001; Mani et al., 2008; Wagner, 2015; Poelwijk et al., 2016). Although some rules have been proposed for interpreting epistasis coefficients, in particular, their sign (Dixon et al., 2009; Lehner, 2011; Baryshnikova et al., 2013), the validity, and robustness of these rules are unknown because there is no theory for how functional relationships translate into measurable epistasis coefficients in any system (Lehner, 2011; Domingo et al., 2019). To avoid this major difficulty, most large-scale empirical studies focus on correlations between epistasis coefficients rather than on their actual values (but see Velenich and Gore, 2013, for a notable exception). Genes with highly correlated epistasis profiles are then interpreted as being functionally related (Segrè et al., 2005; Bellay et al., 2011; Babu et al., 2014; Costanzo et al., 2016; Horlbeck et al., 2018). Although this approach successfully groups genes into protein complexes and larger functional modules (Michaut et al., 2011; Bellay et al., 2011), it does not reveal the functional relationships themselves. As a result, many if not most, genetic interactions between genes and modules still await their biological interpretation (Costanzo et al., 2016; Fang et al., 2019).

While geneticists measure epistasis to learn the architecture of biological networks, evolutionary biologists face the reverse problem: they need to know how the genetic architecture constrains epistasis at the level of fitness. Epistasis determines the structure of fitness landscapes on which populations evolve (Fragata et al., 2019). Understanding it would bear on many important evolutionary questions, such as why so many organisms reproduce sexually (Kondrashov, 2018), how novel phenotypes evolve (Blount et al., 2008; Bridgham et al., 2009; Natarajan et al., 2013; Harms and Thornton, 2014), how predictable evolution is (Weinreich et al., 2006; Tenaillon et al., 2012; Wiser et al., 2013; Kryazhimskiy et al., 2014), etc. So far, evolutionary biologists have relied primarily on abstract models of fitness landscapes (see Orr, 2005, for a review), rather than those firmly grounded in organismal biochemistry and physiology (e.g. Dykhuizen et al., 1987; Das et al., 2020). For example, Fisher’s geometric model—one of the most widely used fitness landscape models—is explicitly devoid of the physiological and biochemical details (Fisher, 1930; Tenaillon, 2014; Martin, 2014).

A theory of epistasis must address two challenges. First, it must specify how the architecture of a biological network constrains epistasis. Such knowledge is important not only for evolutionary questions, but also for the inference problem in genetics. Consider a biological network module that produces a phenotype of interest but whose internal structure is unknown. By genetically perturbing all genes within the module and measuring the phenotype in all single, double and possibly some higher-order mutants, we can obtain the matrix of epistasis coefficients. In principle, we can then fit a network topology and parameters to these data. However, without knowing what information about the network is contained in the matrix in the first place, we cannot be sure whether the inferred topology and parameters are close to their true values or represent one of many possible solutions consistent with the data.

The second challenge is that epistasis may arise at a different level of biological organization than where it is measured by the experimentalist or by natural selection. For example, geneticists are often interested in understanding the structures of specific regulatory or metabolic network modules (Collins et al., 2007; Costanzo et al., 2010). However, measuring the peformance of a module directly is often experimentally difficult or impossible. Then epistasis is measured for an experimentally accessible ‘high-level’ phenotype, such as fitness, which depends on the performance of the focal ‘lower-level’ module, but also on other unrelated modules. However, if we do not know how epistasis that originally emerged in one module maps onto epistasis that is measured, it is unclear what we can infer about module’s internal structure.

Evolutionary biologists encounter a related problem when they wish to learn the evolutionary history of a protein or a larger cellular module. To do so, they would in principle need to know how different mutations in this module affected fitness of the whole organism in its past environment. But such information is rarely available. Instead, it is sometimes possible to reconstruct past mutations and measure their biochemical effects in the lab (Lunzer et al., 2005; Bridgham et al., 2009; Natarajan et al., 2013; Sarkisyan et al., 2016). When interesting patterns of epistasis are identified at the biochemical level, it is usually assumed that the same patterns manifested themselved at the level of fitness and drove module’s evolution. However, this is not obvious. If interactions with other modules distort epistasis as it propagates from the biochemical level to the level of fitness (Snitkin and Segrè, 2011), our ability to infer past evolutionary history from in vitro biochemical measurements could be diminished. Therefore, the second challenge that a theory of epistasis must address is how epistasis propagates from lower-level phenotypes to higher-level phenotypes.

There is a large body of theoretical and computational literature on epistasis. As early as 1934, Sewall Wright realized that epistasis naturally emerges in molecular networks (Wright, 1934). This was later explicitly demonstrated in many mathematical and computational models (e.g. Kacser and Burns, 1981; Keightley, 1989; Szathmáry, 1993; Gibson, 1996; Keightley, 1996; Wagner et al., 1998; Omholt et al., 2000; Peccoud et al., 2004; Gjuvsland et al., 2007; Gertz et al., 2010; Fiévet et al., 2010; Pumir and Shraiman, 2011). Metabolic control analysis became one of the most successful and general frameworks for understanding epistasis between metabolic genes (Kacser and Burns, 1973). Dean et al., 1986, Dykhuizen et al., 1987, Dean, 1989, Lunzer et al., 2005, MacLean, 2010 used it to interpret the empirically measured fitness effects of mutations and their interactions in terms of the metabolic relationships between the products of mutated genes. Kacser and Burns, 1981, Hartl et al., 1985, Keightley, 1989, Clark, 1991, Keightley, 1996, Bagheri-Chaichian et al., 2003, Bagheri and Wagner, 2004, Fiévet et al., 2010 explored the implications of epistasis in metabolism for genetic variation in populations, their response to selection, long-term evolutionary dynamics and outcomes, such as the evolution of dominance. However, most studies analyzed only the linear metabolic pathway (but see Keightley, 1989) and assumed that fitness equals flux through the pathway (but see Szathmáry, 1993), thereby bypassing the problem of epistasis propagation.

There have been few attempts to theoretically relate the molecular architecture of an organism to the types of epistasis that would arise for its high-level phenotypes, such as fitness. Segrè et al., 2005 and He et al., 2010 used flux balance analysis (FBA, Orth et al., 2010) to compute genome-wide distributions of epistasis coefficients in metabolic models of Escherichia coli and Saccharomyces cerevisiae and arrived at starkly discordant conclusions. Recently, Alzoubi et al., 2019 showed that FBA is generally poor in predicting experimentally measured genetic interactions, suggesting that it might be difficult to understand the emergence and propagation of epistasis by relying exclusively on genome-scale computational models. Sanjuán and Nebot, 2008 and Macía et al., 2012 modeled various abstract metabolic and regulatory networks and found a possible link between epistasis and network complexity. The work by Chiu et al., 2012 is a more systematic attempt to develop a general theory of epistasis. They established a fundamental connection between epistasis and the curvature of the function that maps lower-level phenotypes onto a higher-level phenotype. However, further progress has been so far hindered by uncertainty in what types of functions map phenotypes onto one another in real biological systems. Previous studies made various idiosyncratic choices with respect to this mapping, leaving us without a clear guidance as to the conditions or systems where they are expected to hold.

To overcome this problem, here I consider a whole class of hierarchical metabolic networks and obtain the family of all functions that determine how the effective activity of a larger metabolic module can depend on the activities of smaller constituent modules. There are several advantages to this approach. First, it leads to an intuitive understanding of how the structure of the network influences epistasis emergence and propagation. Second, my approach is based on basic biochemical principles, so it should be relevant for many phenotypes. For example, epistasis is often measured at the level of growth rate (Jasnos and Korona, 2007; St Onge et al., 2007; Babu et al., 2014; Costanzo et al., 2016), and metabolism fuels growth. Moreover, metabolic genes occupy a large fraction of most genomes (Orth et al., 2011) and the general organization of metabolism is conserved throughout life (Csete and Doyle, 2004). Thus, by understanding genetic interactions between metabolic genes, we will gain an understanding of a large fraction of all genetic interactions.

In my model, I consider a hierarchical network with first-order kinetics but arbitrary topology, and ask two questions related to the two challenges mentioned above. (1) How does an epistasis coefficient that arose at some level of the metabolic hierarchy propagate to higher levels of the hierarchy? (2) How does the network topology constrain the value of an epistasis coefficient between two mutations that affect different enzymes in this network? I obtain answers to these questions analytically in the limiting case when the effects of mutations are vanishingly small. I then computationally probe the validity of the conclusions outside of the domain where they are expected to hold.

My model is not intended to generate predictions of epistasis for any specific organism. Instead, its main purpose is to provide a baseline expectation for how epistasis that emerges at lower-level phenotypes manifests itself at higher-level whole-organism phenotypes, such as fitness, and what kind of information may be gained from measurements of such higher-level epistasis. One possible outcome of this analysis is that there may be fundamental limitations to what an epistasis measurement at one level of biological organization can tell us about epistasis at another level. On the other hand, if it turns out that there is a general correspondence between epistasis coefficients at different levels in this simple model, then it may be worth developing more sophisticated and general models on which inference from data can be based.

### Model

#### Hierarchical metabolic network

Consider a set of metabolites $A={1,2,…,n}$ with concentrations $S_{1},…,S_{n}$ which can be interconverted by reversible first-order biochemical reactions. The rate of the reaction converting metabolite $i$ into metabolite $j$ is $x_{i⁢j}⁢(S_{i}-S_{j}/K_{i⁢j})$ where $K_{i⁢j}$ is the equilibrium constant. The rate constants $x_{i⁢j}$, which satisfy the Haldane relationships $x_{j⁢i}=x_{i⁢j}/K_{i⁢j}$ (Cornish-Bowden, 2013), form the matrix $x→=∥x_{i⁢j}∥_{i,j=1}^{n}$. The metabolite set $A$ and the rate matrix $x→$ define a biochemical network $𝒩=(A,x→)$.

The first-order kinetics assumption makes the model analytically tractable, as discussed below; biologically, it is equivalent to assuming that all enzymes are far from saturation. The rate constants $x_{i⁢j}$ depend on the concentrations and the specific activities of enzymes and therefore can be altered by mutations. $K_{i⁢j}$ characterize the fundamental chemical nature of metabolites $i$ and $j$ and cannot be altered by mutations (Savageau, 1976).

The whole-cell metabolic network is large, and it is often useful to divide it into subnetworks that carry out certain functions important for the cell. I define subnetworks mathematically as follows. I say that two metabolites $i$ and $j$ are adjacent (in the graph-theoretic sense) if there exists an enzyme that catalyzes a biochemical reaction between them, that is, if $x_{i⁢j}>0$. Now consider a subset of metabolites $A_{\mu}⊂A$. For this subset, let $A_{\mu}^{IO}$ be the set of all metabolites that do not belong to $A_{\mu}$ but are adjacent to at least one metabolite from $A_{\mu}$. Let $x→_{\mu}$ be the submatrix of $x→$ which corresponds to all reactions where both the product and the substrate belong to either $A_{\mu}$ or $A_{\mu}^{IO}$. The metabolite subset $A_{\mu}$ and the rate matrix $x→_{\mu}$ form a subnetwork $\mu=(A_{\mu},x→_{\mu})$ of network $𝒩$. I refer to $A_{\mu}$ and $A_{\mu}^{IO}$ as the sets of internal and ‘input/output’ (‘I/O’ for short) metabolites for subnetwork μ, respectively. Thus, all internal metabolites and all reactions that involve only internal and I/O metabolites are part of the subnetwork. Note that the I/O metabolites do not themselves belong to the subnetwork, but reactions between them, if they exist, are part of the subnetwork. Metabolites that are neither internal nor I/O for μ are referred to as external to subnetwork μ. These definitions are illustrated in Figure 1A.

![Figure 1.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig1-v2.jpg)

**Figure 1.:** (A) White rectangle represents the whole metabolic network $𝒩$. Example subnetworks μ and ν are represented by the dark and light gray rectangles. Only metabolites and reactions that belong to these subnetworks are shown; other metabolites and reactions in $𝒩$ are not shown. Metabolites 1 and 5 may be adjacent to other metabolites in $𝒩$; this fact is represented by short black lines that do not terminate in metabolites. Subnetworks μ and ν are both modules because there exists a simple path connecting their I/O metabolites that lies within μ and ν and contains all their internal metabolites (dashed blue line). (B) Network $𝒩$ can be coarse-grained by replacing module μ at steady state with an effective reaction between its I/O metabolites 1 and 2, with the rate constant is $y_{\mu}$. (C) Network $𝒩$ can be coarse-grained by replacing module ν at steady state with an effective reaction between its I/O metabolites 1 and 5, with the rate constant is $y_{ν}$.

The main objects in this work are biochemical modules, which are a special type of subnetworks. To define modules, I introduce some auxiliary concepts. I say that two metabolites $i$ and $j$ are connected if there exists a series of enzymes that interconvert $i$ and $j$, possibly through a series of intermediates. Mathematically, $i$ and $j$ are connected if there exists a simple (i.e. non-self-intersecting) path between them. If all metabolites in this path are internal to the subnetwork μ (possibly excluding the terminal metabolites $i$ and $j$ themselves) then $i$ and $j$ are connected within the subnetwork μ, and such path is said to lie within μ. By this definition, metabolites $i$ and $j$ can be connected within μ only if they are either internal or I/O metabolites for μ.

#### Definition 1

A subnetwork μ is called a module if (a) it has two I/O metabolites, and (b) for every internal metabolite $i\inA_{\mu}$, there exists a simple path between the I/O metabolites that lies within μ and contains $i$.

This definition is illustrated in Figure 1A. The assumption that modules only have two I/O metabolites is not essential. However, mathematical calculations become unwieldy when the number of I/O metabolites increases. Moreover, modules with just two I/O metabolites already capture two most salient features of metabolism: its directionality, and its complex branched topology (Csete and Doyle, 2004). Such modules are a natural generalization of the linear metabolic pathway which has been extensively studied in the previous literature (Kacser and Burns, 1973; Szathmáry, 1993; Bagheri-Chaichian et al., 2003; MacLean, 2010).

Modules have two important properties. First, for any given concentrations of the two I/O metabolites, all internal metabolites in the module can achieve a unique steady state which depends only on concentrations of these I/O metabolites but not on the concentrations of any other metabolites in the network (see Proposition 1 in Materials and methods). Now consider a module μ whose I/O metabolites are (without loss of generality) labeled 1 and 2 (Figure 1A). The second property is that, at steady state, the flux through this module is $J_{\mu}=y_{\mu}⁢(S_{1}-S_{2}/K_{12})$, where

$$
y_{\mu}=F⁢(x→_{\mu})
$$

is the effective reaction rate constant of module μ (Figure 1B). Importantly, $y_{\mu}$ depends only on the rate matrix $x→_{\mu}$, but not on any other rate constants (see Corollary 2 in Materials and methods), and it can be recursively computed for any module, as described in Materials and methods. In other words, metabolic network $𝒩$ can be coarse-grained by replacing module μ at steady state with a single first-order biochemical reaction with rate $y_{\mu}$. Importantly, such coarse-graining does not alter the dynamics of any metabolites outside of module μ (see Proposition 1 in Materials and methods). This statement is the biochemical analog of the star-mesh transformation (and its generalization, Kron reduction, Rao et al., 2014) well known in the theory of electric circuits (Versfeld, 1970). The biological interpretation of these properties is that a module is somewhat isolated from the rest of the metabolic network. And vice versa, the larger network (i.e. the cell) ‘cares’ only about the total rate at which the I/O metabolites are interconverted by the module but ‘does not care’ about the details of how this conversion is enzymatically implemented. In this sense, the effective rate $y_{\mu}$ quantifies the function of module μ (a macroscopic parameter) while the rates $x→_{\mu}$ describe the specific biochemical implementation of the module (microscopic parameters).

The effective rate constant $y_{\mu}$ of module μ depends on the entire rate matrix $x→_{\mu}$. In general, a single mutation may perturb several rate constants within a module, so that the entire shape of the function $F$ may be important. Here, I focus on a special case when each mutation perturbs one reaction (real or effective) within a module, while all others remain constant. To examine epistasis between mutations, I will also consider two different mutations that perturb two separate reactions within a module. In these special cases, we do not need to know the entire function $F$. We only need to know how module’s effective rate constant $y_{\mu}$ depends on the one or two rate constants of the perturbed reactions. When $y_{\mu}$ is considered as a function of the rate constant ξ of one reaction, I write

$$
y_{\mu}=f_{1}⁢(ξ),
$$

and when $y_{\mu}$ is considered as a function of the rate constants ξ and η of two reactions, I write

$$
y_{\mu}=f_{2}(ξ,η).
$$

The rate constants of all other reactions within module μ play a role of parameters in functions $f_{1}$ and $f_{2}$.

Consider now a network $𝒩$ that has a hierarchical structure, such that there is a series of nested modules $\mu⊂ν⊂⋯$, in the sense that $A_{\mu}⊂A_{ν}⊂⋯$ (Figure 1A). Since any module at steady state can be replaced with an effective first-order biochemical reaction, there exists a hierarchy of quantitative metabolic phenotypes $y_{\mu},y_{ν},…$ (Figure 1B,C). These phenotypes are of course functionally related to each other. Specifically, because ν is a ‘higher-level’ module (in the sense that it contains a ‘lower-level’ module μ), the matrix $x→_{ν}$ can be decomposed into two submatrices $x→_{\mu}$ and $x→_{ν∖\mu}$ where the latter is the matrix of rate constants of reactions that belong to module ν but not to module μ. Since replacing the lower-level module μ with an effective reaction with rate constant $y_{\mu}$ does not alter the dynamics of metabolites outside of μ, $y_{ν}$ must depend on all elements of $x→_{\mu}$ only through $y_{\mu}$, that is,

$$
y_{ν}=f_{1}⁢(y_{\mu}),
$$

where rates $x→_{ν∖\mu}$ act as parameters of function $f_{1}$. Thus, in the hierarchy of metabolic phenotypes $y_{\mu},y_{ν},…$, a phenotype at each subsequent level depends on the phenotype at the preceding level according to Equation 4, and the lowest level phenotype $y_{\mu}$ depends on the actual rate constants accroding to Equation 1. This hierarchy of functionally nested phenotypes is conceptually similar to the hierarchical ‘ontotype’ representation of genomic data proposed recently by Yu et al., 2016.

### Quantification of epistasis

Consider a mutation A that perturbs only one rate constant $x_{i⁢j}$, such that the wildtype value $x_{i⁢j}^{0}$ changes to $x_{i⁢j}^{A}$. This mutation can be quantified at the microscopic level by its relative effect $\delta^{A}⁢x_{i⁢j}=x_{i⁢j}^{A}/x_{i⁢j}^{0}-1$. If the reaction between metabolites $i$ and $j$ belongs to nested modules $\mu,ν,…$, then mutation A may impact the functions of these modules, which can be quantified by the relative effects $\delta^{A}⁢y_{\mu}$, $\delta^{A}⁢y_{ν}$, etc. at each level of the hierarchy.

Consider now another mutation B that only perturbs the rate constant $x_{k⁢ℓ}$ of another reaction. Since mutations A and B perturb distinct enzymes, they by definition do not genetically interact at the microscopic level. However, if both perturbed reactions belong to the metabolic module μ (and, as a consequence, to all higher-level modules which contain μ), they may interact at the level of the function of this module, in the sense that the effect of mutation B on the effective rate $y_{\mu}$ may depend on whether mutation A is present or not. Such epistasis between mutations A and B can be quantified at the level μ of the metabolic hierarchy by a number of various epistasis coefficients (Wagner et al., 1998; Hansen and Wagner, 2001; Mani et al., 2008). I will quantify it with the epistasis coefficient

$$
\epsilon^{A⁢B}⁢y_{\mu}=\frac{\delta^{A⁢B}⁢y_{\mu}-\delta^{A}⁢y_{\mu}-\delta^{B}⁢y_{\mu}}{2⁢\delta^{A}⁢y_{\mu}⁢\delta^{B}⁢y_{\mu}},
$$

where $\delta^{A⁢B}⁢y_{\mu}$ denotes the effect of the combination of mutations A and B on phenotype $y_{\mu}$ relative to the wildtype. Since I only consider two mutations A and B, I will write $\epsilon⁢y_{\mu}$ instead of $\epsilon^{A⁢B}⁢y_{\mu}$ to simplify notations. Note that other epistasis coefficients can always be computed from $\epsilon⁢y_{\mu}$, $\delta^{A}⁢y_{\mu}$ and $\delta^{B}⁢y_{\mu}$, if necessary. Expressions for epistasis coefficients at other levels of the metabolic hierarchy are analogous.

## Results

The central goal of this paper is to understand the patterns of epistasis between mutations that affect reaction rates in the hieararchical metabolic network described above. Specifically, I am interested in two questions. (1) Given that two mutations A and B have an epistasis coefficient $\epsilon⁢y_{\mu}$ at a lower level μ of the metabolic hierarchy, what can we say about their epistasis coefficient $\epsilon⁢y_{ν}$ at a higher level ν of the hierarchy? In other words, how does epistasis propagate through the metabolic hierarchy? (2) If mutation A only perturbs the activity $x_{i⁢j}$ of one enzyme and mutation B only perturbs the activity $x_{k⁢ℓ}$ of another enzyme that belongs to the same module μ, then what values of $\epsilon⁢y_{\mu}$ can we expect to observe based on the topological relationship between the two perturbed reactions within module μ? In other words, what kinds of epistasis emerge in a metabolic network?

### Propagation of epistasis through the hierarchy of metabolic phenotypes

Assuming that the effects of both individual mutations and their combined effect at the lower-level μ are small, it follows from Equation 4 and Equation 5 that

$$
\epsilony_{ν}=\frac{\epsilony_{\mu}}{C}+\frac{H}{2C^{2}}+o(1),
$$

where $C=f_{1}^{′}⁢y_{\mu}/y_{ν}$ and $H=f_{1}^{′′}⁢y_{\mu}^{2}/y_{ν}$ are the first- and second-order control coefficients of the lower-level module μ with respect to the flux through the higher-level module ν and $o⁢(1)$ denotes all terms that vanish as the effects of mutations tend to zero (see Materials and methods for details). Note that Equation 6 is a special case of a more general Equation 49 which describes the case when mutations affect multiple enzymes. Equation 6 defines a linear map $ϕ$ with slope $1/C$ and a fixed point $\epsilon¯=-H⁢(2⁢C⁢(1-C))^{-1}$, which both depend on the topology of the higher-level module ν and the rate constants $x→_{ν∖\mu}$.

To gain some intuition for how the map $ϕ$ governs the propagation of epistasis from a lower level μ to a higher level ν, suppose that module ν is a linear metabolic pathway. In this case, it is intuitively clear that function $f_{1}$ is monotonically increasing (i.e. the higher $y_{\mu}$, the more flux can pass through the linear pathway ν) and concave (i.e. as $y_{\mu}$ grows, other reactions in ν become increasingly more limiting, such that further gains in $y_{\mu}$ yield smaller gains in $y_{ν}$). Indeed, it is easy to show that $C=(1+\alpha⁢y_{\mu})^{-1}>0$ and $H=-2⁢\alpha⁢y_{\mu}⁢(1+\alpha⁢y_{\mu})^{-2}<0$, where α is a positive constant that depends on other reactions in the pathway (see Materials and methods for details). It then immediately follows that any zero or negative epistasis $\epsilon⁢y_{\mu}$ that already arose at the lower level would propagate to negative epistasis $\epsilon⁢y_{ν}$ at the level of the linear pathway ν. Moreover, since $C<1$, the fixed point of the map in Equation 6 is unstable. Therefore, if epistasis $\epsilon⁢y_{\mu}$ was already sufficiently large at the lower level, it would induce even larger positive epistasis $\epsilon⁢y_{ν}$ at the level of the linear pathway ν. In fact, when module ν is a linear pathway, $\epsilon¯=1$, so that $\epsilon⁢y_{ν}>1$ whenever $\epsilon⁢y_{\mu}>1$.

The first result of this paper is the following theorem, which shows that the same rules of propagation of epistasis hold not only for a linear pathway but for any module (Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig2-v2.jpg)

**Figure 2.:** Properties of Equation 6 that maps lower-level epistasis $\epsilon⁢y_{\mu}$ onto higher-level epistasis $\epsilon⁢y_{ν}$. Slope $1/C$ and fixed point $\epsilon¯$ depend on the topology and the rate constants of the higher-level module ν, but they are bounded, as shown. Thus, the fixed point $\epsilon¯$ of this map lies between 0 and 1 and is always unstable (open circle).

#### Theorem 1

For any module ν,

$$
0\leqC\leq1
$$

and

$$
0\leq\epsilon¯\leq1.
$$

The proof of Theorem 1 is given in Materials and methods. Its main idea is the following. The functional form of $f_{1}$ in Equation 4 depends on the topology of module ν. Since the number of topologies of ν is infinite, we might a priori expect that there is also an infinite number of functional forms of $f_{1}$. However, this is not the case. In fact, all higher-level modules that contain a lower-level module fall into three topological classes defined by the location of the lower-level module with respect to the I/O metabolites of the higher-level module (see Proposition 2 and Figure 7 in Materials and methods). To each topological class corresponds a parametric family of the function $f_{1}$, so that there are only three such families. For each family, the values of $C$ and $H$ can be explicitly calculated, yielding the bounds in Equation 7 and Equation 8.

Equation 6 together with Equation 7 and Equation 8 show that the linear map $ϕ$ from epistasis at a lower-level to epistasis at the higher-level has an unstable fixed point between 0 and 1 (Figure 2). This implies that negative epistasis at a lower level of the metabolic hierarchy necessarily induces negative epistasis of larger magnitude at the next level of the hierarchy, that is, $\epsilon⁢y_{ν}\leq\epsilon⁢y_{\mu}<0$. Therefore, once negative epistasis emerges somewhere along the hierarchy, it will induce negative epistasis at all higher levels of the hierarchy, irrespectively of the topology or the kinetic parameters of the network.

Similarly, if epistasis at the lower level of the metabolic hierarchy is positive and strong, $\epsilon⁢y_{\mu}>1$, it will induce even stronger positive epistasis at the next level of the hierarchy, that is, $\epsilon⁢y_{ν}\geq\epsilon⁢y_{\mu}>1$. Therefore, once strong positive epistasis emerges somewhere in the metabolic hierarchy, it will induce strong positive epistasis of larger magnitude at all higher levels of the hierarchy, irrespectively of the topology or the kinetic parameters of the network. If positive epistasis at a lower level of the hierarchy is weak, $0<\epsilon⁢y_{\mu}<1$, it could induce either negative, weak positive or strong positive epistasis at the higher level of the hierarchy, depending on the precise value of $\epsilon⁢y_{\mu}$, the topology of the higher-level module ν and the microscopic rate constants $x→_{ν∖\mu}$.

In summary, there are three regimes of how epistasis propagates through a hierarchical metabolic network. Negative and strong positive epistasis propagate robustly irrespectively of the topology and kinetic parameters of the metabolic network, whereas the propagation of weakly positive epistasis depends on these details. The strongest qualitative prediction that follows from Theorem 1 is that negative epistasis for a lower-level phenotype cannot turn into positive epistasis for a higher-level phenotype, but the converse is possible.

### Emergence of epistasis between mutations affecting different enzymes

Which of the three regimes described above can emerge in metabolic networks and under what circumstances? In other words, if two mutations affect the same module, are there any constraints on epistasis that might arise at the level of the effective rate constant of this module? To address this question, I consider two mutations A and B that affect the rate constants of different single reactions within a given module.

Consider a relatively simple module ν shown in Figure 1A and two mutations A and B that affect the reactions, as shown in Figure 3A. I will now show that the epistasis coefficient $\epsilon⁢y_{ν}$ can take values in all three domains described above, depending on the biochemical details of this module. Using the recursive procedure for evaluating $y_{\mu}$ described in Materials and methods, it is straightforward to obtain an analytical expression for $y_{ν}$ as a function of the rate matrix $x→_{ν}$, from which $\epsilon⁢y_{\mu}$ can also be obtained (see Materials and methods for details). To demonstrate that $\epsilon⁢y_{\mu}$ can take values below 0, between 0 and 1, and above 1, it is convenient to keep all of the rate constants fixed except for the rate constant $z≡x_{34}$ of a reaction that is not affected by mutations A or B, as shown in Figure 3A. Figure 3B then shows how the epistasis coefficient $\epsilon⁢y_{\mu}$ varies as a function of $z$ for one particular choice of all other rate constants. When $z$ is small, $\epsilon⁢y_{\mu}<0$. As $z$ increases, it becomes weakly positive ($0<\epsilon⁢y_{\mu}<1$) and eventually strongly positive ($\epsilon⁢y_{\mu}>1$). Thus, in my model, there are no fundamental constraints on the types of epistasis that can emerge between mutations.

![Figure 3.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig3-v2.jpg)

**Figure 3.:** (A) An example of a simple module ν (same as in Figure 1A) where negative, weak positive and strong positive epistasis can emerge between two mutations A and B. (B) Epistasis between mutations A and B at the level of module ν depicted in (A) as a function of the rate constant $z$ of a third reaction. The values of other parameters of the network are given in Materials and Methods. (C) An example of a simple module where reactions affected by mutations are strictly parallel. In such cases, epistasis for the effective rate constant $y_{ν}$ is non-positive. Dashed blue lines highlight paths that connect the I/O metabolites and each contain only one of the affected reactions. (D) An example of a simple module where reactions affected by mutations are strictly serial. In such cases, epistasis for the effective rate constant $y_{ν}$ is equal to or greater than 1 (i.e. strongly positive). Dashed blue line highlights a path that connects the I/O metabolites and contains both affected reactions.

This simple example also reveals that not only the value but also the sign of epistasis generically depend on the rates of other reactions in the network, such that other mutations or physiological changes in enzyme expression levels can modulate epistasis sign and strength. In other words, ‘higher-order’ and ‘environmental’ epistasis are generic features of metabolic networks.

Upon closer examination, the toy example in Figure 3 also suggests that the sign of $\epsilon⁢y_{ν}$ may depend predictably on the topological relationship between the affected reactions. When $z=0$, the two reactions affected by mutations are parallel, and epistasis is negative. When $z$ is very large, most of the flux between the I/O metabolites passes through $z$ such that the two reactions affected by mutations become effectively serial, and epistasis is strongly positive. Other toy models show consistent results: epistasis between mutations affecting different reactions in a linear pathway is always positive and epistasis between mutations affecting parallel reactions is negative (see Materials and methods for details). These observation suggest an interesting conjecture. Do mutations affecting parallel reactions always exhibit negative epistasis and do mutations affecting serial reactions always exhibit positive epistasis? In fact, such relationship between sign of epistasis and topology has been previously suggested in the literature (e.g. Dixon et al., 2009; Lehner, 2011).

To formalize and mathematically prove this hypothesis, I first define two reactions as parallel within a given module if there exist at least two distinct simple (i.e. non-self-intersecting) paths that connect the I/O metabolites, such that each path lies within the module and contains only one of the two focal reactions. Analogously, two reactions are serial within a given module if there exists at least one simple path that connects the I/O metabolites, lies within the module and contains both focal reactions.

According to these definitions, two reactions can be simultaneously parallel and serial, as, for example, the reactions affected by mutations A and B in Figure 3A. I call such reaction pairs serial-parallel. I define two reactions to be strictly parallel if they are parallel but not serial (Figure 3C) and I define two reactions to be strictly serial if they are serial but not parallel (Figure 3D). Thus, each pair of reactions within a module can be classified as either strictly parallel, strictly serial or serial-parallel.

The second result of this paper is the following theorem.

#### Theorem 2

Let ξ and η be the rate constants of two different reactions in module μ. Suppose that mutation A perturbs only one of these reactions by $\delta^{A}⁢ξ$ and mutation B perturbs only the other reaction by $\delta^{B}⁢η$. In the limit $\delta^{A}⁢ξ→0$ and $\delta^{B}⁢η→0$, the following statements are true. If the affected reactions are strictly parallel then $\epsilon⁢y_{\mu}\leq0$. If the affected reactions are strictly serial, then $\epsilon⁢y_{\mu}\geq1$.

The detailed proof of this theorem is given in Materials and methods. Its key ideas and the logic are the following. It follows from Equation 3 and Equation 5 that

$$
\epsilon⁢y_{\mu}=\frac{H_{ξ⁢η}}{2⁢C_{ξ}⁢C_{η}}+o⁢(1),
$$

where $C_{ξ}=\frac{\partial⁡f_{2}}{\partial⁡ξ}⁢\frac{ξ}{y_{\mu}}$, $C_{η}=\frac{\partial⁡f_{2}}{\partial⁡η}⁢\frac{η}{y_{\mu}}$, $H_{ξ⁢η}=\frac{\partial^{2}⁡f_{2}}{\partial⁡ξ⁢\partial⁡η}⁢\frac{ξ⁢η}{y_{\mu}}$ are the first- and second-order control coefficients of the affected reactions with respect to the flux through module μ and $o⁢(1)$ denotes terms that vanish when $\delta^{A}⁢ξ$ and $\delta^{B}⁢η$ approach zero (see Materials and methods for details). Note that Equation 9 was previously derived by Chiu et al., 2012.

To compute the epistasis coefficient $\epsilon⁢y_{\mu}$ for an arbitrary module μ, we need to know the first and second derivatives of function $f_{2}$. Analogous to function $f_{1}$, there is a finite number of parametric families to which $f_{2}$ can belong. Specifically, all modules fall into nine topological classes with respect to the locations of the affected reactions within the module (see Figure 8), and each of these topologies defines a parametric family of function $f_{2}$ (see Proposition 3 and its Corollary 3 in Materials and methods). Most of these topological classes are broad and contain modules where the affected reactions are strictly parallel, those where they are strictly serial as well as those where they are serial-parallel. And it is easy to show that not all members of each topological class have the same sign of $\epsilon⁢y_{\mu}$. However, modules from the same topological class where the affected reactions are strictly parallel or strictly serial fall into a finite number of topological sub-classes (see Figure 10 through Figure 14, Table 2 and Table 3). Overall, there are only 17 distinct topologies where the affected reactions are strictly parallel (Table 2), which define 17 parametric sub-families of function $f_{2}$. For all members of these sub-families, Equation 9 yields $\epsilon⁢y_{\mu}\leq0$ (see Proposition 7 in Materials and methods). Similarly, there are only 11 distinct topologies where the affected reactions are strictly serial (Table 3), which define 11 parametric sub-families of function $f_{2}$. For all members of these sub-families, Equation 9 yields $\epsilon⁢y_{\mu}\geq1$ (see Proposition 8 in Materials and methods).

The results of Theorem 1 and Theorem 2 together imply that the topological relationship at the microscopic level between two reactions affected by mutations constrains the values of their epistasis coefficient at all higher phenotypic levels. Specifically, if negative epistasis is detected at any phenotypic level, the affected reactions cannot be strictly serial. And conversely, if strong positive epistasis is detected at any phenotypic level, the affected reactions cannot be strictly parallel. In this model, weak positive epistasis in the absence of any additional information does not imply any specific topological relationship between the affected reactions.

### Sensitivity of results with respect to the magnitude of mutational effects

Both Theorem 1 and Theorem 2 strictly hold only when the effects of both mutations are infinitesimal. Next, I investigate how these results might change when the mutational effects are finite.

#### Propagation of epistasis between mutations with finite effect sizes

As mentioned above and discussed in detail in Materials and methods, all higher-level modules that contain a lower-level module fall into three topological classes, which I label $ℳ^{b}$, $ℳ^{io}$ and $ℳ^{i}$, depending on the location of the lower-level module within the higher- level module (see Figure 7). The topological class specifies the parametric family of the function $f_{1}$ which maps the effective rate constant $y_{\mu}$ onto the effective rate constant $y_{ν}$ (see Equation 4). For all modules from the topological class $ℳ^{b}$, function $f_{1}$ is linear (see Equation 29), which implies that the results of Theorem 1 hold exactly even when the effects of mutations are finite. For modules from the topological classes $ℳ^{io}$ and $ℳ^{i}$, function $f_{1}$ is hyperbolic (see Equation 30 and Equation 31), so that the results of Theorem 1 may not hold when the effects of mutations are finite. To test the validity of Theorem 1 in these cases, I calculated the non-linear function $ϕ$ that maps the epistasis coefficient $\epsilon⁢y_{\mu}$ onto the epistasis coefficient $\epsilon⁢y_{ν}$ for 1000 randomly generated modules from each of the two topological classes and for mutations that increase or decrease the effective rate constant of the lower-level module $y_{\mu}$ by up to 50% (see Materials and methods for details).

The validity of Theorem 1 depended on the sign of mutational effects. When at least one of the two mutations had a negative effect on $y_{\mu}$, map $ϕ$ had the same properties as described in Theorem 1, even for mutations with large effect, that is, it had a fixed point $\epsilon¯$ in the interval $[0,1]$ and this fixed point was unstable. When the effects of both mutations on $y_{\mu}$ were positive and small, these results also held in about 82% of sampled modules (see Figure 4A, Figure 4—figure supplement 1, Figure 4—figure supplement 2). In the remaining ∼18% of sampled modules, the fixed point $\epsilon¯$ shifted slightly above 1. As the magnitude of mutational effects increased, the fraction of sampled modules with $\epsilon¯>1$ grew, reaching 42% when both mutations increased $y_{\mu}$ by 50%. In most of these cases, $\epsilon¯$ remained below 2, and I found only one module with $\epsilon¯>4$ (Figure 4A, Figure 4—figure supplement 1, Figure 4—figure supplement 2). Whenever the fixed point existed, it was unstable, with the exception of 12 modules for which $ϕ$ was very close to the identity map. For 289 modules (14.5%), the fixed point disappeared when both mutations increased $y_{\mu}$ by 50%. In all these cases, $\epsilon⁢y_{ν}<\epsilon⁢y_{\mu}$, indicating that even large positive epistasis may decline as it propagates through the metabolic hierarchy when the effects of mutations are finite.

![Figure 4.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig4-v2.jpg)

**Figure 4.:** (A) Distribution of the position of the fixed point $\epsilon¯$ of the function $ϕ$ that maps lower-level epistasis $\epsilon⁢y_{\mu}$ onto higher-level epistasis $\epsilon⁢y_{ν}$ in modules with random parameters and for mutations with positive effects on $y_{\mu}$ (see text and Materials and methods for details). All cases are shown in Figure 4—figure supplement 1 and Figure 4—figure supplement 2. The effect size of both mutations is indicated on each panel. ‘No f.p'. indicates that no fixed point exists. (B) Fraction of sampled modules (averaged across generating topologies) where mutations affect strictly serial reactions but the epistasis coefficient is less than 1, contrary to the statement of Theorem 2 (see text and Materials and methods for details). All cases stratified by generating topology are shown in Figure 4—figure supplement 3.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Distribution of the position of the fixed point in 1000 modules from the topological class $ℳ^{io}$ with random parameters.Notations are as in Figure 4.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Distribution of the position of the fixed point in 1000 modules from the topological class $ℳ^{i}$ with random parameters.Notations are as in Figure 4.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Dark gray bars show cases with epistasis below 1 (γ = 0:01). The same data is shown in Figure 4B, averaged over 11 generating topologies. Light gray bars show additional cases where epistasis is clustered around 1 (see Materials and methods for details). The effects of both mutations are indicated on each panel.

#### Emergence of epistasis between mutations with finite effect sizes

As mentioned above and discussed in detail in Materials and methods, modules where the reactions affected by mutations are strictly parallel fall into 17 topological classes (see Table 2) and modules where the reactions affected by mutations are strictly serial fall into 11 topological classes (see Table 3). The topological class specifies the parametric family of the function $f_{2}$ which maps the rate constants ξ and η of the affected reactions onto the effective rate constant $y_{\mu}$. To test how well Theorem 2 holds when the effects of mutations are finite, I calculated $\epsilon⁢y_{\mu}$ for randomly generated modules from these topological classes and for mutations increasing or decreasing ξ and η by up to 50% (see Materials and methods for details).

The validity of Theorem 2 depended most strongly on the topological relationship between the reaction affected by mutations. Whenever the affected reactions were strictly parallel, the epistasis coefficient at the level of module μ was always less than or equal to zero, even when mutations perturbed the rate constants by as much as 50%, consistent with Theorem 2. This was also true for strictly serial reactions, as long as both mutations had positive effects. When the affected reaction were strictly serial and at least one of the mutations had a negative effect, the epistasis coefficient was always positive, but in some cases it was less than 1 (see Figure 4B, Figure 4—figure supplement 3), in disagreement with Theorem 2. This indicates that when the effects of mutations are not infinitesimal, even mutations that affect strictly serial reactions can potentially produce negative epistasis for higher-level phenotypes.

Taken together, these results suggest that both Theorem 1 and Theorem 2 extend reasonably well, but not perfectly, to mutations with finite effect sizes. The domains of validity of both theorems appear to depend on the sign of mutational effects. The way in which the theorems break down as their assumptions are violated appears to be stereotypical: when the mutational effects increase, more types of mutations produce weak epistasis, and the bias toward negative epistasis increases during propagation from lower to higher levels of the metabolic hierarchy.

### Beyond first-order kinetics: epistasis in a kinetic model of glycolysis

The results of previous sections revealed a relationship between network topology and the ensuing epistasis coefficients in an analytically tractable model. However, the assumptions of this model are most certainly violated in many realistic situations. It is therefore important to know whether the same or similar rules of epistasis emergence and propagation hold beyond the scope of this model. I address this question here by analyzing a computational kinetic model of glycolysis developed by Chassagnole et al., 2002. This model keeps track of the concentrations of 17 metabolites, reactions between which are catalyzed by 18 enzymes (Figure 5A and Figure 5—figure supplement 1; see Materials and methods for details). This model falls far outside of the analytical framework introduced in this paper: some reactions are second-order, reaction kinetics are non-linear, and in several cases the reaction rates are modulated by other metabolites (Chassagnole et al., 2002).

![Figure 5.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig5-v2.jpg)

**Figure 5.:** (A) Simplified schematic of the model (see Figure 5—figure supplement 1 for details). Different shades of gray in the background highlight four modules as indicated (see text). Light blue circles represent metabolites. Reactions are shown as lines with dark gray boxes. The enzymes catalyzing reactions whose control coefficients with respect to the flux through the module are positive are named; other enzyme names are ommitted for clarity (see Table 5 and Table 6 for abbreviations). Three reactions, catalyzed by PGI, PFK, PGDH, for which the epistasis coefficients are shown in panel B are highlighted in dark blue, red, and orange, respectively. (B) Epistasis coefficients for flux through each module between mutations perturbing the respective reactions, computed at steady state (see text and Materials and methods for details). Reactions catalyzed by PGI and PGDH are strictly parallel (path g6p-f6p-fdp-gap contains only PGI, path g6p-6pg-ribu5p-gap contains only PGDH and there is no simple path in UGPP between g6p and gap that contains both PGI and PGDH). Reactions catalyzed by PGI and PFK are serial-parallel (path g6p-f6p-fdp-gap contains both reactions, path g6p-f6p-gap contains only PGI, path g6p-6pg-ribu5p-f6p-fdp-gap contains only PFK). Reactions catalyzed by PFK and PGDH are also serial-parallel (path g6p-6pg-ribu5p-f6p-fdp-gap contains both reactions, path g6p-f6p-fdp-gap contains only PFK, path g6p-6pg-ribu5p-gap contains only PGDH).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Blue circles indicate metabolites (see Table 5 for abbreviations). Orange rectangles indicate enzymes (see Table 6 for abbreviations). Double-arrows indicate reversible reactions. Arrows with a fletch indicate irreversible reactions. Black circles indicate reactions with multiple substrates or products. Different shades of gray indicate the FULL, GPP, UGPP, and LG models defined in Table 4.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The first-order flux control coefficients (FCCs) of all 18 reactions with respect to the output flux in the unpperturbed FULL model are shown. Eleven out of 18 reactions have positive FCCs, five (TA, TKa, TKb, R5PI, Ru5P) have zero FCCs and two (G6PDH and PEPCxyl) have negative FCCs. The 11 reactions with positive FCCs were retained for further analysis, the others were excluded. For these 11 reactions, the FCCs and epistasis coefficients with respect to fluxes through all modules (FULL, GPP, UGPP, LG) are shown in Figure 5—figure supplement 3.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** The top row shows the FCCs of 11 reactions whose FCCs in the FULL model are positive (see Figure 5—figure supplement 2). The matrix below shows the epistasis coefficients for each pair of these reactions. The topological relationship between reactions is indicated in the lower left corner of each panel ('P', strictly parallel; 'S', strictly serial; 'SP' serial-parallel). Points are colored orange (green) if the epistasis coefficient is less than zero (greater than one). Backgrounds of different shades of gray indicate the sub-modules, as in Figure 5—figure supplement 1.

Testing the predictions of the analytical theory in this computational model faces two complications. First, in a non-linear model, modules are no longer fully characterized by their effective rate constants, even at steady state. Instead, each module is described by the flux between its I/O metabolites which non-linearly depends on the concentrations of these metabolites. Consequently, the effects of mutations and epistasis coefficients also become functions of the I/O metabolite concentrations. An epistasis coefficient at the level of module ν can still be evaluated according to Equation 5, with $y_{ν}$ now representing the flux through module ν evaluated at a particular concentration of the I/O metabolites. For simplicity, I computationally find the steady state of the full glycolysis network and evaluate the epistasis coefficients only at this steady state, that is, for each module, I keep the concentrations of the I/O metabolites fixed at their steady-state values for the full network (see Materials and methods for details).

The second complication is that some control coefficients are so small that they fall below the threshold of numerical precision. Perturbing such reactions has no detectable effect on flux (Figure 5—figure supplement 2). In the analysis that follows, I ignore such reactions because the epistasis coefficient defined by Equation 5 can only be computed for mutations with non-zero effects on flux. In addition, the control coefficients of some reactions are negative, which implies that an increase in the rate of such reaction decreases the flux through the module (Figure 5—figure supplement 2). I also ignore such reactions because there is no analog for them in the analytical theory presented above. After excluding seven reactions for these reasons, I examine epistasis in 55 pairs of mutations that affect the remaining 11 reactions.

The glycolysis network shown in Figure 5A (see also Figure 5—figure supplement 1) can be naturally partitioned into four modules which I name ‘LG’ (lower glycolysis), ‘UGPP’ (upper glycolysis and pentose phosphate), ‘GPP’ (glycolysis and pentose phosophate), and ‘FULL’. Modules LG and UGPP are non-overlappng and both of them are nested in module GPP which in turn is nested in the FULL module. Thus, at least for some reaction pairs it is possible to calculate epistasis coefficients at three levels of metabolic hierarchy. There are three such pairs, and the results for them are shown in Figure 5B. Epistasis for the remaining pairs of reactions can be evaluated only at one or two levels of the hierarchy because these reactions belong to different modules at the lowest levels or because their individual effects are too small. The results for all reaction pairs are shown in Figure 5—figure supplement 3.

The strongest qualitative prediction of the analytical theory described above is that negative epistasis for a lower-level phenotype cannot turn into positive epistasis for a higher-level phenotype, while the converse is possible. Figure 5B and Figure 5—figure supplement 3 show that the data are consistent with this prediction. Another prediction is that epistasis between strictly parallel reactions should be negative. There is only one pair of reactions that are strictly parallel, those catalyzed by glucose-6-phosphate isomerase (PGI) and 6-phosphogluconate dehydrogenase (PGDH), and indeed the epistasis coefficients between mutations affecting these reactions are negative at all levels of the hierarchy (Figure 5B). Finally, the analytical theory predicts that mutations affecting strictly serial reactions should exhibit strong positive epistasis. There are 36 reaction pairs that are strictly serial. Epistasis is positive between mutations in 33 of them, and it is strongly positive in 17 of them (Figure 5—figure supplement 3). Three pairs of strictly serial reactions (those where one reaction is catalyzed by PK and the other is catalyzed by PGI, PGDH, or PFK) exhibit negative epistasis (Figure 5—figure supplement 3). These results suggest that, although one may not be able to naively extrapolate the rules of emergence and propagation of epistasis derived in the simple analytical model to more complex networks, some generalized versions of these rules may nevertheless hold more broadly.

## Discussion

Genetic interactions are a powerful tool in genetics, and they play an important role in evolution. Yet, how epistasis emerges from the molecular architecture of the cell and how it propagates to higher-level phenotypes, such as fitness, remains largely unknown. Several recent studies made a statistical argument that the structure of the fitness landscape (and, as a consequence, the epistatic interactions between mutations at the level of fitness) may be largely independent of the underlying molecular architecture of the organism (Martin, 2014; Lyons et al., 2020; Reddy and Desai, 2020). If mutations are typically highly pleiotropic (i.e. affect many independent phenotypes relevant for fitness) or are engaged in a large number of idiosyncratic epistatic interactions with other mutations in the genome, the resulting fitness landscapes converge to certain limiting shapes, such as the Fisher’s geometric model (Martin, 2014; Tenaillon, 2014). To what extent these arguments indeed apply in practice is unclear. But if they do, most genetic interactions detected at the fitness level may be uninformative about the architecture of the underlying biological networks.

In this paper, I took a ‘mechanistic’ approach, which is in a sense orthogonal to the statistical one. In my model of a hierarchical metabolic network, mutations are highly pleiotropic (a mutation in any enzyme affects all the fluxes in the module) and highly epistatic (a mutation in any enzyme interacts with mutations in any other enzyme). Yet, these pleiotropic and epistatic effects appear to be sufficiently structured that some information about the topology of the network is preserved through all levels of the hierarchy. Indeed, the emergence and propagation of epistasis follow two simple rules in my model. First, once epistasis emerges at some level of the hierarchy, its propagation through the higher levels of the hierarchy depends weakly on the details of the network. Specifically, negative epistasis at a lower level induces negative epistasis at all higher levels and strong positive epistasis induces strong positive epistasis at all higher levels, irrespectively of the topology or the kinetic parameters of the network. Second, what type of epistasis emerges in the first place depends on the topological relationship between the reactions affected by mutations. In particular, negative epistasis emerges between mutations that affect strictly parallel reactions and positive epistasis emerges between mutations that affect strictly serial reactions. Insofar as my model is relevant to nature, the key conclusion from it is that epistasis at high-level phenotypes carries some, albeit incomplete, information about the underlying topological relationship between the affected reactions.

These results have implications for the interpretation of empirically measured epistasis coefficients. It is often assumed that a positive epistasis coefficient between mutations that affect distinct genes signals that their gene products act in some sense serially, whereas a negative epistasis coefficient is a signal of genetic redundency, that is, a parallel relationship between gene products (Dixon et al., 2009). My results suggest that this reasoning is generally correct, but that the relationship between epistasis and topology is more nuanced. In particular, the sign of the epistasis coefficient in my model constrains but does not uniquely specify the topological relationship, such that a negative epistasis coefficient implies that the affected reactions are not strictly serial (but may or may not be strictly parallel) and an epistasis coefficient exceeding unity excludes a strictly parallel relationship (but does not necessarily imply a strictly serial relationship). My model suggests that one should also be careful with inferences going in the other direction, that is, extrapolating the patterns of epistasis measured at the biochemical level to those at the level of fitness. For example, if one wishes to infer the past evolutionary trajectory of an enzyme and finds two amino acid changes that exhibit a positive interaction at the level of enzymatic activity, it does not automatically imply that these mutations will exhibit a positive interaction at the level of fitness.

The strongest results presented here rely on several assumptions. I proved Theorem 1 and Theorem 2 in the limit of vanishingly small mutational effects. Some results of the metabolic control analysis, notably the summation theorem, are sensitive to this assumption (Bagheri-Chaichian et al., 2003; Bagheri and Wagner, 2004). To test the sensitivity of my analytical results with respect to this assumption, I used numerical simulations of networks with randomly sampled kinetic parameters and found that the results hold reasonably well when the effects of mutations are not infinitesimal.

The most restrictive assumption in the present work is that of first-order kinetics. Networks with only first-order kinetics clearly fail to capture some biologically important phenomena, such as sign epistasis (Weinreich et al., 2005; Chou et al., 2014; Ewald et al., 2017; Kemble et al., 2020). I discuss possible ways to relax this assumption below. But at present, a major question remains whether the rules of epistasis and propagation described here hold for realistic biological networks and whether they can be directly used to interpret empirical epistasis coefficients. My analysis of a fairly realistic computational model of glycolysis cautions against overinterpreting empirical epistasis coefficients using the rules derived here. But it also suggests that more general rules of propagation and emergence of epistasis may be found for more realistic networks. Thus, the simple rules derived here should probably be thought of as null expectations.

Relaxing the first-order kinetics assumption is analytically challenging because it is critical for replacing a module with a single effective reaction without altering the dynamics of the rest of the network. Although such lossless replacement is almost certainly not possible in networks with more complex kinetics, advanced network coarse-graining techniques may offer a promising way forward (Rao et al., 2014). Flux balance analysis (FBA) is an alternative approach (Orth et al., 2010). FBA is appealing because it entirely removes the dependence of the model on reaction kinetics. However, this comes at a substantial cost. In FBA models, fitness and other high-level phenotypes become independent of the internal kinetic parameters, which is clearly unrealistic. Nevertheless, FBA is often very good at capturing the effects of mutations that change the topology of metabolic networks, such as reaction additions and deletions (reviewed in Gu et al., 2019). At the same time, there is no natural way within FBA to model mutations that perturb reaction kinetics (He et al., 2010; Alzoubi et al., 2019). In short, FBA and my approach are complementary (see Appendix 5 for a more detailed discussion).

### Generic properties of epistasis in biological systems

Simple models help us identify generic phenomena—those that are shared by a large class of systems—which should inform our ‘null’ expectations in empirical studies. Deviations from such null in a given system under examination inform us about potentially interesting peculiarities of this system. The model presented here suggests several generic features of epistasis between genome-wide mutations.

### Epistasis has two contributions

My analysis shows that the value of an epistasis coefficient measured for a higher level phenotype is a result of two contributions (Domingo et al., 2019), propagation and emergence, which correspond to two terms in Equation 6 (or the more general Equation 49). The first term, propagation, shows that if two mutations exhibit epistasis for a lower-level phenotype they also generally exhibit epistasis for a higher-level phenotype. The second contribution comes from the fact that lower-level phenotypes map onto higher-level phenotypes via non-linear functions. This is true even in a simple model with linear kinetics considered here. As a result, even if two mutations exhibit no epistasis at the lower-level phenotype, epistasis must emerge for the higher-level phenotype, as previously pointed out by multiple authors (e.g. Kacser and Burns, 1981; DePristo et al., 2005; Martin et al., 2007; Chiu et al., 2012; Otwinowski et al., 2018; Domingo et al., 2019; Husain and Murugan, 2020).

### Epistasis depends on the genetic background and environment

My analysis shows that the value of an epistasis coefficient for a particular pair of mutations is in large part determined by the topological relationship between reactions affected by them. Since the topology of the metabolic network itself depends on the genotype (which genes are present in the genome) and on the environment (which enzymes are active or not), the topological relationship between two specific reactions might change if, for example, a third mutation knocks out another enzyme or if an enzyme is up- or down-regulated due to an environmental change (see Figure 3). Thus, we should generically expect epistasis between mutations to depend on the environment and on the presence or absence of other mutations in the genome. In other words, $G\timesG\timesG$ interactions (higher-oder epistasis) and $G\timesG\timesE$ interactions (environmental epistasis) should be common (Snitkin and Segrè, 2011; Flynn et al., 2013; Lindsey et al., 2013; Taylor and Ehrenreich, 2015; Sailer and Harms, 2017a). This fact complicates the interpretation of inter-gene epistasis since mutations in the same pair of genes can exhibit qualitatively different genetic interactions in different strains, organisms and environments, as has been observed (St Onge et al., 2007; Musso et al., 2008; Tischler et al., 2008; Dowell et al., 2010; Heigwer et al., 2018; Li et al., 2019). However, the situation may not be hopeless because the topological relationship between two reactions cannot change arbitrarily after addition or removal of a single reaction. For example, if two reactions are strictly parallel, removing a third reaction does not alter their relationship (see Proposition 5). Thus, comparing matrices of epistasis coefficients measured in different environments or genetic backgrounds could inform us about how the organism rewires its metabolic network in response to these perturbations (St Onge et al., 2007; Musso et al., 2008; Heigwer et al., 2018; Li et al., 2019).

### Skew in the distribution of epistasis coefficients

Studies that measure epistasis for fitness-related phenotypes among genome-wide mutations usually find both positive and negative epistases, but the preponderance of positive and negative epistasis varies. Some authors reported a skew toward positive interactions among deleterious mutations (Jasnos and Korona, 2007; He et al., 2010; Johnson et al., 2019), whereas others reported a skew toward negative interactions (Szappanos et al., 2011; Costanzo et al., 2016). Beneficial mutations appear to predominantly exhibit negative epistasis, also known as ‘diminishing returns’ epistasis (e.g. Martin et al., 2007; Khan et al., 2011; Chou et al., 2011; Kryazhimskiy et al., 2014; Schoustra et al., 2016). The reasons for these patterns are currently unclear. Several recent theoretical papers offer possible statistical explanations for them (Martin, 2014; Lyons et al., 2020; Reddy and Desai, 2020). On the other hand, mechanistic predictions for the distribution of epistasis coefficients are not yet available (but see Sanjuán and Nebot, 2008; Macía et al., 2012; Chiu et al., 2012). The present work does not directly address this problem either, but it provides some additional clues.

First, my model shows that the sign of epistasis at least to some extent reflects the topology of the network. Thus, the distribution of epistasis coefficients at high-level phenotypes in real organisms should ultimately depend on the preponderance of different topological relationships between the edges in biological networks. It then seems a priori unlikely that positive and negative interactions would be exactly balanced. Thus, we should expect the distribution of epistasis coefficients to be skewed in one or another direction.

The second observation is that in the metabolic model considered here a positive epistasis coefficient at one level of the hierarchy can turn into a negative one at a higher level, but the reverse is not possible. This bias toward negative epistasis at higher-level phenotypes appears to be even stronger in networks with saturating kinetics (Figure 5 and Figure 5—figure supplement 3).

The third observation is that epistasis among beneficial and deleterious mutations affecting metabolic genes should be identical at the level where they arise, provided that beneficial and deleterious mutations are identically distributed among metabolic reactions. Thus, a stronger skew toward negative epistasis among beneficial mutations at the level of fitness could arise in my model for two mutually non-exclusive reasons. One possibility is that beneficial mutations tend to affect certain special subsets of genes, those that predominantly give rise to negative epistasis. For example, beneficial mutations may for some reason predominantly arise in enzymes that catalyze strictly parallel reactions. Another possibility is that when epistasis between beneficial mutations propagates through the metabolic hierarchy it tends to exhibit a stronger negative bias compared to epistasis between deleterious mutations. Indeed, this phenomenon arises in my model among mutations with large effect (see Figure 4A, Figure 4—figure supplement 1 and Figure 4—figure supplement 2).

### Epistasis is generic

Perhaps the most important—and also the most intuitive—conclusion of this work is that we should expect epistasis for high-level phenotypes, such as fitness, to be extremely common. Consider first a unicellular organism growing exponentially. Its fitness is fully determined by its growth rate, which can be thought of as the rate constant of an effective biochemical reaction that converts external nutrients into cells (see Appendix 6 for a simple mathematical model of this statement). In other words, growth rate is the most coarse-grained description of a metabolic network and, as such, it depends on the rate constants of all underlying biochemical reactions. Many previous studies have shown that within-protein epistasis is extremely common (e.g. Lunzer et al., 2005; DePristo et al., 2005; Sailer and Harms, 2017b; Husain and Murugan, 2020). Present work shows that, once epistasis arises at the level of protein activity, it will propagate all the way up the metabolic hierarchy and will manifest itself as epistasis for growth rate. It also suggests that growth rate is a generically non-linear function of the rate constants of the underlying biochemical reactions, such that all mutations that affect growth rate individually would also exhibit pairwise epistasis for growth rate with each other (Kacser and Burns, 1981; DePristo et al., 2005; Martin et al., 2007; Chiu et al., 2012; Otwinowski et al., 2018; Husain and Murugan, 2020).

In more complex organisms and/or in certain variable environments, it may be possible to decompose fitness into multiplicative or additive components, for example, plant’s fitness may be equal to the product of the number of seeds it produces and their germination probability, as pointed out by Chou et al., 2011. Then, mutations that affect different components of fitness would exhibit no epistasis. However, such situations should be considered exceptional, as they require fitness to be decomposable and mutations to be non-pleiotropic.

If epistasis is in fact generic for high-level phenotypes, why do we not observe it more frequently? For example, a recent study that tested almost all pairs of gene knock-out mutations in yeast found genetic interactions for fitness for only about 4% of them (Costanzo et al., 2016). One possibility is that many pairs of mutations exhibit epistasis that is simply too small to detect with current methods. As the precision of fitness measurements improves, we would then expect the fraction of interacting gene pairs to grow. Another possibility is that systematic shifts in the distribution of estimated epistasis coefficients away from zero are taken by researchers as systematic errors rather than real phenomena, and are normalized out. Thus, some epistasis that would otherwise be detectable may be lost during data processing.

If epistasis is indeed as ubiquituous as the present analysis suggests, it would call into question how observations of inter-gene epistasis are interpreted. In particular, contrary to a common belief, a non-zero epistasis coefficient does not necessarily imply any specific functional relationship between the components affected by mutations beyond the fact that both components somehow contribute to the measured phenotype (Boyle et al., 2017). The focus of future research should then be not merely on documenting epistasis but on developing theory and methods for a robust inference of biological relationships from measured epistasis coefficients.

## Materials and methods

### Key ideas and logic of proofs of Theorems 1 and 2

Before proceeding to the detailed proofs of Theorem 1 and Theorem 2, I informally outline some key ideas and the basic logic.

The central object of the theory is a metabolic module. Modules have two key properties. First, a module is somewhat isolated from the rest of the metabolic network, in the sense that all metabolites inside it interact with only two metabolites outside, the I/O metabolites. The second property is that the metabolites within the module are sufficiently connected that each of them individually as well as any subset of them collectively can achieve a quasi-steady state (QSS), given the concentrations of the remaining metabolites. This property is proven in Proposition 1.

When some metabolites are at QSS, they can be effectively removed from the network and replaced with effective reactions among the remaining metabolites. In other words, one can ‘coarse-grain’ the network by removing metabolites. This approach is a standard biochemical-network reduction technique (Segel, 1988); for example, the Briggs-Haldane derivation of the Michaelis-Menten formula is based on this idea. In general, the resulting effective reactions have more complex (non-linear) kinetics than the original reactions. However, when the original reactions are first-order, the effective reactions are also first-order, that is, there is no increase in complexity. In Network coarse graining and an algorithm for evaluating the effective rate constant for an arbitrary module, I formally define the coarse-graining procedure (CGP) that eliminates one or multiple metabolites and replaces them with effective reactions.

CGP is an essential concept in my theory. I use it to compute the QSS concentrations for internal metabolites within a module (Corollary 1) and thereby prove Proposition 1, mentioned above. Since any module μ can achieve a QSS at any concentrations of its I/O metabolites and since any module has only two I/O metabolites, it can be replaced with a single effective reaction (Corollary 2). CGP provides a way to calculate the rate constant $y_{\mu}$ of this reaction. In other words, the CGP is an algorithm for evaluating function $F⁢(x→_{\mu})$ in Equation 1 for any module μ.

CGP has an important property: its result does not depend on the order in which metabolites are eliminated. Therefore, in computing the effective rate constant of a module, we can choose any convinient way to eliminate its metabolites. Suppose that one module μ is nested within another module ν as in Figure 1A. A convenient way to compute the effective rate $y_{ν}$ of the larger module is to first coarse-grain the smaller module μ, replacing it with an effective rate $y_{\mu}$, and then eliminate all the remaining metabolites in ν. Since effective rates after coarse-graining do not depend on the order of metabolite elimination, $y_{ν}$ must depend on the rate constants $x→_{\mu}$ only indirectly, through $y_{\mu}$. In other words, all the information about the smaller module μ that is relevant for the performance of the larger module ν is contained in $y_{\mu}$. Therefore, if a mutation or mutations perturb only reactions inside of the smaller module μ, we only need to know their effects on the effective rate constant $y_{\mu}$ to completely understand how they will perturb the performance of the larger module ν. Specifically, if we have two such mutations A and B, all the information about them is contained in three numbers, $\delta^{A}⁢y_{\mu}$, $\delta^{B}⁢y_{\mu}$ and $\epsilon⁢y_{\mu}$. Theorem 1 then describes how epistasis at the level of module μ propagates to epistasis at the level of module ν.

The proof of Theorem 1 proceeds as follows. Let $a$ be the effective reaction with rate constant $y_{\mu}$ that represents module μ within the larger module ν, and consider $y_{ν}$ as a function of $y_{\mu}$, as in Equation 4. To obtain $f_{1}⁢(y_{\mu})$, it is convenient to first eliminate all metabolites that do not participate in reaction $a$. No matter what the initial structure of module ν is, such coarse-graining will produce only one of three topologically distinct ‘minimal’ modules, which differ by the location of reaction $a$ with respect to the I/O metabolites of module ν (Figure 7). This implies that the function $f_{1}$ can belong to three parameteric families, where the parameters are the effective rate constants of reactions other than $a$ in each of the minimal modules. This is the essence of Proposition 2. Then Theorem 1 can be easily proven by explicitly evaluating the first- and second-order control coefficients for each of the three functions and showing that the statements of the theorem hold for all of them, irrespectively of the function’s parameters.

Now consider two reactions $a$ and $b$ with rate constants ξ and η, and imagine the two mutations A and B that affect these reactions. To understand what value of $\epsilon⁢y_{\mu}$ will occur, we need to obtain $y_{\mu}$ as a function of ξ and η (Equation 3). To do so, it is convenient to first eliminate all metabolites that do not participate in reactions $a$ or $b$. No matter what the initial structure of module μ is, such coarse-graining will produce only one of nine topologically distinct minimal modules, which differ by the location of reactions $a$ and $b$ with respect to the I/O metabolites of module μ and each other (Figure 8). This implies that the function $f_{2}$ can belong to nine parameteric families. This is the essence of Proposition 3 and Corollary 3.

How does the topological relationship between reactions $a$ and $b$ translate into epistasis? First, there are only three types of relationships between any pair of reactions in a module: strictly serial, strictly parallel, or serial-parallel (see Figure 3). Second, Proposition 4 and Corollary 4 show that coarse-graining does not alter the strict relationships, that is, if reactions $a$ and $b$ are strictly serial or strictly parallel before coarse-graining they will remain so after coarse-graining. This is important because it implies that to prove Theorem 2 we do not need to consider an infinitely large space of all modules but only a much smaller space of all minimal modules, that is, those that have only those metabolites that participate in the affected reactions $a$ and $b$. Although the space of all minimal modules is still infinite, the space of their topologies is finite (see Figure 8). For some minimal topologies, the connection between the strictly serial or strictly parallel relationship and epistasis can be established very easily. For example, if reaction $a$ and reaction $b$ both share an I/O metabolite as a substrate (see topological class $ℳ^{io,io,IO}$ in Figure 8), then they are always strictly parallel, no matter what the rest of the module looks like. Evaluating the first- and second-order control coefficients for the function $f_{2}$ that corresponds to this topological class reveals that $\epsilon⁢y_{\mu}\leq0$ for any parameter values of $f_{2}$.

Unfortunately, most topological classes are too broad and include modules where reactions $a$ and $b$ are strictly serial as well as modules where they are strictly parallel or serial-parallel (e.g., class $ℳ^{io,io,∅}$). Consequently, the sign of $\epsilon⁢y_{\mu}$ for such modules can change depending on the values of the rate constants. However, since the number of distinct minimal topologies is finite, it is possible to identify all minimal topologies where the reactions $a$ and $b$ are strictly serial or strictly parallel. These topological sub-classes define parametric sub-families of function $f_{2}$, and we can explicitly calculate $\epsilon⁢y_{\mu}$ for all such functions. However, such brute-force approach is extremely cumbersome because the number of distinct minimal topologies is very large.

Fortunately, the following simple and intuitive fact greatly simplifies this problem. If two reactions are strictly serial or strictly parallel, this relationship does not change if a third reaction is removed from the module. This statement is the essence of Proposition 5. However, if the two reactions are serial-parallel, removal of a third reaction can change the relationship to a strictly serial or a strictly parallel one. As a consequence, there exist certain most connected ‘generating’ topologies where the relationship between the focal reactions is strictly parallel or strictly serial, and any other strictly serial minimal topology can be produced from at least one of the generating topologies by removal of reactions. This is the essence of Proposition 6. All generating topologies can be discovered by a simple algorithm provided in Appendix 3. They are listed in Table 2 and Table 3 and shown in Figure 10 through Figure 14. Each generating topology defines a parametric sub-family of function $f_{2}$, and I explicitly evaluate the first- and second-order control coefficients for all these sub-families (see Proposition 7 and Proposition 8) which essentially completes the proof of Theorem 2.

### Network coarse-graining

#### Notations and definitions

Here, I give a more precise definition of the model and introduce additional notations and definitions. As mentioned above, all reactions are first order and reversible. Thus, each reaction $i↔j$ has one substrate $i\inA$ and one product $j\inA$, and it is fully described by its rate constant $x_{i⁢j}$. By definition, $x_{i⁢i}=0$. I denote the set of all reactions by $R={i↔j:i,j\inA,x_{i⁢j}>0}$. The dynamics of metabolite concentrations $S_{1},…,S_{n}$ in the network $𝒩$ are governed by equations

$$
S˙_{i}=\sumj=1nx_{j⁢i}⁢S_{j}-D_{i}⁢S_{i},i\inA
$$

where

$$
D_{i}=\sumj=1nx_{i⁢j},i\inA.
$$

In what follows, it will be important to distinguish three types of reactions within a module, based on their topological relationship to the I/O metabolites of that module. The topology of the module μ is determined by its set of reactions $R_{\mu}={i↔j\inR:i,j\inA_{\mu}∪A_{\mu}^{IO}}$. I call all reactions where both the substrate and the product are internal to module μ as reactions internal to μ, and I denote the set of all such reactions by $R_{\mu}^{i}⊂R_{\mu}$. For example, module μ in Figure 1A has one internal reaction $3↔4$. I call all reactions where one of the metabolites is internal to μ and the other is an I/O metabolite as the i/o reactions for μ, and I denote the set of all such reactions by $R_{\mu}^{io}⊂R_{\mu}$. (I reserve upper-case ‘I/O’ for metabolites and use lower-case ‘i/o’ for reactions.) For example, module μ in Figure 1A has three i/o reactions $1↔3$, $1↔4$ and $2↔4$. Finally, I refer to reactions between any two I/O metabolites for module μ as bypass reactions for module μ, and I denote the set of all such reactions by $R_{\mu}^{b}⊂R_{\mu}$. For example, module μ in Figure 1A has no bypass reactions but reaction $1↔5$ is a bypass reaction for module ν. By definition, all these three sets of reactions $R_{\mu}^{i}$, $R_{\mu}^{io}$ and $R_{\mu}^{b}$ are non-overlapping, and $R_{\mu}=R_{\mu}^{i}∪R_{\mu}^{io}∪R_{\mu}^{b}$.

Another important concept are the simple paths that lie within a module. For any two metabolites $i,j\inA∪A_{\mu}^{IO}$, I denote a simple path between them that lies within μ as $p_{i⁢j}^{\mu}$ or, equivalently as $i↔k_{1}↔…↔k_{m}↔j$ (where all $k_{ℓ}\inA_{\mu}$). I say that each of the metabolites $k_{ℓ}$ belongs to (or is contained in) path $p_{i⁢j}^{\mu}$ (denoted by $k_{ℓ}\inp_{i⁢j}^{\mu}$). Similarly, I say that each of the reactions $k_{ℓ}↔k_{ℓ+1}$ belong to (or are contained in) path $p_{i⁢j}^{\mu}$ (denoted by $k_{ℓ}↔k_{ℓ+1}\inp_{i⁢j}^{\mu}$). I will drop superindex μ from $p_{i⁢j}^{\mu}$ if it is clear what module is being referred to.

#### Network coarse graining and an algorithm for evaluating the effective rate constant for an arbitrary module

In this section, I formally introduce and characterize the coarse-graining procedure (CGP). First, I introduce the main idea, which is to eliminate a metabolite that is at QSS and to replace it with a set of new reactions between metabolites adjacent to the eliminated one. This is exactly analogous to the star-mesh transformation in the theory of electric circuits (Versfeld, 1970). The resulting network is a coarse-grained version of the original network in the sense that it has one less metabolite. Next, I define the CGP, which is simply multiple metabolite eliminations applied successively. I prove Proposition 1, which justifies applying the CGP to a whole module and replacing it with a single effective reaction (Corollary 2). Finally, I show how to apply the CGP in practice to compute function $F$ from Equation 1 for modules with some simple topologies.

### Elimination of a single metabolite

I begin by outlining the main idea behind the CGP, which is to replace one metabolite internal to a module with a series of effective reactions between metabolites adjacent to it. If the effective rate constants are defined appropriately, the dynamics of all metabolites in the resulting coarse-grained network are the same as in the original network, provided that the eliminated metabolite is at QSS in the original network.

To formalize this idea, suppose that module $\mu=(A_{\mu},x→_{\mu})$ contains $m$ internal metabolites. Let $k\inA_{\mu}$ be the internal metabolites that will be eliminated. Let $A^{{k}}=A∖{k}$ be the reduced metabolite set and let $x→^{{k}}$ be the reduced $(n-1)\times(n-1)$ matrix of rate constants defined by 

$$
x_{ij}^{{k}}=x_{ij}+\frac{x_{ik}x_{kj}}{D_{k}},i,j\inA^{{k}},i\neqj,
$$



$$
x_{ii}^{{k}}=0,i\inA^{{k}},
$$

where $D_{k}$ is given by Equation 11.

Such metabolite elimination has three properties that follow immediately from Equation 12 and Equation 13. First, the rate constants of reactions do not change as long as the eliminated metabolite does not participate in them. Mathematically, $x_{i⁢j}^{{k}}=x_{i⁢j}$ for all metabolites $i$ and $j$ that are not adjacent to the eliminated metabolite $k$. In particular, this is true for all metabolites external to module μ. Second, because equilibrium constants have the property $K_{i⁢j}=K_{i⁢ℓ}⁢K_{ℓ⁢j}$ for any metabolites $i,j,ℓ$, the rate constants $x_{i⁢j}^{{k}}$ obey Haldane’s relationships. Therefore, the reduced metabolite set $A^{{k}}$ and the reduced rate matrix $x→^{{k}}$ define a new ‘coarse-grained’ metabolic network $𝒩^{{k}}=(A^{{k}},x→^{{k}})$. It is easy to show that subnetwork μ after the elimination of metabolite $k$ is still a module. Third, the reaction set of module μ (i.e., its topology) in the coarse-grained network $𝒩^{{k}}$ depends only on the reaction set of this module in the original network $𝒩$, but not on the particular values in the rate matrix $x→_{\mu}$.

Next, I will show that the dynamics of metabolites in the coarse-grained network $𝒩^{{k}}$ are identical to the dynamics of metabolites in the original network $𝒩$ where metabolite $k$ is at QSS. Note that if metabolite $k$ is at QSS in the network $𝒩$, its concentration is given by

$$
S_{k}=\sumj\inA_{\mu}^{IO}∪A_{\mu}∖{k}\frac{x_{j⁢k}⁢S_{j}}{D_{k}},
$$

which follows from Equation 10. Now, the dynamics of metabolites in the network $𝒩^{{k}}$ are governed by equations

$$
S˙_{i}=\sumj\inA^{{k}}x_{ji}^{{k}}S_{j}−D_{i}^{{k}}S_{i},fori\inA^{{k}},
$$

where $D_{i}^{{k}}=\sum_{j\inA^{{k}}}x_{i⁢j}^{{k}}$. As mentioned above, $x_{i⁢j}^{{k}}=x_{i⁢j}$ for all pairs of metabolites where at least one metabolite is external to module μ. Therefore, Equation 15 for the external metabolites are identical to Equation 10 that govern the dynamics of these metabolites in the original network $𝒩$. Next, consider the dynamics of the I/O and internal metabolites for module μ in the coarse-grained network $𝒩^{{k}}$, that is, those in the set $A_{\mu}^{IO}∪A_{\mu}∖{k}$. For any such metabolite $i$, the sum in the righthand side of Equation 15 can be re-written as

$$
\sumj\inA_{\mu}^{IO}∪A_{\mu}∖{k}x_{ji}^{{k}}S_{j}=\sumj\inA_{\mu}^{IO}∪A_{\mu}∖{k}(x_{ji}+\frac{x_{jk}x_{ki}}{D_{k}})S_{j}−\frac{x_{ik}x_{ki}}{D_{k}}S_{i}=\sumj\inA_{\mu}^{IO}∪A_{\mu}∖{k}x_{ji}S_{j}+x_{ki}\sumj\inA_{\mu}^{IO}∪A_{\mu}∖{k}\frac{x_{jk}S_{j}}{D_{k}}−\frac{x_{ik}x_{ki}}{D_{k}}S_{i}.
$$

According to Equation 14, the second term in Equation 16 equals $x_{k⁢i}⁢S_{k}$, so that Equation 16 becomes

$$
\sumj\inA_{\mu}^{IO}∪A_{\mu}∖{k}x_{j⁢i}^{{k}}⁢S_{j}=\sumj\inA_{\mu}^{IO}∪A_{\mu}x_{j⁢i}⁢S_{j}-\frac{x_{i⁢k}⁢x_{k⁢i}}{D_{k}}⁢S_{i}.
$$

For any metabolite $i\inA_{\mu}^{IO}∪A_{\mu}∖{k}$, the second term in the righthand side of Equation 15 can be re-written as

$$
D_{i}^{{k}}=\sumj\inA_{\mu}^{IO}∪A_{\mu}∖{k}(x_{i⁢j}+\frac{x_{i⁢k}⁢x_{k⁢j}}{D_{k}})-\frac{x_{i⁢k}⁢x_{k⁢i}}{D_{k}}=D_{i}-\frac{x_{i⁢k}⁢x_{k⁢i}}{D_{k}}.
$$

Substituting Equation 17 and Equation 18 into Equation 15, we see that Equation 15 is in fact equivalent to Equation 10 for all $i\inA∖{k}$ with $S_{k}$ given by Equation 14.

### The coarse-graining procedure (CGP)

Here, I define the CGP for an arbitrary set of internal metabolites by applying metabolite elimination recursively.

Let $E⊆A_{\mu}$ be an arbitrary subset of metabolites internal to module μ in the metabolic network $𝒩$ and let $n_{E}$ be the number of elements in $E$. Let $A^{E}=A∖E$ be the reduced metabolite set after the metabolites have been eliminated. I define the reduced $(n-n_{E})\times(n-n_{E})$ matrix of rate constants $x→^{E}$ as follows. If $n_{E}=1$, the matrix $x→^{E}$ is defined by Equation 12 and Equation 13. If $n_{E}>1$, then I define it recursively. Suppose that all metabolites in $E$ other than some metabolite $k\inE$ have been previously eliminated, such that the coarse-grained network $𝒩^{E^{′}}=(A^{E^{′}},x→^{E^{′}})$ is defined, with the set of eliminated metabolites $E^{′}=E∖{k}$, $A^{E^{′}}=A∖E^{′}$, and the known matrix $x→^{E^{′}}$. Then, I define the matrix $x→^{E}$ through the elimination of metabolite $k$ from $𝒩^{E^{′}}$, that is, 

$$
x_{i⁢j}^{E}=x_{i⁢j}^{E^{′}}+\frac{x_{i⁢k}^{E^{′}}⁢x_{k⁢j}^{E^{′}}}{D_{k}^{E^{′}}},i,j\inA^{E},i\neqj,
$$



$$
x_{i⁢i}^{E}=0,i\inA^{E},
$$

with

$$
D_{k}^{E^{′}}=\sumj\inA^{E^{′}}x_{k⁢j}^{E^{′}}.
$$

I define the the coarse-graining procedure that eliminates the metabolite set E as a map

$$
CG^{E}:𝒩↦𝒩^{E}=(A^{E},x→^{E}).
$$

As with the elimination of a single metabolite, it is straightforward to show that the rate constants $x_{i⁢j}^{E}$ obey Haldane’s relationships, so that $𝒩^{E}$ is indeed a metabolic network. $CG^{E}$ maps module μ within the metabolic network $𝒩$ onto a subnetwork $\mu^{′}$ within the metabolic network $𝒩^{E}$. It is straightforward to show that $\mu^{′}$ is a module. Whenever there is no ambiguity, I will label both the original and the coarse-grained versions of the module by μ. To simplify notations, if the CGP eliminates the entire module μ (i.e., if $E=A_{\mu}$), I label it $CG^{\mu}$. I label the coarse-grained network that restults from the application of $CG^{\mu}$ by $𝒩^{\mu}$ and I label the effective rate of the reaction substituting module μ in network $𝒩^{\mu}$ as $y_{\mu}$.

Intuitively, the result of coarse-graining should not depend on the order in which the metabolites are eliminated. To see this, let us obtain explicit (i.e. not recursive) expressions for $x_{i⁢j}^{E}$. First, by applying the recursion Equation 19, it is easy to show that elimination of two metabolites $E={k,ℓ}$ yields effective rate constants

$$
x_{ij}^{{k,ℓ}}=x_{ij}^{{k}}+\frac{x_{iℓ}^{{k}}x_{ℓj}^{{k}}}{D_{ℓ}^{{k}}}(22)=x_{ij}+\frac{D_{k}x_{iℓ}x_{ℓj}+D_{ℓ}x_{ik}x_{kj}+x_{ik}x_{kℓ}x_{ℓj}+x_{iℓ}x_{ℓk}x_{kj}}{D_{k}D_{ℓ}−x_{kℓ}x_{ℓk}}(23)=x_{ij}+\frac{x_{iℓ}x_{ℓj}}{D_{ℓ}^{{k}}}+\frac{x_{ik}x_{kj}}{D_{k}^{{ℓ}}}+\frac{x_{ik}x_{kℓ}x_{ℓj}}{D_{k}^{{ℓ}}D_{ℓ}}+\frac{x_{iℓ}x_{ℓk}x_{kj}}{D_{ℓ}^{{k}}D_{k}},i,j\inA∖{k,ℓ},i\neqj.
$$

As expected, Equation 22 and Equation 23 are symmetric with respect to the eliminated metabolites k and $ℓ$. Extrapolating from Equation 23, it is possible to show that for an arbitrary metabolite subset $E⊆A_{\mu}$ that contains $n_{E}$ metabolites,

$$
x_{i⁢j}^{E}=x_{i⁢j}+\sumL=1n_{E}\sum(k_{1},…,k_{L})\frac{x_{i⁢k_{1}}}{1}⁢\frac{x_{k_{1}⁢k_{2}}}{D_{k_{1}}^{E∖{k_{1}}}}⁢⋯⁢\frac{x_{k_{L-1}⁢j}}{D_{k_{L}}^{E∖{k_{1},k_{2},…,k_{L}}}},i,j\inA∖E,i\neqj.
$$

Here, the second sum is taken over all $n_{E}!/(n_{E}-L)!$ ordered lists of metabolites $(k_{1},…,k_{L})$ from $E$. Each list can be thought of as a simple path within $E$ that connects metabolites $i$ and $j$. The proof of Equation 24 can be found in Appendix 1. As expected, Equation 24 shows that the effective reation rate $x_{i⁢j}^{E}$ does not depend on the order in which metabolites are eliminated. This and other properties of the CGP are listed in Box 1.

One of key building blocks of the proofs of Theorem 1 and Theorem 2 is the fact that modules can be classified into a finite number of topological classes (see below). To arrive at this classification, it will be convenient to define a composition of coarse-graining procedures, as follows. Suppose that $CG^{E_{1}}$ and $CG^{E_{2}}$ are two coarse-graining procedures of network $𝒩$ for two subsets of metabolites $E_{1}⊂A_{\mu}$ and $E_{2}⊂A_{\mu}$. If the sets $E_{1}$ and $E_{2}$ are non-overlapping, $CG^{E_{2}}$ is also defined for the coarse-grained network $𝒩^{E_{1}}$ which is the result of applying $CG^{E_{1}}$ to the original network $𝒩$. The result of applying $CG^{E_{2}}$ to the $𝒩^{E_{1}}$ is called the composition of coarse-graining procedures $CG^{E_{1}}$ and $CG^{E_{2}}$ of the original network $𝒩$ and is denoted as $CG^{E_{1}}∘CG^{E_{2}}$.

As defined above, coarse-graining is a formal procedure, and there is no a priori guarantee that (a) it can in fact be carried out for every set of metabolites and (for example, because a metabolite set does not have a steady-state solution); and (b) it will not distort the dynamics in the rest of the network. The following proposition alleviates both of these concerns and thereby justifies the use of the CGP for any subset of internal metabolites within a module (including the entire module μ). It is straightforward to prove it by induction, using the same logic as in the elimination of a single metabolite.

#### Proposition 1

Let $E$ be any subset of metabolites internal to module μ. Then,

#### Corollary 1

Without loss of generality, suppose that the I/O metabolites for module μ are labeled 1 and 2 and its internal metabolites are labeled $A_{\mu}={3,4,…,m}$. There exists a unique QSS $S¯_{i}$ for all $i\inA_{\mu}$. The QSS concentrations can be obtained by recursively applying equation.

$$
S¯_{k}=\frac{1}{D_{k}^{{k+1,…,m}}}⁢(x_{1⁢k}^{{k+1,…,m}}⁢S_{1}+x_{2⁢k}^{{k+1,…,m}}⁢S_{2}+\sumj\in{3,…,k-1}x_{j⁢k}^{{k+1,…,m}}⁢S¯_{j})
$$

for $k=3,4,…,m$.

Equation 25 follows from Equation 10 for the coarse-grained network obtained by eliminating metabolites $k+1,…,m$.

#### Corollary 2

Without loss of generality, suppose that the I/O metabolites for module μ are labeled 1 and 2. Module μ can be replaced with a single effective reaction between its I/O metabolites, whose rate constant $y_{\mu}$ can be calculated using Equation 19 and Equation 20 or Equation 24. The dynamics of all metabolites in the resulting coarse-grained metabolic network are identical to their dynamics in the original network $N$ where all metabolites internal to module μ are at the QSS determined by Equation 25.

#### Computation of effective rate constants for simple modules

Corollary 2 provides a method for replacing any module μ at QSS with an effective rate $y_{\mu}=F⁢(x→_{\mu})$, which can be calculated using Equation 19 and Equation 20 or Equation 24. Here, I show how to implement this calculation for three simple metabolic modules.

### Linear pathway

Consider a linear pathway with I/O metabolites 1 and $m$ and internal metabolites $2,3,…,m-1$ (Figure 6A). This labeling of metabolites is more convenient for the linear pathway. To calculate $y_{\mu}$, I will apply recursion Equation 19 and Equation 20. I start by eliminating metabolite 2. After this initial coarse-graining step, the resulting module is still a linear pathway, where two reactions $1↔2↔3$ were replaced with a single reaction $1↔3$ with the effective rate constant.

$$
x_{13}^{{2}}=\frac{x_{12}⁢x_{23}}{x_{21}+x_{23}}=(\frac{1}{K_{12}⁢x_{23}}+\frac{1}{x_{12}})^{-1}.
$$

![Figure 6.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig6-v2.jpg)

**Figure 6.:** (A) Linear pathway. (B) Two parallel pathways.

All other rate constants remain unchanged. Next, I eliminate metabolite 3. The resulting module is still a linear pathway, where now three reactions $1↔2↔3↔4$ were replaced with a single reaction $1↔4$ with the effective rate constant

$$
x_{14}^{{2,3}}=\frac{x_{13}^{{2}}⁢x_{34}}{x_{31}^{{2}}+x_{34}}=(\frac{1}{K_{13}⁢x_{34}}+\frac{1}{K_{12}⁢x_{23}}+\frac{1}{x_{12}})^{-1}.
$$

All other rate constants remain unchanged. Continuing this process until all internal metabolites are eliminated, I obtain

$$
y_{\mu}=(\sumi=1m-1\frac{1}{K_{1⁢i}⁢x_{i⁢i+1}})^{-1},
$$

which is identical to the expression originally obtained by Kacser and Burns, 1973.

### Two parallel pathways

Consider two parallel pathways with I/O metabolites 1 and 2 and internal metabolites 3 and 4 (Figure 6B). I obtain the effective rate constant using Equation 22 with $i=1$, $j=2$, $k=3$, $ℓ=4$. Since $x_{12}=x_{34}=0$, Equation 22 simplifies to

$$
y_{\mu}=\frac{D_{3}⁢x_{14}⁢x_{42}+D_{4}⁢x_{13}⁢x_{32}}{D_{3}⁢D_{4}}=\frac{x_{14}⁢x_{42}}{x_{41}+x_{42}}+\frac{x_{13}⁢x_{32}}{x_{31}+x_{32}}.
$$

Thus, the contributions of parallel pathways are simply added.

### Module μ in Figure 1

To obtain the effective rate constant for module μ shown in Figure 1, I again use Equation 22 with $i=1$, $j=2$, $k=3$, $ℓ=4$.

$$
y_{\mu}=\frac{D_{3}⁢x_{14}⁢x_{42}+D_{4}⁢x_{13}⁢x_{32}+x_{13}⁢x_{34}⁢x_{42}+x_{14}⁢x_{43}⁢x_{32}}{D_{3}⁢D_{4}-x_{34}⁢x_{43}},
$$

with $D_{3}=x_{31}+x_{32}+x_{34}$ and $D_{4}=x_{41}+x_{42}+x_{43}$.

### Classification of modules with respect to ‘marked’ reactions, and the parametric families of functions f1 and f2

The CGP described above allows us to calculate the function $F$ that maps the rate matrix $x→_{\mu}$ for an arbitrary module μ onto the module’s effective rate constant $y_{\mu}$. $F$ is a multivariate function of the entire matrix $x→_{\mu}$. However, in many applications, only one or two reactions are varied at a time while all others remain constant, and we want to know how module’s effective parameter $y_{\mu}$ depends on these one or two perturbed reactions. I refer to such singled-out reactions as ‘marked’. When $y_{\mu}$ is considered as a function of the rate constant ξ of one marked reaction, I write $y_{\mu}=f_{1}⁢(ξ)$, as in Equation 2. When $y_{\mu}$ is considered as a function of the rate constants ξ and η of two marked reactions, I write $y_{\mu}=f_{2}⁢(ξ,η)$ as in Equation 3.

The functional form of $F$ and, as a consequence, the functional forms of $f_{1}$ and $f_{2}$ depend only on the topology of module μ (see Property #5 of the CGP in Box 1). In other words, modules with identical topologies have the same functional forms of $f_{1}$ and $f_{2}$, such that each topology of module μ defines a parametric family of functions $f_{1}$ and $f_{2}$, where all rate constants within module μ other than ξ, or ξ and η, play a role of parameters.

Since the number of possible topologies is infinite, there is an infinite number of functional forms of $F$. However, the number of parameteric families of functions $f_{1}$ and $f_{2}$ is finite, and it turns out to be small. To see this, notice that for any module with a single marked reaction, the CGP can be carried out in two stages. In the first stage, we can eliminate all metabolites that do not participate in the marked reaction. The resulting coarse-grained module is minimal in the sense that it can have at most two internal metabolites. Such minimal modules (and, as a consequence, all modules with one marked reaction) fall into three distinct topological classes, which are specified by the location of the marked reaction with respect to the I/O metabolites, as shown in Figure 7. This implies that there are only three parameteric families of the function $f_{1}$. The topologies of the three minimal modules are sufficiently simple that the three corresponding parametric functional forms of $f_{1}$ can be easily computed by applying the coarse-graining Equation 19 or Equation 22. This result is formulated in Proposition 2.

![Figure 7.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig7-v2.jpg)

**Figure 7.:** Left column shows a general module from each topological class. The right column shows a minimal fully connected module in each topological class (see text for details). Circles represent metabolites and lines represent reactions. Only the I/O metabolites and the metabolites that participate in the marked reaction are shown, all other metabolites are suppressed. Short lines that have only one terminal metabolite represent all remaining reactions in which this metabolite participates, reactions between all other metabolites are suppressed. Metabolites are labeled according to the conventions listed in the text. The marked reaction is colored orange and labeled $a$. The module is represented by a gray rectangle, and the rest of the network is not shown.

The same logic applies to modules with two marked reactions. CGP that eliminates all metabolites that do not participate in the marked reactions maps all such modules onto respective minimal modules, which can have at most four internal metabolites (see Figure 8). This result is formulated in Proposition 3. Minimal modules (and, as a consequence, all modules with two marked reactions) fall into nine distinct topological classes, which are specified by the locations of the marked reactions. All modules from the same topological class are described by functions $f_{2}$ from the same parametric family. These families are characterized in Corollary 3.

![Figure 8.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig8-v2.jpg)

**Figure 8.:** Notations as in Figure 7.

These topological classifications are extremely useful for the following reason. If we can show that all functions from the same parameteric family (corresponding to a given topological class) have some common property irrespectively of the values of the parameters, it would imply that this property holds for all modules from the corresponding topological class. This logic is a key part of the proofs of both Theorem 1 and Theorem 2.

To formalize this reasoning, consider module $\mu=(A_{\mu},x→_{\mu})$ and let $a=i_{a}↔j_{a}$ and $b=i_{b}↔j_{b}$ be two reactions from its set of reactions $R_{\mu}$. I call a pair $(\mu,a)$ a single-marked module and I call a triplet $(\mu,a,b)$ a double-marked module, and I refer to reactions $a$ and $b$ as marked within module μ. The topology of a single-marked module $(\mu,a)$ is determined not only by the reaction matrix $R_{\mu}$, but also by the position of the marked reaction, so I refer to the pair $(R_{\mu},a)$ as the topology of the single-marked module $(\mu,a)$. Similarly, I refer to the triplet $(R_{\mu},a,b)$ as the topology of the double-marked module $(\mu,a,b)$. I denote by $x→_{\mu∖a}$ the matrix of rate constants of all reactions in module μ other than reaction $a$ and I denote by $x→_{\mu∖{a,b}}$ the matrix of all rate constants in module μ other than reactions $a$ and $b$. I denote the sets of all single- and double-marked modules by $ℳ_{1}$ and $ℳ_{2}$, respectively. To avoid metabolite labeling ambiguities, I adopt the following conventions:

It is easy to see that the set of all single-marked modules $ℳ_{1}$ can be partitioned into three non-overlapping topological classes depending on the type of the marked reaction $a$. I denote the classes of all single-marked modules where the marked reaction is bypass, i/o or internal (see Notations and definitions) by $ℳ^{b}$, $ℳ^{io}$ and $ℳ^{i}$, respectively (Figure 7). Similarly, the set $ℳ_{2}$ can be partitioned into nine non-overlapping topological classes according to the types of marked reactions and the type of metabolite that is shared by both of these reactions (I/O, internal, or none). These classes are listed in Table 1 and illustrated in Figure 8.

**Table 1.**
 Classification of double-marked modules.Metabolites are labeled according to conventions described in the text. $m_{ℳ}$ is the minimum number of internal metabolites in a module from class $ℳ$. $A_{ℳ}$ is the set of internal and I/O metabolites in all minimal modules in class $ℳ$.


<table>
  <thead>
    <tr>
      <th>Class</th>
      <th>a</th>
      <th>b</th>
      <th>Shared metab.</th>
      <th>Verbal description</th>
      <th>mℳ</th>
      <th>Aℳ</th>
      <th>Equation for f2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ℳb,io,IO</td>
      <td>(1,2)</td>
      <td>(1,3)</td>
      <td>1</td>
      <td>Bypass and i/o reactions, shared I/O metabolite</td>
      <td>2</td>
      <td>{1,2,3}</td>
      <td>Equation (34)</td>
    </tr>
    <tr>
      <td>ℳb,i,∅</td>
      <td>(1,2)</td>
      <td>(3,4)</td>
      <td>–</td>
      <td>Bypass and internal reactions, no shared metabolies</td>
      <td>2</td>
      <td>{1,2,3,4}</td>
      <td>Equation (35)</td>
    </tr>
    <tr>
      <td>ℳio,io,I</td>
      <td>(1,3)</td>
      <td>(2,3)</td>
      <td>3</td>
      <td>i/o reactions, shared internal metabolite</td>
      <td>1</td>
      <td>{1,2,3}</td>
      <td>Equation (36)</td>
    </tr>
    <tr>
      <td>ℳio,io,IO</td>
      <td>(1,3)</td>
      <td>(1,4)</td>
      <td>1</td>
      <td>i/o reactions, shared I/O metabolite</td>
      <td>2</td>
      <td>{1,2,3,4}</td>
      <td>Equation (37)</td>
    </tr>
    <tr>
      <td>ℳio,io,∅</td>
      <td>(1,3)</td>
      <td>(2,4)</td>
      <td>–</td>
      <td>i/o reactions, no shared metabolites</td>
      <td>2</td>
      <td>{1,2,3,4}</td>
      <td>Equation (38)</td>
    </tr>
    <tr>
      <td>ℳio,i,I</td>
      <td>(1,3)</td>
      <td>(3,4)</td>
      <td>3</td>
      <td>i/o and internal reactions, shared internal metabolite</td>
      <td>2</td>
      <td>{1,2,3,4}</td>
      <td>Equation (39)</td>
    </tr>
    <tr>
      <td>ℳio,i,∅</td>
      <td>(1,3)</td>
      <td>(4,5)</td>
      <td>–</td>
      <td>i/o and internal reactions, no shared metabolites</td>
      <td>3</td>
      <td>{1,2,3,4,5}</td>
      <td>Equation (40)</td>
    </tr>
    <tr>
      <td>ℳi,i,I</td>
      <td>(3,4)</td>
      <td>(3,5)</td>
      <td>3</td>
      <td>Internal reactions, shared internal metabolite</td>
      <td>3</td>
      <td>{1,2,3,4,5}</td>
      <td>Equation (41)</td>
    </tr>
    <tr>
      <td>ℳi,i,∅</td>
      <td>(3,4)</td>
      <td>(5,6)</td>
      <td>–</td>
      <td>Internal reactions, no shared metabolites</td>
      <td>4</td>
      <td>{1,2,3,4,5,6}</td>
      <td>Equation (42)</td>
    </tr>
  </tbody>
</table>

Each topological class contains infinitely many modules, with various numbers of metabolites and various topologies. However, for each topological class $ℳ$, there is a minimum number of internal metabolites $m_{ℳ}$, such that all modules within $ℳ$ must have at least $m_{ℳ}$ internal metabolites. I denote the set of metabolites minimal in the topological class $ℳ$ by $A_{ℳ}$. It is clear that for the single-marked module classes $ℳ^{b}$ and for $ℳ^{io}$, $m_{ℳ^{b}}=m_{ℳ^{io}}=1$ and $A_{ℳ^{b}}=A_{ℳ^{io}}={3}$, and for $ℳ^{i}$, $m_{ℳ^{i}}=2$ and $A_{ℳ^{i}}={3,4}$ (see second column in Figure 7). For the double-marked modules, $m_{ℳ}$ and $A_{ℳ}$ are given in Table 1 and illustrated in Figure 8.

If a single-marked module from the topological class $ℳ$ has the minimum number of metabolites $n_{ℳ}$ in that class, I call such module and its topology minimal in $ℳ$. There may be several minimal topologies in a topological class, but there is only one minimal topology that is fully connected. A topology $(R_{\mu},a)$ is called fully connected if the reaction set $R_{\mu}$ is complete in the sense that it contains reactions between all pairs of metabolites in the minimal metabolite set $A_{ℳ}$. I denote such complete reaction set for the class $ℳ$ by $R_{ℳ}$, and I denote the respective fully connected topology by $(R_{ℳ},a)$. I employ the same terminology and analogous notations for double-marked modules. The minimal fully connected topologies are shown in the second column in Figure 7 and Figure 8.

Next, I prove Proposition 2, which is the key step toward the proof of Theorem 1. This proposition states that there are only three functional forms for the function $f_{1}$ and characterizes them. The idea of the proof is the following. According to Property 5 (Box 1), all single-marked modules that are mapped by the CGP onto a minimal module with the same topology $(R_{\mu},a)$ have the same functional form of $f_{1}$. In other words, each minimal topology $(R_{\mu},a)$ specifies a parameteric family of the function $f_{1}$. Since the number of possible minimal topologies is finite, the claim of Theorem 1 can be tested for each corresponding functional form of $f_{1}$. However, the number of minimal topologies is rather large. Fortunately, another simplification is possible. Since the reaction set $R_{\mu}$ of any minimal single-marked module is a subset of the complete reaction set $R_{ℳ}$, the fully connected topology $(R_{ℳ},a)$ specifies the largest parametric family of the function $f_{1}$ for the class $ℳ$, such that all other families can be obtained from it by setting some parameters to zero, which is equivalent to removing reactions from the fully connected topology. In other words, all single-marked modules that belong to the topological class $ℳ$ are described by functions $f_{1}$ that belong to one parameteric family corresponding to the fully connected topology minimal in $ℳ$. The three parameteric families of $f_{1}$ are characterized by Proposition 2.

One important consequence of Proposition 2 is that it is not necessary to test the claim of Theorem 1 for each family of $f_{1}$ that corresponds to each minimal topology. Instead, it is sufficient to test it for the three families that correspond to the fully connected minimal topologies in each class.

#### Proposition 2

Let $(\mu,a)$ be a single-marked module, and let ξ be the rate constant of reaction $a$. Then $y_{\mu}=f_{1}⁢(u)$, where $u=ξ+\alpha$ for some $\alpha\geq0$, and the function $f_{1}$ is given by one of the following expressions.

$$
f_{1}(u)=u,if(\mu,a)\inℳ^{b},
$$



$$
f_{1}(u)=w_{12}+\frac{uw_{32}}{u/K_{13}+w_{32}},if(\mu,a)\inℳ^{io},
$$



$$
f_{1}(u)=w_{12}+\frac{D_{3}w_{14}w_{42}+D_{4}w_{13}w_{32}+w_{13}w_{42}u+w_{14}w_{32}u/K_{34}}{D_{3}D_{4}−u^{2}/K_{34}}, if(\mu,a)\inℳ^{i}.
$$

Here $D_{3}=w_{31}+w_{32}+u$, $D_{4}=w_{41}+w_{42}+u/K_{34}$, and all $w_{i⁢j}\geq0$ are independent of ξ.

##### Proof

Since any single-marked module $(\mu,a)$ belongs to exactly one of three classes $ℳ^{b}$, $ℳ^{io}$ and $ℳ^{io}$, I consider these three cases one by one.

Case $(\mu,a)\inM^{b}$. According to the labeling conventions outlined above, $a=1↔2$ (see Figure 7). Equation 29 follows directly from Property #4 of the CGP (Box 1).

Case $(\mu,a)\inM^{io}$. According to the labeling conventions, $a=1↔3$ (see Figure 7). According to Property #1 of the CGP, module μ can be coarse-grained in two stages, by first applying $CG^{A_{\mu}∖{3}}$ which eliminates metabolites $4,…,m$ (those that do not participate in the marked reaction) and then applying $CG^{{3}}$ which eliminates the remaining metabolite 3. Mathematically, $CG^{\mu}=CG^{A_{\mu}∖{3}}∘CG^{{3}}$. After applying $CG^{A_{\mu}∖{3}}$, the resulting coarse-grained module $\mu^{′}$ has a single internal metabolite 3 and at most three effective reactions $1↔2$, $1↔3$ and $2↔3$ (Figure 7), that is, it is minimal in $ℳ^{io}$. By virtue of Properties #2 and #4 of the CGP, the effective rate constants $w_{12}$, $w_{23}$ are independent of ξ and $u≡w_{13}=ξ+\alpha$. Note that $w_{12}$ may equal zero, but $w_{23}\neq0$ because $\mu^{′}$ is a module. Regardless, the reaction set $R_{\mu^{′}}$ of module $\mu^{′}$ is always a subset of the complete reaction set $R_{ℳ^{io}}$. Thus, to obtain the effective rate constant $y_{\mu}$, I consider the most general case when $\mu^{′}$ is fully connected and eliminate the remaining internal metabolite 3, which leads to Equation 30.

Case $(\mu,a)\inℳ^{i}$. According to the labeling conventions, $a=3↔4$ (see Figure 7). Otherwise, the logic of the proof is exactly the same as for the case $(\mu,a)\inℳ^{io}$.

Next I prove Proposition 3 which states that, for any double-marked module that belongs to a given topological class, there exists a double-marked module that is minimal in the same class, such that both modules have the same function $f_{2}$. The corresponding minimal module is obtained from the original module by applying the CGP. This proposition is important because it implies that all functions $f_{2}$ can be completely characterized by only examing minimal modules. Then, analogously to single-marked modules, Corollary 3 states that function $f_{2}$ can belong to one of nine parameteric families which are defined by the fully connected minimal topologies in each topological class.

#### Proposition 3

Let $(\mu,a,b)$ be a double-marked module that belongs to the topological class $M$, and let ξ and η be the rate constants of reactions $a$ and $b$, respectively. Then there exist non-negative constants α and β and a double-marked module $(\mu^{′},a,b)$ minimal in $M$ such that $y_{\mu}=y_{\mu^{′}}=f_{2}⁢(u,v)$, where

$$
u=ξ+\alpha,
$$



$$
v=η+\beta
$$

are the rate constants of the marked reactions $a$ and $b$ in $\mu^{′}$, respectively, and all other rate constants in $\mu^{′}$ are independent of ξ or η. Module $\mu^{′}$ is obtained from μ by the coarse-graining procedure $CG^{\mu∖{a,b}}$ that eliminates all metabolites internal to module μ that do not participate in reactions $a$ or $b$.

##### Proof

To prove this proposition, I will construct the double-marked module $(\mu^{′},a,b)$ minimal in $ℳ$ by applying $CG^{\mu∖{a,b}}$. Let $m_{ℳ}$ be the mimimal number of internal metabolites in class $ℳ$ (see Table 1). According to the metabolite labeling conventions, metabolites $n_{ℳ}+3,n_{ℳ}+4,…$ are neither I/O nor do they participate in the marked reactions. $CG^{\mu∖{a,b}}$ eliminates all these metabolites and maps module μ onto module $\mu^{′}$, all of whose internal metabolites participate in reactions $a$ and/or $b$. Therefore, $(\mu^{′},a,b)$ is minimal in class $ℳ$ (Figure 8). According to Properties #2 and #4 of the CGP (Box 1), the effective rate constants $u$ and $v$ of reactions $a$ and $b$ in module $\mu^{′}$ are given by linear relationships in Equation 32 and Equation 33, and the remaining effective rate constants are independent of ξ and η. The fact that $y_{\mu}=y_{\mu^{′}}$ follows from Property #1 of the CGP, $CG^{\mu}=CG^{\mu∖{a,b}}∘CG^{A_{\mu^{′}}}$.

#### Corollary 3

Let $(\mu,a,b)$ be a double-marked module, and let ξ and η be the rate constants of reactions $a$ and $b$, respectively. The function $f_{2}$ that maps ξ and η onto module’s effective rate constant $y_{\mu}$ belongs to one of nine parametric families. If $(\mu,a,b)\inM^{b,io,IO}$, then

$$
f_{2}(u,v)=u+\frac{vw_{32}}{v/K_{13}+w_{32}}.
$$

If $(\mu,a,b)\inM^{b,i,∅}$, then

$$
f_{2}(u,v)=u+\frac{D_{3}w_{14}w_{42}+D_{4}w_{13}w_{32}+w_{13}w_{42}v+w_{14}w_{32}v/K_{34}}{D_{3}D_{4}−v^{2}/K_{34}},D_{3}=w_{31}+w_{32}+v,D_{4}=w_{41}+w_{42}+v/K_{34}.
$$

If $(\mu,a,b)\inM^{io,io,I}$, then

$$
f_{2}(u,v)=w_{12}+\frac{uv}{u/K_{13}+v},
$$

If $(\mu,a,b)\inM^{io,io,IO}$, then

$$
f_{2}(u,v)=w_{12}+\frac{D_{3}vw_{42}+D_{4}uw_{32}+uw_{34}w_{42}+vw_{43}w_{32}}{D_{3}D_{4}−w_{34}w_{43}},D_{3}=u/K_{13}+w_{32}+w_{34},D_{4}=v/K_{14}+w_{42}+w_{43}.
$$

If $(\mu,a,b)\inM^{io,io,∅}$, then

$$
f_{2}(u,v)=w_{12}+\frac{D_{3}w_{14}v/K_{24}+D_{4}uw_{32}+uw_{34}v/K_{24}+w_{14}w_{43}w_{32}}{D_{3}D_{4}−w_{34}w_{43}},D_{3}=u/K_{13}+w_{32}+w_{34},D_{4}=w_{41}+v/K_{24}+w_{43}.
$$

If $(\mu,a,b)\inM^{io,i,I}$, then

$$
f_{2}(u,v)=w_{12}+\frac{D_{3}w_{14}w_{42}+D_{4}uw_{32}+uvw_{42}+w_{14}w_{32}v/K_{34}}{D_{3}D_{4}−v^{2}/K_{34}},D_{3}=u/K_{13}+w_{32}+v,D_{4}=w_{41}+w_{42}+v/K_{43}.
$$

If $(\mu,a,b)\inM^{io,i,∅}$, then

$$
f_{2}(u,v)=W_{12}+\frac{W_{13}W_{32}}{W_{31}+W_{32}},W_{ij}=w_{ij}+\frac{D_{4}w_{i5}w_{5j}+D_{5}w_{i4}w_{4j}+w_{i4}vw_{5j}+w_{i5}w_{4j}v/K_{45}}{D_{4}D_{5}−v^{2}/K_{45}},D_{4}=w_{41}+w_{42}+w_{43}+v,D_{5}=w_{51}+w_{52}+w_{53}+v/K_{45},w_{13}≡u.
$$

If $(\mu,a,b)\inM^{i,i,I}$, then

$$
f_{2}(u,v)=W_{12}+\frac{D_{3}W_{14}W_{42}+D_{4}W_{13}W_{32}+W_{13}W_{34}W_{42}+W_{14}W_{43}W_{32}}{D_{3}D_{4}−W_{34}W_{43}},W_{ij}=w_{ij}+\frac{w_{i5}w_{5j}}{D_{5}},D_{3}=W_{31}+W_{32}+W_{34},D_{4}=W_{41}+W_{42}+W_{43},D_{5}=w_{51}+w_{52}+w_{53}+w_{54},w_{34}≡u,w_{35}≡v.
$$

If $(\mu,a,b)\inM^{i,i,∅}$, then

$$
(42)f_{2}(u,v)=W_{12}+\frac{D_{3}W_{14}W_{42}+D_{4}W_{13}W_{32}+W_{13}W_{34}W_{42}+W_{14}W_{43}W_{32}}{D_{3}D_{4}−W_{34}W_{43}},(43)W_{ij}=w_{ij}+\frac{D_{5}w_{i6}w_{6j}+D_{6}w_{i5}w_{5j}+w_{i5}w_{6j}v+w_{i6}w_{5j}v/K_{56}}{D_{5}D_{6}−v^{2}/K_{56}},D_{3}=W_{31}+W_{32}+W_{34},D_{4}=W_{41}+W_{42}+W_{43},D_{5}=w_{51}+w_{52}+w_{53}+w_{54}+v,D_{6}=w_{61}+w_{62}+w_{63}+w_{64}+v/K_{56},w_{34}≡u.
$$

In Equation 34 through Equation 35, $u$ and $v$ are given by Equation 32 and Equation 33. All effective activities $w_{i⁢j}\geq0$ are constants (other than cases where they stand for $u$ or $v$) that depend on the topology of module μ and on the parameters $x→_{\mu∖{a,b}}$ but do not depend on ξ and η.

##### Proof

This statement and Equation 34 through Equation 35 follow directly from Proposition 3 and the fact that the reaction set of any double-marked module in any given topological class is a subset of the complete reaction set in that topological class.

### Derivation of Equation 6 and Equation 9

Consider a higher-level phenotype $y$, such as the effective activity of a module, which is function of a multivariate lower-level phenotype $x→=(x_{1},x_{2},…,x_{n})$, such as the rates of individual reactions within the module, $y=F⁢(x→)$. Denote the wildtype values of the phenotypes as $x→^{0}=(x_{1}^{0},x_{2}^{0},…,x_{n}^{0})$ and $y^{0}=F⁢(x→^{0})$. Consider a mutation that perturbes these values, so that the mutant has lower-level phenotypic values $x→^{′}=(x_{1}^{′},x_{2}^{′},…,x_{n}^{′})$. The relative effect of the mutation on phenotype xi is $\delta⁢x_{i}=x_{i}^{′}/x_{i}^{0}-1$. If all $∥\delta⁢x_{i}∥≪1$ where $∥x→∥$ denotes the length of vector $x→$, then the value of the higher-level phenotype $y^{′}$ in the mutant is given by

$$
y^{′}=y^{0}⁢(1+\sumi=1nC_{i}⁢\delta⁢x_{i}+\frac{1}{2}⁢\sumi,j=1nH_{i⁢j}⁢\delta⁢x_{i}⁢\delta⁢x_{j})+o⁢(∥\delta⁢x→∥^{2}).
$$

where

$$
C_{i}=\frac{x_{i}^{0}}{y^{0}}\frac{∂F}{∂x_{i}}|_{x→=x→^{0}},i=1,…,n,
$$



$$
H_{ij}=\frac{x_{i}^{0}x_{j}^{0}}{y^{0}}\frac{∂^{2}F}{∂x_{i}∂x_{j}}|_{x→=x→^{0}},i,j=1,…,n,
$$

which I refer to as first- and second-order control coefficients of the lower-level phenotypes $x_{i}$ and $x_{j}$ with respect to the higher-level phenotype $y$.

Now consider two single mutants, A and B, and the double-mutant AB. Each mutation A and B and their combination may perturb all $x_{i}$ phenotypes such that $x_{i}^{A}=x_{i}^{0}⁢(1+\delta^{A}⁢x_{i})$, $x_{i}^{B}=x_{i}^{0}⁢(1+\delta^{B}⁢x_{i})$, and $x_{i}^{A⁢B}=x_{i}^{0}⁢(1+\delta^{A⁢B}⁢x_{i})=x_{i}^{0}⁢(1+\delta^{A}⁢x_{i}+\delta^{B}⁢x_{i}+2⁢\delta^{A}⁢x_{i}⁢\delta^{B}⁢x_{i}⁢\epsilon⁢x_{i}).$

Assuming that $∥\delta^{A}⁢x→∥≪1$, $∥\delta^{B}⁢x→∥≪1$ and $∥\delta^{A⁢B}⁢x→∥≪1$, using the approximation in Equation 44 and the definition of $\epsilon⁢x_{i}$ (analogous to Equation 5), I obtain

$$
\delta^{A}⁢y=\sumi=1nC_{i}⁢\delta^{A}⁢x_{i}+o⁢(∥\delta^{A}⁢x→∥),
$$



$$
\delta^{B}⁢y=\sumi=1nC_{i}⁢\delta^{B}⁢x_{i}+o⁢(∥\delta^{B}⁢x→∥),
$$



$$
\epsilony=\frac{\sumi=1nC_{i}\epsilonx_{i}\delta^{A}x_{i}\delta^{B}x_{i}+\frac{1}{2}\sumi,j=1nH_{ij}\delta^{A}x_{i}\delta^{B}x_{j}}{\sumi=1n\sumj=1nC_{i}C_{j}\delta^{A}x_{i}\delta^{B}x_{j}}+o(1),
$$

where $o⁢(1)$ refers to terms that are vanishingly small as $\delta^{A}⁢x_{i}→0$ , $\delta^{B}⁢x_{i}→0$, $i=1,…⁢n$.

I examine two special cases of Equation 49. The first special case is when both mutations affect a single phenotype $x_{k}$, that is, when all $\delta^{A}⁢x_{i}=0$ and all $\delta^{B}⁢x_{i}=0$ except for $i=k$. Then Equation 47, Equation 48, Equation 49 simplify to

$$
\delta^{A}⁢y=C_{k}⁢\delta^{A}⁢x_{k}+o⁢(|\delta^{A}⁢x_{k}|),
$$



$$
\delta^{B}⁢y=C_{k}⁢\delta^{B}⁢x_{k}+o⁢(|\delta^{B}⁢x_{k}|),
$$



$$
\epsilony=\frac{\epsilonx_{k}}{C_{k}}+\frac{H_{kk}}{2C_{k}^{2}}+o(1).
$$

Equation 52 is equivalent to Equation 6.

The second special case is when mutation A affects a single phenotypes $x_{k}$ and mutation B affects a single phenotype $x_{ℓ}$ ($k\neqℓ$), i.e., all $\delta^{A}⁢x_{i}=0$ except for $i=k$, all $\delta^{B}⁢x_{i}=0$ except for $i=ℓ$, and all $\epsilon⁢x_{i}=0$. Then Equation 47, Equation 48, Equation 49 simplify to

$$
\delta^{A}⁢y=C_{k}⁢\delta^{A}⁢x_{k}+o⁢(|\delta^{A}⁢x_{k}|),
$$



$$
\delta^{B}⁢y=C_{ℓ}⁢\delta^{B}⁢x_{ℓ}+o⁢(|\delta^{B}⁢x_{ℓ}|),
$$



$$
\epsilony=\frac{H_{kℓ}}{2C_{k}C_{ℓ}}+o(1).
$$

Equation 55 is equivalent to Equation 9.

### Calculation of epistasis in simple modules

Equation 52 and Equation 55 allow me to compute how epistasis propagates and emerges in arbitrary metabolic networks. In this section, I show how to implement these calculations for three simple metabolic modules considered above and in module ν shown in Figure 3.

### Linear pathway

First, consider how epistasis propagates through a linear pathway (Figure 6A). For simplicity, assume that both mutations A and B affect the same reaction $1↔2$. It follows from Equation 26 that

$$
y_{\mu}=f_{1}⁢(ξ)=(\frac{1}{ξ}+\alpha)^{-1},
$$

where α is a positive constant. Therefore, the first- and second-order control coefficients of reaction $1↔2$ with respect to the flux through the linear pathway μ are given by

$$
C=\frac{y_{\mu}}{ξ}=\frac{1}{1+\alphaξ},
$$



$$
H=−\frac{2\alphaξ}{(1+\alphaξ)^{2}}.
$$

Substituting these expressions into the expression for the fixed point $\epsilon¯=-H⁢(2⁢C⁢(1-C))^{-1}$, I find that $\epsilon¯=1$, irrespectively of the rates of other reactions in the linear pathway. This implies that epistasis $\epsilon⁢ξ<1$ at the level of reaction $1↔2$ would induce a lower value of epistasis $\epsilon⁢y_{\mu}<\epsilon⁢ξ<1$ at the level of the entire linear pathway, any value $\epsilon⁢ξ>1$ would induce a higher value of epistasis $\epsilon⁢y_{\mu}>\epsilon⁢ξ>1$, and $\epsilon⁢ξ=1$ would induce $\epsilon⁢y_{\mu}=1$.

Now consider emergence of epistasis in a linear pathway. Suppose that mutation A affects reaction $1↔2$ and mutation B affects reaction $2↔3$. Denote the rate constant of reactions $1↔2$ and $2↔3$ by $ξ≡x_{12}$ and $η≡x_{23}$, respectively. It follows from Equation 26 that

$$
y_{\mu}=f_{2}⁢(ξ,η)=(\frac{1}{ξ}+\frac{1}{K_{12}⁢η}+\beta)^{-1},
$$

where β is a positive constant. Therefore,

$$
C_{ξ}=\frac{y_{\mu}}{ξ},C_{η}=\frac{y_{\mu}}{K_{12}η},H_{ξη}=\frac{2y_{\mu}^{2}}{K_{12}ξη},
$$

which, after substituting into Equation 9, yield $\epsilon⁢y_{\mu}=1$. Together with the fact that $\epsilon¯=1$ (see above), this result implies that epistasis coefficient between any two mutations that affect different reactions in a linear pathway equals 1.

### Two parallel pathways

Suppose that mutation A affects reaction $1↔3$ and mutation B affects reaction $1↔4$ in the linear metabolic pathway shown in Figure 6B. Denote the rate constants of reaction $1↔3$ and $1↔4$ by $ξ≡x_{13}$ and $η≡x_{14}$. It follows from Equation 27 that

$$
y_{\mu}=f_{2}⁢(ξ,η)=(\frac{1}{ξ}+\alpha)^{-1}+(\frac{1}{η}+\beta)^{-1},
$$

where $\alpha=1/(K_{13}⁢x_{32})$ and $\beta=1/(K_{14}⁢x_{42})$. Thus, we have $H_{ξ⁢η}=0$, and there is no epistasis between such mutations.

### Module ν in Figure 3A

I denote the rate of the reactions affected by mutations A and B by $ξ=x_{13}$ and $η=x_{42}$, and I also denote $z=x_{34}$. I will calculate the epistasis coefficient $\epsilon⁢y_{ν}$ in two stages, by first calculating the epistasis coefficient $\epsilon⁢y_{\mu}$ and then propagating it to $\epsilon⁢y_{ν}$ using Equation 6. Here I am specifically interested in how $\epsilon⁢y_{ν}$ depends on the rate constant $z$.

To compute epistasis between mutations A and B at the level of module μ, I rewrite Equation 28 as

$$
y_{\mu}=\frac{a⁢ξ⁢η+b_{ξ}⁢ξ+b_{η}⁢η+c}{d⁢ξ⁢η+e_{ξ}⁢ξ+e_{η}⁢η+f},
$$

where $a=x_{14}/K_{13}+x_{32}+z$, $b_{ξ}=x_{32}⁢(x_{41}+z/K_{34})$, $b_{η}=x_{14}⁢(x_{32}+z)$, $c=x_{14}⁢x_{32}⁢z/K_{34}$, $d=1/K_{13}$, $e_{ξ}=(x_{41}+z/K_{34})/K_{13}$, $e_{η}=x_{32}+z$, $f=x_{32}⁢z/K_{34}+x_{41}⁢z+x_{32}⁢x_{41}$. I obtain the following expressions for the first- and second-order control coefficients.

$$
C_{ξ}=\frac{ξ}{y_{\mu}}⁢(\frac{c~_{1}⁢z+d~_{1}}{D})^{2},
$$



$$
C_{η}=\frac{η}{y_{\mu}}⁢\frac{1}{K_{14}}⁢(\frac{c~_{2}⁢z+d~_{2}}{D})^{2},
$$



$$
H_{ξ⁢η}=\frac{ξ⁢η}{y_{\mu}}⁢\frac{2⁢z}{K_{14}}⁢\frac{(c~_{1}⁢z+d~_{1})⁢(c~_{2}⁢z+d~_{2})}{D^{3}},
$$

where $D=d⁢ξ⁢η+e_{ξ}⁢ξ+e_{η}⁢η+f$, $c~_{1}=x_{23}/K_{24}+η$, $d~_{1}=x_{32}⁢(x_{41}+η)$, $c~_{2}=ξ+x_{14}$, $d~_{2}=x_{14}⁢(ξ/K_{13}+x_{32})$. Substituting Equation 56 through Equation 58 into Equation 53 through Equation 55, I obtain

$$
\delta^{A}⁢y_{\mu}=\frac{ξ}{y_{\mu}}⁢(\frac{c~_{1}⁢z+d~_{1}}{D})^{2}⁢\delta^{A}⁢ξ,
$$



$$
\delta^{B}⁢y_{\mu}=\frac{η}{y_{\mu}}⁢\frac{1}{K_{14}}⁢(\frac{c~_{2}⁢z+d~_{2}}{D})^{2}⁢\delta^{B}⁢η.
$$



$$
\epsilon⁢y_{\mu}=\frac{z⁢(a~⁢z+b~)}{(c~_{1}⁢z+d~_{1})⁢(c~_{2}⁢z+d~_{2})},
$$

where $a~=c~_{1}⁢c~_{2}$ and $b~=(ξ/K_{13}+x_{32})⁢x_{14}⁢η+(x_{41}+η)⁢x_{32}⁢ξ$.

To obtain the expression for $\epsilon⁢y_{ν}$, I coarse-grain module ν by eliminating the only remaining internal metabolite 2 and obtain

$$
y_{ν}=x_{15}+\frac{y_{\mu}⁢x_{25}}{y_{\mu}/K_{12}+x_{25}}.
$$

I then apply equation Equation 6 with

$$
C=\frac{y_{\mu}}{y_{ν}}\frac{x_{25}^{2}}{(y_{\mu}/K_{12}+x_{25})^{2}},
$$



$$
H=−\frac{2y_{\mu}^{2}}{y_{ν}K_{12}}\frac{x_{25}^{2}}{(u/K_{12}+x_{25})^{3}}.
$$

Figure 3B illustrates how $\epsilon⁢y_{ν}$ changes as a function of $z$. It was generated using the following matrix of rate constants:

$$
x→=(00.3780.5140.23701.8100001.00142.23200z2.4467.9570z/2.4400.25906.9820.9940.2570).
$$

The Matlab code is available at https://github.com/skryazhi/epistasis_theory.

Next, I consider thress special cases of the toy network depicted in Figure 3A that relate this network to those in Figure 3C and D.

### Proof of Theorem 1

As discussed above, the key step toward the proof is Proposition 2, which states that the function $f_{1}$ belongs to one of three parameteric families, given by Equation 29, Equation 30, Equation 31. To complete the proof, I now explicitly evalute the control coefficient $C$ and the $H$ in Equation 6 for each of these functions and show that the inequalities in Equation 7 and Equation 8 hold for all parameter values.

#### Proof of Theorem 1

Let $a$ be the effective reaction within higher-level module ν that represents the lower-level module μ. To simplify notations, I denote $y_{\mu}≡ξ$. According to Proposition 2, the functional from of $f_{1}$ depends only on the topological class of the single-marked module $(ν,a)$. So, I consider the three classes one by one.

Case $(ν,a)\inM^{b}$. From Equation 29, $C=ξ/y_{ν}$ and $H=0$. Therefore, inequalities in Equation 7 and Equation 8 hold.

Case $(ν,a)\inM^{io}$. From Equation 30,

$$
C=\frac{ξ}{y_{ν}}(\frac{w_{32}}{D})^{2},
$$



$$
H=−2\frac{ξ^{2}}{y_{ν}}\frac{w_{32}^{2}}{D^{3}}\frac{1}{K_{13}}=−2C\frac{ξ/K_{13}}{D},
$$

where $D=(ξ+\alpha)/K_{13}+w_{32}$. From Equation 64, it is clear that $C\geq0$. Re-writing Equation 64 as

$$
C=(\frac{ξ⁢w_{32}/D}{y_{ν}})⁢(\frac{w_{32}}{D})
$$

it is also clear that $C\leq1$ since both ratios in this expression do not exceed 1. From Equation 65 and the fact that $0\leqC\leq1$, it follows that $\epsilon¯\geq0$. To show that $\epsilon¯\leq1$, note that

$$
D⁢(1-C)=\frac{ξ+\alpha}{K_{13}}+w_{32}⁢(1-\frac{ξ⁢w_{32}/D}{y_{ν}})\geq\frac{ξ}{K_{13}}.
$$

Therefore,

$$
\epsilon¯=\frac{ξ/K_{13}}{D⁢(1-C)}\leq1.
$$

Therefore, inequalities in Equation 7 and Equation 8 hold.

Case $(ν,a)\inM^{i}$. I re-write Equation 31 as

$$
y_{ν}=w_{12}+\frac{A~⁢u+B~}{D},
$$

with $u=ξ+\alpha$, $D=C~⁢u+D~$, $A~=(w_{13}+w_{14})⁢(w_{42}+w_{32}/K_{34})$, $B~=(w_{31}+w_{32})⁢w_{14}⁢w_{42}+(w_{41}+w_{42})⁢w_{13}⁢w_{32}$, $C~=(w_{31}+w_{32})/K_{34}+(w_{41}+w_{42})$, $D~=(w_{31}+w_{32})⁢(w_{41}+w_{42})$, which yields

$$
C=\frac{ξ}{y_{ν}}\frac{A~D~−B~C~}{D^{2}},
$$



$$
H=−2\frac{ξ^{2}}{y_{ν}}\frac{(A~D~−B~C~)C~}{D^{3}}=−2C\frac{C~ξ}{D}.
$$

Next, it is straightforward to show that $A~⁢D~-B~⁢C~=(w_{41}⁢w_{32}-w_{31}⁢w_{42})^{2}/K_{31}\geq0$, which implies that $C\geq0$. To show that $C\leq1$, I expand the denominator in Equation 66 and obtain

$$
y_{ν}⁢D^{2}\geq(A~⁢u+B~)⁢(C~⁢u+D~)\gequ⁢(A~⁢D~+B~⁢C~)\geqξ⁢(A~⁢D~-B~⁢C~).
$$

Therefore, numerator in Equation 66 cannot exceed the denominator. The fact that $\epsilon¯\geq0$ follows directly from Equation 67 together with $C\leq1$. To show that $\epsilon¯\leq1$, first note that

$$
y_{ν}=w_{12}+\frac{A~⁢ξ}{D}+\frac{A~⁢\alpha+B~}{D}\geq\frac{A~⁢ξ}{D}.
$$

Therefore,

$$
D⁢(1-C)=C~⁢ξ+C~⁢\alpha+D~⁢(1-\frac{A~⁢ξ/D}{y_{ν}})+\frac{ξ}{D}⁢\frac{B~⁢C~}{y_{ν}}\geqC~⁢ξ.
$$

Hence,

$$
\epsilon¯=\frac{C~ξ}{D(1−C)}\leq1.
$$

Therefore, inequalities in Equation 7 and Equation 8 hold in this case as well, which completes the proof.

### Proof of Theorem 2

Proving Theorem 2 involves several auxiliary steps. First, I note that any two reactions $a$ and $b$ within any module μ can be either strictly serial, strictly parallel or serial-parallel. Then, Proposition 4 and its Corollary 4 establish that strictly parallel (serial) reactions in $(\mu,a,b)$ are also strictly parallel (serial) in a minimal module $(\mu^{′},a,b)$, which is obtained from μ by eliminating all metabolites that do not participate in the marked reactions. Next, recall that in both modules $(\mu,a,b)$ and $(\mu^{′},a,b)$ the same function $f_{2}$ maps the rate constants of two marked reactions onto module’s effective rate constant (Proposition 3). Since the epistasis coefficient depends only on the shape of this function, we only need to consider all minimal modules in order to understand what kinds of epistasis may arise between mutations affecting strictly serial and strictly parallel reactions in any module. This is a big simplification because the number of different minimal topologies is finite and the parameteric families of function $f_{2}$ are known for all of them (see Corollary 3). As a consequence, to prove Theorem 2, we could in principle list all of the minimal topologies, identify those where the marked reactions are strictly serial or strictly parallel and evalulate the epistasis coefficient using Equation 9 for every respective function $f_{2}$.

Unfortunately, the number of minimal topologies is very large, so that such brute-force approach would be quite cumbersome. I take a less cumbersome approach which is based on the realization that a strictly serial or strictly parallel relationship between two reactions cannot be altered by removing a third reaction from the module (Proposition 5). This implies that every minimal topology where the two reactions are strictly serial can be produced from another, more connected, ‘generating’ topology by removing some reactions; and similarly for minimal modules where the reactions are strictly parallel (Proposition 6). All generating topologies can be identified by a simple algorithm given in Appendix 3.

Finally, I prove Theorem 2 in three steps. First, Proposition 7 shows that $\epsilon⁢y_{\mu}\leq0$ for any minimal module μ with any strictly parallel generating topology. Second, Proposition 8 shows that that $\epsilon⁢y_{\mu}\geq1$ for any minimal module μ with any strictly serial generating topology. Third, the proof of Theorem 2 formally extends this argument to all modules with strictly serial and strictly parallel reactions.

#### Topological relationships between reactions within a module

Consider module μ with the I/O metabolites 1 and 2. As described above, a simple path connecting two metabolites $i$ and $j$ within module μ is denoted by $p_{i⁢j}^{\mu}=i↔k↔…↔ℓ↔j$. If such path contains reactions $a_{1},a_{2},…$ and does not contain reactions $b_{1},b_{2},…$, I denote it as $p_{i⁢j}^{\mu}⁢(a_{1},a_{2},…,b¯_{1},b¯_{2},…)$. I denote the set of all paths $p_{i⁢j}^{\mu}⁢(a_{1},a_{2},…,b¯_{1},b¯_{2},…)$ by $𝒫_{i⁢j}^{\mu}⁢(a_{1},a_{2},…,b¯_{1},b¯_{2},…)$.

According to Lemma 1 proven in Appendix 2, any reaction in the module belongs to at least one simple path within module μ that connects the I/O metabolites. Mathematically, $𝒫_{12}^{\mu}⁢(a)\neq∅$ for any reaction $a\inR_{\mu}$. Thus, we can define different topological relationships between any two reactions within a module based on the existence of various paths that do or do not contain them. Consequently, we can classify any double-marked module $(\mu,a,b)$ based on the toplogocial relationship between its marked reactions. This classification is orthogonal to that given in Table 1.

Two reactions $a\inR_{\mu}$ and $b\inR_{\mu}$ are called parallel within module μ if there exists a simple path $p_{12}^{\mu}⁢(a,b¯)$ and a simple path $p_{12}^{\mu}⁢(b,a¯)$. Two reactions $a\inR_{\mu}$ and $b\inR_{\mu}$ are called serial within module μ if there exist at least one simple path $p_{12}^{\mu}⁢(a,b)$. Two reactions are called strictly parallel within module μ if they are parallel but not serial, they are called strictly serial within module μ if they are serial but not parallel, and they are called serial-parallel within module μ if they are both serial and parallel. It is straightforward to show that there are no other logical possibilities for any two reactions to be anything other than strictly serial, strictly parallel or serial-parallel. This implies that two reactions are strictly parallel if they are not serial, and they are strictly serial if they are not parallel. If reactions $a$ and $b$ are serial, parallel, strictly serial, strictly parallel or serial-parallel within module μ, I also refer to the double-marked module $(\mu,a,b)$ as serial, parallel, etc. Since the relationship between reactions depends only on the topology of the module, but not on its rate constants, I also refer to the topology $(R_{\mu},a,b)$ as serial, parallel, etc.

Recall that coarse-graining procedure $CG^{\mu∖{a,b}}$ eliminates all metabolites internal to module μ other than those participating in reactions $a$ and $b$. If the double-marked module $(\mu,a,b)$ belongs to the topological class $ℳ$, then, according to Proposition 3, $CG^{\mu∖{a,b}}$ maps $(\mu,a,b)$ onto a minimal double-marked module $(\mu^{′},a,b)$ from the same class $ℳ$. The following proposition, which is easy to prove using Property #9 of the CGP (see Box 1), establishes how this procedure alters the topological relationship between reactions $a$ and $b$.

#### Proposition 4

Let $(\mu,a,b)$ be a double-marked module from the topological class $M$ (Table 1) and let $(\mu^{′},a,b)$ be the minimal double-marked module in $M$ onto which $(\mu,a,b)$ is mapped by $CG^{\mu∖{a,b}}$.

Note that the converse of the second claim in Proposition 4 is not true. In other words, if two reactions $a$ and $b$ are parallel in $(\mu,a,b)$, they may not be parallel in $(\mu^{′},a,b)$. Figure 9 shows a counter-example illustrating this.

![Figure 9.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig9-v2.jpg)

**Figure 9.:** Reactions $a$ and $b$ are parallel in $(\mu,a,b)$. CGP maps the double-marked module $(\mu,a,b)$ onto the minimal double-marked module $(\mu^{′},a,b)$ where reactions $a$ and $b$ are not parallel.

#### Corollary 4

Corollary 4 is an important step toward proving Theorem 2. According to Proposition 3, the function that maps the rate constants ξ and η of the reactions $a$ and $b$ in module μ onto the effective rate constant $y_{\mu}$ is the same function that maps the rate constants $u$ and $v$ of these reactions in the minimal module $\mu^{′}$ onto the effective rate constant $y_{\mu^{′}}$. It then immediately follows from Equation 9 that the epistasis coefficient $\epsilon⁢y_{\mu}$ between mutations affecting reactions $a$ and $b$ in the original module μ is the same as the epistasis coefficient $\epsilon⁢y_{\mu^{′}}$ in the minimal module $\mu^{′}$. Now, if the reactions $a$ and $b$ are strictly parallel in $(\mu,a,b)$, then, according to Corollary 4, these reactions are also strictly parallel in $(\mu^{′},a,b)$. Hence, to demonstrate that $\epsilon⁢y_{\mu}\leq0$ for any such double-marked module $(\mu,a,b)$, it is sufficient to show that $\epsilon⁢y_{\mu^{′}}\leq0$ for all double-marked modules $(\mu^{′},a,b)$ that are minimal in $ℳ$ and where the reactions $a$ and $b$ are strictly parallel. And similarly for the strictly serial reactions.

According to this logic, Theorem 2 can be proven by identifying all double-marked modules that are minimal in each of the topological classes listed in Table 1 and where the marked reactions are strictly parallel, evaluating epistasis for all of them, and showing that it is non-positive, irrespectively of the rate constants of any reactions, and similarly for the strictly serial reactions.

#### Generating topologies

Since the number of topologically distinct minimal double-marked modules is finite, the approach outlined above is in principle feasible. Unfortunately, the number of topologies to be considered is very large, so in practice it is very cumbersome. To avoid this complication, I take an alternative approach that is based on the same key idea as the proof of Theorem 1. Rather than considering one by one, each minimal topology where the marked reactions are strictly serial or strictly parallel (and the corresponding parametric families of $f_{2}$), the idea is to identify the most connected minimal topologies (and the corresponding largest parametric families of $f_{2}$) such that all the other minimal topologies with the strictly serial or strictly parallel reactions (and the corresponding parametric families) can be obtained from them by removing reactions (i.e. setting some parameters to zero).

This idea can be implemented using the following observations. If the two marked reactions are strictly parallel or strictly serial in a minimal module, then removing a third reaction from it does not change this relationship. This statement is proven in Proposition 5. As a consequence, all minimal modules in the topological classes $ℳ^{b,io,IO}$, $ℳ^{b,i,∅}$ and $ℳ^{io,io,IO}$ must be strictly parallel because the fully connected minimal topologies are strictly parallel (Figure 8). Similarly, all minimal modules in the topological class $ℳ^{io,io,I}$ must be strictly serial because the fully connected minimal topology is strictly serial (Figure 8). The fully connected minimal topologies in all other topological classes are serial-parallel. If the two reactions are serial-parallel, removing a third reaction can change their relationship into a strictly serial or strictly parallel one, depending on which reaction is removed, as shown for example in Figure 3A,C and D. In fact, by removing reactions from the fully connected minimal modules shown in Figure 8, it is easy to show that the topological classes $ℳ^{io,io,∅}$, $ℳ^{io,i,I}$, $ℳ^{io,i,∅}$, $ℳ^{i,i,I}$, $ℳ^{i,i,∅}$ contain both strictly serial and strictly parallel modules.

These observations suggests that adding reactions to a minimal module where the marked reactions are strictly serial or strictly parallel will either change their relationship into serial-parallel or will preserve their relationship until the minimal module is fully connected. Therefore, among all minimal modules in a topological class, there must exist the most connected modules where the marked reactions are strictly parallel or strictly serial, such that all other less connected strictly serial or strictly parallel modules can be produced from the most connected ones by removal of reactions. This statement is proven in Proposition 6. Such most connected strictly parallel and strictly serial minimal topologies, which I refer to as ‘generating’, are listed in Table 2 and Table 3. They define the largest parameteric familes of functions $f_{2}$ which I then examine for the value of $\epsilon⁢y_{\mu}$.

**Table 2.**
 Strictly parallel generating topologies.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Marked reactions</th>
      <th colspan="3">Generating topology</th>
    </tr>
    <tr>
      <th>Class</th>
      <th>a</th>
      <th>b</th>
      <th>ID</th>
      <th>Excluded reactions</th>
      <th>Figure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ℳb,io,IO</td>
      <td>1↔2</td>
      <td>1↔3</td>
      <td>b,io,IO,F</td>
      <td>∅</td>
      <td>Figure 7</td>
    </tr>
    <tr>
      <td>ℳb,i,∅</td>
      <td>1↔2</td>
      <td>3↔4</td>
      <td>b,i,∅,F</td>
      <td>∅</td>
      <td>Figure 7</td>
    </tr>
    <tr>
      <td>ℳio,io,IO</td>
      <td>1↔3</td>
      <td>1↔4</td>
      <td>io,io,IO,F</td>
      <td>∅</td>
      <td>Figure 7</td>
    </tr>
    <tr>
      <td>ℳio,io,∅</td>
      <td>1↔3</td>
      <td>2↔4</td>
      <td>io,io,∅,P</td>
      <td>{3↔4}</td>
      <td>Figure 9</td>
    </tr>
    <tr>
      <td>ℳio,i,I</td>
      <td>1↔3</td>
      <td>3↔4</td>
      <td>io,i,I,P</td>
      <td>{2↔4}</td>
      <td>Figure 10</td>
    </tr>
    <tr>
      <td rowspan="3">ℳio,i,∅</td>
      <td rowspan="3">1↔3</td>
      <td rowspan="3">4↔5</td>
      <td>io,i,∅,P1</td>
      <td>{3↔4,3↔5}</td>
      <td rowspan="3">Figure 11</td>
    </tr>
    <tr>
      <td>io,i,∅,P2</td>
      <td>{2↔5,3↔5}</td>
    </tr>
    <tr>
      <td>io,i,∅,P3</td>
      <td>{2↔4,2↔5}</td>
    </tr>
    <tr>
      <td rowspan="2">ℳi,i,I</td>
      <td rowspan="2">3↔4</td>
      <td rowspan="2">3↔5</td>
      <td>i,i,I,P1</td>
      <td>{2↔4,2↔5}</td>
      <td rowspan="2">Figure 12</td>
    </tr>
    <tr>
      <td>i,i,I,P2</td>
      <td>{1↔5,2↔5}</td>
    </tr>
    <tr>
      <td rowspan="7">ℳi,i,∅</td>
      <td rowspan="7">3↔4</td>
      <td rowspan="7">5↔6</td>
      <td>i,i,∅,P1</td>
      <td>{3↔5,3↔6,4↔5,4↔6}</td>
      <td rowspan="7">Figure 13</td>
    </tr>
    <tr>
      <td>i,i,∅,P2</td>
      <td>{1↔5,1↔6,2↔5,2↔6}</td>
    </tr>
    <tr>
      <td>i,i,∅,P3</td>
      <td>{2↔4,2↔6,3↔6,4↔5,4↔6}</td>
    </tr>
    <tr>
      <td>i,i,∅,P4</td>
      <td>{2↔4,2↔5,2↔6,4↔5,4↔6}</td>
    </tr>
    <tr>
      <td>i,i,∅,P5</td>
      <td>{1↔6,2↔4,2↔5,2↔6,4↔6}</td>
    </tr>
    <tr>
      <td>i,i,∅,P6</td>
      <td>{1↔4,1↔6,2↔4,2↔6,4↔6}</td>
    </tr>
    <tr>
      <td>i,i,∅,P7</td>
      <td>{1↔4,1↔5,2↔3,2↔6,3↔5,4↔6}</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Strictly serial generating topologies.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Marked reactions</th>
      <th colspan="3">Generating topologies</th>
    </tr>
    <tr>
      <th>Class</th>
      <th>a</th>
      <th>b</th>
      <th>ID</th>
      <th>Excluded reactions</th>
      <th>Figure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ℳio,io,I</td>
      <td>1↔3</td>
      <td>2↔3</td>
      <td>io,io,I,F</td>
      <td>∅</td>
      <td>Figure 7</td>
    </tr>
    <tr>
      <td>ℳio,io,∅</td>
      <td>1↔3</td>
      <td>2↔4</td>
      <td>io,io,∅,S</td>
      <td>{2↔3}</td>
      <td>Figure 9</td>
    </tr>
    <tr>
      <td rowspan="2">ℳio,i,I</td>
      <td rowspan="2">1↔3</td>
      <td rowspan="2">3↔4</td>
      <td>io,i,I,S1</td>
      <td>{2↔3}</td>
      <td rowspan="2">Figure 10</td>
    </tr>
    <tr>
      <td>io,i,I,S2</td>
      <td>{1↔4}</td>
    </tr>
    <tr>
      <td rowspan="3">ℳio,i,∅</td>
      <td rowspan="3">1↔3</td>
      <td rowspan="3">4↔5</td>
      <td>io,i,∅,S1</td>
      <td>{1↔4,1↔5}</td>
      <td rowspan="3">Figure 11</td>
    </tr>
    <tr>
      <td>io,i,∅,S2</td>
      <td>{2↔3,2↔4,3↔5}</td>
    </tr>
    <tr>
      <td>io,i,∅,S3</td>
      <td>{1↔5,2↔3,2↔5}</td>
    </tr>
    <tr>
      <td rowspan="2">ℳi,i,I</td>
      <td rowspan="2">3↔4</td>
      <td rowspan="2">3↔5</td>
      <td>i,i,I,S1</td>
      <td>{1↔3,2↔3}</td>
      <td rowspan="2">Figure 12</td>
    </tr>
    <tr>
      <td>i,i,I,S2</td>
      <td>{2↔3,2↔5,4↔5}</td>
    </tr>
    <tr>
      <td rowspan="2">ℳi,i,∅</td>
      <td rowspan="2">3↔4</td>
      <td rowspan="2">5↔6</td>
      <td>i,i,∅,S1</td>
      <td>{2↔3,2↔5,2↔6,4↔5,4↔6}</td>
      <td rowspan="2">Figure 13</td>
    </tr>
    <tr>
      <td>i,i,∅,S2</td>
      <td>{1↔3,1↔6,2↔3,2↔6,4↔6}</td>
    </tr>
  </tbody>
</table>

#### Proposition 5

Let $(\mu,a,b)$ and $(\mu^{′},a,b)$ be two minimal double-marked modules from the same topological class whose sets of reactions are $R_{\mu}$ and $R_{\mu^{′}}$, respectively, and $R_{\mu^{′}}=R_{\mu}∖{c}$ where $c\inR_{\mu}∖{a,b}$.

##### Proof

Denote the I/O metabolites in both modules μ and $\mu^{′}$ by 1 and 2. Since $\mu^{′}$ and μ are topologically identical except for $\mu^{′}$ lacking one reaction $c$, it must be true that $𝒫_{12}^{\mu^{′}}⁢(a_{1},a_{2},…,b¯_{1},b¯_{2},…)⊆𝒫_{12}^{\mu}⁢(a_{1},a_{2},…,b¯_{1},b¯_{2},…)$ for any reactions $a_{1},a_{2},…$, $b_{1},b_{2},…$ from $R_{\mu^{′}}$. In other words, there could only be fewer paths connecting the I/O metabolites within module $\mu^{′}$ compared to module μ. The rest of the proof follows immediately from this fact and the definitions of strictly serial and strictly parallel relatioships.

Next, I define a minimal topology as generating either if it is a fully connected topology (as in topological classes $ℳ^{b,io,IO}$, $ℳ^{b,i,∅}$ and $ℳ^{io,io,IO}$, $ℳ^{io,io,I}$) or if adding any reaction to it would make the marked reactions serial-parallel.

Denote the sets of all double-marked topologies minimal in class $ℳ$ where the marked reactions are strictly serial, strictly parallel and serial-parallel by by $ℛ_{ℳ}^{ser}$, $ℛ_{ℳ}^{par}$ and $ℛ_{ℳ}^{sp}$, respectively.

#### Definition 2

Topology $(R,a,b)$ minimal in $M$ is called a strictly serial generating topology in $M$ if it is strictly serial (i.e. $(R,a,b)\inR_{M}^{ser}$) and either it is fully connected (i.e. $R=R_{M}$) or $(R∪{c},a,b)\inR_{M}^{sp}$ for any reaction $c\inR_{M}∖R$.

#### Definition 3

Topology $(R,a,b)$ minimal in $M$ is called a strictly parallel generating topology in $M$ if it is strictly parallel (i.e. $(R,a,b)\inR_{M}^{par}$) and either it is fully connected (i.e. $R=R_{M}$) or $(R∪{c},a,b)\inR_{M}^{sp}$ for any reaction $c\inR_{M}∖R$.

Clearly, a topological class $ℳ$ may have multiple generating topologies, and it is easy to show that every topological class has at least one generating topology. I denote the set of all strictly serial generating topologies for the class $ℳ$ by $𝒢_{ℳ}^{ser}$ and I denote the set of all strictly parallel generating topologies for class $ℳ$ by $𝒢_{ℳ}^{par}$. The following proposition justifies the name ‘generating topology’. It states that any strictly serial minimal topology can be produced from some strictly serial generating topology by removing one or multiple reactions, and similarly for any strictly parallel minimal topology.

#### Proposition 6

If $(R,a,b)$ is a strictly parallel topology minimal in the topological class $M$, then there exists a strictly parallel generating topology $(R_{g},a,b)$ in $M$, such that $R⊆R_{g}$. If $(R,a,b)$ is a strictly serial topology minimal in the topological class $M$, then there exists a strictly serial generating topology $(R_{g},a,b)$ in $M$, such that $R⊆R_{g}$.

##### Proof

Suppose that $ℳ$ is one of the topological classes $ℳ^{b,io,IO}$, $ℳ^{b,i,∅}$, or $ℳ^{io,io,IO}$. Since the fully connected minimal topology $(R_{ℳ},a,b)$ is strictly parallel, it is a generating topology in $ℳ$. Then, according to Proposition 5, any topology $(R,a,b)$ minimal in $ℳ$ is strictly parallel, and Proposition 6 holds. By the same logic, Proposition 6 holds for the topological class $ℳ^{io,io,I}$.

Suppose that $ℳ$ is one of the remaining topological classes $ℳ^{io,io,∅}$, $ℳ^{io,i,I}$, $ℳ^{io,i,∅}$, $ℳ^{i,i,I}$ or $ℳ^{i,i,∅}$. Then the fully connected minimal topology $(R_{ℳ},a,b)$ is serial-parallel. Suppose that $(R,a,b)$ is strictly parallel. Then $R$ must be a strict subset of $R_{ℳ}$, so that the set $C=R_{ℳ}∖R$ is not empty. Then, either $(R,a,b)\in𝒢_{ℳ}^{par}$ or $(R,a,b)∉𝒢_{ℳ}^{par}$. If $(R,a,b)\in𝒢_{ℳ}^{par}$, the Proposition 6 holds. Suppose that $(R,a,b)∉𝒢_{ℳ}^{par}$. This implies that there exists a reaction $c_{1}\inC$, such that $R_{1}=R∪{c_{1}}$ and $(R_{1},a,b)\inℛ_{ℳ}^{par}$ ($(R_{1},a,b)$ cannot be in $ℛ_{ℳ}^{ser}$ due to Proposition 5). There are three possibilities.

Option (a) is not possible since $(R_{1},a,b)\inℛ_{ℳ}^{par}$ while $(R_{ℳ},a,b)\inℛ_{ℳ}^{sp}$. Option (b) implies that the Proposition 6 holds. Option (c) implies that there exists a reaction $c_{2}\inC∖{c_{1}}$, such that $R_{2}=R_{1}∪{c_{2}}$ and $(R_{2},a,b)\inℛ_{ℳ}^{par}$, and we have the same three possibilities for $R_{2}$ as above. Thus, by induction, Proposition 6 must hold. The proof is analogous if $(R,a,b)$ is strictly serial.

Discovering all strictly serial and strictly parallel generating topologies in any given topological class $ℳ$ is straightforward because all minimal topologies within $ℳ$ can be produced by removing reactions from the unique fully connected topology minimal in $ℳ$ shown in Figure 8. In Appendix 3, I provide an algorithm that discovers all strictly serial and strictly parallel generating topologies by sequentially removing reactions from the fully connected minimal topology in each topological class. The code implementing this algorithm in Matlab is available at https://github.com/skryazhi/epistasis_theory. All strictly parallel generating topologies are listed in Table 2 and all strictly serial generating topologies are listed in Table 3. They are also illustrated in Figure 8 and Figure 10 through Figure 14. I label each generating topology by a four-letter combination (see column 4 in Table 2 and Table 3): the first three letters denote the topological class and the last letter (F, P, or S) denotes the specific generating topology within that class. Letter ‘F’ (stands for ‘full’) denotes the fact that the reaction set in the generating topology is complete. Letters ‘P’ (for ‘parallel’) and ‘S’ (stands for ‘serial’) denote strictly parallel and strictly serial generating topologies, respectively; if there are a multiple generating topologies within the same class, they are distinguished by subindices, for example, $io,i,∅,P_{1}$; $io,i,∅,P_{2}$, etc.

![Figure 10.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig10-v2.jpg)

**Figure 10.:** Graphical representation of strictly serial and strictly parallel generating topologies in the class $M^{io,io,∅}$.Fully connected topology $io,io,∅,F$ is shown for reference (same as in Figure 8).

#### Topological relationship between reactions and epistasis

Each strictly serial and strictly parallel generating topology in a given class $ℳ$ (listed in Table 2 and Table 3) is produced by removing reactions from the fully connected topology minimal in $ℳ$ (shown in Figure 8). This implies that the parametric family of function $f_{2}$ that corresponds to any generating topology is obtained from Equation 34 through Equation 35 by setting some parameters $w_{i⁢j}$ to zero. In other words, these parametric families are known. Next, I prove Proposition 7 that shows that $\epsilon⁢y_{\mu}\leq0$ for every member of every parameteric family of $f_{2}$ that corresponds to a strictly parallel generating topology and the analogous Proposition 8 for strictly serial topologies.

Now, any minimal strictly parallel topology can in turn be produced by removing reactions from some strictly parallel generating topology, and any minimal strictly serial topology can be produced by removing reactions from some strictly serial generating topology. This implies that any function $f_{2}$ that corresponds to any strictly parallel minimal topology belongs to the parametric family that corresponds to some strictly parallel generating topology; and any function $f_{2}$ that corresponds to any strictly serial minimal topology belongs to the parametric family that corresponds to some strictly serial generating topology. Therefore, Propositions 7 and 8 imply that $\epsilon⁢y_{\mu}\leq0$ for any minimal strictly parallel topology and that $\epsilon⁢y_{\mu}\geq1$ for any minimal strictly serial topology. The proof of Theorem 2 is then concluded by recalling that every strictly parallel module is mapped onto its effective rate constant via function $f_{2}$ that corresponds to some minimal strictly parallel module, and similarly for strictly serial modules.

#### Proposition 7

Let $(\mu,a,b)$ be a minimal double-marked module in the topological class $M$, with $u$ and $v$ being the rates of reactions $a$ and $b$, respectively, and let $y$ be the effective rate constant of this module. Suppose that mutation A perturbs only reaction $a$ by $\delta^{A}⁢u$, and mutation B perturbs only reaction $b$ by $\delta^{B}⁢v$, such that $|\delta^{A}⁢u|≪1$, $|\delta^{B}⁢v|≪1$. If reactions $a$ and $b$ are strictly parallel in $(\mu,a,b)$, then $\epsilon⁢y\leq0$.

##### Proof

According to Proposition 6, the topology of module $(\mu,a,b)$ can be produced by removing reactions from some strictly parallel generating topology $(R_{g},a,b)$. Therefore, the function $f_{2}$ that maps $u$ and $v$ in this module onto its effective rate constant $y$ belongs to the parametric family that corresponds to $(R_{g},a,b)$. According to Equation 55,

$$
\epsilony=\frac{H_{uv}}{2C_{u}C_{v}}+o(1),
$$

where

$$
C_{u}=\frac{u}{y}⁢\frac{\partial⁡f_{2}}{\partial⁡u},
$$



$$
C_{v}=\frac{v}{y}⁢\frac{\partial⁡f_{2}}{\partial⁡v},
$$



$$
H_{u⁢v}=\frac{u⁢v}{y}⁢\frac{\partial^{2}⁡f_{2}}{\partial⁡u⁢\partial⁡v}.
$$

According to Theorem 1, $0\leqC_{u}\leq1$ and $0\leqC_{v}\leq1$. And since all $y>0$, $u>0$, $v>0$, to prove Proposition 7, it is sufficient to show that $\frac{\partial^{2}⁡f_{2}}{\partial⁡u⁢\partial⁡v}\leq0$ for any member of any parametric family that corresponds to generating topologies listed in Table 2.

Generating topologies $b,io,IO,F$ and $b,i,∅,F$ (Figure 8). According to Equation 34 and Equation 35, $y=f_{2}⁢(u,v)=u+ϕ⁢(v)$, which implies that $\epsilony=0$.

Generating topology $io,io,IO,F$ (Figure 8). According to Equation 37,

$$
y=f_{2}⁢(u,v)=w_{12}+\frac{A⁢u⁢v+B⁢u+B⁢v}{D},
$$

where $D=E⁢u⁢v+F⁢u+G⁢v+B$, $A=w_{42}/K_{13}+w_{32}/K_{14}$, $B=w_{32}⁢w_{42}+w_{32}⁢w_{43}+w_{34}⁢w_{42}$, $E=1/(K_{13}⁢K_{14})$, $F=(w_{42}+w_{43})/K_{13}$, $G=(w_{32}+w_{34})/K_{14}$. Therefore,

$$
\frac{∂^{2}f_{2}}{∂u∂v}=−2\frac{w_{34}}{K_{14}}\frac{(w_{32}v/K_{14}+B)(w_{42}u/K_{13}+B)}{D^{3}}\leq0.
$$

Generating topology $io,io,∅,P$ (Figure 10). According to Equation 38, $y=f_{2}⁢(u,v)=w_{12}+ϕ⁢(u)+ψ⁢(v)$, which implies $\epsilony=0$.

Generating topology $io,i,I,P$ (Figure 11). Notice that metabolite 4 together with reactions $1↔4$, $a$ and $b$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 1 and 3 and which is minimal in the topological calss $ℳ^{b,io,IO}$. Denote the effective reaction rate of module $\mu^{′}$ by $y^{′}$. Therefore, $\epsilon⁢y^{′}=0$, as shown above. Since module $\mu^{′}$ is contained in μ, by Theorem 1, $\epsilon⁢y\leq0$.

![Figure 11.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig11-v2.jpg)

**Figure 11.:** Graphical representation of strictly serial and strictly parallel generating topologies in class $M^{io,i,I}$.Fully connected topology $io,i,I,F$ is shown for reference (same as in Figure 8).

Generating topology $io,i,∅,P_{1}$ (Figure 12). According to Property 1 of the CGP (Box 1), module μ can be coarse-grained by first eliminating metabolite 3. In the resulting module $\mu^{′}$, mutation A perturbs only the rate constant $u^{′}$ of the effective reaction $a^{′}≡1↔2$ (by Properties 2 and 4 of the CGP). Then, according to Equation 50 and Theorem 1, $|\delta^{A}⁢u^{′}|≪1$. The double-marked module $(\mu^{′},a^{′},b)$ is minimal in the topological class $ℳ^{b,i,∅}$ which implies that $\epsilon⁢y=0$, as shown above.

![Figure 12.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig12-v2.jpg)

**Figure 12.:** Graphical representation of strictly serial and strictly parallel generating topologies in class $M^{io,i,∅}$.Fully connected topology $io,i,∅,F$ is shown for reference (same as in Figure 8).

Generating topology $io,i,∅,P_{2}$ (Figure 12). Module μ can be coarse-grained by first eliminating metabolite 5, which will result in a double-marked module $(\mu^{′},a,b^{′})$ that is minimal in the topological class $ℳ^{io,io,IO}$. The rest of the proof for this topology is analogous to that for the topology $io,i,∅,P_{1}$.

Generating topology $io,i,∅,P_{3}$ (Figure 12). Notice that metabolites 4 and 5 together with reactions $a$, $b$, $1↔4$, $1↔5$, $3↔4$ and $3↔5$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 1 and 3 and which is minimal in the topological calss $ℳ^{b,i,∅}$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,P$.

Generating topology $i,i,I,P_{1}$ (Figure 13). Notice that metabolites 4 and 5 together with reactions $a$, $b$, $1↔3$, $1↔4$, $1↔5$ and $4↔5$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 1 and 3 and which is minimal in the topological calss $ℳ^{io,io,IO}$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,P$.

![Figure 13.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig13-v2.jpg)

**Figure 13.:** Graphical representation of strictly serial and strictly parallel generating topologies in class $M^{i,i,I}$.Fully connected topology $i,i,I,F$ is shown for reference (same as in Figure 8).

Generating topology $i,i,I,P_{2}$ (Figure 13). Notice that metabolite 5 together with reactions $a$, $b$, and $4↔5$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 3 and 4 and which is minimal in the topological calss $ℳ^{b,io,IO}$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,P$.

Generating topology $i,i,∅,P_{1}$ (Figure 14). According to Equation 35, $y=f_{2}⁢(u,v)=x_{12}+ϕ⁢(u)+ψ⁢(v)$, which implies $\epsilony=0$.

![Figure 14.](https://cdn.elifesciences.org/articles/60200/elife-60200-fig14-v2.jpg)

**Figure 14.:** Graphical representation of strictly serial and strictly parallel generating topologies in class $M^{i,i,∅}$.Fully connected topology $i,i,∅,F$ is shown for reference (same as in Figure 8).

Generating topology $i,i,∅,P_{2}$ (Figure 14). Notice that metabolites 5 and 6 together with reactions $a$, $b$, $3↔5$, $3↔6$, $4↔5$ and $5↔6$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 3 and 4 and which is minimal in the topological calss $ℳ^{b,i,∅}$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,P$.

Generating topology $i,i,∅,P_{3}$ (Figure 14). Module μ can be coarse-grained by first eliminating metabolites 4 and 6, which will result in a double-marked module $(\mu^{′},a^{′},b^{′})$ that is minimal in the topological class $ℳ^{io,io,IO}$. The rest of the proof for this topology is analogous to that for the topology $io,i,∅,P_{1}$.

Generating topology $i,i,∅,P_{4}$ (Figure 14). Module μ can be coarse-grained by first eliminating metabolite 4, which will result in a double-marked module $(\mu^{′},a^{′},b)$ that is minimal in the topological class $ℳ^{io,i,∅}$ with a strictly parallel generating topology $io,i,∅,P_{3}$. The rest of the proof for this topology is analogous to that for the topology $io,i,∅,P_{1}$.

Generating topology $i,i,∅,P_{5}$ (Figure 14). Module μ can be coarse-grained by first eliminating metabolite 6, which will result in a double-marked module $(\mu^{′},a,b^{′})$ that is minimal in the topological class $ℳ^{i,i,I}$ with a strictly parallel generating topology $i,i,I,P_{1}$. The rest of the proof for this topology is analogous to that for the topology $io,i,∅,P_{1}$.

Generating topology $i,i,∅,P_{6}$ (Figure 14). Notice that metabolites 4 and 6 together with reactions $a$, $b$, $3↔5$, $3↔6$, $4↔5$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 3 and 5 and which is minimal in the topological calss $ℳ^{io,io,∅}$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,P$.

Generating topology $i,i,∅,P_{7}$ (Figure 14). Using Equation 42, I show in Appendix 4 that

$$
\frac{\partial^{2}⁡f_{2}}{\partial⁡u⁢\partial⁡v}=\frac{2⁢\beta}{K_{31}}⁢\frac{(A_{u}⁢v+B_{u})⁢(A_{v}⁢u+B_{v})}{(E_{u}⁢v+F_{u})^{3}},
$$

where $A_{v}$, $B_{v}$, $E_{u}$, $F_{u}$ are all non-negative constants and $\beta\leq0$.

#### Proposition 8

Let $(\mu,a,b)$ be a minimal double-marked module in the topological class $M$, with $u$ and $v$ being the rates of reactions $a$ and $b$, respectively, and let $y$ be the effective rate constant of this module. Suppose that mutation A perturbs only reaction $a$ by $\delta^{A}⁢u$, and mutation B perturbs only reaction $b$ by $\delta^{B}⁢v$, such that $|\delta^{A}⁢u|≪1$, $|\delta^{B}⁢v|≪1$. If reactions $a$ and $b$ are strictly serial in $(\mu,a,b)$, then $\epsilon⁢y\geq1$.

##### Proof

The logic of the proof is the same as for Proposition 7, that is, it is sufficient to show that $\epsilon⁢y\geq1$ for any double-marked module $(\mu,a,b)$ with any strictly serial generating topology listed in Table 3.

Generating topology $io,io,I,F$ (Figure 8). According to Equation 36,

$$
y=f_{2}⁢(u,v)=w_{12}+\frac{u⁢v}{D}
$$

where $D=u/K_{13}+v$. Therefore,

$$
C_{u}=(\frac{v}{D})^{2}\frac{u}{y},C_{v}=\frac{1}{K_{12}}(\frac{u}{D})^{2}\frac{v}{y},H_{uv}=\frac{2}{K_{12}}\frac{1}{yD}(\frac{uv}{D})^{2}.
$$

Substituting these expressions into Equation 68, I obtain

$$
\epsilon⁢y=\frac{y}{u⁢v/D}\geq1
$$

because $y\gequ⁢v/D$ according to Equation 73.

Generating topology $io,io,∅,S$ (Figure 10). According to Property 1 of the CGP (Box 1), module μ can be coarse-grained by first eliminating metabolite 3. In the resulting module $\mu^{′}$, mutation A perturbs only the rate constant $u^{′}$ of the effective reaction $a^{′}≡1↔4$ (by Properties 2 and 4 of the CGP). Then, according to Equation 50 and Theorem 1, $|\delta^{A}⁢u^{′}|≪1$. The double-marked module $(\mu^{′},a^{′},b)$ is minimal in the topological class $ℳ^{io,io,I}$ which implies that $\epsilon⁢y\geq1$, as shown above.

Generating topology $io,i,I,S_{1}$ (Figure 11). Notice that metabolite 3 together with reactions $a$, $b$, and $1↔4$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 1 and 4 and which is minimal in the topological calss $ℳ^{io,io,I}$. Therefore, if the effective reaction rate of module $\mu^{′}$ is $y^{′}$, $\epsilon⁢y^{′}\geq1$, as shown above. According to Equation 50, Equation 51 and Theorem 1, $|\delta^{A}⁢y^{′}|≪1$, $|\delta^{B}⁢y^{′}|≪1$. Since module $\mu^{′}$ is contained in μ, by Theorem 1, $\epsilon⁢y\geq1$.

Generating topology $io,i,I,S_{2}$ (Figure 11). Module μ can be coarse-grained by first eliminating metabolite 4, which results in a double-marked module $(\mu^{′},a,b^{′})$ that is minimal in the topological class $ℳ^{io,io,I}$. The rest of the proof for this topology is analogous to that for the topology $io,io,∅,S$.

Generating topology $io,i,∅,S_{1}$ (Figure 12). Module μ can be coarse-grained by first eliminating metabolites 4 and 5, which results in a double-marked module $(\mu^{′},a,b^{′})$ that is minimal in the topological class $ℳ^{io,io,I}$. The rest of the proof for this topology is analogous to that for the topology $io,io,∅,S$.

Generating topology $io,i,∅,S_{2}$ (Figure 12). Notice that metabolites 3 and 4 together with reactions $a$, $b$, $1↔4$, $1↔5$ and $3↔4$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 1 and 5 and which is minimal in the topological calss $ℳ^{io,io,∅}$ with the strictly serial generating topology $io,io,∅,S$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,S_{1}$.

Generating topology $io,i,∅,S_{3}$ (Figure 12). Notice that metabolites 3 and 5 together with reactions $a$, $b$, $1↔4$, $3↔4$, and $3↔5$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 1 and 4 and which is minimal in the topological calss $ℳ^{io,io,∅}$ with the strictly serial generating topology $io,io,∅,S$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,S_{1}$.

Generating topology $i,i,I,S_{1}$ (Figure 13). Notice that metabolite 3 together with reactions $a$, $b$, and $4↔5$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 4 and 5 and which is minimal in the topological calss $ℳ^{io,io,I}$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,S_{1}$.

Generating topology $i,i,I,S_{2}$ (Figure 13). Notice that metabolites 3 and 5 together with reactions $a$, $b$, $1↔3$, $1↔4$, and $1↔5$ form a double-marked module $(\mu^{′},a,b)$ whose I/O metabolites are 1 and 4 and which is minimal in the topological calss $ℳ^{io,i,I}$ with the strictly serial generating topology $io,i,I,S_{2}$. The rest of the proof for this topology is analogous to that for the topology $io,i,I,S_{1}$.

Generating topology $i,i,∅,S_{1}$ (Figure 14). Module μ can be coarse-grained by first eliminating metabolites 5 and 6, which results in a double-marked module $(\mu^{′},a,b^{′})$ that is minimal in the topological class $ℳ^{io,i,I}$ with the strictly serial generating topology $io,i,I,S_{1}$. The rest of the proof for this topology is analogous to that for the topology $io,io,∅,S$.

Generating topology $i,i,∅,S_{2}$ (Figure 14). Module μ can be coarse-grained by first eliminating metabolite 6, which results in a double-marked module $(\mu^{′},a,b^{′})$ that is minimal in the topological class $ℳ^{i,i,I}$ with the strictly serial generating topology $i,i,I,S_{1}$. The rest of the proof for this topology is analogous to that for the topology $io,io,∅,S$.

#### Proof of Theorem 2

According to Proposition 3, the coarse-graining procedure $CG^{\mu∖{a,b}}$ maps the double-marked module $(\mu,a,b)$ onto a double-marked module $(\mu^{′},a,b)$ that is minimal in the same topological class as $(\mu,a,b)$, and the rates $u$, $v$ of reactions $a$, $b$ in $\mu^{′}$ are given by linear relations in Equation 32 and Equation 33. Clearly, $|\delta^{A}⁢u|≪1$ and $|\delta^{B}⁢v|≪1$. Furthermore, none of the other reaction rates $w_{i⁢j}$ in $\mu^{′}$ depend on ξ or η, so that $\delta^{A}⁢w_{i⁢j}=0$ and $\delta^{B}⁢w_{i⁢j}=0$ for all $w_{i⁢j}$ other than $u$ and $v$, and $\epsilon⁢w_{i⁢j}=0$ for all $w_{i⁢j}$ including $u$ and $v$. It then follows from Proposition 3 that $\epsilon⁢y_{\mu}=\epsilon⁢y_{\mu^{′}}$.

Now, according to Corollary 4, if reactions $a$ and $b$ are strictly parallel in $(\mu,a,b)$, they are also strictly parallel in $(\mu^{′},a,b)$. Therefore, by Proposition 7, $\epsilon⁢y_{\mu^{′}}\leq0$. Analogously, if reactions $a$ and $b$ are strictly serial in $(\mu,a,b)$, they are also strictly serial in $(\mu^{′},a,b)$. Therefore, by Proposition 8, $\epsilon⁢y_{\mu^{′}}\geq1$.

### Sensitivity of Theorem 1 and Theorem 2 with respect to the magnitude of mutational effects

According to Proposition 2, function $f_{1}$ for any module belongs to one of three parametric families, which correspond to the three minimal fully connected modules shown in Figure 7. As mentioned in the Results, for modules in the class $ℳ^{b}$, function f1 is linear, so that the claims of Theorem 1 continue to hold for mutations with finite effects. To evaluate the sensitivity of Theorem 1 with respect to the effect sizes of mutations for the topological classes $ℳ^{io}$ and $ℳ^{i}$, I generated 1000 minimal single-marked modules ν from each of these topological classes with random parameters. Evaluating only minimal modules is sufficient because for any module from a given topological class there exists a minimal module from the same class, such that both of them map the lower level phenotype $y_{\mu}$ onto the higher-level phenotype $y_{ν}$ via the same function f1 (see Proposition 2).

To this end, I drew each $x_{i⁢j}$ ($i<j$) from a mixture of a point measure at 0 (with weight 0.25) and an exponential distribution with mean 1 (with weight 0.75). The point measure at 0 ensures that minimal modules that are not fully connected are represented in the sample. I drew each $K_{i⁢j}$ ($i<j$) as a ratio of two random numbers from an exponential distribution with mean 1. As a result, the distribution of non-zero $x_{i⁢j}$ values had the interdecile range of $(5.7\times10^{-2},3.91)$ with median 0.65.

I denote the effective rate constant of the reaction that represents the lower-level module μ by $ξ≡y_{\mu}$. In modules from the topological class $ℳ^{io}$, it is reaction $1↔3$ and in modules from the topological class $ℳ^{i}$, it is the reaction $3↔4$. I perturbed ξ by two mutations A and B with relative effects $\delta^{A}⁢ξ$ and $\delta^{B}⁢ξ$ and epistasis $\epsilon⁢ξ$. I chose nine different pairs of mutational effects $(\delta^{A}ξ,\delta^{B}ξ):(−0.01,−0.01)$, $(-0.1,-0.1)$, $(-0.5,-0.5)$, $(0.01,0.01)$, $(0.1,0.1)$, $(0.5,0.5)$, $(-0.01,0.01)$, $(-0.1,0.1)$, $(-0.5,0.5)$, and 16 different values of $\epsilon⁢ξ$ ranging from −1 to 2 with an increment of 0.2. Since the rate constant $ξ^{A⁢B}$ of the double mutant cannot be negative, I skipped those combinations of perturbations and epistasis values for which $\delta^{A}⁢ξ+\delta^{B}⁢ξ+2⁢(\epsilon⁢ξ)⁢(\delta^{A}⁢ξ)⁢(\delta^{B}⁢ξ)<-1$. I then computed the resulting values $\delta^{A}⁢y_{ν}$, $\delta^{B}⁢y_{ν}$ and $\epsilon⁢y_{ν}$ at the level of the effective rate constant $y_{ν}$ of the higher-level module ν.

Using these data, I inferred the function $ϕ$ that maps lower-level epistasis $\epsilon⁢ξ$ onto higher-level epistasis $\epsilon⁢y_{ν}$, as follows. For any minimal single-marked module from the topological classes $ℳ^{io}$ or $ℳ^{i}$, the effective rate constant $y_{ν}$ can be written as

$$
y_{ν}=x_{12}+\frac{A~⁢ξ+B~}{D},
$$

where $D=C~⁢ξ+D~$ and $A~=x_{32}$, $B~=0$, $C~=1/K_{13}$ , $D~=x_{32}$ for modules from the topological class $ℳ^{io}$ (see Equation 30), and $A~=(x_{13}+x_{14})⁢(x_{42}+x_{32}/K_{34})$, $B~=(x_{31}+x_{32})⁢x_{14}⁢x_{42}+(x_{41}+x_{42})⁢x_{13}⁢w_{32}$, $C~=(x_{31}+x_{32})/K_{34}+(x_{41}+x_{42})$ , $D~=(x_{31}+x_{32})⁢(x_{41}+x_{42})$ for modules from the topological class $ℳ^{i}$ (see Equation 31). Therefore, for any perturbation $\delta⁢ξ$, we have

$$
\delta⁢y_{ν}=\frac{A~⁢D~-B~⁢C~}{D^{2}}⁢\frac{ξ}{y_{ν}}⁢\frac{\delta⁢ξ}{1+(C~⁢ξ/D)⁢\delta⁢ξ}.
$$

Since $\delta^{A⁢B}⁢ξ$ is a linear function of $\epsilon⁢ξ$, $\delta^{A⁢B}⁢y_{ν}$ is a hyperbolic function of $\epsilon⁢ξ$. Therefore, $\epsilon⁢y_{ν}$ is also a hyperbolic function of $\epsilon⁢ξ$,

$$
\epsilon⁢y_{ν}=ϕ⁢(\epsilon⁢ξ)=a-\frac{b}{\epsilon⁢ξ+c},
$$

where constants $a$, $b$ and $c$ depend on the parameters of module ν and on the mutational effect sizes $\delta^{A}⁢ξ$ and $\delta^{B}⁢ξ$. I numerically calculated these parameters for each sampled module and each pair of mutational effects.

The main results of Theorem 1 are that, when the effects of mutations are infinitesimal, the map $ϕ$ has a fixed point $\epsilon¯$, this fixed point is located between 0 and 1, and it is unstable. I use equation Equation 74 to test whether these statements also hold when the effects of mutations are finite. Specifically, it is easy to see that the map $ϕ$ has a fixed point $\epsilon¯$ if the discriminant $d=(a-c)^{2}-4⁢(b-a⁢c)$ is positive. In this case, I designate $\epsilon¯$ as the one of two roots $1/2⁢(a-c\pm\sqrt{d})$ that is closer to zero. I then check whether this fixed point is located between 0 and 1. I check whether it is unstable by comparing the derivative of $ϕ$ at $\epsilon¯$ with 1.

According to Proposition 6, function $f_{2}$ for any module where the reactions affected by mutations are strictly parallel belongs to one of 17 parameteric families, which correspond to the strictly parallel generating topologies listed in Table 2. And similarly, function $f_{2}$ for any module where the reactions affected by mutations are strictly serial belongs to one of 11 parameteric families, which correspond to the strictly serial generating topologies listed in Table 3. Therefore, to evaluate the sensitivity of Theorem 2 with respect to the effect sizes of mutations I generated 104 double-marked modules $(\mu,a,b)$ with each of the strictly serial and strictly parallel topologies with random parameters. I drew $x_{i⁢j}$ and $K_{i⁢j}$ as described above. I chose the same nine pairs of mutational effects $(\delta^{A}⁢ξ,\delta^{B}⁢η)$ as above, where ξ and η are the rate constants of reactions affected by mutations A and B: $(-0.01,-0.01)$, $(-0.1,-0.1)$, $(-0.5,-0.5)$, $(0.01,0.01)$, $(0.1,0.1)$, $(0.5,0.5)$, $(-0.01,0.01)$, $(-0.1,0.1)$, $(-0.5,0.5)$.

I found that, for some modules, individual mutational perturbations $\delta^{A}⁢y_{\mu}$ and/or $\delta^{B}⁢y_{\mu}$ at the level of the whole module were too small, which resulted in numerical instabilities. To avoid them, I calculated epistasis $\epsilon⁢y_{\mu}$ only for cases where the effects of both mutations $\delta^{A}⁢y_{\mu}$ and $\delta^{B}⁢y_{\mu}$ exceeded the precision threshold of $10^{-5}$. As a result, I evaluated epistasis in less than 104 modules per generating topology and pair of mutational effects, but this number never fell below 1000. When comparing the values of epistasis with 0 and 1, I used the same precision threshold of $10^{-5}$ to avoid numerical problems. In addition, I found that for mutations affecting strictly serial reactions there is a substantial fraction of modules where $\epsilon⁢y_{\mu}$ falls between 0.99 and 1 (see Figure 4—figure supplement 3). This is not a numerical artifact, but probably reflects real clustering of epistasis coefficients around 1, which is expected for the linear pathway irrespective of its parameters (see above).

The Matlab code for this analysis is available at https://github.com/skryazhi/epistasis_theory.

### Kinetic model of glycolysis

I downloaded the kinetic metabolic model of E. coli glycolysis by Chassagnole et al., 2002 from the BioModels database (Malik-Sheriff et al., 2019) on September 15, 2015 (model ID BIOMD0000000051). I used the Matlab SimBiology toolbox to interpret the model. To validate the model, I simulated it for 40 s and reproduced Figures 4 and 5 from Chassagnole et al., 2002. The Matlab code is available at https://github.com/skryazhi/epistasis_theory.

#### Modifications to the original model

I simplified and modified the model by (a) fixing the concentrations of ATP, ADP, AMP, NADPH, NADP, NADH, NAD at their steady-state values given in Table V of Chassagnole et al., 2002 and (b) removing dilution by growth. I then created four models of sub-modules of glycolysis by retaining the subsets of metabolites and enzymes shown in Figure 5—figure supplement 1 and Table 4 and removing other metabolites and enzymes. Each sub-module has one input and one output metabolite. Note that, since some reactions are irreversible, it is important to distinguish the input metabolite from the output metabolite. The concentrations of the input and the output metabolites in each model are held constant at their steady-state values given in Table 4. I defined the flux through the sub-module as the flux toward the output metabolite contributed by the sub-module (Table 4). This flux is the equivalent of the quantitative phenotype $y_{\mu}$ of a module in the analytical model. In addition, I made the following modifications specific to individual sub-modules.

**Table 4.**
 Definition of modules in the glycolysis network shown in Figure 5—figure supplement 1.Enzyme abbreviations are listed in Table 6. Metabolite abbreviations are listed in Table 5.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Internal metabolites</th>
      <th>Concentrations of I/O metabolites</th>
      <th>Reactions</th>
      <th>Output flux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>UGPP</td>
      <td>6 pg, dhap, e4p, f6p, fdp, rib5p, ribu5p, sed7p, xyl5p</td>
      <td>[g6p]=3.82 mM, [gap]=0.44 mM</td>
      <td>ALDO, G6PDH, PFK, PGDH, PGI, Ru5P, R5PI, TA, TIS, TKa, TKb</td>
      <td>JALDO+JTIS+JTKb+JTKa-JTA</td>
    </tr>
    <tr>
      <td>LG</td>
      <td>2 pg, 3 pg, pgp</td>
      <td>[gap]=0.44 mM, [pep]=0.08 mM</td>
      <td>ENO, GAPDH, PGK, PGM</td>
      <td>JENO</td>
    </tr>
    <tr>
      <td>GPP</td>
      <td>all in UGPP and in LG, gap</td>
      <td>[g6p]=3.82 mM, [pep]=0.08 mM</td>
      <td>all in UGPP and in LG</td>
      <td>JENO</td>
    </tr>
    <tr>
      <td>FULL</td>
      <td>all in GPP, g6p, pep</td>
      <td>[Ext glu]=2 µM, [pyr]=10 µM</td>
      <td>all in GPP, PTS, PK, PEPCxyl</td>
      <td>JPK+JPTS</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Names of metabolites used in the kinetic model of glycolysis.


<table>
  <thead>
    <tr>
      <th>2 pg</th>
      <th>2-Phosphoglycerate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3 pg</td>
      <td>3-Phosphoglycerate</td>
    </tr>
    <tr>
      <td>6 pg</td>
      <td>6-Phosphogluconate</td>
    </tr>
    <tr>
      <td>dhap</td>
      <td>Dihydroxyacetonephosphate</td>
    </tr>
    <tr>
      <td>e4p</td>
      <td>Erythrose-4-phosphate</td>
    </tr>
    <tr>
      <td>f6p</td>
      <td>Fructose-6-phosphate</td>
    </tr>
    <tr>
      <td>fdp</td>
      <td>Fructose-1,6-bisphosphate</td>
    </tr>
    <tr>
      <td>g6p</td>
      <td>Glucose-6-phosphate</td>
    </tr>
    <tr>
      <td>gap</td>
      <td>Glyceraldehyde-3-phosphate</td>
    </tr>
    <tr>
      <td>glu</td>
      <td>Glucose</td>
    </tr>
    <tr>
      <td>pep</td>
      <td>Phosphoenolpyruvate</td>
    </tr>
    <tr>
      <td>pgp</td>
      <td>1,3-Diphosphoglycerate</td>
    </tr>
    <tr>
      <td>pyr</td>
      <td>Pyruvate</td>
    </tr>
    <tr>
      <td>rib5p</td>
      <td>Ribose-5-phosphate</td>
    </tr>
    <tr>
      <td>ribu5p</td>
      <td>Ribulose-5-phosphate</td>
    </tr>
    <tr>
      <td>sed7p</td>
      <td>Sedoheptulose-7-phosphate</td>
    </tr>
    <tr>
      <td>xyl5p</td>
      <td>Xylulose-5-phosphate</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Names of enzymes used in the kinetic model of glycolysis.


<table>
  <thead>
    <tr>
      <th>ALDO</th>
      <th>Aldolase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ENO</td>
      <td>Enolase</td>
    </tr>
    <tr>
      <td>G6PDH</td>
      <td>Glucose-6-phosphate dehydrogenase</td>
    </tr>
    <tr>
      <td>GAPDH</td>
      <td>Glyceraldehyde-3-phosphate dehydrogenase</td>
    </tr>
    <tr>
      <td>PFK</td>
      <td>Phosphofructokinase</td>
    </tr>
    <tr>
      <td>PGDH</td>
      <td>6-Phosphogluconate dehydrogenase</td>
    </tr>
    <tr>
      <td>PGI</td>
      <td>Glucose-6-phosphateisomerase</td>
    </tr>
    <tr>
      <td>PGK</td>
      <td>Phosphoglycerate kinase</td>
    </tr>
    <tr>
      <td>PGM</td>
      <td>Phosphoglycerate mutase</td>
    </tr>
    <tr>
      <td>PEPCxyl</td>
      <td>PEP carboxylase</td>
    </tr>
    <tr>
      <td>PK</td>
      <td>Pyruvate kinase</td>
    </tr>
    <tr>
      <td>PTS</td>
      <td>Phosphotransferase system</td>
    </tr>
    <tr>
      <td>R5PI</td>
      <td>Ribose-phosphateisomerase</td>
    </tr>
    <tr>
      <td>Ru5P</td>
      <td>Ribulose-phosphate epimerase</td>
    </tr>
    <tr>
      <td>TA</td>
      <td>Transaldolase</td>
    </tr>
    <tr>
      <td>TIS</td>
      <td>Triosephosphate isomerase</td>
    </tr>
    <tr>
      <td>TKa</td>
      <td>Transketolase, reaction a</td>
    </tr>
    <tr>
      <td>TKb</td>
      <td>Transketolase, reaction b</td>
    </tr>
  </tbody>
</table>

#### Calculation of flux control coefficients and epistasis coefficients

I calculate the first- and second-order flux control coefficients (FCC) $C_{i}$ and $H_{i⁢j}$ for flux $J$ with respect to reactions $i$ and $j$ as follows (see Equation 45 and Equation 46). I perturb the $r_{max,i}$ of reaction $i$ by factor between 0.75 and 1.25 (10 values in a uniformly-spaced grid), such that $\delta⁢r_{max,i}\in[-0.25,0.25]$. Then, I obtain the steady-state flux $J^{′}$ in each perturbed model and calculate the flux perturbations $\delta⁢J=J^{′}/J^{0}-1$, where $J^{0}$ is the corresponding flux in the unperturbed model. Then, to obtain $C_{i}$ and $H_{i⁢i}$, I fit the linear model

$$
\delta⁢J∼C_{i}⁢(\delta⁢r_{max,i})+\frac{H_{i⁢i}}{2}⁢(\delta⁢r_{max,i})^{2}
$$

by least squares. If the estimated value of $C_{i}$ was below $10^{-4}$ for a given sub-module, I set $C_{i}$ to zero and exclude this reaction from further consideration in that sub-module because it does not affect flux to the degree that is accurately measurable. If the estimated value of $H_{i⁢i}$ is below $10^{-4}$, I set $H_{i⁢i}$ to zero.

To calculate the non-diagonal second-order control coefficients $H_{i⁢j}$, I create a $4\times4$ grid of perturbations of $\delta⁢r_{max,i}$ and $\delta⁢r_{max,j}$ and calculate the resulting flux perturbations $\delta⁢J$ (16 perturbations total). Since $C_{i}$, $C_{j}$, $H_{i⁢i}$ and $H_{j⁢j}$ are known, I obtain $H_{i⁢j}$, by regressing

$$
\delta⁢J-(C_{i}⁢(\delta⁢r_{max,i})+\frac{H_{i⁢i}}{2}⁢(\delta⁢r_{max,i})^{2})-(C_{j}⁢(\delta⁢r_{max,j})+\frac{H_{j⁢j}}{2}⁢(\delta⁢r_{max,j})^{2})
$$

against

$$
(\delta⁢r_{max,i})⁢(\delta⁢r_{max,j}).
$$

If the estimated value of $H_{i⁢j}$ is below $10^{-4}$, I set $H_{i⁢j}$ to zero. I estimate the epistasis coefficient $\epsilon⁢J$ between mutations affecting reactions $i$ and $j$ as

$$
\epsilon⁢J=\frac{H_{i⁢j}}{2⁢C_{i}⁢C_{j}}.
$$

#### Establishing the topological relationships between pairs of reactions

To establish the topological relationship (strictly serial, strictly parallel, or serial-parallel) between two reactions, I consider the smallest module (LG, UGPP, GPPP, or FULL) which contains both reactions. I then manually identify whether there exists a simple path connecting the input metabolite with the output metabolite for that module that passes through both reactions. (Note that, since some reactions are irreversible in this model, it is important to distinguish the input metabolite from the output metabolite). If such path does not exist, I classify the topological relationship between the two reactions as strictly parallel. If such path exists, I check if there are two paths connecting the input to the output metabolites such that each path contains only one of the two focal reactions. If such paths do not exist, I classify the topological relationship between the two reactions as strictly serial. Otherwise, I classify it as serial-parallel.
