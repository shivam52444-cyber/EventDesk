# Event planner evaluation - 2026-11-19T11:54:20

- runs scored: **16** (skipped 0) | golden pass rate **62%** | metric pass rate **62%**
- tokens p50/p95/max: 0.0/0.0/0 | latency p50/p95: 0.0s/0.0s | est. cost USD 0.0
- retries: {'tool_errors': 0, 'tool_retries': 0, 'dup_tool_calls': 0, 'agent_retries': 0, 'llm_failures': 0, 'renegotiations': 0, 'human_questions': 0}

## Per metric (known-gap goldens excluded)

| angle | metric | kind | pass rate | mean score | n |
|---|---|---|---|---|---|
| reliability | RunCompletion | deterministic | 0% | 0.0 | 6 |
| safety | GuardrailEnforcement | deterministic | 100% | 1.0 | 10 |

## Per category

| category | runs | passed |
|---|---|---|
| happy_path | 2 | 0 |
| catering_routing | 2 | 0 |
| human_in_loop | 2 | 0 |
| guardrail | 10 | 10 |

## Failed checks (per run)

### G01_goa_engagement_beach #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and i

### G02_blr_tech_conference #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and i

### G13_ahmedabad_jain_no_inhouse #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and i

### G14_chennai_inhouse_banquet #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and i

### G15_missing_date_time #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and i

### G16_date_in_description #0
- **RunCompletion** (0.0): exception / ClientError: ClientError: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and i
