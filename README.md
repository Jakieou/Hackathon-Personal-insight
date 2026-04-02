# Hackathon-Personal-insight
### Dynamic Misalignment Between Policy, Public Trust, and Pandemic Outcomes

---

## Project Overview

This project studies the relationship between government policy, public trust, and real-world outcomes, with a focus on identifying and understanding the mismatch (gap) between policy actions and public perception. Rather than only analyzing policy effectiveness or trust separately, this project emphasizes whether policy and public trust adjust synchronously, and what happens when they do not.

If, in the future, the government continues to make rapid policy adjustments in response to crises while public trust fails to keep pace, the costs of policy implementation, public resistance, and the risk of a mismatch between policy and public perception will all increase. It suggests that future governance should focus not only on policy effectiveness, but also on the alignment between policy timing and public trust, since unmanaged mismatch may undermine policy acceptance and long-run effectiveness.

---

## Analytical Framework

The project is structured into three main components:

### 1. Dynamic Mechanism (VAR / IRF)

We examine how pandemic shocks (cases and deaths) dynamically affect policy response and public trust.

The focus is on understanding the timing and direction of responses:

- how policy reacts to shocks  
- how trust responds to both shocks and policy  
- whether these adjustments are synchronized  

---

### 2. Gap Measurement

We construct a policy–trust gap to quantify the mismatch between policy intensity and public trust.

This measure allows us to:

- capture the extent of misalignment  
- identify periods when mismatch is most severe  

---

### 3. 2×2 Structural Framework

We categorize the system into four states:

| Policy Effectiveness | Public Trust | Interpretation |
|--------------------|-------------|----------------|
| High               | High        | Ideal alignment |
| High               | Low         | Effective policy but low acceptance |
| Low                | High        | Perception bias or lagged belief |
| Low                | Low         | Policy and trust both fail |

---

## Data and Variables

This project uses daily data for the United Kingdom.

Variables include:

**Trust (Y)**  
- Source: YouGov  
- Interpretation: public confidence in government pandemic response  

**Policy Stringency (X)**  
- Source: Our World in Data  
- Interpretation: government restriction intensity (0–100)  

**Death Rate**  
- Source: Our World in Data  
- Interpretation: deaths per million  

**New Case Rate**  
- Source: Our World in Data  
- Interpretation: cases per million  

**Vaccination Rate (optional extension)**  
- Source: Our World in Data  

All data are aligned to daily frequency and processed (e.g., differencing and normalization).

---

## Method Objective

The goal is to identify how policy, trust, and real-world shocks interact dynamically, and to determine whether systematic misalignment exists between policy actions and public perception.

---

## Key Findings

### 1. Shock → Policy Response  
Rising deaths or cases lead to stricter policy.  
Government behavior is reactive.

### 2. Policy → Outcome  
Policy tightening reduces pandemic spread.  
Policies are effective in controlling outcomes.

### 3. Policy and Outcome → Trust  
Worsening pandemic reduces trust.  
Policy tightening also reduces trust in the short run.

---

## Mechanism

The dynamic process can be summarized as:

```
Pandemic shock increases  
→ policy tightens  
→ outcomes improve  
→ trust declines in the short run  
```

The key feature is that policy and trust do not adjust synchronously.

---

## Key Insight

Policy reacts quickly to changes in pandemic severity, while public trust adjusts more slowly and often negatively in the short term. This creates a structural misalignment between policy actions and public perception.

---

## Reusable Framework

This project proposes a general analytical pipeline:

1. Problem definition (policy–perception mismatch)  
2. Data construction (policy, outcome, trust)  
3. Dynamic analysis (VAR / IRF)  
4. Gap measurement  
5. Structural classification (2×2 framework)  
6. Driver identification (regression analysis)  
7. Policy application (adjust timing and communication)  

---

## Applications

This framework can be applied to multiple domains:

- Public health policy  
- Education reform  
- Environmental regulation  
- Urban governance  
- Organizational or corporate policy  

---

## Core Message

This project focuses not only on policy or trust individually, but on the dynamic misalignment between them, and provides a reusable framework for identifying, measuring, and analyzing such mismatch across different policy contexts.

## Notes on AI Assistance

The project design, analytical framework, and overall structure were independently developed.  
AI tools were used only for debugging support and minor writing refinement in the README.
