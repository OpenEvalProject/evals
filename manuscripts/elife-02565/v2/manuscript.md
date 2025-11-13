# A user-friendly, open-source tool to project impact and cost of diagnostic tests for tuberculosis

## Authors

- David W Dowdy<sup>1</sup> †
- Jason R Andrews<sup>3</sup>
- Peter J Dodd<sup>4</sup>
- Robert H Gilman<sup>5</sup>

### Affiliations

1. Department of Epidemiology Johns Hopkins Bloomberg School of Public Health Baltimore United States
2. Center for Tuberculosis Research Johns Hopkins University Baltimore United States
3. Division of Infectious Diseases, Department of Medicine Massachusetts General Hospital Boston United States
4. School of Health and Related Research University of Sheffield Sheffield United Kingdom
5. Department of International Health Johns Hopkins Bloomberg School of Public Health Baltimore United States

† Corresponding author

## Abstract

Most models of infectious diseases, including tuberculosis (TB), do not provide results customized to local conditions. We created a dynamic transmission model to project TB incidence, TB mortality, multidrug-resistant (MDR) TB prevalence, and incremental costs over 5 years after scale-up of nine alternative diagnostic strategies. A corresponding web-based interface allows users to specify local costs and epidemiology. In settings with little capacity for up-front investment, same-day microscopy had the greatest impact on TB incidence and became cost-saving within 5 years if delivered at $10/test. With greater initial investment, population-level scale-up of Xpert MTB/RIF or microcolony-based culture often averted 10 times more TB cases than narrowly-targeted strategies, at minimal incremental long-term cost. Xpert for smear-positive TB had reasonable impact on MDR-TB incidence, but at substantial price and little impact on overall TB incidence and mortality. This user-friendly modeling framework improves decision-makers' ability to evaluate the local impact of TB diagnostic strategies.

## Introduction

Infectious disease transmission models are important tools for translating the best current knowledge of the natural history and epidemiology of infectious diseases into projections of epidemiological impact (e.g., incidence, mortality) and costs under alternative strategies for disease control (Garnett et al., 2011). Currently, most published transmission models are either loosely calibrated to reflect global/regional outcomes or more tightly fit to specific epidemiological settings; in either case, model results may be difficult for local decision-makers in the majority of public health settings to utilize. Simplified models designed for in-country use by decision-makers, most notably the Spectrum suite of models supported by the Futures Institute (Stover et al., 2010), have been used to inform decision-making in the fields of reproductive health and human immunodeficiency virus (HIV) for over a decade (Stover, 2004). Estimates from the Spectrum models are now routinely incorporated into official global and country-level estimates of HIV disease burden (Brown et al., 2010) and intervention impact (Farnham et al., 2013). Other simplified models are readily available for impact projections related to non-infectious diseases, where transmission assumptions are less important (Betz Brown et al., 2000; Walker et al., 2013). However, to date, simple, user-friendly transmission models have not been widely used for decision-making related to many infectious diseases other than HIV. Diagnosis of active tuberculosis (TB) is an example of a public health intervention for which transmission models may provide guidance on both global (Dowdy et al., 2006; Abu-Raddad et al., 2009) and country-specific levels (Menzies et al., 2012). Specifically, an unprecedented number of new diagnostic strategies for active TB are now recommended by the World Health Organization (WHO), including same-day microscopy (World Health Organization, 2011), microcolony-based culture techniques (Leung et al., 2012) such as the microscopic-observation drug-susceptibility (MODS) assay (Moore et al., 2006), line-probe assays for drug susceptibility testing (Bwanga et al., 2009), and Xpert MTB/RIF (‘Xpert’), a molecular assay capable of providing results (including rifampin resistance) in 90 min with minimal human resource requirements (Boehme et al., 2010, 2011). TB program decision-makers must repeatedly determine when to invest in scaling up a novel diagnostic test, which test(s) to promote, and whether the implementation strategy should differ by epidemiological situation (Cobelens et al., 2012). Without transmission models to provide locally relevant estimates of cost and impact under alternative implementation strategies, such decisions will be made without systematically considering the implications of available scientific evidence.

To aid in this decision-making process, we created a flexible, simple modeling tool that allows non-expert users to define their local situation according to three key epidemiological parameters (TB incidence, proportion of new TB cases that are multidrug-resistant [MDR], and adult human immunodeficiency virus [HIV] prevalence) and local unit costs of TB diagnosis and treatment. This tool then incorporates those estimates into a combined decision analysis-transmission framework to generate 5-year projections of TB incidence, mortality, and control costs for nine diagnostic strategies (Figures 1 and 2). These strategies are:‘Baseline’: Sputum smear microscopy for each diagnostic attempt, with liquid-media TB culture only to evaluate smear-positive cases with a history of previous TB treatment for drug resistance. (Cultures in all scenarios trigger drug-susceptibility testing if positive.)‘TB culture if previously treated’: Sputum smear microscopy used for patients without a history of TB treatment; smear plus liquid-media culture used to diagnose TB in any previously treated individual with symptoms (regardless of smear status).‘Xpert if HIV-positive’: Xpert MTB/RIF for HIV-infected patients only, with a positive test for rifampin resistance triggering treatment for MDR-TB. Xpert is assumed to be deployed at the district level, such that results cannot generally be provided during the same clinical encounter (Lawn et al., 2012). This strategy is conceived as a ‘best-case’ scenario for HIV-targeted TB testing: if individuals unaware of their HIV status are not tested with Xpert, this strategy will overestimate effectiveness, and if those unaware of their status are tested, it will underestimate costs.‘Xpert if Smear-Positive’: Xpert MTB/RIF for smear-positive patients only (i.e., for rapid DST), with a positive test for rifampin resistance triggering treatment for MDR-TB.‘Xpert for All’: Xpert MTB/RIF for all patients.‘Xpert with Culture DST Confirmation’: Xpert MTB/RIF for all patients, but treatment for MDR-TB only initiated if rifampin resistance is confirmed by culture.‘MODS/TLA’: Sputum smear, plus microcolony-based TB culture (e.g., MODS or thin-layer agar, TLA) for all patients.‘Same-Day Microscopy’: Double the per-test cost of sputum smear microscopy, in exchange for the ability to provide results to patients in the same clinical encounter (e.g., with peripheral, unbatched reading of sputum smears).‘Same-Day Xpert’: Double the per-test cost of Xpert MTB/RIF, in exchange for the ability to provide results to patients in the same clinical encounter (e.g., peripheral deployment, with greater costs reflecting lower volume per machine [Vassall et al., 2011]).

