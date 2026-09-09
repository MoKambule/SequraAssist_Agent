---
title: "SecuraQ — Design Document"
subtitle: "AI-Assisted Security Testing Prioritisation"
---

# 1. Architecture

**Purpose:** SecuraQ does not replace security testing tools. It helps users decide what to test, understand the results, and know what to prioritise.

## System Flow

```
User
 -> Streamlit Dashboard
 -> Business Context (questionnaire)
 -> Risk Assessment
 -> AI Agent
 -> Test Recommendations
 -> Security Testing Tools (OWASP ZAP, Semgrep, Trivy)
 -> Security Findings
 -> AI Agent: Finding Analysis
 -> Risk Prioritisation
 -> Recommendations
 -> back to Dashboard
```

## Components

| Component           | Responsibility 
|---------------------|---------------------------------------------                                                            
| Streamlit Dashboard | Interface for input and results 
| Business Context    | Collects application/business information 
| Risk Assessment     | Scores risk from collected context 
| AI Agent            | Interprets context, recommends tests, analyses findings, prioritises, recommends actions 
| Security Tools      | OWASP ZAP, Semgrep, Trivy — perform technical checks 
| Finding Analysis    | Converts technical output into plain language 
| Risk Prioritisation | Ranks findings by business impact 
| Recommendations     | Suggested next actions for the user 

---

# 2. User Journey

| Step                    | What Happens 
|-------------------------|---------------------------------------------------
| 1. Start                | User opens SecuraQ 
| 2. Business Context     | User answers a short questionnaire about the application 
| 3. Risk Assessment      | SecuraQ returns an overall risk rating (e.g. `HIGH`) with a reason 
| 4. Test Recommendations | SecuraQ prioritises what to test first (e.g. Authentication → Authorization → API → Input Validation) 
| 5. Run Tests            | ZAP / Semgrep / Trivy execute the technical checks 
| 6. Findings             | Tools return raw technical results 
| 7. AI Analysis          | AI Agent explains what the findings mean in plain language 
| 8. Prioritisation       | Findings sorted into `Fix First` / `Fix Next` / `Monitor` 
| 9. Recommendations      | User receives clear next steps 

```
Start -> Business Context -> Risk Assessment -> Test Recommendations
      -> Run Tests -> Findings -> AI Analysis -> Prioritise -> Recommendations
```

---

# 3. Business Context (Questionnaire)

| Category | Question | Why It Matters |
|---|---|---|
| Application | What type of application is it? (Web / API / Mobile / Backend) | Determines which tools and test types apply |
| Exposure | Is it internet-facing or internal? | Public exposure raises likelihood of attack |
| Authentication | Does it require login? What method? Multiple roles? | Weak auth enables unauthorised access; roles imply authorization testing |
| Data | Does it handle personal, sensitive, or financial data? | Higher data sensitivity raises impact of a breach |
| Business Importance | Is it business-critical? How many users affected if down? | Determines business impact of failure |
| Technology | Language, framework, database, container usage | Determines applicable scanners (e.g. Trivy for containers) |

MVP note: not every question above needs to ship first — start with Application, Exposure, Authentication, Data.

---

# 4. Risk & Testing Logic

**Model:** `Risk = Likelihood × Impact`

Inputs: exposure, likelihood, technical impact, business impact, data sensitivity, application importance.

**Levels:** `LOW` · `MEDIUM` · `HIGH` · `CRITICAL`

**Example:** The same vulnerability on a 20-user internal tool vs. a public app with 50,000 users and financial data carries very different business risk — this is where SecuraQ adds value over raw scan output.

## Context → Test Priority Mapping

| Context Signal | Priority Area |
|---|---|
| Login required | Authentication |
| Multiple user roles | Authorization |
| Public API | API Security |
| Sensitive data | Access Control / Data Protection |
| Internet-facing | Configuration / Authentication / API |
| Accepts user input | Input Validation |
| Financial transactions | Business Logic |

Mapped against the **OWASP Web Security Testing Guide (WSTG)**.

## Tooling

| Tool | Role |
|---|---|
| OWASP ZAP | Web application / API security testing |
| Semgrep | Source-code security analysis |
| Trivy | Dependency, container, and IaC vulnerabilities |

```
OWASP WSTG        -> What should we test?
SecuraQ           -> What should we test first, and why?
ZAP / Semgrep / Trivy -> Perform the technical checks
```

---

# 5. AI Agent Design

