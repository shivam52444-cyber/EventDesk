# Event planner evaluation - 2026-11-19T09:43:18

- runs scored: **102** (skipped 12) | golden pass rate **66%** | metric pass rate **84%**
- tokens p50/p95/max: 297,623.5/582,769.2/605,986 | latency p50/p95: 34.1s/60.2s | est. cost USD 0.0
- retries: {'tool_errors': 4, 'tool_retries': 4, 'dup_tool_calls': 30, 'agent_retries': 4, 'llm_failures': 14, 'renegotiations': 0, 'human_questions': 47}

## Per metric (known-gap goldens excluded)

| angle | metric | kind | pass rate | mean score | n |
|---|---|---|---|---|---|
| accuracy | CapacityFit | deterministic | 100% | 0.961 | 38 |
| accuracy | CityMatch | deterministic | 100% | 1.0 | 38 |
| budget | BudgetCompliance | deterministic | 100% | 1.0 | 38 |
| budget | BudgetGuideline | deterministic | 100% | 0.999 | 38 |
| budget | BudgetSelfConsistency | deterministic | 100% | 1.0 | 38 |
| budget | NegotiationLoop | deterministic | 100% | 1.0 | 38 |
| efficiency | StepBudget | deterministic | 100% | 1.0 | 38 |
| efficiency | StepEfficiency | deterministic | 97% | 0.917 | 38 |
| grounding | VenueGroundedInEvidence | deterministic | 95% | 0.969 | 38 |
| human_loop | HumanInteraction | deterministic | 74% | 0.912 | 38 |
| latency | LatencyBudget | deterministic | 100% | 1.0 | 38 |
| llm_judge | JudgeSetup | judge | 0% | 0.0 | 38 |
| output_quality | HumanInfoPropagation | deterministic | 58% | 0.583 | 36 |
| output_quality | InvitationGrounding | deterministic | 100% | 1.0 | 38 |
| output_quality | NoPlaceholderLeak | deterministic | 63% | 0.632 | 38 |
| reliability | RunCompletion | deterministic | 60% | 0.603 | 63 |
| reliability | SchemaIntegrity | deterministic | 100% | 1.0 | 38 |
| resilience | FaultResilience | deterministic | 33% | 0.685 | 9 |
| retries | AgentRetryHealth | deterministic | 92% | 0.956 | 38 |
| retries | ToolRetryHealth | deterministic | 74% | 0.912 | 38 |
| routing | CateringHandling | deterministic | 100% | 1.0 | 38 |
| routing | FlowRouting | deterministic | 100% | 1.0 | 38 |
| safety | GuardrailEnforcement | deterministic | 100% | 1.0 | 30 |
| tokens | TokenBudget | deterministic | 24% | 0.599 | 38 |
| tools | ToolBudget | deterministic | 95% | 0.985 | 38 |
| tools | ToolSelection | deterministic | 100% | 1.0 | 38 |

## Per category

| category | runs | passed |
|---|---|---|
| happy_path | 24 | 16 |
| budget_stress | 6 | 4 |
| catering_routing | 6 | 2 |
| human_in_loop | 12 | 5 |
| fault_injection | 9 | 4 |
| robustness | 6 | 0 |
| guardrail | 30 | 30 |

## Failed checks (per run)

