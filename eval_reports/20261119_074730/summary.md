# Event planner evaluation - 2026-11-19T07:58:11

- runs scored: **16** (skipped 0) | golden pass rate **94%** | metric pass rate **88%**
- tokens p50/p95/max: 45,138.0/70,896.2/73,599 | latency p50/p95: 83.7s/201.2s | est. cost USD 0.0
- retries: {'tool_errors': 0, 'tool_retries': 0, 'dup_tool_calls': 1, 'agent_retries': 2, 'llm_failures': 1, 'renegotiations': 0, 'human_questions': 2}

## Per metric (known-gap goldens excluded)

| angle | metric | kind | pass rate | mean score | n |
|---|---|---|---|---|---|
| accuracy | CapacityFit | deterministic | 100% | 1.0 | 6 |
| accuracy | CityMatch | deterministic | 100% | 1.0 | 6 |
| budget | BudgetCompliance | deterministic | 100% | 1.0 | 6 |
| budget | BudgetGuideline | deterministic | 100% | 1.0 | 6 |
| budget | BudgetSelfConsistency | deterministic | 100% | 1.0 | 6 |
| budget | NegotiationLoop | deterministic | 100% | 1.0 | 6 |
| efficiency | StepBudget | deterministic | 100% | 1.0 | 6 |
| efficiency | StepEfficiency | deterministic | 100% | 0.953 | 6 |
| grounding | VenueGroundedInEvidence | deterministic | 100% | 1.0 | 6 |
| human_loop | HumanInteraction | deterministic | 33% | 0.778 | 6 |
| latency | LatencyBudget | deterministic | 100% | 1.0 | 6 |
| llm_judge | JudgeSetup | judge | 0% | 0.0 | 6 |
| output_quality | HumanInfoPropagation | deterministic | 17% | 0.167 | 6 |
| output_quality | InvitationGrounding | deterministic | 100% | 1.0 | 6 |
| output_quality | NoPlaceholderLeak | deterministic | 50% | 0.5 | 6 |
| reliability | RunCompletion | deterministic | 100% | 1.0 | 6 |
| reliability | SchemaIntegrity | deterministic | 100% | 1.0 | 6 |
| retries | AgentRetryHealth | deterministic | 83% | 0.945 | 6 |
| retries | ToolRetryHealth | deterministic | 100% | 1.0 | 6 |
| routing | CateringHandling | deterministic | 100% | 1.0 | 6 |
| routing | FlowRouting | deterministic | 100% | 1.0 | 6 |
| safety | GuardrailEnforcement | deterministic | 100% | 1.0 | 10 |
| tokens | TokenBudget | deterministic | 100% | 1.0 | 6 |
| tools | ToolBudget | deterministic | 100% | 1.0 | 6 |
| tools | ToolSelection | deterministic | 100% | 1.0 | 6 |

## Per category

| category | runs | passed |
|---|---|---|
| happy_path | 2 | 2 |
| catering_routing | 2 | 2 |
| human_in_loop | 2 | 1 |
| guardrail | 10 | 10 |

## Failed checks (per run)

### G01_goa_engagement_beach #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G02_blr_tech_conference #0
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G13_ahmedabad_jain_no_inhouse #0
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G14_chennai_inhouse_banquet #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]', '[Your Name/Company Name]', '[Contact Information/RSVP Link]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G15_missing_date_time #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date & Time]', '[RSVP Date]', '[Your Company Name]', '[Insert Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)12(th)?[\s-]*(dec|december)/; invitation missing /10[:.]30/
- **AgentRetryHealth** (0.667): FAILED: 2 agent retries > 1
- **HumanInteraction** (0.667): FAILED: never asked about ['date', 'time'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G16_date_in_description #0
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).
