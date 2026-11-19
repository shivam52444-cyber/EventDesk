# Event planner evaluation - 2026-11-19T10:00:12

- runs scored: **16** (skipped 0) | golden pass rate **62%** | metric pass rate **74%**
- tokens p50/p95/max: 38,617.5/66,171.2/68,866 | latency p50/p95: 28.2s/29.3s | est. cost USD 0.0
- retries: {'tool_errors': 0, 'tool_retries': 0, 'dup_tool_calls': 0, 'agent_retries': 2, 'llm_failures': 7, 'renegotiations': 0, 'human_questions': 2}

## Per metric (known-gap goldens excluded)

| angle | metric | kind | pass rate | mean score | n |
|---|---|---|---|---|---|
| accuracy | CapacityFit | deterministic | 100% | 1.0 | 4 |
| accuracy | CityMatch | deterministic | 100% | 1.0 | 4 |
| accuracy | JudgeLogisticsSoundness | judge | 25% | 0.175 | 4 |
| accuracy | JudgeOverallVsRubric | judge | 0% | 0.0 | 4 |
| accuracy | JudgeVenueSuitability | judge | 0% | 0.0 | 4 |
| budget | BudgetCompliance | deterministic | 100% | 1.0 | 4 |
| budget | BudgetGuideline | deterministic | 100% | 1.0 | 4 |
| budget | BudgetSelfConsistency | deterministic | 100% | 1.0 | 4 |
| budget | NegotiationLoop | deterministic | 100% | 1.0 | 4 |
| efficiency | StepBudget | deterministic | 100% | 1.0 | 4 |
| efficiency | StepEfficiency | deterministic | 75% | 0.842 | 4 |
| grounding | FaithfulnessToToolEvidence | judge | 0% | 0.0 | 4 |
| grounding | VenueGroundedInEvidence | deterministic | 100% | 1.0 | 4 |
| human_loop | HumanInteraction | deterministic | 75% | 0.917 | 4 |
| latency | LatencyBudget | deterministic | 100% | 1.0 | 4 |
| output_quality | HumanInfoPropagation | deterministic | 75% | 0.75 | 4 |
| output_quality | InvitationGrounding | deterministic | 100% | 1.0 | 4 |
| output_quality | JudgeCampaignQuality | judge | 0% | 0.0 | 4 |
| output_quality | NoPlaceholderLeak | deterministic | 75% | 0.75 | 4 |
| reliability | RunCompletion | deterministic | 67% | 0.667 | 6 |
| reliability | SchemaIntegrity | deterministic | 100% | 1.0 | 4 |
| retries | AgentRetryHealth | deterministic | 50% | 0.75 | 4 |
| retries | ToolRetryHealth | deterministic | 100% | 1.0 | 4 |
| routing | CateringHandling | deterministic | 100% | 1.0 | 4 |
| routing | FlowRouting | deterministic | 100% | 1.0 | 4 |
| safety | GuardrailEnforcement | deterministic | 100% | 1.0 | 10 |
| safety | Toxicity | judge | 0% | 0.0 | 4 |
| tokens | TokenBudget | deterministic | 100% | 1.0 | 4 |
| tools | ArgumentCorrectness | judge | 0% | 0.0 | 4 |
| tools | ToolBudget | deterministic | 100% | 1.0 | 4 |
| tools | ToolCorrectness | judge | 100% | 1.0 | 4 |
| tools | ToolSelection | deterministic | 100% | 1.0 | 4 |

## Per category

| category | runs | passed |
|---|---|---|
| happy_path | 2 | 0 |
| catering_routing | 2 | 0 |
| human_in_loop | 2 | 0 |
| guardrail | 10 | 10 |

## Failed checks (per run)

### G01_goa_engagement_beach #0
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeVenueSuitability** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeLogisticsSoundness** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeCampaignQuality** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeOverallVsRubric** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **FaithfulnessToToolEvidence** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **ArgumentCorrectness** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **Toxicity** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe

### G02_blr_tech_conference #0
- **AgentRetryHealth** (0.667): FAILED: 2 LLM call failures > 1
- **JudgeVenueSuitability** (0.0): judge error: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- **JudgeLogisticsSoundness** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeCampaignQuality** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeOverallVsRubric** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **FaithfulnessToToolEvidence** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **ArgumentCorrectness** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **Toxicity** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe

### G13_ahmedabad_jain_no_inhouse #0
- **RunCompletion** (0.0): exception / KeyboardInterrupt: KeyboardInterrupt: 

### G14_chennai_inhouse_banquet #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Your Organization/Company Name]']
- **JudgeVenueSuitability** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeLogisticsSoundness** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeCampaignQuality** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeOverallVsRubric** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **FaithfulnessToToolEvidence** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **ArgumentCorrectness** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **Toxicity** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe

### G15_missing_date_time #0
- **RunCompletion** (0.0): exception / KeyboardInterrupt: KeyboardInterrupt: 

### G16_date_in_description #0
- **AgentRetryHealth** (0.333): FAILED: 2 agent retries > 1; 5 LLM call failures > 1
- **StepEfficiency** (0.5): 14 steps; wasted = 0 duplicate calls + 0 tool errors + 5 LLM failures + 2 agent retries
- **JudgeVenueSuitability** (0.0): judge error: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- **JudgeCampaignQuality** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **JudgeOverallVsRubric** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **FaithfulnessToToolEvidence** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **ArgumentCorrectness** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
- **Toxicity** (0.0): judge error: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-4-hydrogen, description: Generate content requests pe
