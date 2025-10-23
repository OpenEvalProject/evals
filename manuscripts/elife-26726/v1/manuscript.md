# Systematic integration of biomedical knowledge prioritizes drugs for repurposing

## Authors

- Daniel Scott Himmelstein<sup>1</sup> ([ORCID: 0000-0002-3012-7446](https://orcid.org/0000-0002-3012-7446))
- Antoine Lizee<sup>2</sup>
- Christine Hessler<sup>2</sup>
- Leo Brueggeman<sup>2</sup>
- Sabrina L Chen<sup>2</sup>
- Dexter Hadley<sup>3</sup>
- Ari Green<sup>2</sup>
- Pouya Khankhanian<sup>2</sup>
- Sergio E Baranzini<sup>1</sup> ([ORCID: 0000-0003-0067-194X](https://orcid.org/0000-0003-0067-194X)) †

### Affiliations

1. Program in Biological and Medical Informatics University of California, San Francisco San Francisco United States
2. Department of Neurology University of California, San Francisco San Francisco United States
3. Department of Pediatrics, Institute for Computational Health Sciences University of California, San Francisco San Francisco United States

† Corresponding author

## Abstract

The ability to computationally predict whether a compound treats a disease would improve the economy and success rate of drug approval. This study describes Project Rephetio to systematically model drug efficacy based on 755 existing treatments. First, we constructed Hetionet (neo4j.het.io), an integrative network encoding knowledge from millions of biomedical studies. Hetionet v1.0 consists of 47,031 nodes of 11 types and 2,250,197 relationships of 24 types. Data was integrated from 29 public resources to connect compounds, diseases, genes, anatomies, pathways, biological processes, molecular functions, cellular components, pharmacologic classes, side effects, and symptoms. Next, we identified network patterns that distinguish treatments from non-treatments. Then we predicted the probability of treatment for 209,168 compound-disease pairs (het.io/repurpose). Our predictions validated on two external sets of treatment and provided pharmacological insights on epilepsy, suggesting they will help prioritize drug repurposing candidates. This study was entirely open and received realtime feedback from 40 community members.