The AI agent is not one step in the pipeline — it operates across the workflow: interpreting context, recommending tests, analysing findings, prioritising, and recommending actions.

| Responsibility | Description |
|---|---|
| Understand context | Reads business/application answers, identifies what matters |
| Interpret risk | Explains *why* the app carries a given risk level |
| Recommend tests | Maps context + risk to a prioritised test list |
| Analyse findings | Translates technical findings into plain language |
| Connect to business impact | Links a technical finding to a business consequence |
| Prioritise | Answers "what do we fix first?" |
| Recommend actions | Gives concrete next steps |

**Example — Finding → Business Meaning:**

| Field | Value |
|---|---|
| Technical finding | Broken Access Control |
| Business meaning | An attacker may access another customer's data |
| Business impact | Data exposure, loss of customer trust |
| Priority | HIGH |

---

# 6. Analysis + Recommendations Module (Claude API)

## What It Does

Takes the **combined tool findings** (ZAP + Semgrep + Trivy output) and the **business context** (from the questionnaire) and returns a single plain-language "here's what this means" output — the bridge between raw scan data and a decision a non-technical stakeholder can act on.

## Where It Sits in the Flow

```
Security Findings (ZAP/Semgrep/Trivy) ─┐
                                        ├─> Claude API (Analysis + Recommendations) -> Dashboard Output
Business Context (risk, data, exposure)┘
```

This replaces/powers the "AI Analysis," "Risk Prioritisation," and "Recommendations" steps in the user journey (Steps 7–9) with a single API call.

## Input Payload (structure)

```json
{
  "business_context": {
    "app_type": "Web application",
    "internet_facing": true,
    "authentication": "Username/password, single role",
    "handles_sensitive_data": true,
    "handles_financial_data": false,
    "business_critical": true,
    "estimated_users": 5000
  },
  "risk_assessment": {
    "overall_risk": "HIGH",
    "reason": "Internet-facing app handling sensitive data with single-factor auth"
  },
  "findings": [
    {
      "tool": "OWASP ZAP",
      "finding": "Broken Access Control",
      "severity": "High",
      "location": "/api/user/profile"
    },
    {
      "tool": "Trivy",
      "finding": "Outdated dependency with known CVE",
      "severity": "Medium",
      "location": "package.json"
    }
  ]
}
```

## Output Contract (structure)

Instruct the model to return **JSON only**, no preamble:

```json
{
  "summary": "Plain-language overview of overall security posture",
  "prioritised_findings": [
    {
      "finding": "Broken Access Control",
      "plain_language_meaning": "An attacker may access another customer's data",
      "business_impact": "Data exposure and loss of customer trust",
      "priority": "Fix First",
      "recommended_action": "Add server-side authorization checks on all user-data endpoints"
    }
  ],
  "overall_recommendation": "Short next-step summary for the user"
}
```

## Prompt Design

**System prompt:**

```
You are a security analyst assistant. You translate technical security
findings into plain-language explanations for a business audience.

Rules:
- Never invent findings that were not provided.
- Always connect each finding to a concrete business consequence.
- Prioritise using the provided business context, not severity scores alone
  (e.g. a Medium finding on a financial, internet-facing app can outrank a
  High finding on a low-impact internal tool).
- Classify every finding as one of: "Fix First", "Fix Next", "Monitor".
- Output valid JSON only. No markdown, no commentary, no preamble.
```

**User message (templated):**

```
Business context:
{business_context_json}

Risk assessment:
{risk_assessment_json}

Findings:
{findings_json}

Return the analysis in the required JSON schema.
```

## Example API Call

```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "claude-sonnet-4-6",
    max_tokens: 1000,
    system: SYSTEM_PROMPT,
    messages: [
      { role: "user", content: buildUserPrompt(businessContext, riskAssessment, findings) }
    ]
  })
});

const data = await response.json();
const raw = data.content.find(b => b.type === "text")?.text ?? "";
const clean = raw.replace(/```json|```/g, "").trim();
const analysis = JSON.parse(clean);
```

## Design Notes

- **Deterministic priority logic stays in code** (the context→priority mapping in Section 4); the model's job is *explanation and synthesis*, not deciding risk from scratch — this keeps output auditable.
- **One call per scan cycle**, not per finding — cheaper, and lets the model weigh findings against each other for prioritisation.
- **Parse defensively**: strip code fences before `JSON.parse`, wrap in try/catch, fall back to showing raw findings if parsing fails.
