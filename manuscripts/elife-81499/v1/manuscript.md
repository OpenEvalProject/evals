# Contrasting action and posture coding with hierarchical deep neural network models of proprioception

## Authors

- Kai J Sandbrink<sup>1</sup>
- Pranav Mamidanna<sup>2</sup>
- Claudio Michaelis<sup>2</sup>
- Matthias Bethge<sup>2</sup> ([ORCID: 0000-0002-6417-7812](https://orcid.org/0000-0002-6417-7812))
- Mackenzie W Mathis<sup>1</sup> ([ORCID: 0000-0001-7368-4456](https://orcid.org/0000-0001-7368-4456)) †
- Alexander Mathis<sup>1</sup> ([ORCID: 0000-0002-3777-2202](https://orcid.org/0000-0002-3777-2202)) †

### Affiliations

1. Brain Mind Institute École Polytechnique Fédérale de Lausanne Genève Switzerland
2. Tübingen AI Center Eberhard Karls Universität Tübingen Tübingen Germany

† Corresponding author

## Abstract

Biological motor control is versatile, efficient, and depends on proprioceptive feedback. Muscles are flexible and undergo continuous changes, requiring distributed adaptive control mechanisms that continuously account for the body's state. The canonical role of proprioception is representing the body state. We hypothesize that the proprioceptive system could also be critical for high-level tasks such as action recognition. To test this theory, we pursued a task-driven modeling approach, which allowed us to isolate the study of proprioception. We generated a large synthetic dataset of human arm trajectories tracing characters of the Latin alphabet in 3D space, together with muscle activities obtained from a musculoskeletal model and model-based muscle spindle activity. Next, we compared two classes of tasks: trajectory decoding and action recognition, which allowed us to train hierarchical models to decode either the position and velocity of the end-effector of one's posture or the character (action) identity from the spindle firing patterns. We found that artificial neural networks could robustly solve both tasks, and the networks'units show tuning properties similar to neurons in the primate somatosensory cortex and the brainstem. Remarkably, we found uniformly distributed directional selective units only with the action-recognition-trained models and not the trajectory-decoding-trained models. This suggests that proprioceptive encoding is additionally associated with higher-level functions such as action recognition and therefore provides new, experimentally testable hypotheses of how proprioception aids in adaptive motor control.
