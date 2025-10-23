# Peer review - Round 1

Editors:
- Peng Liu, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90440.3.sa0](https://doi.org/10.7554/eLife.90440.3.sa0)

This manuscript will provide a valuable method to evaluate the safety of MR in patients with orthopaedic implants, which is required in clinics. A strength of the work is that the in-silicon testbed is solid, based on the widely available human project, and validated. In addition, the toolbox will be open for clinical practice.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90440.3.sa1](https://doi.org/10.7554/eLife.90440.3.sa1)

Summary:

In this work authors are trying to satisfy a real need in MR safety, when concerns can rise about the thermal increase due to metallic materials in patients carrying orthopedic implants. The "MR conditional" labeling of the implant obtained by ASTM in-vitro tests may help to plan the MR scan, but it is normally limited to a single specific MR sequence and a B0 value, and it is not always available. The adoption of an in-silico simulation testbed overcomes this limitation, providing a fast and reliable prediction of temperature increase from RF, in real-life scan conditions on human-like digital models. The FDA is pushing this approach.

Strengths:

The presented in-silico testbed looks valuable and validated. It is based on the widely available Visible Human Project (VHP) datasets, and the testbed is available on-line. The approval of the testbed by the FDA as a medical device development tool (MDDT) is a good premise for the large-scale adoption of this kind of solution.

Weaknesses:

A couple of limitations of the study are now clearly highlighted to the readers in this revised version of the paper. The following aspects:

- the lack of the equivalent modeling for the gradients-related heating;

- the way the implant is embedded in the VHP model that should take in consideration how to manage the removed and stretched tissues;

are now correctly taken in consideration in the discussion, providing additional literature.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90440.3.sa2](https://doi.org/10.7554/eLife.90440.3.sa2)

Summary:

In this article, the authors provide a method of evaluating safety of orthopedic implants in relation to Radiofrequency induced heating issues. The authors provide an open source computational heterogeneous human model and explain computational techniques in a finite element method solver to predict the RF induced temperature increase due to an orthopedic implant while being exposed to MRI RF fields at 1.5 T.

Strengths:

The open access computational human model along with their semiautomatic algorithm to position the implant can help realistically model the implant RF exposure in patient avoiding over- or under-estimation of RF heating measured using rectangular box phantoms such as ASTM phantom. Additionally, using numerical simulation to predict radiofrequency induced heating will be much easier compared to the experimental measurements in MRI scanner, especially when the scanner availability is limited.

Weaknesses:

The proposed method only used radiofrequency (RF) field exposure to evaluate the heating around the implant. However, in the case of bulky implants the rapidly changing gradient field can also produce significant heating due to large eddy currents. So the gradient induced heating still remains an issue to be evaluated to decide on the safety of the patient. Moreover, the method is limited to a single human model and might not be representative of patients with different age, sex and body weights.
