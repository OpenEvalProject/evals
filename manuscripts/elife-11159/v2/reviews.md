# Peer review - Round 1

Editors:
- Russ Fernald, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11159.021](https://doi.org/10.7554/eLife.11159.021)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Burst muscle performance predicts the speed, acceleration, and turning performance of hummingbirds" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers agree in general that this is an interesting and well done study as summarized by one reviewer:

"This study of hummingbird flight is the first to parse out the effects of wing shape vs. muscle capacity in regard to maneuverability. The study system and methodology are ideal for addressing this question, and the manuscript convincingly demonstrates the dominating effect of muscle physiology on maneuverability. Quite interesting. This is supported by a substantial dataset (collected across multiple years), with rigorous analyses and writing that is a pleasure to read. Overall, we believe that this paper will make a strong impact on the field of animal flight mechanics."

That said, all the reviewers had comments provided below. In particular there is concern that you have corrected for body weight twice. Please address all the issues in responding to the reviews with a clear indication of how you have responded.

Comments:

Subsections “Tracking System” and “Maneuvering performance metrics”: General comments on the use of the terms azimuth, pitch, and yaw. Azimuth is a global coordinate reference; pitch and yaw are traditionally body coordinate. Body axis orientation taken from the 2d ellipsoidal trace gives long axis (head/tail) in a local (body) coordinate space; we take it the other two orthogonal axes were assigned without anatomical reference (body lateral and body dorso-ventral). This reference would be required to determine body coordinate space definitions of pitch and yaw (and roll) – which are the traditional uses of the terms (yaw = rotation around a dorso-ventral body axis; pitch = rotation around lateral axis etc.). We suggest the authors make it clear (in the main text) that the "pitch" is therefore not necessarily rotation around the lateral axis (say glenoid to glenoid) of the body, but rather a global "pitch", with the lateral axis being global horizontal (i.e., orthogonal to gravity). Thus, making inferences regarding the anatomical mechanisms in play during these rotations is difficult; a hummingbird in a 90-degree bank to the left, but [body] yawing right will be producing a global "pitch". This problem is in part addressed but not entirely resolved.

Subsection “Maneuvering performance metrics”, third paragraph: 10 cm ~ 1 body length. Is this why 10 cm was chosen? What would the translational velocity cutoff then be? Rather important; 10 cm of movement might be fairly high velocity at some sampling rate. Reading on – the definition of "arcing turn", which has a >. 5 m/s and refers again to a 10 cm limit for vertical distance traveled. Do these reflect the same cutoffs?

Subsection “Maneuvering performance metrics”, fifth paragraph: Yes, if the body is purely vertical, azimuth change is through roll rotation, which is not measured (ambiguous local body coordinates). An azimuth change for a horizontal body will be purely a result of [local coordinate] yaw, provided the animal is not banked; if it is banked, say 45 degrees, then azimuth change will be a result of both [local coordinate] pitch and yaw; at a ninety degree bank, azimuth change is entirely a result of local coordinate pitch. we doubt it changes the overall statistical inferences, but the lack of unambiguous anatomical references may change the magnitude of the accelerations observed and the mechanisms employed to affect those changes – and that's some of what this paper is about.

For a hummer in a steep bank, the rotational acceleration in the azimuth will be affected by largely local coordinate pitch changes, which are a product of bilaterally symmetrical force production of the wings. With no bank, the rotational acceleration in azimuth will be a result of asymmetrical force production by the wings; given the moments of inertia for both these rotations is the same (the radius of gyration for both is the long axis of the body), the accelerations will be smaller for these pure no-bank all-yaw azimuth turns. (Although should the bird produce an posteriorly-directed upstroke force while producing a forward directed downstroke… the Bobcat Loader, or Sherman Tank turn.)

At any rate, while there is probably precedent for use of the terms yaw and pitch in a global sense, it think it's important to be specific here, especially given this paper is making some inferences regarding the anatomical mechanisms used to maneuver.

Subsection “Maneuvering performance metrics”, seventh paragraph: Again, naming it "pitch-roll" further suggests you know around which body axis these maneuvers occur.

Discussion, seventh paragraph, and throughout: I'm concerned that the relative lack of effect of morphology on influence performance may be because the wrong morphology was examined. Maneuvering accelerations are the result of the forces generated relative to the inertia of the bird's mass. Forces are proportional to wing velocity and area (not wing aspect ratio or length – used alone in fixed effect models 1 & 5). Simultaneous effects – significantly negative coefficient for mass, positive for length, and negative for aspect ratio – would infer a wing loading effect, but might it get statistically buried? We think rooting these statistical hypotheses more firmly and clearly in Newtonian expectations would be wise. For example: the biggest effect seen for Acc centripetal max is wing shape. Yes, there may be unsteady effects here, but we know of no aerodynamic theory predicting how aspect ratio would strongly affect this performance variable, given how it was defined.

Wing loading (mass/wing area) would be a more straightforward variable to include, or just area.

A few minor issues: The most salient of these is that it appears to me the authors may have corrected for body mass twice when only one correction was necessary, potentially reducing the size of effect of other parameters. Whether or not this occurred depends on the exact statistical models used and we suggest that the authors examine their models and explain the logic with respect to body mass with a small addition to the text even if no corrections are required.

If we read things correctly this work accounts for body mass in creating the burst performance metric derived from load lifting performance and then also including an intercept for body mass in the maneuvering performance metrics, but from the tables it seems that body mass is never an important effect with a CI not including zero. Is this because it is already corrected for it once and if so, why is a second correction included? The double-correction seems most curious in the acceleration data since load lifting and accelerations are both dependent on force. Perhaps it is simplest to leave body mass out of the burst performance correction and include it in each of the maneuver models? In any case, please provide some explanation of the mass normalization logic in the manuscript text.

The study is flawed overall by the effect that cage size has on the hummingbird flights as compared to actual outdoor flight performance, but this is noted by the authors and outside the scope of what is correctable, given their dataset. We think the results are nevertheless informative and interesting.

Abstract: morphology or physiological -> morphology and physiological, at least according to the Warrick paper you cite later.

Subsection “Maneuvering performance metrics”, fifth paragraph: azimuthal rotation is implemented by rolling the body axis -> rolling about the body axis.

Introduction, first paragraph: Maneuverability is first mentioned here and is a main subject of the paper, but is never defined. We would suggest including it somewhere, and following Dudley's definitions (2002, Int. Comp. Biol.).

Subsection, “Animals and experimental trials”, second paragraph: "We recorded a two-hour solo trial for each bird." It would be worth noting that the recording was with high-speed video.

Subsection “Animals and experimental trials”, third paragraph: "Measurements of wing length and aspect ratio were calculated using custom analysis software in MATLAB". Please tell us how the metrics were defined and generally calculated, for point of comparison with future studies.

Subsection “Tracking System”, first paragraph: "The filming volume was calibrated by moving a single light-emitting diode throughout the arena”. The volume couldn't be calibrated per se by a waved light; was this used for tie points?

In the same subsection, you say: "To minimize the effect of errors in the 3D tracking, we used a forward/reverse non-causal Kalman filter (Rauch-Tung-Striebel smoother)." Applied to what?

Still regarding the same subsection of the text, how were velocities and accelerations calculated? Are they an output from the filter? Where the process covariance matrices are shown, what is the vector multiplied to Q? It seems that estimation for the velocities was included in the filter, with positions being measured. Please clarify the details.

Subsection “Tracking System”, second paragraph and Figure 1: How does the choice in smoothing parameter affect body orientation?

In the same subsection of the text, you state: "Thus, although acceleration values are comparable within a study, caution must be applied when comparing the magnitude of acceleration values among studies differing in camera frame rate, filming volume, calibrations, and smoothing parameters." I believe that Walker (1998) made this same point (and so probably should be cited).

Also in “Tracking System”: What method/function was used to fit the ellipse?

Figure legends:

Figure 1. "The trajectory presented in B is a 2D view of the trajectory shown in A." Is it the top view, x-y projection? You also state: "Level of smoothing had little effect on the performance metrics measured from the maneuvers." The smoothed accelerations range from 10 to 15 m/s2, compared to the unsmoothed value of 54. So although this statement is strictly true, the smoothing did have a large effect on the reported values.

Figure 4. "Aspect ratio was associated with four maneuvering performance metrics." Only 2 metrics are shown. Why not the other 2?

Figure 5. Same comment, 5 vs. 4 metrics shown.

Figure 7. Add "(Arc)" and "(PRT)" after their spelled-out versions.
