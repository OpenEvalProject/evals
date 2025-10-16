# Peer review - Round 1

Editors:
- Juan Helen Zhou, https://ror.org/01tgyzw49 National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96017.3.sa0](https://doi.org/10.7554/eLife.96017.3.sa0)

The methods and findings of the current work are important and well-grounded. The strength of the evidence presented is convincing and backed up by rigorous methodology. The work, when elaborated on how to access the app, will have far-reaching implications for current clinical practice.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96017.3.sa1](https://doi.org/10.7554/eLife.96017.3.sa1)

Summary:

The authors aimed to develop and validate an automated, deep learning-based system for scoring the Rey-Osterrieth Complex Figure Test (ROCF), a widely used tool in neuropsychology for assessing memory deficits. Their goal was to overcome the limitations of manual scoring, such as subjectivity and time consumption, by creating a model that provides automatic, accurate, objective, and efficient assessments of memory deterioration in individuals with various neurological and psychiatric conditions.

Strengths:

Comprehensive Data Collection: The authors collected over 20,000 hand-drawn ROCF images from a wide demographic and geographic range, ensuring a robust and diverse dataset. This extensive data collection is critical for training a generalizable and effective deep learning model.

Advanced Deep Learning Approach: Utilizing a multi-head convolutional neural network to automate ROCF scoring represents a sophisticated application of current AI technologies. This approach allows for detailed analysis of individual figure elements, potentially increasing the accuracy and reliability of assessments.

Validation and Performance Assessment: The model's performance was rigorously evaluated against crowdsourced human intelligence and professional clinician scores, demonstrating its ability to outperform both groups. The inclusion of an independent prospective validation study further strengthens the credibility of the results.

Robustness Analysis Efficacy: The model underwent a thorough robustness analysis, testing its adaptability to variations in rotation, perspective, brightness, and contrast. Such meticulous examination ensures the model's consistent performance across different clinical imaging scenarios, significantly bolstering its utility for real-world applications.

Appraisal and discussion:

By leveraging a comprehensive dataset and employing advanced deep learning techniques, they demonstrated the model's ability to outperform both crowdsourced raters and professional clinicians in scoring the ROCF. This achievement represents a significant step forward in automating neuropsychological assessments, potentially revolutionizing how memory deficits are evaluated in clinical settings. Furthermore, the application of deep learning to clinical neuropsychology opens avenues for future research, including the potential automation of other neuropsychological tests and the integration of AI tools into clinical practice. The success of this project may encourage further exploration into how AI can be leveraged to improve diagnostic accuracy and efficiency in healthcare.

However, the critique regarding the lack of detailed analysis across different patient demographics, the inadequacy of network explainability, and concerns about the selection of median crowdsourced scores as ground truth raises questions about the completeness of their objectives. These aspects suggest that while the aims were achieved to a considerable extent, there are areas of improvement that could make the results more robust and the conclusions stronger.

Comments on revised version:

I appreciate the opportunity to review this revised submission. Having considered the other reviews, I believe this study presents an important advance in using AI methods for clinical applications, which is both innovative and has implications beyond a single subfield.

The authors have developed a system using fundamental AI that appears sufficient for clinical use in scoring the Rey-Osterrieth Complex Figure (ROCF) test. In human neuropsychology, tests that generate scores like this are a key part of assessing patients. The evidence supporting the validity of the AI scoring system is compelling. This represents a valuable step towards evaluating more complex neurobehavioral functions.

However, one area where the study could be strengthened is in the explainability of the AI methods used. To ensure the scores are fully transparent and consistent for clinical use, it will be important for future work to test the robustness of the approach, potentially by comparing multiple methods. Examining other latent variables that can explain patients' cognitive functioning would also be informative.

In summary, I believe this study provides an important proof-of-concept with compelling evidence, while also highlighting key areas for further development as this technology moves towards real-world clinical applications.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96017.3.sa2](https://doi.org/10.7554/eLife.96017.3.sa2)

The authors aimed to develop and validate a machine-learning driven neural network capable of automatic scoring of the Rey-Osterrieth Complex Figure. They aimed to further assess the robustness of the model to various parameters such as tilt and perspective shift in real drawings. The authors leveraged the use of a huge sample of lay workers in scoring figures and also a large sample of trained clinicians to score a subsample of figures. Overall, the authors found their model to have exceptional accuracy and perform similarly to crowdsourced workers and clinicians with, in some cases, less degree of error/score dispersion than clinicians.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96017.3.sa3](https://doi.org/10.7554/eLife.96017.3.sa3)

This study presented a valuable inventory of scoring a neuropsychological test, ROCFT, with constructing an artificial intelligence model.

Comments on latest version:

The authors made the system with fundamental AI that is sufficient for clinical use for humans. In human neuropsychology, the test that generates the score is fundamental and relatively easy. Neuropsychologists apply patients to many tests; therefore, the present system is one of them, where we cannot tell the total neurofunction of a patient. The evidence for scoring is thought to be compelling quality, enough for clinical use now and we progress to evaluate other more complicated human neuropsychological functions. For example, persons with dementia change their performance easily when they feel other emotions (worry, boredom, etc.) and notice other stimulation (announcements in the hospital, a walking nurse by chance, etc.). The score of ROCF is definitely changing, compelling the effort of AI scoring. We should grasp this behavior of humans with diverse tests totally. Therefore, scoring AI with compelling quality is a fundamental step for the next, evaluation against the changeable and ambiguous neurobehavior of humans.