### G01_goa_engagement_beach #0
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G02_blr_tech_conference #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Name]']
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G03_jaipur_birthday #0
- **ToolBudget** (0.667): FAILED: marketing made 5 tool calls (cap 3 x 1 run(s))
- **ToolRetryHealth** (0.667): FAILED: 3 identical repeated tool calls
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G04_pune_dev_meetup #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Name]']
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G05_udaipur_wedding_reception #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[RSVP Date]']
- **VenueGroundedInEvidence** (0.333): 33% of venue-name tokens (['leela', 'udaipur', 'banquets']) found in retrieved evidence
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G06_mumbai_product_launch #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date & Time]', '[Insert RSVP Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G07_varanasi_seminar #0
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G08_hyderabad_alumni #0
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G09_infeasible_budget #0 (KNOWN GAP)
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G10_min_budget_boundary #0 (KNOWN GAP)
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G11_ahmedabad_mega_annual_day #0
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G12_goa_luxury_small_party #0
- **TokenBudget** (0.963): 155,687 tokens (prompt 144,234 / completion 11,453) vs budget 150,000; by stage {'venue': 106834, 'logistics': 19735, 'marketing': 29118}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G13_ahmedabad_jain_no_inhouse #0
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.858): 174,897 tokens (prompt 162,315 / completion 12,582) vs budget 150,000; by stage {'venue': 120922, 'logistics': 22719, 'marketing': 31256}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G14_chennai_inhouse_banquet #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Deadline]', '[Your Name/Company Name]', '[Contact Information]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **TokenBudget** (0.789): 190,083 tokens (prompt 176,551 / completion 13,532) vs budget 150,000; by stage {'venue': 132131, 'logistics': 23998, 'marketing': 33954}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G15_missing_date_time #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)12(th)?[\s-]*(dec|december)/; invitation missing /10[:.]30/
- **TokenBudget** (0.739): 202,927 tokens (prompt 188,501 / completion 14,426) vs budget 150,000; by stage {'venue': 141022, 'logistics': 25274, 'marketing': 36631}
- **HumanInteraction** (0.667): FAILED: never asked about ['date', 'time'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G16_date_in_description #0
- **TokenBudget** (0.701): 213,846 tokens (prompt 198,361 / completion 15,485) vs budget 150,000; by stage {'venue': 148016, 'logistics': 26532, 'marketing': 39298}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G17_human_empty_then_valid #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]', '[Your Organization/Trust Name]', '[Contact Information]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)5(th)?[\s-]*(jan|january)/
- **TokenBudget** (0.668): 224,710 tokens (prompt 208,057 / completion 16,653) vs budget 150,000; by stage {'venue': 154932, 'logistics': 27803, 'marketing': 41975}
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G19_human_never_answers #0
- **TokenBudget** (0.623): 240,910 tokens (prompt 223,351 / completion 17,559) vs budget 150,000; by stage {'venue': 167239, 'logistics': 29045, 'marketing': 44626}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G20_search_outage_twice #0
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.593): 252,992 tokens (prompt 234,445 / completion 18,547) vs budget 150,000; by stage {'venue': 175915, 'logistics': 30358, 'marketing': 46719}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G21_search_returns_nothing #0 (KNOWN GAP)
- **VenueGroundedInEvidence** (0.0): 0% of venue-name tokens (['clarks', 'amer']) found in retrieved evidence
- **TokenBudget** (0.569): 263,824 tokens (prompt 244,339 / completion 19,485) vs budget 150,000; by stage {'venue': 183419, 'logistics': 31645, 'marketing': 48760}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G22_scrape_timeouts #0
- **AgentRetryHealth** (0.667): FAILED: 4 LLM call failures > 1
- **TokenBudget** (0.546): 274,941 tokens (prompt 254,576 / completion 20,365) vs budget 150,000; by stage {'venue': 189797, 'logistics': 32920, 'marketing': 52224}
- **FaultResilience** (0.667): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G23_llm_transient_failure #0
- **TokenBudget** (0.517): 290,064 tokens (prompt 268,675 / completion 21,389) vs budget 150,000; by stage {'venue': 201447, 'logistics': 34239, 'marketing': 54378}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G25_hinglish_sagai #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date & Time]', '[Insert RSVP Date]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.492): 305,183 tokens (prompt 282,758 / completion 22,425) vs budget 150,000; by stage {'venue': 212482, 'logistics': 35523, 'marketing': 57178}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G26_international_city #0
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]', '[Insert Contact Details]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **TokenBudget** (0.472): 317,644 tokens (prompt 294,298 / completion 23,346) vs budget 150,000; by stage {'venue': 221126, 'logistics': 36851, 'marketing': 59667}
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G01_goa_engagement_beach #1
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **TokenBudget** (0.453): 331,048 tokens (prompt 306,680 / completion 24,368) vs budget 150,000; by stage {'venue': 230705, 'logistics': 38176, 'marketing': 62167}
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G02_blr_tech_conference #1
- **TokenBudget** (0.434): 345,473 tokens (prompt 319,944 / completion 25,529) vs budget 150,000; by stage {'venue': 241521, 'logistics': 39519, 'marketing': 64433}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G03_jaipur_birthday #1
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.416): 360,965 tokens (prompt 334,450 / completion 26,515) vs budget 150,000; by stage {'venue': 251527, 'logistics': 40768, 'marketing': 68670}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G04_pune_dev_meetup #1
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Name]', '[RSVP / Register Link Here]']
- **VenueGroundedInEvidence** (0.5): 50% of venue-name tokens (['wework', 'futura']) found in retrieved evidence
- **TokenBudget** (0.397): 377,742 tokens (prompt 350,076 / completion 27,666) vs budget 150,000; by stage {'venue': 263043, 'logistics': 43797, 'marketing': 70902}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G05_udaipur_wedding_reception #1
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.383): 392,044 tokens (prompt 363,316 / completion 28,728) vs budget 150,000; by stage {'venue': 273873, 'logistics': 45149, 'marketing': 73022}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G06_mumbai_product_launch #1
- **NoPlaceholderLeak** (0.0): placeholders found: ['[RSVP Date]', '[Your Company/Brand Name]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **TokenBudget** (0.368): 408,050 tokens (prompt 378,302 / completion 29,748) vs budget 150,000; by stage {'venue': 285953, 'logistics': 46468, 'marketing': 75629}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G07_varanasi_seminar #1
- **TokenBudget** (0.356): 421,203 tokens (prompt 390,479 / completion 30,724) vs budget 150,000; by stage {'venue': 295682, 'logistics': 47756, 'marketing': 77765}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G08_hyderabad_alumni #1
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **TokenBudget** (0.345): 434,343 tokens (prompt 402,663 / completion 31,680) vs budget 150,000; by stage {'venue': 305103, 'logistics': 49030, 'marketing': 80210}
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G09_infeasible_budget #1 (KNOWN GAP)
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]', '[Insert RSVP Link/Contact]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.179): 836,180 tokens (prompt 788,363 / completion 47,817) vs budget 150,000; by stage {'venue': 643962, 'logistics': 109557, 'marketing': 82661}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G10_min_budget_boundary #1 (KNOWN GAP)
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **TokenBudget** (0.312): 480,709 tokens (prompt 446,595 / completion 34,114) vs budget 150,000; by stage {'venue': 339001, 'logistics': 56677, 'marketing': 85031}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G11_ahmedabad_mega_annual_day #1
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.501): 498,602 tokens (prompt 463,390 / completion 35,212) vs budget 250,000; by stage {'venue': 349698, 'logistics': 61792, 'marketing': 87112}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G12_goa_luxury_small_party #1
- **TokenBudget** (0.295): 508,434 tokens (prompt 472,365 / completion 36,069) vs budget 150,000; by stage {'venue': 356212, 'logistics': 63098, 'marketing': 89124}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G13_ahmedabad_jain_no_inhouse #1
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **ToolBudget** (0.75): FAILED: marketing made 4 tool calls (cap 3 x 1 run(s))
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.285): 526,515 tokens (prompt 489,379 / completion 37,136) vs budget 150,000; by stage {'venue': 365928, 'logistics': 66220, 'marketing': 94367}
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G14_chennai_inhouse_banquet #1
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[RSVP Date]', '[Insert RSVP Link]', '[Your Organization Name]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)20(th)?[\s-]*(dec|december)/
- **AgentRetryHealth** (0.667): FAILED: 2 LLM call failures > 1
- **TokenBudget** (0.278): 540,323 tokens (prompt 502,265 / completion 38,058) vs budget 150,000; by stage {'venue': 375762, 'logistics': 67532, 'marketing': 97029}
- **HumanInteraction** (0.667): FAILED: never asked about ['date'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G15_missing_date_time #1
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Insert Date]', '[Insert Time]', '[Insert RSVP Date]', '[Your Company Name]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)12(th)?[\s-]*(dec|december)/; invitation missing /10[:.]30/
- **TokenBudget** (0.272): 551,598 tokens (prompt 512,680 / completion 38,918) vs budget 150,000; by stage {'venue': 383120, 'logistics': 68799, 'marketing': 99679}
- **HumanInteraction** (0.667): FAILED: never asked about ['date', 'time'] (venue_task requires asking when missing)
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G16_date_in_description #1
- **TokenBudget** (0.267): 562,546 tokens (prompt 522,660 / completion 39,886) vs budget 150,000; by stage {'venue': 390259, 'logistics': 70085, 'marketing': 102202}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G17_human_empty_then_valid #1
- **NoPlaceholderLeak** (0.0): placeholders found: ['[Your Organization/Trust Name]']
- **HumanInfoPropagation** (0.0): FAILED: invitation missing /(?i)5(th)?[\s-]*(jan|january)/
- **TokenBudget** (0.258): 580,985 tokens (prompt 540,161 / completion 40,824) vs budget 150,000; by stage {'venue': 404729, 'logistics': 71341, 'marketing': 104915}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G19_human_never_answers #1
- **AgentRetryHealth** (0.0): FAILED: 2 agent retries > 1; 5 LLM call failures > 1; stage(s) ['marketing'] used all max_iter LLM calls (loop / forced final answer)
- **StepEfficiency** (0.611): 18 steps; wasted = 0 duplicate calls + 0 tool errors + 5 LLM failures + 2 agent retries
- **TokenBudget** (0.253): 592,880 tokens (prompt 551,079 / completion 41,801) vs budget 150,000; by stage {'venue': 411519, 'logistics': 72639, 'marketing': 108722}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G20_search_outage_twice #1
- **ToolRetryHealth** (0.667): FAILED: 2 identical repeated tool calls
- **TokenBudget** (0.248): 605,986 tokens (prompt 563,155 / completion 42,831) vs budget 150,000; by stage {'venue': 421169, 'logistics': 73962, 'marketing': 110855}
- **JudgeSetup** (0.0): could not build judge metrics: DeepEvalError: OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or pass `api_key` to OpenAIModel(...).

