# Author response - Round 1

Authors:
- Willem AM Wybo ([ORCID: 0000-0003-1385-4980](https://orcid.org/0000-0003-1385-4980))
- Jakob Jordan ([ORCID: 0000-0003-3438-5001](https://orcid.org/0000-0003-3438-5001))
- Benjamin Ellenberger
- Ulisses Marti Mengual
- Thomas Nevian ([ORCID: 0000-0001-9804-608X](https://orcid.org/0000-0001-9804-608X))
- Walter Senn ([ORCID: 0000-0003-3622-0497](https://orcid.org/0000-0003-3622-0497))

## Response text

DOI: [10.7554/eLife.60936.sa2](https://doi.org/10.7554/eLife.60936.sa2)

[…] Reviewers agreed that the writing needs to be clearer throughout. Terms need to be defined. Implicit references to other work or to concepts need to be replaced with explicit, declarative sentences and explanations. On the technical side the paper also needs a fuller explanation of how fitting of voltage-gated conductances is performed. Finally, a fuller discussion and illustration of the limitations would be appropriate, e.g. explicitly showing cases where further reductions cannot be achieved without fundamentally changing the system. These necessarily exist in a nonlinear system so this is not a shortcoming of the method, rather an important point that some readers may not appreciate.

We have rewritten the sections that were highlighted by the reviewers, in order to explain the unclarities. We have now clearly defined the quantities that we use. We have also explained more elaborately how the voltage-gated channels are fitted. To aid with this, we have added a further panel to Figure 1—figure supplement 1. Finally, we have added a paragraph to the Discussion, where we explain possible lines of inquiry if a reduction does not reproduce dynamics of the full model that need to be retained. To illustrate these lines of inquiry, we have added a new supplementary figure (Figure 3—figure supplement 1) where we perform a similar simulation as in Figure 3J, K, but where we left out compartments in the apical trunk. This reduction is too strong and the generation of a spike-burst cannot be mimicked by the reduced model.

Full reviewer comments are included below for information.

Reviewer #2:

[…] (1) The initial part of the Results section is important for understanding how the software works but is hard to follow. I think more care needs to be taken with defining terms clearly and explaining the logic of the approach in an accessible way.

We have added substantial clarifications to this section.

(2) How the approach deals with voltage-gated ion channels could be made much clearer. E.g. In the subsection “A systematic simplification of complex neuron morphologies”, the text states that GVh,chan depends on the unknown maximal ion channel conductance parameters. How? Why maximal? Voltage-gated channels cannot be maximally activated at all of the voltages tested. I don't understand how to get from here to channel conductances. It could be helpful to make a figure illustrating how fits are obtained for exemplar voltage-gated conductances.

We have explicitly described the elements of the matrix Gvh in the manuscript, so that the parameters that are fitted are now clear. In the Materials and methods – “Quasi-active channels” subsection, we show how the linearized channel currents that go in the matrix Gvh are obtained. It can be seen that they are the product of a ‘maximal conductance parameter’ with a factor that follows from the linearization, and that determines the fraction of that maximal conductance that is open at a given vh. This factor thus changes with vh. Fitting our model simultaneously at a representative set of vh values allows the fit to find a best estimate for the maximal conductance parameter. An additional panel to Figure 1—figure supplement 1 now illustrates how the impedance matrix of the full model, and the inverse of the conductance matrix for the reduced model, changes under different vh. We have furthermore added a subsection to the Materials and methods, titled ”The conductance matrix”, where we explicitly describe how Equation 3 in the main text is obtained. We believe that with our added explanations, it is now clear what the matrix Gvh is and how the maximal conductance parameter is fitted.

(3) The section 'Conditions under which afferent spatial connectivity motifs can be simplified' could also be written more clearly. Concerns are similar to in point 1 above.

We have added additional explanations to this section, more accurately describing things that may have been unclear. We now more explicitly motivate this section, by stating that up until this section we only considered reductions where the synaptic inputs (or electrode current inputs) were located at the compartment sites. Here, we investigate what happens if this is not the case. We also changed the terminology from ‘impedances’ to ‘resistances’. We furthermore explicitly describe why βcurr is close to one (because the transfer impedance zcs is close to the input impedance zcc if the compartment site c is located more proximal than the synaptic input site s), with help of an additional panel to Figure 1—figure supplement 1. Finally, we have substantially extended the second-to-last paragraph of this section, and were able to describe the precise nature and motivation of our simulation experiments (Figure 4G-J) more clearly.
