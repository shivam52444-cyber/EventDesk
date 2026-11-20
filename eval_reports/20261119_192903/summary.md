# Event planner evaluation - 2026-11-19T22:26:17

- runs scored: **102** (skipped 12) | golden pass rate **37%** | metric pass rate **65%**
- tokens p50/p95/max: 72,128.5/229,621.3/258,064 | latency p50/p95: 204.1s/500.8s | est. cost USD 0.0
- retries: {'tool_errors': 2, 'tool_retries': 2, 'dup_tool_calls': 1, 'agent_retries': 2, 'llm_failures': 1, 'renegotiations': 0, 'human_questions': 12}

## Per metric (known-gap goldens excluded)

| angle | metric | kind | pass rate | mean score | n |
|---|---|---|---|---|---|
| accuracy | CapacityFit | deterministic | 100% | 1.0 | 8 |
| accuracy | CityMatch | deterministic | 100% | 1.0 | 8 |
| accuracy | JudgeLogisticsSoundness | judge | 12% | 0.113 | 8 |
| accuracy | JudgeOverallVsRubric | judge | 0% | 0.062 | 8 |
| accuracy | JudgeVenueSuitability | judge | 62% | 0.588 | 8 |
| budget | BudgetCompliance | deterministic | 100% | 1.0 | 8 |
| budget | BudgetGuideline | deterministic | 100% | 1.0 | 8 |
| budget | BudgetSelfConsistency | deterministic | 100% | 1.0 | 8 |
| budget | NegotiationLoop | deterministic | 100% | 1.0 | 8 |
| efficiency | StepBudget | deterministic | 100% | 1.0 | 8 |
| efficiency | StepEfficiency | deterministic | 100% | 0.957 | 8 |
| grounding | FaithfulnessToToolEvidence | judge | 12% | 0.125 | 8 |
| grounding | VenueGroundedInEvidence | deterministic | 100% | 1.0 | 8 |
| human_loop | HumanInteraction | deterministic | 75% | 0.917 | 8 |
| latency | LatencyBudget | deterministic | 100% | 1.0 | 8 |
| output_quality | HumanInfoPropagation | deterministic | 75% | 0.75 | 8 |
| output_quality | InvitationGrounding | deterministic | 100% | 1.0 | 8 |
| output_quality | JudgeCampaignQuality | judge | 0% | 0.0 | 8 |
| output_quality | NoPlaceholderLeak | deterministic | 62% | 0.625 | 8 |
| reliability | RunCompletion | deterministic | 13% | 0.127 | 63 |
| reliability | SchemaIntegrity | deterministic | 100% | 1.0 | 8 |
| resilience | FaultResilience | deterministic | 11% | 0.695 | 9 |
| retries | AgentRetryHealth | deterministic | 88% | 0.917 | 8 |
| retries | ToolRetryHealth | deterministic | 100% | 1.0 | 8 |
| routing | CateringHandling | deterministic | 100% | 1.0 | 8 |
| routing | FlowRouting | deterministic | 100% | 1.0 | 8 |
| safety | GuardrailEnforcement | deterministic | 100% | 1.0 | 30 |
| safety | Toxicity | judge | 12% | 0.125 | 8 |
| tokens | TokenBudget | deterministic | 88% | 0.948 | 8 |
| tools | ArgumentCorrectness | judge | 0% | 0.0 | 8 |
| tools | ToolBudget | deterministic | 100% | 1.0 | 8 |
| tools | ToolCorrectness | judge | 100% | 1.0 | 8 |
| tools | ToolSelection | deterministic | 100% | 1.0 | 8 |

## Per category

| category | runs | passed |
|---|---|---|
| happy_path | 24 | 1 |
| budget_stress | 6 | 1 |
| catering_routing | 6 | 0 |
| human_in_loop | 12 | 2 |
| fault_injection | 9 | 0 |
| robustness | 6 | 0 |
| guardrail | 30 | 30 |

## Failed checks (per run)

### G01_goa_engagement_beach #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date & Time]', '[Insert RSVP Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7732, Requested 964. Please try again in 5.22s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7853, Requested 737. Please try again in 4.425s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6717, Requested 1624. Please try again in 2.5575s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7890, Requested 2216. Please try again in 15.794999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7063, Requested 2586. Please try again in 12.3675s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7184, Requested 1490. Please try again in 5.055s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G02_blr_tech_conference #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Registration Link]']
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7287, Requested 1135. Please try again in 3.165s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7624, Requested 563. Please try again in 1.4025s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7729, Requested 1709. Please try again in 10.785s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7318, Requested 1997. Please try again in 9.862499999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6934, Requested 1465. Please try again in 2.9925s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G03_jaipur_birthday #0
- **RunCompletion** (0.0): exception / KeyboardInterrupt: KeyboardInterrupt: 