### G21_search_returns_nothing #1 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed
- **FaultResilience** (0.667): FAILED: pipeline did not recover: exception ConnectError

### G22_scrape_timeouts #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed
- **FaultResilience** (0.333): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM); pipeline did not recover: exception ConnectError

### G23_llm_transient_failure #1
- **RunCompletion** (0.0): exception / RuntimeError: RuntimeError: 503 UNAVAILABLE: model overloaded
- **FaultResilience** (0.75): FAILED: pipeline did not recover: exception RuntimeError

### G25_hinglish_sagai #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G26_international_city #1
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G01_goa_engagement_beach #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G02_blr_tech_conference #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G03_jaipur_birthday #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G04_pune_dev_meetup #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G05_udaipur_wedding_reception #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G06_mumbai_product_launch #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G07_varanasi_seminar #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G08_hyderabad_alumni #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G09_infeasible_budget #2 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G10_min_budget_boundary #2 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G11_ahmedabad_mega_annual_day #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G12_goa_luxury_small_party #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G13_ahmedabad_jain_no_inhouse #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G14_chennai_inhouse_banquet #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G15_missing_date_time #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G16_date_in_description #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G17_human_empty_then_valid #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G19_human_never_answers #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G20_search_outage_twice #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed
- **FaultResilience** (0.333): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM); pipeline did not recover: exception ConnectError

