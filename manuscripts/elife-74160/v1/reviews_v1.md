# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/04t0gwh46 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74160.sa0](https://doi.org/10.7554/eLife.74160.sa0)

This article presents a new method for simulating cytoskeletal dynamics inside cells. This is an important problem in the life sciences, and the numerical methods and derived results described in the paper seem very promising to facilitate computational modelling of cell dynamics. Although the user- friendliness of the software can still be improved, the method will be of interest to a broad community of biologists and biophysicists.


---

# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/04t0gwh46 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74160.sa1](https://doi.org/10.7554/eLife.74160.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "aLENS: towards the cellular-scale simulation of motor-driven cytoskeletal assemblies" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you will see from the reports below, the referees were favourably impressed by the performance on your numerical method, which allows to stimulate a large number of filaments and motors in a reasonable time. This paper is seen as the presentation of a new tool illustrated by examples, rather than the presentation of new scientific results. The essential revisions include:

1. Software availability (all referees) To be of value, the software should be freely available and useable. This does not seem to be the case at present.

2. Benchmarking (referees 1 and 3) It is important to provide some level of validation of the algorithm, which is currently missing. This can be done by comparing some aspects of the numerical results to existing analytical models. Regarding the binding and motor activity of cross linker, some simple toy model (e.g. gliding assay for motors, bound fraction for crosslinkers) would already be very informative, but more complex properties could also be considered as in Lera-Ramirez and Nedelec , Cytoskeleton 2019 (Theory of antiparallel microtubule overlap stabilization by motors and diffusible crosslinkers). Regarding collective effect, validation of the results could follow approaches such as the ones employed in Gao etal. PRE 2015 (Multiscale modeling and simulation of microtubule-motor-protein assemblies). Performance benchmark compared to other available algorithm should also be discussed.

3. Modularity (referees 2 and 3). At present, only rigid filaments interacting with one type of crosslinker are presented. The extension flexible filaments and different types of interacting proteins are discussed as possibilities but are not implemented at the moment. Although this can be seen as the natural next step, this modularity is essential for the algorithm to be useful to the community.

Reviewer #1:

The study by Yan et al., developed a novel computational framework for modelling cytoskeletal cellular processes that allows for further investigations into the material properties associated with such processes. The computational methodology involves modelling cytoskeletal filaments as rigid spherocylinders while the Hookean law is employed to model crosslinkers. The computational algorithm, aLENS performs three key tasks in a sequential manner that lends itself naturally to high performance computing. To demonstrate the applicability and usefulness of aLENS, the authors present (i) self-aligning and buckling networks for a significantly large number of filaments than previously studied, and (ii) the interplay between polarity of motor walking and polarity of filaments, which seems to suggest that the ability of motors to continuously walk without end-pausing is crucial to effective polarity sorting. The authors also investigated the formation of asters, which seem to form when crosslinking motors reorganise filaments so that their minus ends are clustered and held tight by paused motors.

Strengths

1. The development of an alternative novel computational framework that offers far more flexibility, applicability and is scalable across multi-scales.

2. The methodology overcomes the timescale limitations imposed by conventional explicit time-stepping methods that are key to modelling the dynamics of the cytoskeletal filaments and motors.

3. aLENS utilizes efficiently high-performance parallel computing resources to scale to cellular scale systems.

Weakness

1. The lack of bench-marking that is associated with algorithm comparisons for performance and robustness.

2. The lack of rigorous validation of the algorithm against suitably identified grounds truths.

3. No clear demonstration of the efficiency of the algorithm and how it compares to current conventional algorithms of this nature.

4. There are no clear comparisons between predictions of the computational algorithm and experimental data or observations.

My recommendations to authors are as follows:

(i) To consider rigorous validation of the computational methodology either by using synthetic or experimental data.

(ii) To demonstrate computational efficiency and robustness of the algorithm by comparing results to current conventional methodologies.

(iii) To demonstrate efficiency and accuracy when aLENS is compared to current conventional methodologies.

Reviewer #2:

In this article, the authors present a new method for modeling cytoskeletal networks inside cells. In particular they model the interactions between filaments (microtubules in this case but the method is not limited to this) and motors. The main contribution appears to be in the efficiency of this method. The main challenge in this area of numerical research is handling steric interactions between the large numbers of interacting cytoskeletal filaments. Essentially, hard repulsion methods require very small timescales that can make reasonable simulations infeasible while soft repulsion approximations of these can lead to numerical issues. Their method takes a mathematically different approach to addressing this issue that may substantially speed these simulations allowing users to simulate more realistically sized systems consisting of up to 106-107 filaments.