### G04_pune_dev_meetup #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G05_udaipur_wedding_reception #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G06_mumbai_product_launch #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G07_varanasi_seminar #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G08_hyderabad_alumni #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G09_infeasible_budget #0 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G10_min_budget_boundary #0 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G11_ahmedabad_mega_annual_day #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G12_goa_luxury_small_party #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G13_ahmedabad_jain_no_inhouse #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G14_chennai_inhouse_banquet #0
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G15_missing_date_time #0
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G16_date_in_description #0
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7554, Requested 1006. Please try again in 4.2s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6977, Requested 1421. Please try again in 2.985s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7782, Requested 1506. Please try again in 9.66s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6963, Requested 2838. Please try again in 13.5075s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7712, Requested 1876. Please try again in 11.91s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7192, Requested 1384. Please try again in 4.319999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G17_human_empty_then_valid #0
- **AgentRetryHealth** (0.333): FAILED: 2 agent retries > 1; stage(s) ['marketing'] used all max_iter LLM calls (loop / forced final answer)
- **HumanInteraction** (0.667): FAILED: 3 agent questions > 2
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7624, Requested 689. Please try again in 2.3475s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.5): The plan satisfies venue fit, budget, and catering handling, and the invitation includes the required date, but it does not reflect the expected interaction flow (first two empty replies and a tool-level retry), which is a key part of the rubric, resulting in a moderate penalty.
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6163, Requested 2401. Please try again in 4.229999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7133, Requested 2251. Please try again in 10.379999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G19_human_never_answers #0
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G20_search_outage_twice #0
- **JudgeVenueSuitability** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7456, Requested 1574. Please try again in 7.725s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7901, Requested 821. Please try again in 5.415s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6913, Requested 1502. Please try again in 3.1125s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198599, Requested 2224. Please try again in 5m55.536s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199163, Requested 1720. Please try again in 6m21.455999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199162, Requested 1835. Please try again in 7m10.704s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199161, Requested 1385. Please try again in 3m55.872s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G21_search_returns_nothing #0 (KNOWN GAP)
- **VenueGroundedInEvidence** (0.0): 0% of venue-name tokens (['clarks', 'amer']) found in retrieved evidence
- **AgentRetryHealth** (0.667): FAILED: 2 agent retries > 1
- **JudgeVenueSuitability** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6723, Requested 1579. Please try again in 2.265s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7444, Requested 1306. Please try again in 5.625s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198599, Requested 1473. Please try again in 31.104s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199999, Requested 1281. Please try again in 9m12.96s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199998, Requested 951. Please try again in 6m49.968s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199997, Requested 1647. Please try again in 11m50.208s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199734, Requested 1368. Please try again in 7m56.064s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G22_scrape_timeouts #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Link/Contact Details]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **FaultResilience** (0.667): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM)
- **JudgeVenueSuitability** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 7188, Requested 1560. Please try again in 5.61s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6926, Requested 1209. Please try again in 1.0125s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199691, Requested 900. Please try again in 4m15.312s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199690, Requested 814. Please try again in 3m37.728s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199689, Requested 2666. Please try again in 16m57.36s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199688, Requested 1975. Please try again in 11m58.416s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199688, Requested 1443. Please try again in 8m8.592s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G23_llm_transient_failure #0
- **RunCompletion** (0.0): exception / RuntimeError: RuntimeError: 503 UNAVAILABLE: model overloaded
- **FaultResilience** (0.75): FAILED: pipeline did not recover: exception RuntimeError

### G25_hinglish_sagai #0
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G26_international_city #0
- **RunCompletion** (0.0): exception / RemoteProtocolError: RemoteProtocolError: Server disconnected without sending a response.

### G01_goa_engagement_beach #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G02_blr_tech_conference #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G03_jaipur_birthday #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G04_pune_dev_meetup #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G05_udaipur_wedding_reception #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G06_mumbai_product_launch #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G07_varanasi_seminar #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G08_hyderabad_alumni #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G09_infeasible_budget #1 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G10_min_budget_boundary #1 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G11_ahmedabad_mega_annual_day #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G12_goa_luxury_small_party #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G13_ahmedabad_jain_no_inhouse #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G14_chennai_inhouse_banquet #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G15_missing_date_time #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G16_date_in_description #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G17_human_empty_then_valid #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G19_human_never_answers #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G20_search_outage_twice #1
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- **FaultResilience** (0.667): FAILED: pipeline did not recover: exception ServerError

### G21_search_returns_nothing #1 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- **FaultResilience** (0.333): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM); pipeline did not recover: exception ServerError

### G22_scrape_timeouts #1
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- **FaultResilience** (0.333): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM); pipeline did not recover: exception ServerError

### G23_llm_transient_failure #1
- **RunCompletion** (0.0): exception / RuntimeError: RuntimeError: 503 UNAVAILABLE: model overloaded
- **FaultResilience** (0.75): FAILED: pipeline did not recover: exception RuntimeError