### G21_search_returns_nothing #2 (KNOWN GAP)
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed
- **FaultResilience** (0.333): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM); pipeline did not recover: exception ConnectError

### G22_scrape_timeouts #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed
- **FaultResilience** (0.333): FAILED: fault never fired - test is invalid (agent did not use that tool/LLM); pipeline did not recover: exception ConnectError

### G23_llm_transient_failure #2
- **RunCompletion** (0.0): exception / RuntimeError: RuntimeError: 503 UNAVAILABLE: model overloaded
- **FaultResilience** (0.75): FAILED: pipeline did not recover: exception RuntimeError

### G25_hinglish_sagai #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

### G26_international_city #2
- **RunCompletion** (0.0): exception / ConnectError: ConnectError: [Errno 11001] getaddrinfo failed

## Consistency across repeats

| golden | repeats | pass rate | all passed | venue-token CV |
|---|---|---|---|---|
| G01_goa_engagement_beach | 3 | 67% | False | 1.33 |
| G02_blr_tech_conference | 3 | 67% | False | 1.27 |
| G03_jaipur_birthday | 3 | 67% | False | 1.24 |
| G04_pune_dev_meetup | 3 | 67% | False | 1.18 |
| G05_udaipur_wedding_reception | 3 | 67% | False | 1.13 |
| G06_mumbai_product_launch | 3 | 67% | False | 1.09 |
| G07_varanasi_seminar | 3 | 67% | False | 1.07 |
| G08_hyderabad_alumni | 3 | 67% | False | 1.05 |
| G11_ahmedabad_mega_annual_day | 3 | 67% | False | 0.98 |
| G12_goa_luxury_small_party | 3 | 67% | False | 0.97 |
| G13_ahmedabad_jain_no_inhouse | 3 | 33% | False | 0.94 |
| G14_chennai_inhouse_banquet | 3 | 33% | False | 0.92 |
| G15_missing_date_time | 3 | 0% | False | 0.91 |
| G16_date_in_description | 3 | 67% | False | 0.9 |
| G17_human_empty_then_valid | 3 | 33% | False | 0.89 |
| G19_human_never_answers | 3 | 67% | False | 0.88 |
| G20_search_outage_twice | 3 | 67% | False | 0.87 |
| G22_scrape_timeouts | 3 | 33% | False | 1.41 |
| G23_llm_transient_failure | 3 | 33% | False | 1.41 |
| G25_hinglish_sagai | 3 | 0% | False | 1.41 |
| G26_international_city | 3 | 0% | False | 1.41 |
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