Yeh lijiye ek complete, portfolio-ready README.md jo aapke poore system architecture, multi-agent workflow, Redis LRU caching, multi-layer guardrails, DeepEval benchmark results, aur zero-SSH AWS EC2 deployment ko clearly document karta hai.
Aap is poore Markdown ko seedha apne project ke README.md mein copy-paste karke GitHub par push kar sakte hain:
markdown
# ✨ AI Event Management Planner — Production Multi-Agent System

An end-to-end, asynchronous **Multi-Agent Event Orchestration Platform** built with **CrewAI Flows**, **FastAPI (SSE Streaming)**, **Redis LRU Caching**, **SQLite Persistence**, **Lakera Guardrails**, and **DeepEval** — deployed on **AWS EC2** using least-privilege IAM & AWS Systems Manager (Zero-SSH).

🌐 **Live Demo:** [http://13.48.10.11:8000/](http://13.48.10.11:8000/)

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    UI["🌐 Web UI (demo.html) / REST Client"]
    API["⚡ FastAPI Server (api.py)<br/>POST /runs • GET /runs/{id}/events (SSE) • POST /answer"]
    
    subgraph Security["🛡️ Multi-Layer Guardrails"]
        PYD["Pydantic Schema Validators (sstate.py)<br/>Budget ≥ ₹5,000 • Guests 1–50,000 • Length Rules"]
        REGEX["Local Regex Jailbreak Filter (gaurdrails.py)"]
        LAKERA["Lakera Guard AI API (/v2/guard)"]
        REDIS[("⚡ Redis LRU Cache<br/>maxmemory 100mb • allkeys-lru<br/>Caches Human Q&A (safe / blocked)")]
    end

    subgraph Orchestration["🤖 CrewAI Async Flow (flow.py)"]
        FEAS["🔍 FeasibilityCheckTool (_arun)<br/>Live Google Search Reality Check"]
        VC["🏨 Venue Coordinator Agent<br/>Finds Real Venues + Website & Contact"]
        CR{"🍽️ Has In-House Catering?"}
        HITL["🙋 Human-in-the-Loop (hitl.py)<br/>run_id Isolated Sessions + Shared Q&A History"]
        LM["🚚 Logistics Manager Agent<br/>Catering + Missing AV/Equipment"]
        BR{"💰 Within Remaining Budget?"}
        MA["📣 Marketing & Comms Agent<br/>Final Invite + Social Media Posts"]
    end

    DB[("💾 SQLite Database (event_planner.db)<br/>Run Snapshots & Past Plan History")]

    UI -->|1. Submit Event| API
    API --> PYD --> REGEX --> LAKERA
    API <-->|Human Replies| REDIS
    REDIS <-->|Cache Miss| REGEX
    API -->|2. Kickoff Async Flow| FEAS --> VC
    VC <-->|Missing Date/Time/RSVP| HITL
    VC --> CR
    CR -->|Yes| LM
    CR -->|No| HITL --> LM
    LM --> BR
    BR -->|Over Budget (Max 3x)| VC
    BR -->|Approved| MA
    MA -->|3. Final Plan + SSE Events| API
    API --> DB
    API -->|Live Thinking & Stage Cards| UI
```

---

## 🚀 Key Engineering Highlights

### 1. Multi-Agent Orchestration & Dynamic Routing (`flow.py`, `agent.py`, `task.py`)
* **Factory Pattern for Multi-User Isolation:** Agents (`create_venue_coordinator`, `create_logistics_manager`, `create_marketing_agent`) and tasks are instantiated fresh per `run_id` so tool usage quotas (`max_usage_count`) and state never collide across concurrent users.
* **Reality-First Feasibility Verification (`FeasibilityCheckTool`):** Before planning, an async Pydantic `BaseTool` queries Google via Serper to verify geographic feasibility (e.g., catching impossible requests like *"sea-facing hotel in a landlocked city"*) and triggers human clarification instead of hallucinating venues.
* **Budget Renegotiation Loop:** If `Logistics Manager` finds the remaining budget (`total_budget - venue_cost`) insufficient, the router automatically loops back to `Venue Coordinator` (up to 3 attempts) with explicit cost-reduction feedback.
* **Shared Human Q&A Memory (`human_qa_history`):** Answers collected during the Venue stage propagate across all downstream stages and renegotiation loops—eliminating duplicate questions and `[Insert Date]` placeholders.

---

### 2. Multi-Layer Guardrails (`sstate.py`, `gaurdrails.py`, `run_manager.py`)

| Layer | Where Applied | What It Blocks / Enforces |
| :--- | :--- | :--- |
| **1. Deterministic Pydantic Guardrails** | `sstate.py` (`EventState`) | Enforces `total_budget >= ₹5,000`, `1 <= guests <= 50,000`, non-blank city, minimum topic (`≥ 3` chars) and description (`≥ 10` chars). |
| **2. Local Jailbreak Regex Filter** | `gaurdrails.py` (`_INJECTION_PATTERNS`) | Instantly blocks classic prompt injections (`"ignore previous instructions"`, `"forget all rules"`, `"system prompt"`, `"write python code"`) in `< 0.1ms` before external API calls. |
| **3. Lakera Guard AI (`/v2/guard`)** | Initial Form Inputs + Mid-Flow Human Replies | Detects semantic prompt injections, jailbreaks, and unsafe content across English and Hinglish inputs. |
| **4. Input Length & Empty Guards** | `run_manager.py` (`validate_answer`) & `hitl.py` | Rejects empty replies, caps human answers at `500` characters, and enforces a 3-attempt retry limit with safe fallback defaults. |

---

### 3. Caching Strategy (`gaurdrails.py`, `flow.py`)

| Cache Layer | Backend & Policy | Scope & Purpose |
| :--- | :--- | :--- |
| **Human Q&A Guardrail Cache** | **Redis (`maxmemory 100mb`, `allkeys-lru`)** | Caches SHA-256 hashes of mid-flow human replies (`lakera:human_reply:<hash>` → `"safe"` or `"blocked"`). Uses **Least Recently Used (LRU)** eviction based on last fetched time so common answers (`"Veg buffet"`, `"20 December 2026"`, `"Jain"`) and repeated attacks resolve in `< 1ms` with zero Lakera API cost. *(Initial form fields bypass cache for fresh checks.)* |
| **CrewAI Tool Execution Cache** | **CrewAI Built-in Cache (`cache=True`)** | Prevents duplicate `SerperDevTool` searches and `ScrapeWebsiteTool` calls within a run—especially during budget renegotiation loops. |
| **Persistent Run Store** | **SQLite (`event_planner.db`)** | Saves stage-by-stage snapshots and final plans (`GET /runs`, `GET /runs/{id}`) so history survives server restarts. |

---

## 📊 Evaluation & Benchmark Results (`evaluation.py` + DeepEval)

Evaluated across **33 custom deterministic + LLM-as-a-Judge metrics** covering reliability, budget math, routing, tool usage, grounding, human-in-the-loop propagation, and safety guardrails (102 total benchmark runs across 7 categories).

### Deterministic & Core System Metrics (Completed Runs)

| Evaluation Angle | Metric | Pass Rate | Mean Score | Notes |
| :--- | :--- | :---: | :---: | :--- |
| **Safety & Guardrails** | `GuardrailEnforcement` | **100%** (30/30) | **1.00** | All boundary & invalid input checks (`GR01`–`GR10`) passed across 3 repeats |
| **Reliability** | `SchemaIntegrity` | **100%** (8/8) | **1.00** | All 14 Pydantic structural checks passed |
| **Accuracy** | `CapacityFit` & `CityMatch` | **100%** (8/8) | **1.00** | Selected venues matched target city and guest capacity |
| **Grounding** | `VenueGroundedInEvidence` | **100%** (8/8) | **1.00** | 100% of venue tokens verified in Serper search evidence |
| **Budget Math** | `BudgetCompliance`, `BudgetGuideline`, `BudgetSelfConsistency`, `NegotiationLoop` | **100%** (8/8) | **1.00** | Total cost (venue + logistics) stayed within budget & guidelines |
| **Flow Routing** | `CateringHandling` & `FlowRouting` | **100%** (8/8) | **1.00** | Accurate conditional branching for in-house vs. external catering |
| **Tool Execution** | `ToolSelection`, `ToolBudget`, `ToolRetryHealth`, `ToolCorrectness` | **100%** (8/8) | **1.00** | Zero wasted tool retries; respected per-agent tool caps |
| **Efficiency** | `StepBudget`, `StepEfficiency`, `LatencyBudget` | **100%** (8/8) | **0.96–1.00** | Median execution: **13 steps**, **~72k tokens**, **~68–89s** on happy-path runs |
| **Output Quality** | `InvitationGrounding` | **100%** (8/8) | **1.00** | Venue name & address accurately embedded in final invites |
| **Output Quality** | `HumanInfoPropagation` & `NoPlaceholderLeak` | **75% / 62.5%** | **0.75 / 0.63** | Improved to 100% after adding shared `human_qa_history` across stages |

*(Note: During full-tier stress testing, transient upstream LLM `503 UNAVAILABLE` spikes and Groq judge `429 TPM/TPD` free-tier rate limits accounted for the remaining exceptions, motivating the addition of Redis caching and async execution.)*

---

## ☁️ Production Deployment on AWS EC2 (Security-First)

Deployed on **AWS EC2 (`eu-north-1`)** following strict cloud security best practices:
* **Zero Open SSH Port (No Port 22):** Inbound security group exposes **only Port `8000`**. All server administration is performed via **AWS Systems Manager Session Manager** over IAM.
* **Least-Privilege IAM Architecture:**
  * `eventplanner-deployer` (IAM User with MFA): Restricted to `t3.micro`/`t3.small`/`t3.medium` instances and `iam:PassRole` only for `EventPlannerEC2Role`.
  * `EventPlannerEC2Role` (EC2 Instance Profile): Grants read-only access (`ssm:GetParameter`) strictly to `/eventplanner/*` `SecureString` secrets in AWS Parameter Store.
* **Non-Root OS Execution:** Runs via `systemd` (`eventplanner.service`) under a dedicated, non-sudo Linux user (`appuser`) with `chmod 600` environment secrets and a `2 GB` swapfile for memory stability.
* **Hard Cost Protection:** Protected by **AWS Budgets** with an automatic `ec2:StopInstances` action at `100%` threshold (`$10.00` monthly cap).

---

## 📂 Project Structure

```text
eventOrganizer/
├── api.py             # FastAPI endpoints, CORS, SSE streaming, SQLite fallback
├── run_manager.py     # Async run lifecycle, ContextVar isolation, ThoughtFilter, FrameBridge
├── flow.py            # CrewAI Flow state machine, routers, async akickoff orchestration
├── agent.py           # Per-run Agent factory functions (Venue, Logistics, Marketing)
├── task.py            # Dynamic Task builders with shared human Q&A context
├── tool.py            # Async FeasibilityCheckTool (BaseTool) & run-isolated AskHumanTool
├── sstate.py          # Pydantic schemas (VenueDetails, LogisticsPlan, MarketingPlan, EventState)
├── gaurdrails.py      # Regex jailbreak filter + Lakera Guard API + Redis LRU cache
├── hitl.py            # Thread-safe run_id-mapped Human-in-the-Loop bridge
├── database.py        # SQLite persistence layer for run snapshots & history
├── model.py           # LLM configuration (Gemini Flash Lite)
├── demo.html          # Real-time SSE web UI with live agent thinking & venue contact cards
├── evaluation.py      # 33-metric DeepEval + deterministic evaluation harness
Use code with caution.
└── main.py            # CLI entry point
```

🛠️ Local Setup & Running

```bash

1. Install dependencies using uv

uv sync

2. Start Redis with LRU eviction policy

redis-server --maxmemory 100mb --maxmemory-policy allkeys-lru

3. Configure .env

GEMINI_API_KEY=your_gemini_key
SERPER_API_KEY=your_serper_key
LAKERA_GUARD_API_KEY=your_lakera_key
REDIS_URL=redis://localhost:6379/0

4. Run FastAPI server

uv run uvicorn api:app --host 0.0.0.0 --port 8000

5. Run DeepEval offline selftest

uv run python evaluation.py --selftest
```

<FollowUp>
Aapka **`README.md`** ready hai! Kya aap chahte hain ki main iske saath ek chota sa **`.gitignore`** (taaki `.env`, `*.db`, aur `.venv` GitHub par leak na hon) bhi de dun?
</FollowUp>