![Figure 1.](https://cdn.elifesciences.org/articles/02565/elife-02565-fig1-v2.jpg)

**Figure 1.:** Users are asked, via open-source computer script or Web interface, to select one of the nine diagnostic strategies and to provide unit costs and three basic epidemiological parameters (TB incidence, MDR-TB prevalence among new cases, and adult HIV prevalence). The selected diagnostic strategy is used to populate a decision tree that calculates (a) the probability of missed diagnosis, unsuccessful treatment, and successful treatment, (b) costs, and (c) diagnostic delays. These outputs depend on patients' TB (yes/no, and drug susceptibility status), HIV, and TB treatment history status. The selected epidemiological parameters are then used to populate a dynamic transmission model, creating a steady-state population that reflects local TB epidemiology. The decision tree—which inputs user-defined unit costs—is then incorporated into the transmission model to project outcomes under the selected diagnostic scenario. Users can sequentially select multiple diagnostic scenarios for comparison, and the computer script (though not the Web interface) allows users to manipulate input parameters at their discretion.

![Figure 2.](https://cdn.elifesciences.org/articles/02565/elife-02565-fig2-v2.jpg)

**Figure 2.:** Boxes represent sub-populations in the model, and arrows represent rates of movement between those sub-populations. Parallel structures exist for: (a) HIV-infected vs HIV-uninfected; (b) never-treated vs previously treated (for TB); and (c) among TB-infected individuals, drug-susceptible vs isoniazid-monoresistant vs rifampin-resistant (including MDR). ‘Pre-diagnostic’ TB refers to individuals who are infectious but have not yet begun to seek care. Mortality occurs from all sub-populations (not shown), and at a higher rate among those with HIV and active TB.

For purposes of illustration, we evaluated each of these diagnostic strategies in four emblematic epidemiological settings, defined by TB incidence, MDR-TB prevalence among new cases, and adult HIV prevalence:‘Reference/High-Incidence Setting’ (e.g., Southeast Asia): TB incidence 250 per 100,000/year (twice the global incidence [World Health Organization, 2012]), MDR-TB prevalence of 3.7% in new TB cases (the estimated global prevalence [World Health Organization, 2012]), adult HIV prevalence of 0·83% (the estimated global prevalence [UNAIDS, 2012]);‘Low-Incidence Setting’ (e.g., United States, Western Europe): TB incidence at entry of 8.9 per 100,000/year and declining, with similar MDR-TB (as a proportion of new cases) and HIV prevalence as above;‘High MDR Setting’ (e.g., former Soviet Union): TB incidence 100 per 100,000/year, MDR-TB prevalence of 10% in new TB cases, adult HIV prevalence of 0.83%; and‘High HIV Setting’ (e.g., sub-Saharan Africa): Adult HIV prevalence of 20%, TB incidence 500 per 100,000, and MDR-TB prevalence among new cases of 3.7%.

In each setting, we used a uniform set of costs for purposes of comparison (Table 1). Although these four settings form the basis of the results presented here, decision-makers can use the open-source model program (included as Supplementary file 1, written in the open-source programming language Python, Version 2.7, www.python.org) to re-define any parameter in Table 1 according to their best local knowledge; a manual for doing so is also included as Supplementary file 2. Capacity to create non-equilibrium settings (e.g., declining TB incidence, increasing MDR-TB) is included. We also provide a web-based interface (flexdx.modeltb.org) that allows users to input local TB incidence, MDR-TB prevalence, HIV prevalence, and unit costs; this interface provides customized results without the requirement to manipulate programming code. The program corresponding to the web version is also available on a public repository (https://github.com/JJPennington/FlexDx-TB-Web-Django).

**Table 1.**
 Model input parameters*


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
      <th>Reference(s)/Rationale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">TB and HIV Transmission</td>
    </tr>
    <tr>
      <td>Transmission rate, per smear-positive/highly  infectious person-year</td>
      <td></td>
      <td>Calibrated to user-defined TB incidence†</td>
    </tr>
    <tr>
      <td>Proportional reduction in per-case transmission  rate, MDR-TB</td>
      <td></td>
      <td>Calibrated to user-defined MDR-TB prevalence†</td>
    </tr>
    <tr>
      <td>Proportional reduction in fitness,  isoniazid-monoresistant TB</td>
      <td>25% of MDR-TB reduction</td>
      <td>Assumption</td>
    </tr>
    <tr>
      <td>HIV incidence rate, per year</td>
      <td></td>
      <td>Calibrated to user-defined HIV prevalence†</td>
    </tr>
    <tr>
      <td>Relative transmission rate from  smear-negative/less infectious TB</td>
      <td>0.22</td>
      <td>(Behr et al., 1999)</td>
    </tr>
    <tr>
      <td>Proportion of pulmonary TB that is  smear-positive/highly infectious</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>0.63</td>
      <td>(Steingart et al., 2006a; Steingart et al., 2006b)</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>0.50</td>
      <td>(Getahun et al., 2007)</td>
    </tr>
    <tr>
      <td colspan="3">TB Progression</td>
    </tr>
    <tr>
      <td>Endogenous reactivation rate</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>0.0005/year</td>
      <td>(Horsburgh et al., 2010)</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>0.05/year</td>
      <td>(Antonucci et al., 1995)</td>
    </tr>
    <tr>
      <td>Proportion of recent infections resulting in  rapid progression</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>0.14</td>
      <td>(Vynnycky and Fine, 1997; Dye et al., 1998)</td>
    </tr>
    <tr>
      <td rowspan="2">HIV-infected</td>
      <td>0.47</td>
      <td>0.75 without ART, (Daley et al., 1992)</td>
    </tr>
    <tr>
      <td></td>
      <td>75% reduction if on ART, (Williams et al., 2010) 50% ART coverage</td>
    </tr>
    <tr>
      <td>Reduction in TB rapid progression probability  due to latent TB infection (HIV-negative only)</td>
      <td>0.79</td>
      <td>(Andrews et al., 2012)</td>
    </tr>
    <tr>
      <td colspan="3">TB Mortality and Resolution</td>
    </tr>
    <tr>
      <td>Life expectancy at age 15</td>
      <td>55 years</td>
      <td>(World Bank, 2012)</td>
    </tr>
    <tr>
      <td>Annual mortality from HIV</td>
      <td>0.05/year</td>
      <td>(UNAIDS, 2012)</td>
    </tr>
    <tr>
      <td>Annual mortality from TB</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative, smear-positive/highly infectious</td>
      <td>0.23/year</td>
      <td>(Tiemersma et al., 2011)</td>
    </tr>
    <tr>
      <td>HIV-negative, smear-negative/less infectious</td>
      <td>0.07/year</td>
      <td>(Tiemersma et al., 2011)</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>1.0/year</td>
      <td>(Corbett et al., 2003; Corbett et al., 2007; Wood et al., 2007)</td>
    </tr>
    <tr>
      <td>Rate of spontaneous TB resolution  (HIV-negative only)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Smear-positive/highly infectious</td>
      <td>0.1/year</td>
      <td>(Tiemersma et al., 2011)</td>
    </tr>
    <tr>
      <td>Smear-negative/less infectious</td>
      <td>0.27/year</td>
      <td>(Tiemersma et al., 2011)</td>
    </tr>
    <tr>
      <td colspan="3">TB Treatment Outcomes and Emergence of Drug Resistance</td>
    </tr>
    <tr>
      <td>Probability of failure or relapse (within 1 year)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Drug-susceptible</td>
      <td>0.04</td>
      <td>(World Health Organization, 2012)</td>
    </tr>
    <tr>
      <td>INH-monoresistant, first-line therapy</td>
      <td>0.21</td>
      <td>(Menzies et al., 2009b)</td>
    </tr>
    <tr>
      <td>INH-monoresistant, retreatment or 2nd-line</td>
      <td>0.16</td>
      <td>(Menzies et al., 2009b)</td>
    </tr>
    <tr>
      <td>MDR-TB, first-line or retreatment</td>
      <td>0.50</td>
      <td>(Espinal et al., 2000)</td>
    </tr>
    <tr>
      <td>MDR-TB, second-line therapy</td>
      <td>0.30</td>
      <td>(World Health Organization, 2010)</td>
    </tr>
    <tr>
      <td>Proportion of one-year recurrence due to failure</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Drug-susceptible</td>
      <td>0.14</td>
      <td>(Lew et al., 2008)</td>
    </tr>
    <tr>
      <td>INH-monoresistant</td>
      <td>0.33</td>
      <td></td>
    </tr>
    <tr>
      <td>MDR-TB</td>
      <td>0.56</td>
      <td></td>
    </tr>
    <tr>
      <td>Probability of acquired drug resistance  (per treatment course)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Susceptible becoming INH-monoresistant</td>
      <td>0.001</td>
      <td>(Menzies et al., 2009a; Menzies et al., 2009b)</td>
    </tr>
    <tr>
      <td>Susceptible becoming MDR-TB</td>
      <td>0.002</td>
      <td></td>
    </tr>
    <tr>
      <td>INH-monoresistant becoming MDR-TB</td>
      <td>0.045</td>
      <td></td>
    </tr>
    <tr>
      <td>If treated with 2 effective drugs for &gt;6 mos</td>
      <td>0.017</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Behavioral Parameters</td>
    </tr>
    <tr>
      <td>Infectious months before starting to seek care</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>9 months</td>
      <td>(Dowdy et al., 2013)</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>1 month</td>
      <td>(Corbett et al., 2004)</td>
    </tr>
    <tr>
      <td>Diagnostic frequency while seeking care</td>
      <td>5.0/year</td>
      <td>(Storla et al., 2008; Sreeramareddy et al., 2009)</td>
    </tr>
    <tr>
      <td>Probability of treatment in a TB patient  whose microbiological test is negative</td>
      <td>0.25</td>
      <td>(Wilkinson et al., 2000; Dowdy et al., 2008)</td>
    </tr>
    <tr>
      <td>Loss to follow-up between diagnostic  presentation and treatment initiation</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sputum smear or GXP (not same-day)</td>
      <td>0.15</td>
      <td>(MacPherson et al., 2014)</td>
    </tr>
    <tr>
      <td>Culture (microcolony or commercial liquid)</td>
      <td>0.25</td>
      <td>(Dowdy et al., 2008)</td>
    </tr>
    <tr>
      <td>Same-day diagnosis</td>
      <td>0</td>
      <td>Assumption</td>
    </tr>
    <tr>
      <td colspan="3">Diagnostic Accuracy</td>
    </tr>
    <tr>
      <td>Sensitivity for smear-negative/less-infectious TB</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sputum smear microscopy</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <td>Xpert MTB/RIF</td>
      <td>0.72</td>
      <td>(Brownell et al., 2012)</td>
    </tr>
    <tr>
      <td>Culture (microcolony or commercial liquid)</td>
      <td>0.85</td>
      <td>(Cruciani et al., 2004; Leung et al., 2012)</td>
    </tr>
    <tr>
      <td>Specificity for TB</td>
      <td></td>
      <td>(Steingart et al., 2006; Boehme et al., 2011; Leung et al., 2012)</td>
    </tr>
    <tr>
      <td>Sputum smear microscopy</td>
      <td>0.98</td>
      <td></td>
    </tr>
    <tr>
      <td>Xpert MTB/RIF</td>
      <td>0.98</td>
      <td></td>
    </tr>
    <tr>
      <td>Microcolony culture</td>
      <td>0.98</td>
      <td></td>
    </tr>
    <tr>
      <td>Sensitivity for drug resistance (if TB detected)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Microcolony culture (rifampin and isoniazid)</td>
      <td>0.98</td>
      <td>(Minion et al., 2010)</td>
    </tr>
    <tr>
      <td>Xpert MTB/RIF (rifampin only)</td>
      <td>0.94</td>
      <td>(Boehme et al., 2011)</td>
    </tr>
    <tr>
      <td>Specificity for drug resistance (if TB detected)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Microcolony culture (isoniazid)</td>
      <td>0.96</td>
      <td>(Minion et al., 2010)</td>
    </tr>
    <tr>
      <td>Microcolony culture (rifampin)</td>
      <td>0.99</td>
      <td>(Minion et al., 2010)</td>
    </tr>
    <tr>
      <td>Xpert MTB/RIF (rifampin)</td>
      <td>0.98</td>
      <td>(Boehme et al., 2011)</td>
    </tr>
    <tr>
      <td colspan="3">Diagnostic Delay and non-TB Care-Seeking</td>
    </tr>
    <tr>
      <td>Days from presentation to treatment initiation</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sputum smear or Xpert MTB/RIF</td>
      <td>7 days</td>
      <td>Assume 1 week</td>
    </tr>
    <tr>
      <td>Microcolony or commercial liquid culture</td>
      <td>30 days</td>
      <td>(Boehme et al., 2011)</td>
    </tr>
    <tr>
      <td>Months of therapy before a failing regimen will  be changed, or before default and recurrence</td>
      <td>6 months</td>
      <td>Assumption</td>
    </tr>
    <tr>
      <td>Annual rate of diagnostic evaluation for TB,  among people who do not have active TB</td>
      <td>0.01/year</td>
      <td>10% of suspects have TB, high-incidence setting</td>
    </tr>
    <tr>
      <td colspan="3">Cost Parameters (user-defined; values below for comparison purposes only)</td>
    </tr>
    <tr>
      <td>Per-patient cost of TB therapy</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>First-line</td>
      <td>US$500</td>
      <td>User-defined</td>
    </tr>
    <tr>
      <td>Retreatment</td>
      <td>US$1000</td>
      <td>(Vassall et al., 2011)</td>
    </tr>
    <tr>
      <td>Second-line/MDR</td>
      <td>US$5000</td>
      <td>(Vassall et al., 2011)</td>
    </tr>
    <tr>
      <td>Outpatient visit (diagnosis or follow-up)</td>
      <td>US$10</td>
      <td>(Vassall et al., 2011)</td>
    </tr>
    <tr>
      <td>Per-test cost:</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sputum smear</td>
      <td>US$2</td>
      <td>(Vassall et al., 2011)</td>
    </tr>
    <tr>
      <td>Same-day sputum smear</td>
      <td>US$10</td>
      <td>Assumption</td>
    </tr>
    <tr>
      <td>Xpert MTB/RIF</td>
      <td>US$15</td>
      <td>(Vassall et al., 2011)</td>
    </tr>
    <tr>
      <td>Same-day Xpert MTB/RIF</td>
      <td>US$30</td>
      <td>Assumption</td>
    </tr>
    <tr>
      <td>Microcolony culture (with DST)</td>
      <td>US$5</td>
      <td>(Solari et al., 2011)</td>
    </tr>
    <tr>
      <td>Commercial liquid-media culture</td>
      <td>US$20</td>
      <td>(Vassall et al., 2011)</td>
    </tr>
    <tr>
      <td>Commercial liquid-media culture + DST</td>
      <td>US$40</td>
      <td>(Vassall et al., 2011)</td>
    </tr>
  </tbody>
</table>

_*In the actual model program (Supplementary file 1), users can change any parameter based on local values.†For reference, the transmission rate (in infections per person-year during diagnosis-seeking active TB) is 36.9 in the reference scenario, 14.0 in the low-incidence scenario, 25.4 in the high MDR scenario, and 12.9 in the high HIV scenario. Corresponding proportional reductions in MDR-TB transmission rate are 0.23, 0.23, 0.21, and 0.19; and HIV incidence estimates (per 1000 adult person-years) are 0.7, 0.6, 0.6, and 18.9._

## Results

### Model validation

To validate the model, we compared selected model outcomes to published global estimates. In the high-incidence setting, our model estimated TB mortality at 14% of incidence (95% uncertainty range: 7–20%, WHO global estimate 14% [World Health Organization, 2012]), HIV-associated TB at 13% of all incident TB (95% uncertainty range: 4–14%, global estimate 13% [World Health Organization, 2012]), previously treated cases at 13% of all incident cases (95% uncertainty range: 9–34%, global estimate 14% [World Health Organization, 2012]), and duration of TB disease at 1.2 years (95% uncertainty range 0.8–2.1, global estimate 1.4 years [World Health Organization, 2012]). Our model estimated that MDR-TB prevalence in previously treated cases was 15.4% (WHO estimate 20% [World Health Organization, 2012]), but unlike our model, WHO notifications often count failure and recurrence after default (in the same person) as two separate cases. At steady-state in the model, 80% of incident TB was due to recent infection rather than reactivation.

### Comparison of diagnostic strategies in the high incidence scenario

Figure 3 shows the projected incremental 5-year cost and impact of each of nine selected diagnostic strategies (described in greater detail in the ‘Materials and methods’ section), in the high-incidence scenario. In general, both the cost and impact of targeted strategies (culture for retreatment, Xpert for HIV-positive, Xpert for smear-positive) on incidence were small relative to broader diagnostic strategies (Xpert for all, MODS/TLA, same-day Xpert). The incremental cost-effectiveness, in terms of cost per case averted (i.e., slope of the line from origin to each point in Figure 3), was similar across all strategies with the exception of same-day smear, which was cost-saving and had greater effectiveness than the baseline. Same-day microscopy remained cost-saving by year 5 as long as same-day results could be provided at less than five times the per-smear cost of routine results (i.e., <$10/test). Among the targeted strategies, Xpert for smear-positives was the most expensive but had the greatest impact on MDR-TB cases averted, whereas Xpert for HIV-infected individuals and culture for retreatment cases offered smaller gains at lower cost. Among the broad strategies, culture confirmation of rifampin-resistant tests on Xpert saved costs with little reduction in effectiveness. There was little difference between culture-confirmed Xpert and MODS/TLA, and same-day Xpert was the most expensive and most effective strategy.

![Figure 3.](https://cdn.elifesciences.org/articles/02565/elife-02565-fig3-v2.jpg)

**Figure 3.:** Shown are cumulative projected 5-year costs and impact (averted TB cases [panel A] or MDR-TB cases [panel B]) of each diagnostic strategy described in the Introduction, incremental to the baseline strategy, per 100,000 population. Strategies with greater impact appear to the right on the x-axis; more costly strategies appear higher on the y-axis. The same-day smear strategy is cost-saving but shown at an incremental cost of $0 for simplicity.

### Comparison of diagnostic strategies across settings

The projected impacts and costs of the nine diagnostic strategies relative to the baseline strategy, in each of four selected epidemiological settings, are shown in Figure 4. In all four settings, the ranking of diagnostic strategies remained similar for all outcomes, although the cost of broader diagnostic strategies relative to targeted strategies fell substantially over 5 years in higher-incidence settings as the broader strategies generated declines in TB incidence. In the low-incidence setting, where a higher proportion of TB treatments are false-positive and more incident TB is also due to reactivation (60% of all new cases), the relative cost of improved TB diagnosis was the highest, while the relative impact was the least. In the high HIV setting, the impact of diagnostic interventions on TB incidence was diminished relative to the high-incidence setting, though the impact on TB mortality was similar. Additionally in this setting, the Xpert for HIV-positive strategy was substantially more costly, but also more effective, than in other settings.

![Figure 4.](https://cdn.elifesciences.org/articles/02565/elife-02565-fig4-v2.jpg)

**Figure 4.:** Shown are projected changes in TB incidence, MDR-TB incidence, TB mortality, and costs (in Year 1 and Year 5 after immediate implementation), relative to baseline (Strategy 1) after implementing each of the diagnostic strategies described in the text. Epidemiological outcomes are measured at the end of Year 5. Panel A (high incidence) shows a setting with TB incidence of 250 per 100,000/year, stable MDR-TB prevalence of 3.7% among new cases, adult HIV prevalence of 0.83%, and cost of $500 to treat one case of TB with first-line therapy. In panel B (low incidence), the TB incidence is reduced to 8.3 per 100,000/year (implemented by gradual decline in incidence over 50 years). In panel C (high MDR), MDR-TB prevalence among new cases is set at 3.7% in the beginning of year 1, increasing to 10.7% by the end of year 5. In panel D (high HIV), adult HIV prevalence is set to 20% and TB incidence is set to 500 per 100,000/year.

### Sensitivity analyses

The impact of the ‘Xpert for all’ strategy on TB incidence (selected a priori as the primary outcome for sensitivity analysis) was most sensitive to three parameters, both in terms of absolute effects on impact estimates and partial rank correlation coefficients. These three parameters were: (1) the proportion of TB patients who would be empirically treated even if microbiologic testing yielded a negative result (‘empiric treatment proportion’), (2) duration of infectiousness before seeking care (‘pre-diagnostic delay’), and (3) rate of reactivation from latent infection to active disease (‘reactivation rate’). For this latter parameter, in-depth investigation revealed that the key determinant was not the reactivation rate per se, but rather the proportion of active TB representing recent vs remote infection. If the empiric treatment proportion was increased from 25% to 37.5%, the projected reduction in TB incidence fell from 20% to 13%. By contrast, when only 12.5% of false-negative patients were started on therapy, ‘Xpert for all’ achieved a 31% reduction in incidence. Corresponding reductions in incidence with ‘Xpert for all’ (20% at baseline) included: 27% if pre-diagnostic delay was shortened from 9 months to 4.5 months, 14% if pre-diagnostic delay was lengthened to 13.5 months, 15% if the reactivation rate was doubled from 0.05% to 0.1% per year, and 23% if reactivation was halved to 0.025% per year. The projected 5-year reduction in incidence for this strategy did not fall outside the range of 12–25% under variation of any other model parameter, up to 50% of that parameter's baseline value (Table 1).

Both costs and incremental costs were more sensitive to the cost of TB treatment than the cost of diagnostics. For example, doubling the cost of first-line therapy (from $500 to $1000 per person) augmented the incremental year 1 costs for ‘Xpert for all’ from a 57% increase over baseline to a 77% increase, and doubling the cost of MDR therapy (from $5000 to $10,000 per person) generated an 86% increase in incremental year 1 costs, whereas doubling the unit cost of Xpert (from $15 to $30) only resulted in a 72% increase. Unit costs other than those for first-line treatment, MDR treatment, and the diagnostic modality under study in each scenario were not important determinants of incremental costs.

## Discussion

To date, most transmission models of infectious disease control interventions present results that are not directly usable by decision makers because they are not customizable to local conditions. We present a flexible, user-friendly model of TB diagnosis and transmission that allows users without modeling expertise to define an epidemiologic setting (according to TB incidence, MDR-TB prevalence, and HIV prevalence) and unit costs, evaluating various diagnostic strategies in that setting in terms of population-level costs and impact. While this model cannot precisely replicate the epidemiological situation in any given location, it applies a standardized methodology across a wide range of settings, thereby illustrating important interactions between epidemiological parameters and projected impact. We provide both a web interface for rapid calculations and full model code whereby users can change any model parameter for ‘personalized’ sensitivity analysis. Our model results suggest that the rank-ordering of diagnostic strategies may be relatively stable across epidemiological settings, but that the actual population-level costs and impact differ dramatically. This model also serves as an example of how epidemiologists can provide decision-makers across a wide variety of local settings with rapid access to customizable ‘first-pass’ projections of cost and impact from transmission models without the need to construct tightly fitted models to represent all epidemiological settings.

Our results provide important guidance to TB decision-makers. Specifically, in settings where little additional up-front investment is possible (<25% increase in TB control budget), same-day microscopy has the greatest impact on TB incidence with no increase in overall cost at 5 years, provided that same-day microscopy can be feasibly delivered for less than $10 per patient.  For settings in which containing MDR-TB is the most important consideration, Xpert for smear-positives has the greatest effectiveness for this outcome, but at substantial price and very little impact on overall TB incidence and mortality. Xpert for HIV-positives and culture for retreatment cases both offer meaningful, albeit small, gains; the cost and impact of these strategies are the highest in HIV-endemic settings. In settings where more initial investment is possible (about 50% increase in TB control budget), broader scale-up of either Xpert or MODS/TLA for all TB diagnosis can offer substantially greater benefits, both in terms of reduced incidence (often 10 times more TB cases averted than with the more narrowly-targeted strategies above) and long-term costs (in that the incremental cost of these strategies declines greatly by Year 5). In general, culture confirmation of positive Xpert results before committing to a course of second-line therapy is preferred. Finally, where the greatest impact is sought, combination of Xpert for all plus infrastructure for same-day diagnosis achieves this aim in all settings, but at the highest cost.

Although this model represents a highly simplified framework, it compares well to other global estimates to which it was not fit (e.g., WHO estimates of TB mortality, previously treated TB, HIV-associated TB, and MDR-TB prevalence among previously treated cases). Its results are also similar to those of other mathematical models of TB diagnosis that are fit to specific locations. For example, Menzies et al. (2012) modeled scale-up of Xpert for people living with HIV in southern Africa, estimating a 6% reduction in incidence, 21% reduction in TB mortality, 25% reduction in MDR-TB incidence that declines to <10% over a longer time frame, and 40% increase in costs (not including costs of antiretroviral therapy). Our corresponding estimates for the Xpert for HIV-positive strategy in the high-HIV setting are 5% reduction in incidence, 25% reduction in TB mortality, 7% reduction in MDR-TB incidence, and increase in costs from 41% (year 1) to 28% (year 5). For purposes of deciding between alternative strategies of scaling up TB diagnostics, the estimates from these two models are likely to provide similar guidance.

For any such simplified transmission model to have an impact on decision-making, it is important to consider who the eventual users of such a model might be, and to develop the model in consultation with those groups. In this case, we identified a number of potential end-user organizations including technical assistance agencies (e.g., KNCV Tuberculosis Foundation), funding bodies (e.g., Global Fund for AIDS, Tuberculosis, and Malaria), non-governmental organizations (e.g., Medecins Sans Frontiers), National Tuberculosis Programs, and regional offices of the World Health Organization. We then invited representatives of these organizations to attend a 1-day workshop (April 2014, The Hague, The Netherlands) describing methods and challenges related to modeling of TB diagnostics in general, including this transmission model in particular. We developed ‘hands-on’ exercises for participants to better learn the model and solicited specific feedback, which is being incorporated into the model structure and web interface in ongoing fashion. We next intend to develop a series of informal ‘case studies’ whereby the use of this model for in-country decision-making can be demonstrated and disseminated.

As with any modeling analysis, this research has important limitations. In order to provide sufficient flexibility and generalizability, we make a number of strong assumptions that include a constant population, homogeneous mixing, no change in parameter values over time, and simplistic incorporation of HIV and drug resistance. Without making such simplifying assumptions, it is impossible to deliver a flexible modeling framework that can generate transparent, customizable, rapid results (i.e., without complex statistical fitting to each individual epidemiological scenario). This model can replicate user-defined TB incidence, MDR-TB prevalence, and HIV incidence but does not describe the breakdown of these values in key subpopulations (e.g., congregate settings or geographical ‘hotspots’), nor does it incorporate operational aspects of the TB diagnostic system in any one setting. Thus, this model does not ameliorate the need for more detailed models in settings where precise estimates are needed; rather it provides access to ‘first-pass’ estimates in settings (i.e., the vast majority of local decision-makers) where such tightly calibrated model projections are not available. This model focuses on transmission dynamics and thus does not include pediatric TB and extrapulmonary TB; these largely non-infectious disease manifestations remain very important components of the TB epidemic that are not captured here. We validate our model against global estimates and other models; ideally, further validation would be performed over time using field data across a wide variety of settings. Our model allows users to define three key epidemiological parameters (as well as other model assumptions within the program), but data to inform even these three parameters—as well as unit costs—are unlikely to be available on sub-national levels. As a result, users wishing to adapt the model to a smaller geographic scale will need to perform additional data-gathering exercises to inform these estimates if they wish to maximize the utility of the model.

Nevertheless, even if high-quality data are not available at the local level, this model allows decision-makers to estimate epidemiological and economic values according to reasonable assumptions (e.g., comparison of TB notification rates or budget line-items to those in the published literature or at the national level), vary those assumptions in real-time, and obtain corresponding projections of comparative impact that incorporate the best available current data on epidemiological or natural history parameters (e.g., TB progression and reactivation). Future efforts might also provide flexibility to specify operational characteristics (e.g., health system capacity) as well.

A final concern is that, by providing users the ability to specify TB incidence, MDR-TB prevalence, and adult HIV prevalence, a number of scenarios can be created (e.g., low TB incidence and very high adult HIV prevalence) that are not epidemiologically realistic. Although there is danger in allowing uninformed users to make projections for such scenarios (and the model will reject or alert users to highly implausible values), we believe that this risk is outweighed by the benefit of providing full flexibility to model epidemiological scenarios (e.g., sub-district level data) that will never be captured by a limited number of closely-calibrated TB transmission models.

In summary, we have created a flexible modeling framework that allows users without modeling expertise to generate simulated populations with locally relevant values for TB incidence, MDR-TB prevalence, adult HIV prevalence, and TB treatment costs. By comparing an array of diagnostic options across emblematic epidemiological scenarios, we provide guidance to decision-makers who seek to ascertain the optimal diagnostic strategy to achieve their selected disease control targets, and to do so using a standardized methodology. Success in the fight against infectious disease generally, and TB specifically, depends on our ability to place global knowledge in the hands of local decision-makers, enabling them to choose those interventions that are likely to have the greatest impact, given existing resources and local epidemiological realities. This flexible modeling framework of diagnostic interventions takes an important step in that direction.

## Materials and methods

### Transmission model

Using previously published models of TB diagnostics as a guide (Dye et al., 1998; Abu-Raddad et al., 2009; Menzies et al., 2012; Dowdy et al., 2013), we constructed a transmission model of TB using ordinary differential equations. This model categorizes patients according to HIV status (positive or negative), TB treatment status (never treated or previously treated), TB disease status (as shown in Figure 2), and among those who are infected with TB, drug resistance status (susceptible, isoniazid-monoresistant, and rifampin-resistant including MDR), and level of infectiousness (smear-negative/less-infectious and smear-positive/highly infectious). Individuals enter the model at age 15, and TB with no pulmonary component (i.e., not infectious) is not included. For purposes of transparent communication, we chose a population size of 100,000 (to match standard reporting of TB outcomes) and assumed a constant population with no net population growth or immigration/emigration. After constructing the transmission framework, we used decision analysis to estimate (a) the probability of each diagnostic outcome; (b) the diagnostic delay; and (c) the cost of TB diagnosis and treatment under each of the nine diagnostic strategies, assuming immediate implementation at the beginning of a given year (‘Year 1’). Two separate authors (DWD and PJD) independently coded the model; these models gave comparable results.

### Model initiation

After setting probabilities and costs under each diagnostic strategy, we then created a flexible modeling structure capable of generating epidemiological scenarios as a function of three variables, which the user specifies: HIV prevalence (assuming a global mean level of antiretroviral therapy coverage), TB incidence, and MDR-TB prevalence among new TB cases. We accomplished this by allowing three key parameters to vary across model scenarios: annual HIV incidence, rate of TB transmission per smear-positive/highly infectious person-year, and relative per-case transmission rate of rifampin-resistant TB. We also allow users to specify all relevant unit costs for TB diagnosis and treatment; other model parameters were estimated from existing literature (Table 1). We then created a program that numerically generates a unique steady-state population meeting the user-defined values; this population serves as the baseline strategy (Strategy 1 above) at the beginning of the time frame under evaluation. The program has flexibility to create its steady-state population 50 years in the past, allowing it to replicate the protracted, slow declines in TB incidence as seen in many lower-incidence settings; this is done automatically for any scenario with a target TB incidence less than 50 per 100,000/year.

### Model compartments

The mathematical model consists of the following TB compartments:Uhp, UninfectedLhdp, Latently infectedEhdp, Early active (infectious status i = 0)Ahdip, Late activePhdip, Active ‘pre-treatment’: diagnosis in progress, will lead to appropriate therapyIhdip, Active ‘inappropriate treatment’: receiving therapy that ends in default or failure

In these compartments, the subscript h refers to HIV status (h = 0 if HIV-uninfected, 1 if HIV-infected), d refers to drug resistance status (d = 0 if drug-susceptible, 1 if isoniazid [INH]-monoresistant, and 2 if multidrug-resistant [MDR]), i refers to infectious status (i = 0 if smear-negative/less infectious and 1 if smear-positive/highly infectious), and p refers to previous treatment status (p=0 if never treated, 1 if previously treated). Infectious status can be conceptualized as an individual's sputum smear status, if two smears were to be performed in a quality-assured laboratory at any given point in time.

### Model structure

The model assumes an adult population of stable size with no immigration or emigration: the number of individuals entering the uninfected compartment U is set as equal to the number who die (whether from TB or other causes) from all other compartments. Pediatric and purely extrapulmonary TB are not explicitly considered because the diagnostic considerations for these manifestations are different. In the short-term, however, to the extent that these forms of TB are non-infectious and equally fatal as adult pulmonary TB, their effects on TB incidence and mortality may be approximated by dividing the model's projected incidence and mortality by (1 − proportion of TB that is not adult pulmonary), to obtain a new incidence/mortality estimate. Thus, if 20% of all TB in a given location is extrapulmonary or paediatric, the rough projected total TB incidence would be (projected TB incidence)/(0.8).

In this model, we consider latent TB infection to be asymptomatic and non-infectious, with a constant rate of reactivation and ongoing risk of exogenous reinfection leading to active TB; individuals successfully treated for TB are assumed to return to this compartment upon initiation of effective therapy (i.e., therapy that will result in completion, with no relapse for 2 years). Upon developing active TB, individuals enter a ‘pre-diagnostic’ phase that is characterized by a low level of infectiousness and mortality (equivalent to smear-negative TB) and during which individuals do not actively seek diagnosis. The duration of this phase (9 months) was selected a priori based on an existing model (Dowdy et al., 2013) in which the total duration of disease after incorporating this phase reflected the global ratio of prevalence to incidence, as estimated by the World Health Organization. We compared the total duration of disease to this ratio as part of our model validation and assumed that this ‘pre-diagnostic’ phase is much shorter for HIV-infected vs HIV-uninfected individuals. Upon completing this ‘pre-diagnostic’ phase, individuals progress to a diagnosis-seeking phase of active disease, which is characterized by separation into highly infectious (‘smear-positive’) and less infectious (‘smear-negative’) compartments. Among HIV-uninfected individuals, the highly infectious compartment also carries higher mortality risk. Diagnosis-seeking active TB implies active seeking of diagnosis at a defined rate; the probability that any single diagnostic attempt will result in effective therapy is calculated as a function of diagnostic sensitivity, probability of empiric therapy (i.e., without bacteriological confirmation), prior treatment status, and losses to follow-up, as described below. Each diagnostic attempt, if successful, leads either to effective therapy (which is initiated after a defined diagnostic delay) or to ineffective therapy (defined as leading to failure or default). In order to focus on differences between the nine selected strategies above in a tractable framework, we subsumed all other diagnostic tests and procedures (e.g., chest X-ray, antibiotic trials) as a probability of non-microbiologic diagnosis, without attempting to specify the associated cost or diagnostic delay. Once effective therapy is initiated, it is assumed to immediately render the individual non-infectious, with no residual risk of mortality. Upon initiation of ineffective therapy, individuals are assumed to remain infectious (at the ‘smear-negative’/less infectious level) for a defined period before either failing (followed by another round of therapy, which can be either appropriate/curative or ineffective) or default. Reasoning that default will occur, on average, at the midpoint between receipt of fully-ineffective and fully-effective therapy, half of defaulters are presumed to develop recurrent TB (which is assumed to occur immediately), while the other half return to the latent TB compartment (from which reactivation or reinfection remains possible). All individuals who relapse within 1 year are included as failures; thus, no specific parameter for relapse is incorporated. Individuals who are effectively treated, or whose disease is contained without therapy, return to the latent compartment following the convention of other TB models (Dye et al., 1998; Abu-Raddad et al., 2009).

### Role of HIV coinfection

As the goal of this model is to focus on TB-related interventions, HIV is modeled as occurring at a defined annual incidence, calibrated to achieve a given user-defined prevalence at baseline. We do not explicitly model HIV infection in dynamic fashion (i.e., the HIV incidence rate does not depend on the number of HIV-infected individuals in the model). HIV infection is assumed to affect all parameters related to TB disease, including the level of immune protection afforded by latent infection (assumed zero if HIV-infected), mortality rate (increased), rate of reactivation from latent TB (increased), duration of ‘pre-diagnostic’ TB (decreased), and risk of ‘primary’ progression to active disease upon infection (increased). For purposes of maintaining a simple model structure, we do not explicitly model CD4 counts or antiretroviral therapy (ART), but instead assume the global average of ART coverage, as estimated by UNAIDS (2012). We weight all HIV-related parameters according to this estimated probability of ART receipt; this probability can be modified by users.

### Drug resistance

We assume infection with TB strains of three different drug resistance levels: fully susceptible, INH-monoresistant, and MDR. Dual infection with multiple strains is not considered in this model, but superinfection (i.e., reinfection of a latently infected individual with a different strain, resulting in primary progression to disease with the reinfecting strain) is allowed, as is acquisition of resistance (i.e., change of strain from more susceptible to less susceptible) as a result of therapy.

### Individuals without TB

A key consideration with any TB diagnostic strategy is the role of the diagnostic test as applied to individuals who do not have TB (i.e., specificity). We included this element by considering that a small proportion of the population without TB would present with TB-like symptoms each year. This proportion (selected such that 10% of individuals being evaluated in the high-incidence setting actually have underlying TB) remains constant across all scenarios, such that the pre-test probability of TB is higher in settings of high TB incidence, and declines over time as successful TB control strategies are employed. Individuals without TB who are (inappropriately) treated for TB incur costs of TB therapy and are also marked as ‘previously treated’ for purposes of diagnostic evaluation in the future.

### Economic evaluation

Economic parameters are estimated using a unit-costing approach, whereby the unit cost of a TB diagnostic attempt and a TB treatment course (separately for first-line, category two, and second-line therapy) is enumerated under each scenario, and this cost is multiplied by the number of diagnostic attempts and treatment courses performed. For simplicity, we adopt the perspective of a TB control program for our costing; additional costs of HIV care and general health services (e.g., hospitalization) are not included. The decision tree below is used to estimate the cost per diagnostic attempt or treatment course, conditional on an individual's HIV, drug resistance, and previous treatment status. Individuals who default or die on therapy are assumed to incur half the cost of a treatment course. Given the short time horizon (5 years), the focus on costs and outcomes (rather than cost-effectiveness per se), and the desire to compare costs in year 1 and at the end of year 5 in equivalent terms, we did not discount future costs or outcomes for this analysis. All costs are reported in US dollars, assuming the year of costs that is specified by the user.

### Decision analysis: probability of diagnostic success

Under each scenario, we use decision analysis to ascertain the following quantities related to each diagnostic attempt:Probability of receiving successful treatment.Probability of receiving ineffective treatment (resulting in failure or default, including the probability of acquired resistance).Cost of treatment (conditional on whether treatment is successful or ineffective).Cost of diagnosis.Diagnostic delay incurred before treatment initiated.

These quantities are calculated conditional on each patient's infectious (smear) status, drug resistance status, HIV status, and prior treatment status. These probabilities are calculated for each diagnostic attempt, with the result fed back into the transmission model for purposes of appropriately allocating flows between compartments. Inputs into the decision model include the probabilities of failure/recurrence, probability of empiric therapy, loss to follow-up before treatment, diagnostic accuracy, diagnostic delay, and economic parameters as shown in Table 1. Outputs from the decision tree appear as parameters in the model, as described in Table 2 and the following equations.

**Table 2.**
 Model parameters and symbolic representations


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Representation</th>
      <th>Baseline value (see Table 1)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Transmission rate (transmission events per highly  infectious person-year)</td>
      <td>β</td>
      <td>Calibrated to TB incidence</td>
    </tr>
    <tr>
      <td>Proportional reduction in per-case transmission rate</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Drug-susceptible TB</td>
      <td>φ0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>Isoniazid-monoresistant TB</td>
      <td>φ1</td>
      <td>25%* of φ2</td>
    </tr>
    <tr>
      <td>MDR-TB</td>
      <td>φ2</td>
      <td>Calibrated</td>
    </tr>
    <tr>
      <td>HIV incidence rate, per year</td>
      <td>θ</td>
      <td>Calibrated to HIV prevalence</td>
    </tr>
    <tr>
      <td>Relative transmission rate from smear-negative/less  infectious TB</td>
      <td>ζ</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td>Proportion of pulmonary TB that is smear-positive/highly  infectious</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>ψ0</td>
      <td>0.63</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>ψ1</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>Endogenous reactivation rate, per year</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>ε0</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>ε1</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>Proportion of recent infections resulting in rapid  progression</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>π0</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>π1</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>Reduction in TB rapid progression probability due to  latent TB infection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>ι</td>
      <td>0.79</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>Not included</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Baseline mortality rate, per year</td>
      <td>μbl</td>
      <td>1/55 = 0.018</td>
    </tr>
    <tr>
      <td>Additional HIV-related mortality rate, per year</td>
      <td>μh</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>Additional untreated TB-related mortality rate, per year</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative, smear-positive/highly infectious</td>
      <td>μt1</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>HIV-negative, smear-negative/less infectious</td>
      <td>μt0</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>μth</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>Rate of spontaneous TB resolution, per year</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Smear-positive/highly infectious</td>
      <td>ν1</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>Smear-negative/less infectious</td>
      <td>ν0</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>Not included</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rate of starting diagnosis-seeking in active TB, per year</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>HIV-negative</td>
      <td>δe0</td>
      <td>1.33 (9 months)</td>
    </tr>
    <tr>
      <td>HIV-infected</td>
      <td>δe1</td>
      <td>12 (1/month)</td>
    </tr>
    <tr>
      <td>Rate of progression: ineffective therapy to repeat  therapy (failure) or active TB (relapse), per year</td>
      <td>δf</td>
      <td>6/12 = 0.5</td>
    </tr>
    <tr>
      <td>Rate of diagnostic evaluation for TB, per year</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Late active TB</td>
      <td>Input into decision tree</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>No active TB</td>
      <td>τ0</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>Decision tree outputs (in addition to unit costs):</td>
      <td></td>
      <td>Vary by intervention</td>
    </tr>
    <tr>
      <td>Successful diagnosis rate of late active TB, per year</td>
      <td>σhdip</td>
      <td></td>
    </tr>
    <tr>
      <td>Rate of movement from successful diagnosis to  treatment (1/diagnostic delay), per year</td>
      <td>ρhdip</td>
      <td></td>
    </tr>
    <tr>
      <td>Ineffective diagnosis rate of late active TB, per year</td>
      <td>κhdip</td>
      <td></td>
    </tr>
    <tr>
      <td>Rate of diagnosis and treatment leading to new  resistance, per year</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>susceptible to INH-monoresistant</td>
      <td>αsihip</td>
      <td></td>
    </tr>
    <tr>
      <td>susceptible to MDR</td>
      <td>αsmhip</td>
      <td></td>
    </tr>
    <tr>
      <td>INH-monoresistant to MDR</td>
      <td>αimhip</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Calculated such that (1−φ1) = 0.25*(1−φ2)._

### Outcomes and sensitivity analysis

Our primary outcomes under each scenario were TB incidence, TB mortality, MDR-TB incidence, and incremental TB diagnostic and treatment costs (during year 1 and at the end of the 5-year period) relative to the baseline strategy. By giving flexibility to change model inputs, we provide users the ability to conduct any sensitivity analysis desired. However, for illustrative purposes, we also conducted a series of one-way sensitivity analyses in which each model parameter in Table 1 was varied by ±50% of its listed value (for proportions, 50% of the difference between the value and either zero or one). Our primary outcome for sensitivity analysis was the change in TB incidence, comparing the ‘Xpert for all’ strategy to baseline in the high incidence setting.

We also conducted multivariable uncertainty analyses by calculating partial rank correlation coefficients (Kendall, 1942) between each natural history parameter and the outcomes of TB incidence, TB mortality, and 5-year costs. In addition, we constructed 95% uncertainty intervals around our estimates of outcomes in each individual country by simultaneously varying each model parameter by ±10% over a uniform distribution and each target value (i.e., TB incidence, HIV prevalence, and MDR-TB prevalence) over its reported uncertainty range. In this fashion, we constructed 10,000 simulations using Latin Hypercube Sampling (McKay et al., 1979) and took 95% uncertainty ranges as the 2.5th and 97.5th percentiles of outcomes in these simulations; these ranges are provided in the web-based version of the model for each country.

### Model equations

Rates of flow between compartments are governed by the system of ordinary differential equations listed in Equations 1–6.

We first define the forces of infection (according to resistance status) and total mortality for simplicity.

#### Forces of infection (λd)

$$
\lambda_{d}(t)=[\frac{\beta}{N(t)}]*\phi_{d}*{ζ*\sumh,p[E_{hdp}(t)+A_{hd0p}(t)+P_{hd0p}(t)+I_{hd0p}(t)]+\sumh,p[A_{hd1p}(t)+P_{hd1p}(t)]}
$$

Thus, TB infection is modelled as a density-dependent process, a function of the transmission rate (β), total number of individuals in the population N(t), number of individuals with ‘less infectious’ TB (E, early active; Ahd0p, late active smear-negative; Phd0p, ‘pre-treatment’ smear-negative; and I, active on ineffective treatment) weighted by the relative transmission rate ζ, and the number of individuals with fully infectious TB (Ahd1p, late active smear-positive; Phd1p, ‘pre-treatment’ smear-positive). Three separate forces of infection are calculated for the three separate strains of drug resistance, with relative transmission weights of φd. We use λtot to denote the sum of these three forces.

#### Total mortality (μtot)

$$
\mu_{tot}(t)=\mu_{bl}*N(t)+\mu_{h}*\sump{U_{1p}(t)+\sumd[L_{1dp}(t)+E_{1dp}(t)+\sumi(A_{1dip}(t)+P_{1dip}(t)+I_{1dip}(t))]}+\mu_{t0}*\sump,d{E_{0dp}(t)+A_{0d0p}(t)+P_{0d0p}(t)+\sumi(I_{0dip}(t))}+\mu_{t1}*\sump,h,d{A_{0d1p}(t)+P_{0d1p}(t)}+\mu_{th}*\sump,d{E_{1dp}(t)+\sumi(A_{1dip}(t)+P_{1dip}(t)+I_{1dip}(t))}
$$

Thus, total mortality is the sum of:baseline mortality μbl (experienced by all individuals N),HIV-associated mortality μh (experienced by all individuals with HIV, h = 1),‘less infectious’ (i.e., lower) TB-associated mortality μt0 (experienced by all HIV-uninfected individuals with early active TB, E, smear-negative active and ‘pre-treatment’ TB, A0d0p and P0d0p, and ineffectively treated TB, I0dip),‘highly infectious’ (i.e., higher) TB-associated mortality μt1 (experienced by all HIV-uninfected individuals with smear-positive active and ‘pre-treatment’ TB, A0d0p and P0d0p), andTB/HIV–associated mortality μth (experienced by all HIV-infected individuals with any form of TB).

### Uninfected compartment (U)

$$
\frac{dU_{hp}(t)}{dt}=I_{h=0,p=0}*\mu_{tot}(t)−[\lambda_{0}(t)+\lambda_{1}(t)+\lambda_{2}(t)+\mu_{bl}(t)]*U_{hp}(t)−I_{h=0}*[\theta*U_{0p}(t)]+I_{h=1}*[\theta*U_{0p}(t)−\mu_{h}*U_{1p}(t)]−I_{p=0}*[\tau_{0}*(1−s_{h})*U_{h0}(t)]+I_{p=1}*[\tau_{0}*(1−s_{h})*U_{h0}(t)]
$$

where μtot is the sum of all mortality (to maintain a constant population), λd is the force of infection for a given drug resistance strain, μbl is the baseline mortality rate, μh is the HIV-specific mortality rate, Ieq is an indicator function (= 1 if the condition eq is met, 0 otherwise), θ is the HIV incidence rate, τ0 is the rate of seeking diagnosis among people without TB, and sh is the specificity of the diagnostic test. Thus, uninfected individuals exit through infection and death, acquire HIV according to the HIV incidence rate, and become previously treated for TB (inappropriately) according to the specificity of the test. The HIV-uninfected, not previously treated compartment is replenished at a rate that matches total mortality and thereby maintains a constant population.

### Latently infected compartment (L)

$$
\frac{dL_{hdp}(t)}{dt}=\lambda_{d}(t)*(1−\pi_{h})*{U_{hp}(t)+\sumd[L_{hdp}(t)*(1−I_{h=0}*ι)]}+I_{p=1}*\sumi,p[ρ_{hdip}*P_{hdip}(t)]+I_{h=0}*{ν_{0}*E_{0dp}+\sumi[ν_{i}*(A_{0dip}+P_{0dip}+I_{0dip})]}−{[(\lambda_{0}(t)+\lambda_{1}(t)+\lambda_{2}(t))*(1−I_{h=0}*ι)+\epsilon_{h}+\mu_{bl}+I_{h=1}*\mu_{h}]*L_{hdp}(t)}−I_{h=0}*[\theta*L_{0dp}(t)]+I_{h=1}*[\theta*L_{0dp}(t)]
$$

where λd is the strain-specific force of infection, πh is the proportion of recent infections that progress rapidly to active TB, ι is the relative reduction in rapid progression after infection among people with latent TB, Ieq is an indicator function (= 1 if the condition eq is met, 0 otherwise), ρhdip is the rate of treatment after successful diagnosis is initiated, νi is the spontaneous recovery rate, εh is the endogenous reactivation rate, μbl is the baseline mortality rate, μh is the HIV-specific mortality rate, and θ is the HIV incidence rate. Thus, individuals enter the latently infected compartment through initial TB infection (without rapid progression), reinfection (without rapid progression, and accounting for immune protection), initiation of successful treatment, or spontaneous resolution. Individuals completing treatment only enter the previously treated compartment (p=1). Individuals exit this compartment through TB reinfection, endogenous reactivation, and death, and they acquire HIV infection at a constant rate.

### Early active compartment (E)

$$
\frac{dE_{hdp}(t)}{dt}=\lambda_{d}(t)*\pi_{h}*{U_{hp}(t)+\sumd[L_{hdp}(t)*(1−I_{h=0}*ι)]}+L_{hdp}(t)*\epsilon_{h}−{[\mu_{bl}+I_{h=0}*(\mu_{t0}+ν_{0}+\delta_{e0})+I_{h=1}*(\mu_{h}+\mu_{th}+\delta_{e1})]*E_{hdp}(t)}−I_{h=0}*[\theta*E_{0dp}(t)]+I_{h=1}*[\theta*E_{0dp}(t)]
$$

where λd is the force of infection, πh is the proportion of recent infections that progress rapidly to active TB, ι is the relative reduction in rapid progression after infection among people with latent TB, Ih=0 is an indicator function of HIV status (= 1 if h = 0, 0 otherwise), εh is the endogenous reactivation rate, μbl is the baseline mortality rate, μt0 is the TB-specific mortality rate for less-infectious TB, ν0 is the spontaneous recovery rate for less-infectious TB, δeh is the HIV-specific rate of progression to late active TB, μh is the HIV-specific mortality rate, μth is the TB-specific mortality rate for people living with HIV, and θ is the HIV incidence rate. Thus, individuals enter this compartment through rapid progression of recent infection or endogenous reactivation of latent infection. They exit through progression to late active disease, spontaneous cure (if HIV-uninfected), or death, and they acquire HIV infection at a constant rate.

### Late active compartment (A)

$$
\frac{dA_{hdip}(t)}{dt}=\delta_{eh}*[I_{i=1}*ψ_{h}+I_{i=0}*(1−ψ_{h})]*E_{hdp}(t)+\delta_{f}*I_{hdip}(t)−A_{hdip}(t)*[\mu_{bl}+I_{h=0}*(\mu_{ti}+ν_{i}+\sigma_{0dip}+κ_{0dip}+I_{d=0}*\alphasi_{0ip}+I_{d=0}*\alphasm_{0ip}+I_{d=1}*\alphaim_{0ip})+I_{h=1}*(\mu_{h}+\mu_{th}+\sigma_{1dip}+κ_{1dip}+I_{d=0}*\alphasi_{1ip}+I_{d=0}*\alphasm_{1ip}+I_{d=1}*\alphaim_{1ip})]−I_{h=0}*[\theta*A_{0dip}(t)]+I_{h=1}*[\theta*A_{0dip}(t)]
$$

where δeh is the rate of progression from early active TB, Ieq is an indicator function (= 1 if the condition eq is met, 0 otherwise), ψh is the proportion of active TB that is highly infectious (smear-positive), δf is the rate (1/duration) of ineffective therapy, μbl is the baseline mortality rate, μti is the TB-specific mortality rate for non-HIV-associated TB, μh is the HIV-specific mortality rate, μth is the TB-specific mortality rate for people living with HIV, νi is the spontaneous recovery rate, σhdip is the rate of diagnosis ultimately leading to successful treatment, κhdip is the rate of placing individuals on ineffective treatment that does not generate acquired resistance, αsihip is the rate of placing individuals on ineffective treatment that generates INH monoresistance, αsmhip and αimhip are the rates of placing individuals on ineffective treatment that generates MDR-TB, and θ is the HIV incidence rate. Thus, individuals enter this compartment through progression from early active disease or relapse/failure after ineffective treatment. They exit through spontaneous recovery, diagnosis leading to successful treatment, initiation of ineffective treatment (which can, in turn, generate acquired drug resistance), or death, and they acquire HIV infection at a constant rate.

### Active ‘pre-treatment’ compartment (P)

This compartment consists of individuals who have initiated a diagnostic attempt that will lead to successful treatment, yet remain infectious while awaiting initiation of treatment. Inclusion of this compartment is designed to capture the effects of diagnostic delays.

$$
\frac{dP_{hdip}(t)}{dt}=\sigma_{hdip}*A_{hdip}(t)−P_{hdip}(t)*[\mu_{bl}+I_{h=0}*(\mu_{ti}+ν_{i}+ρ_{0dip})+I_{h=1}*(\mu_{h}+\mu_{th}+ρ_{1dip})]−I_{h=0}*[\theta*P_{0dip}(t)]+I_{h=1}*[\theta*P_{0dip}(t)]
$$

where σhdip is the rate of initiating successful diagnostic attempts, Ih=0 is an indicator function of HIV status (= 1 if h = 0, 0 otherwise), μbl is the non-TB mortality rate, μti is the TB-specific mortality rate for non-HIV-associated TB, μh is the HIV-specific mortality rate, μth is the TB-specific mortality rate for people living with HIV, νi is the spontaneous recovery rate, ρhdip is the rate of starting therapy after initiating a successful diagnostic attempt (1/diagnostic delay), and θ is the HIV incidence rate. Thus, individuals enter this compartment by initiation of successful diagnostic attempts and exit through initiation of treatment, spontaneous cure, or death. They acquire HIV infection at a constant rate.

### Active ‘inappropriately treated’ compartment (I)

This compartment contains all individuals being treated whose treatment course ends in default or failure. Unlike the previous (successful treatment) compartment, diagnostic delay is not explicitly incorporated into this compartment, as to do so would prolong the duration of time until individuals who default re-enter the ‘late active’ compartment. Inclusion of a diagnostic delay before this compartment does not materially affect results. Individuals exit this compartment either in default after partial therapy—which has a defined probability of achieving cure despite not being completed—or failure. Failure leads immediately to another course of treatment, which can either be successful (i.e., transition to the latent compartment) or unsuccessful (i.e., remain in the inappropriate treatment compartment—which results in transition to the ‘previously treated’ compartment, p=1, not shown below).

$$
\frac{dI_{hdip}(t)}{dt}=κ_{hdip}*A_{hdip}(t)+I_{d=1}*\alphasi_{hdip}*A_{h0ip}(t)+I_{d=2}*[\alphasm_{hip}*A_{h0ip}(t)+\alphaim_{hip}*A_{h1ip}(t)]−I_{hdip}(t)*[\mu_{bl}+I_{h=0}*(\mu_{t0}+ν_{i}+\delta_{f})+I_{h=1}*(\mu_{h}+\mu_{th}+\delta_{f})]−I_{h=0}*[\theta*I_{0dip}(t)]+I_{h=1}*[\theta*I_{0dip}(t)]
$$

where κhdip is the rate of placing individuals on ineffective treatment that does not generate acquired resistance, αsihip is the rate of placing individuals on ineffective treatment that generates INH monoresistance from drug-susceptible TB, αsmhip is the rate of placing individuals on ineffective treatment that generates MDR-TB from drug-susceptible TB, αimhip is the rate of placing individuals on ineffective treatment that generates MDR-TB from INH-monoresistant TB, μbl is the non-TB mortality rate, μti is the TB-specific mortality rate for non-HIV-associated TB, μh is the HIV-specific mortality rate, μth is the TB-specific mortality rate for people living with HIV, νi is the spontaneous recovery rate, δf is the rate (1/duration) of ineffective therapy, and θ is the HIV incidence rate. Thus, individuals enter this compartment through ineffective treatment from the late active compartment (conditional on whether that treatment also generates new drug resistance) and exit through completion of a course of ineffective therapy, spontaneous resolution, or death. They acquire HIV infection at a constant rate.

### Model fitting

The equations above comprise a series of 100 ordinary differential equations. In order to generate an equilibrium population according to user specifications of TB incidence, MDR-TB prevalence, and HIV prevalence, it is necessary to solve for the roots of a system of these 100 equations, plus three additional equations to account for the user inputs. We accomplish this using the ‘fsolve’ routine in SciPy (www.scipy.org). To solve for these three additional equations, we first match each user input to a single parameter: TB incidence to the transmission rate β, MDR-TB prevalence to the relative reduction in transmission for MDR-TB φ2, and HIV prevalence to the HIV incidence rate θ. We then constrain the system of equations such that the total population remains constant at 100,000, and we add the following three equations to the system:

$$
d\beta/dt=(calculated TB incidence)−(user-defined TB incidence)
$$



$$
d\phi_{2}/dt=(calculated MDR-TB prevalence)−(user-defined MDR-TB prevalence)
$$



$$
d\theta/dt=(calculated HIV prevalence)−(user-defined HIV prevalence)
$$

By solving for the roots at which this system of equations equals zero, we generate an equilibrium (steady-state) population that also defines β, φ2, and θ such that the user-defined targets are also met.

Additional complexity is added to account for non-equilibrium in TB incidence and MDR-TB prevalence. We accomplish this by fitting an equilibrium defined by the user-specified target of HIV prevalence, and the user-specified ‘initial’ values of TB incidence and MDR-TB prevalence. This equilibrium is set to be 50 years in the past; at this time, the system of equations is solved as above. We then allow for the parameters β and φ2 to be altered from their original values (corresponding to the equilibrium condition) such that a second set of targets are attained after 50 years (start of the analysis). If these calculated values at the end of 50 years do not match the user-defined targets, the parameter values are changed accordingly, and the model is re-run from equilibrium until the appropriate parameter value is identified that generates the user-defined TB incidence and MDR-TB prevalence, within a relative tolerance of 0.05 in each variable. These parameters may then be further modified such that they change over the analysis frame of five years (e.g., to describe an epidemic with increasing MDR-TB prevalence over time).

In the primary version of the model, this is only automated for low-incidence scenarios in which the user inputs a TB incidence of less than 50 per 100,000/year. In such cases, the model generates an equilibrium population 50 years in the past with a TB incidence of 50 per 100,000/year and reduces the transmission parameter β until the user-defined TB incidence is achieved 50 years later (i.e., the start of the analytic period). This accounts for the fact that most low-incidence settings have substantially more latent TB infection than would be estimated by an equilibrium population with a very low TB incidence—thereby more appropriately reflecting a higher proportion of TB due to reactivation rather than recent infection. However, we include code (described in the user manual below) that allows users to define high incidence scenarios that are likewise not at equilibrium, as well as ‘emerging MDR’ scenarios in which the prevalence of MDR-TB is increasing rather than stable.
