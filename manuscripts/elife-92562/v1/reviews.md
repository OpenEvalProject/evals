# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92562.3.sa0](https://doi.org/10.7554/eLife.92562.3.sa0)

This useful study introduces a simple mechanical model of C. elegans locomotion that captures aspects of the worm's behavioral repertoire beyond forward crawling. While the kinetic model (ElegansBot) provides a compromise and starting point to help understand the mechanical components of C. elegans behavior, the claim that this work improves on extant mechanical models is incomplete, including modeling a 3-dimensional turning behavior with a 2-dimensional model without sufficient justification. In addition, the results of the application of the model to previously unstudied behaviors are primarily qualitative and do not produce new predictions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92562.3.sa1](https://doi.org/10.7554/eLife.92562.3.sa1)

Summary:

This work describes a simple mechanical model of worm locomotion, using a series of rigid segments connected by damped torsional springs and immersed in a viscous fluid. It uses this model to simulate forward crawling movement, as well as omega turns.

Strengths:

The primary strength is in applying a biomechanical model to omega-turn behaviors. The biomechanics of nematode turning behaviors are relatively less well described and understood than forward crawling, and the increase in power during omega turns is one of the more novel results. The model itself may be a useful implementation to other researchers, particularly owing to its simplicity.

Weaknesses:

The strength of the model presented in this work relative to prior approaches is not well supported, and in general the paper would be improved with a better description of the broader context of existing modeling literature related to undulatory locomotion. This paper claims to improve on previous approaches to taking body shapes as inputs. However, the sole nematode model cited aims to do something different, and arguably more significant, which is to use experimentally derived parameters to model both the neural circuits that induce locomotion as well as the biomechanics and to subsequently compare the model to experimental data. Other modeling approaches do take experimental body kinematics as inputs and use them to produce force fields, however, they are not cited or discussed. Finally, the overall novelty of the approach is questionable. A functionally similar approach was developed in 2012 to describe worm locomotion in lattices (Majmudar, 2012, Roy. Soc. Int.), which is not discussed and would provide an interesting comparison and needed context.

In some sense, because the model takes kinematics as an input and uses previously established techniques to model mechanics, it is unsurprising that it can reproduce experimentally observed kinematics, however, the forces calculated and the variation of parameters could be of interest, but other methods derived from kinematics could provide similar results. It is unclear what the predictive power of the model is.

Relatedly, a justification of why the drag coefficients had to be changed by a factor of 100 should be explored. Plate conditions are difficult to replicate and the rheology of plates likely depends on several factors, but is for example, changes in hydration level likely to produce a 100-fold change in drag? or something more interesting/subtle within the model producing the discrepancy?

Finally, the language used to distinguish different modeling approaches was often unclear. For example, it was unclear in what sense the model presented in Boyle, 2012 was a "kinetic model" and in many situations, it appeared that the term kinematic might have been more appropriate. Other phrases like "frictional forces caused by the tension of its muscles" were unclear at first glance, and might benefit from revision and more canonical usage of terms.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92562.3.sa2](https://doi.org/10.7554/eLife.92562.3.sa2)

Summary:

Developing a mechanical model of C. elegans is difficult to do from basic principles because it moves at low (but not very small) Reynolds number, is itself visco-elastic, and often is measured moving at a solid/liquid interface. The ElegansBot is a good first step at a kinetic model that reproduces a wide range of C. elegans motility behavior.

Strengths:

The model is general due to its simplicity and likely useful for various undulatory movements. The model reproduces experimental movement data using realistic physical parameters (e.g. drags, forces, etc). The model is predictive (semi?) as shown in the liquid to solid gait transition. The model is straightforward in implementation and so likely is adaptable to modification and addition of control circuits.

Comments on revised version:

This is a revised manuscript. I'm happy with the changes made, including the specific responses to my previous concerns.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92562.3.sa3](https://doi.org/10.7554/eLife.92562.3.sa3)

A mechanical model of C. elegans, embedded in a resistive force environment, is used to calculate input torque patterns required to generate output curvature patterns and coordinates, corresponding to a number of different locomotion behaviors in C. elegans.

Strengths:

The use of a mechanical model to study a variety of locomotor sequences and the grounding in empirical data are strengths. The matching of speeds (though requiring adjusted drag coefficients) is a strength.

Weaknesses:

The paper lacks evidence of numerical validation or comparison with the results and tools in the literature. E.g. is it surprising that the uniform torque distribution yields maximal speed? What is the relation between input and output data? How does the input-output relation depend on the parameters of the model? What novel model predictions are made?

In particular, if validated, the breakdown of drag forces and torque distributions during forward locomotion and turning behaviors may be interesting to compare to predictions by other tools, and to empirical measurement. One caveat is that the worm touches itself during such turns, and even crosses over itself in delta turns, and so the estimated drag coefficients and the resultant mechanical forces are likely incorrect.
