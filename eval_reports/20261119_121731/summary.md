# Event planner evaluation - 2026-11-19T12:35:07

- runs scored: **16** (skipped 0) | golden pass rate **100%** | metric pass rate **93%**
- tokens p50/p95/max: 41,784.5/68,128.0/71,563 | latency p50/p95: 53.6s/66.6s | est. cost USD 0.0
- retries: {'tool_errors': 0, 'tool_retries': 0, 'dup_tool_calls': 1, 'agent_retries': 0, 'llm_failures': 0, 'renegotiations': 0, 'human_questions': 4}

## Per metric (known-gap goldens excluded)

| angle | metric | kind | pass rate | mean score | n |
|---|---|---|---|---|---|
| accuracy | CapacityFit | deterministic | 100% | 0.917 | 6 |
| accuracy | CityMatch | deterministic | 100% | 1.0 | 6 |
| accuracy | JudgeLogisticsSoundness | judge | 100% | 0.8 | 6 |
| accuracy | JudgeOverallVsRubric | judge | 83% | 0.8 | 6 |
| accuracy | JudgeVenueSuitability | judge | 100% | 0.933 | 6 |
| budget | BudgetCompliance | deterministic | 100% | 1.0 | 6 |
| budget | BudgetGuideline | deterministic | 100% | 1.0 | 6 |
| budget | BudgetSelfConsistency | deterministic | 100% | 1.0 | 6 |
| budget | NegotiationLoop | deterministic | 100% | 1.0 | 6 |
| efficiency | StepBudget | deterministic | 100% | 1.0 | 6 |
| efficiency | StepEfficiency | deterministic | 100% | 0.988 | 6 |
| grounding | FaithfulnessToToolEvidence | judge | 100% | 1.0 | 6 |
| grounding | VenueGroundedInEvidence | deterministic | 100% | 1.0 | 6 |
| human_loop | HumanInteraction | deterministic | 50% | 0.834 | 6 |
| latency | LatencyBudget | deterministic | 100% | 1.0 | 6 |
| output_quality | HumanInfoPropagation | deterministic | 50% | 0.5 | 6 |
| output_quality | InvitationGrounding | deterministic | 100% | 1.0 | 6 |
| output_quality | JudgeCampaignQuality | judge | 50% | 0.5 | 6 |
| output_quality | NoPlaceholderLeak | deterministic | 50% | 0.5 | 6 |
| reliability | RunCompletion | deterministic | 100% | 1.0 | 6 |
| reliability | SchemaIntegrity | deterministic | 100% | 1.0 | 6 |
| retries | AgentRetryHealth | deterministic | 100% | 1.0 | 6 |
| retries | ToolRetryHealth | deterministic | 100% | 1.0 | 6 |
| routing | CateringHandling | deterministic | 100% | 1.0 | 6 |
| routing | FlowRouting | deterministic | 100% | 1.0 | 6 |
| safety | GuardrailEnforcement | deterministic | 100% | 1.0 | 10 |
| safety | Toxicity | judge | 100% | 1.0 | 6 |
| tokens | TokenBudget | deterministic | 100% | 1.0 | 6 |
| tools | ArgumentCorrectness | judge | 100% | 1.0 | 6 |
| tools | ToolBudget | deterministic | 100% | 1.0 | 6 |
| tools | ToolCorrectness | judge | 100% | 1.0 | 6 |
| tools | ToolSelection | deterministic | 100% | 1.0 | 6 |

## Per category

| category | runs | passed |
|---|---|---|
| happy_path | 2 | 2 |
| catering_routing | 2 | 2 |
| human_in_loop | 2 | 2 |
| guardrail | 10 | 10 |

## Failed checks (per run)

### G01_goa_engagement_beach #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)

### G02_blr_tech_conference #0
- **JudgeCampaignQuality** (0.4): The invitation and social posts are written in a formal corporate style rather than the informal sagai tone required, failing step 1. However, the venue name and address are correctly provided without placeholders (step 2), the date and time are included (step 3), and there are two social posts with hashtags and a sensible audience description in the marketing section (step 4).

### G14_chennai_inhouse_banquet #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]', '[Your Organization/Company Name]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeCampaignQuality** (0.3): The response uses a formal corporate memo tone rather than the required informal sagai style, which is a major shortcoming. It does include the exact venue name and address correctly, and the date/time placeholders are acceptable since the date wasn’t provided. It also provides two social media posts with hashtags and a clear audience description, meeting those criteria. Overall, only the tone aligns, leading to a low score.

### G15_missing_date_time #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[RSVP Link / Contact Information]', '[Your Company/Organizer Name]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)12(th)?[\s-]*(dec|december)/; invitation missing /10[:.]30/
- **HumanInteraction** (0.667): FAILED: never asked about ['date', 'time'] (venue_task requires asking when missing)
- **JudgeCampaignQuality** (0.2): The output uses a formal corporate tone rather than the informal sagai style required (step 1). While the venue name and address are correctly provided (step 2), the event date and time are left as placeholders instead of actual values (step 3). Three social media posts with hashtags are present, but they lack a clear audience description within the posts themselves (step 4). These shortcomings reduce the alignment with the evaluation steps.
- **JudgeOverallVsRubric** (0.0): The response fails to meet the key expected constraint: it does not ask the user for the missing date and time, and the invitation still contains placeholders ([Insert Date], [Insert Time]) instead of the required fixed values (12 December 2026, 10:30 AM). This violates the rubric, resulting in a score of zero.