This is a technically strong and well written article addressing a problem of significant importance. I will note that it is difficult for me assess the value of its content to the field without seeing how this is implemented. The main value of this method is that it can do what other methods already do, but faster. My understanding is that much of the method is previously published and has been repackaged for use in this domain. In that sense, it is a tool. That is only of value if it is deployed in a manner that is well structured, documented, and at least somewhat usable and modifiable by technically capable users. Since the github link has not been included, I cannot assess this at the moment. Given that this is life sciences journal rather than a numerical methods journal, I think for publication at eLife it is critical that this be more than a methods article.

Without seeing this, I have a few questions. The computationally intensive elements of this method are in C++, but what about the more model specification oriented elements. Is this fully C++ or are you interfacing with a higher level language? Second, is this essentially an internal use code, or are you attempting to make this at least somewhat usable to other researchers. I strongly recommend the latter otherwise this will not really be an advancement over approaches such as Cytosim or MEDYAN. Faster but less usable is a losing combination.

I think this approach has strong potential, provided this issue is addressed. Below I'll note a few specific comments.

Specific comments

Line 74 – Here it is mentioned that all filaments will be considered to be strait and rigid but that this can be relaxed by jointing smaller segments together. While these filaments may have long persistence lengths relative to the cell size, their bending capacity is still vitally important to their dynamics and so if this is simple to implement, the authors should include this capability in the origination of this method.

Equation 3 – Please specify here what [s,p] are. As far as I can tell, these are not even fully defined in the SM. Also, is there really value in calling this a quaternion? Are you ever using either the geometric or algebraic properties of these? If not, I would suggest just defining it as a set of orientation variables. Also, for the general reader, it would be useful to describe why the orientation variable here is in R4 rather than R3.

SM Figures 4 / 5 – Can you clarify what you are quantifying for speed? Is this wall time / timestep or is it wall time / simulated second.

Reviewer #3:

In this article, the authors describe a new software for simulating cytoskeleton assemblies, and provide exiting examples of the software capabilities. The software offers the possibility to treat steric interactions as constraints rather than as stiff potentials, which should greatly improve performance. Thermodynamics of protein binding also seem carefully implemented.

While the software ships with great features, and fulfill a possible need in the field, there are several issues to take in consideration:

Software issues:

1- (No link to the software is provided in the article. aLens nonetheless is available on GitHub after a quick search, so this review is based on the current GitHub version)

My first concern is the difficulty to compile aLens. Installing aLens requires running an external script to alter one's environment (or significantly altering the compile file CMakeList.txt). Therefore, I was not able to compile this program, being unwilling to run a script to change my environment. Compiling of the software should be made much easier to be used by a wider, biology-oriented audience.

2- Modularity:

While the authors mention the cross linking model to have a modular design, the software itself does not appear to be modular. There is currently no possibility of having different types of proteins (or different type of filaments). This is a very strong limitation for its general use.

Scientific issues:

1 – Currently, aLens can only simulate straight filaments. The authors claim that aLens could easily as chain of short jointed segments. I would not think this easy, except possibly for the authors. However, many studies showed the paramount importance of bending rigidity in the mechanics of networks. Notably, Lenz and Gardel showed that because of this flexibility, networks tended to be globally contractile rather than extensile (filaments can buckle but not stretch). Therefore, aLens currently has access to only a manifold of the phase diagram, that may not be relevant e.g. for example 1, figure 2. Moreover, the filaments are not dynamic.

2 – While very interesting examples are provided, the authors do not provide a verification of their algorithm and implementation. While simple examples such as buckling cannot be addressed, maybe collective effects could be used as theoretical benchmarks? These could include collective effects of motors and nematic ordering, for which there exist theoretical results.

The authors therefore found success in simulating large systems with adequate thermodynamics. This seems like a notable technical advance. They were successful in providing impressive examples derived from the software. However, the lack of benchmarking (theoretical and performance-wise) mean that is not currently possible to assess exactly how successful the authors were.

The lack of filament flexibility and dynamics, as well as the impossibility to use more than one type of proteins will drastically limit its use by the biological community. The lack of code modularity will limit the possibility of external developers participating.

Overall, it seems that this is a very powerful approach, but the article needs to find a message. It could be emphasizing either:

– the implementation, in which case theoretical, and maybe performance benchmarks should be provided.

– the software package itself, in which case the software should be made more usable by the community, and possibly encompass a more general family of problems (or make them at least possible to implement via code modularity).

– the scientific results: in which case theoretical benchmark should be provided for simpler systems as a verification, and more complicated results should be put in their scientific context.

Currently, while very impressive technically, the software and associated article seem to fall short in each category.