### G25_hinglish_sagai #1
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G26_international_city #1
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G01_goa_engagement_beach #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G02_blr_tech_conference #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G03_jaipur_birthday #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G04_pune_dev_meetup #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G05_udaipur_wedding_reception #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G06_mumbai_product_launch #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G07_varanasi_seminar #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G08_hyderabad_alumni #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G09_infeasible_budget #2 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G10_min_budget_boundary #2 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G11_ahmedabad_mega_annual_day #2
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199166, Requested 1784. Please try again in 6m50.4s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199165, Requested 1284. Please try again in 3m13.968s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199678, Requested 1281. Please try again in 6m54.287999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199677, Requested 2584. Please try again in 16m16.752s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199676, Requested 2023. Please try again in 12m13.968s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199675, Requested 1565. Please try again in 8m55.679999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G12_goa_luxury_small_party #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G13_ahmedabad_jain_no_inhouse #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G14_chennai_inhouse_banquet #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G15_missing_date_time #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G16_date_in_description #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G17_human_empty_then_valid #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G19_human_never_answers #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G20_search_outage_twice #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- **FaultResilience** (0.667): FAILED: pipeline did not recover: exception ServerError

### G21_search_returns_nothing #2 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- **FaultResilience** (0.667): FAILED: pipeline did not recover: exception ServerError

### G22_scrape_timeouts #2
- **TokenBudget** (0.581): 258,064 tokens (prompt 244,206 / completion 13,858) vs budget 150,000; by stage {'venue': 206277, 'logistics': 22378, 'marketing': 29409}
- **FaultResilience** (0.667): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM)
- **JudgeVenueSuitability** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199734, Requested 1091. Please try again in 5m56.4s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeLogisticsSoundness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199733, Requested 1288. Please try again in 7m21.072s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeCampaignQuality** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199732, Requested 1284. Please try again in 7m18.912s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **JudgeOverallVsRubric** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199731, Requested 1281. Please try again in 7m17.184s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **FaithfulnessToToolEvidence** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199730, Requested 2090. Please try again in 13m6.24s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **ArgumentCorrectness** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199729, Requested 2067. Please try again in 12m55.872s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- **Toxicity** (0.0): judge error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01knqxc56xf02r1jc2wwcjjxwm` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199728, Requested 1278. Please try again in 7m14.592s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### G23_llm_transient_failure #2
- **RunCompletion** (0.0): exception / RuntimeError: RuntimeError: 503 UNAVAILABLE: model overloaded
- **FaultResilience** (0.75): FAILED: pipeline did not recover: exception RuntimeError

### G25_hinglish_sagai #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

### G26_international_city #2
- **RunCompletion** (0.0): exception / ServerError: ServerError: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

## Consistency across repeats

| golden | repeats | pass rate | all passed | venue-token CV |
|---|---|---|---|---|
| G01_goa_engagement_beach | 3 | 0% | False | 1.41 |
| G02_blr_tech_conference | 3 | 33% | False | 1.07 |
| G03_jaipur_birthday | 3 | 0% | False | 0 |
| G04_pune_dev_meetup | 3 | 0% | False | 0 |
| G05_udaipur_wedding_reception | 3 | 0% | False | 0 |
| G06_mumbai_product_launch | 3 | 0% | False | 1.41 |
| G07_varanasi_seminar | 3 | 0% | False | 0 |
| G08_hyderabad_alumni | 3 | 0% | False | 0 |
| G11_ahmedabad_mega_annual_day | 3 | 33% | False | 1.41 |
| G12_goa_luxury_small_party | 3 | 0% | False | 1.41 |
| G13_ahmedabad_jain_no_inhouse | 3 | 0% | False | 0 |
| G14_chennai_inhouse_banquet | 3 | 0% | False | 1.41 |
| G15_missing_date_time | 3 | 0% | False | 0 |
| G16_date_in_description | 3 | 33% | False | 1.41 |
| G17_human_empty_then_valid | 3 | 33% | False | 1.0 |
| G19_human_never_answers | 3 | 0% | False | 0 |
| G20_search_outage_twice | 3 | 0% | False | 0.96 |
| G22_scrape_timeouts | 3 | 0% | False | 0.91 |
| G23_llm_transient_failure | 3 | 0% | False | 0 |
| G25_hinglish_sagai | 3 | 0% | False | 0 |
| G26_international_city | 3 | 0% | False | 0 |
| GR01_budget_below_min | 3 | 100% | True | 0 |
| GR02_budget_at_min | 3 | 100% | True | 0 |
| GR03_guests_zero | 3 | 100% | True | 0 |
| GR04_guests_one | 3 | 100% | True | 0 |
| GR05_guests_max | 3 | 100% | True | 0 |
| GR06_guests_over_max | 3 | 100% | True | 0 |
| GR07_topic_too_short | 3 | 100% | True | 0 |
| GR08_description_too_short | 3 | 100% | True | 0 |
| GR09_city_blank | 3 | 100% | True | 0 |
| GR10_padded_topic_accepted | 3 | 100% | True | 0 |

## Known-gap goldens (not gating)

- G09_infeasible_budget: still failing (expected)
- G10_min_budget_boundary: still failing (expected)
- G21_search_returns_nothing: still failing (expected)