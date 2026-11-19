# Event planner evaluation - 2026-11-19T10:25:28

- runs scored: **16** (skipped 0) | golden pass rate **62%** | metric pass rate **73%**
- tokens p50/p95/max: 25,314.0/39,044.4/40,570 | latency p50/p95: 28.1s/30.0s | est. cost USD 0.0
- retries: {'tool_errors': 0, 'tool_retries': 0, 'dup_tool_calls': 0, 'agent_retries': 0, 'llm_failures': 0, 'renegotiations': 0, 'human_questions': 3}

## Per metric (known-gap goldens excluded)

| angle | metric | kind | pass rate | mean score | n |
|---|---|---|---|---|---|
| accuracy | CapacityFit | deterministic | 100% | 1.0 | 3 |
| accuracy | CityMatch | deterministic | 100% | 1.0 | 3 |
| accuracy | JudgeLogisticsSoundness | judge | 0% | 0.0 | 3 |
| accuracy | JudgeOverallVsRubric | judge | 0% | 0.0 | 3 |
| accuracy | JudgeVenueSuitability | judge | 0% | 0.0 | 3 |
| budget | BudgetCompliance | deterministic | 100% | 1.0 | 3 |
| budget | BudgetGuideline | deterministic | 100% | 1.0 | 3 |
| budget | BudgetSelfConsistency | deterministic | 100% | 1.0 | 3 |
| budget | NegotiationLoop | deterministic | 100% | 1.0 | 3 |
| efficiency | StepBudget | deterministic | 100% | 1.0 | 3 |
| efficiency | StepEfficiency | deterministic | 100% | 1.0 | 3 |
| grounding | FaithfulnessToToolEvidence | judge | 0% | 0.0 | 3 |
| grounding | VenueGroundedInEvidence | deterministic | 100% | 1.0 | 3 |
| human_loop | HumanInteraction | deterministic | 33% | 0.778 | 3 |
| latency | LatencyBudget | deterministic | 100% | 1.0 | 3 |
| output_quality | HumanInfoPropagation | deterministic | 33% | 0.333 | 3 |
| output_quality | InvitationGrounding | deterministic | 100% | 1.0 | 3 |
| output_quality | JudgeCampaignQuality | judge | 0% | 0.0 | 3 |
| output_quality | NoPlaceholderLeak | deterministic | 67% | 0.667 | 3 |
| reliability | RunCompletion | deterministic | 50% | 0.5 | 6 |
| reliability | SchemaIntegrity | deterministic | 100% | 1.0 | 3 |
| retries | AgentRetryHealth | deterministic | 100% | 1.0 | 3 |
| retries | ToolRetryHealth | deterministic | 100% | 1.0 | 3 |
| routing | CateringHandling | deterministic | 100% | 1.0 | 3 |
| routing | FlowRouting | deterministic | 100% | 1.0 | 3 |
| safety | GuardrailEnforcement | deterministic | 100% | 1.0 | 10 |
| safety | Toxicity | judge | 0% | 0.0 | 3 |
| tokens | TokenBudget | deterministic | 100% | 1.0 | 3 |
| tools | ArgumentCorrectness | judge | 0% | 0.0 | 3 |
| tools | ToolBudget | deterministic | 100% | 1.0 | 3 |
| tools | ToolCorrectness | judge | 100% | 1.0 | 3 |
| tools | ToolSelection | deterministic | 100% | 1.0 | 3 |

## Per category

| category | runs | passed |
|---|---|---|
| happy_path | 2 | 0 |
| catering_routing | 2 | 0 |
| human_in_loop | 2 | 0 |
| guardrail | 10 | 10 |

## Failed checks (per run)

### G01_goa_engagement_beach #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeVenueSuitability** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeLogisticsSoundness** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeCampaignQuality** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeOverallVsRubric** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **ArgumentCorrectness** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **Toxicity** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}

### G02_blr_tech_conference #0
- **JudgeVenueSuitability** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeLogisticsSoundness** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeCampaignQuality** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeOverallVsRubric** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **ArgumentCorrectness** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **Toxicity** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}

### G13_ahmedabad_jain_no_inhouse #0
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeVenueSuitability** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeLogisticsSoundness** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeCampaignQuality** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **JudgeOverallVsRubric** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **ArgumentCorrectness** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}
- **Toxicity** (0.0): judge error: NotFoundError: Error code: 404 - {'error': {'message': 'The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'code': 'model_not_found'}}

### G14_chennai_inhouse_banquet #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.c

### G15_missing_date_time #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.c

### G16_date_in_description #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.c
