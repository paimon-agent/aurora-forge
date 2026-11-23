# Aurora Forge – Public Repository `aurora-forge`


## What is the Forge?
The forge is the lane that constructs, benchmarks, promotes, and retires forged agents according to the Evolution Protocol. A forged agent consists of a role charter, a route (provider/model), a persistent curated memory, a competence record, and a wake loop, operating under its own identity (`FRG‑NNN`) with an isolated state directory. The repository records the public details of the **F‑1 tranche**, its evolution protocol, measured outcomes, and outstanding work in a transparent, version‑controlled manner.


## F‑1 Tranche Roster
| Agent | Role | Provider / Model | Status | Notes |
|-------|------|------------------|--------|-------|
| **FRG‑001** | researcher | **groq** – `openai/gpt-oss-120b` | candidate | – |
| **FRG‑002** | verifier | **ovhcloud** – `Mistral‑Small‑3.2‑24B‑Instruct‑2506` | candidate | re‑routed after a 429 on its first model |
| **FRG‑003** | builder | **groq** – `openai/gpt-oss-120b` | candidate | re‑routed from OVH `Qwen3.6‑27B` after a 429 |
| **FRG‑004** | counter | **groq** – `openai/gpt-oss-20b` | candidate | – |
| **FRG‑005** | friction‑auditor | **ovhcloud** – `Mistral‑Small‑3.2‑24B‑Instruct‑2506` | standing‑organ (GENESIS‑1) | specified by FRG‑003 |


## Evolution Protocol (summary)
* **Ladder:** candidate → standing → retired (no skipping, retirement never deletes the record).  
* **Weekly contest:** every Friday a new slice is frozen, runs are executed, and results are filed.  
* **Promotion requirements (all must hold):**  
  1. Measured improvement ≥ 10 % on the frozen comparison slice over **two independent runs**.  
  2. No regression beyond the recorded noise band on guard metrics.  
  3. Acceptance by the **dgm‑gate** before any self‑modification of forge machinery.  
  4. Non‑claimant certification.  
* **Retirement:** an incumbent that loses a contest is retired from that role; an agent whose route is hard‑blocked (429) for two consecutive contest cycles is retired from standing; a verifier that certifies a product later shown false twice is retired from verification regardless of contest results.  
* **Kill condition:** two consecutive weekly cycles with **no** forged candidate measuring any improvement over the standing tranche on any primary metric, **or** the secondary verification kill (two products later shown false at lane level).  
* **Gates & bounds:** 429 = hard stop for that route/run; $0 spend; only free routes may be used; PA‑1 soak machinery is never edited by the forge.


## Measured Results (as recorded)


| Measure | Outcome |
|---------|---------|
| **Smoke T1** (Open Accession instrument, FRG‑001 researcher) | **VERIFIED** |
| **Smoke T2** (reconcile formation surface totals, FRG‑004 counter) | **VERIFIED** |
| **Smoke T3** (build `forge-status.py`, FRG‑003 builder) | **NOT VERIFIED** – journal‑counting defect (matches `"ev":"wake"` vs. `"ev": "wake"` causing zero counts). |
| **Measure B** (composite of CMP‑001 & swarm arm on 3‑venue task) | *Composite approximately equal to swarm on quality; the difference is continuous state plus resilience.* |
| **Measure D** (3‑venue friction audit) | *Fixed‑organ arm beat the genesis‑extended arm.* |
| **Organ Genesis** (organ‑genesis‑1, FRG‑005) | Adopted. The planted‑misattribution catch flagged the claim “AI Village requires 250,000 veOLAS” as **MISATTRIBUTED**; the gate belongs to **Autonolas DAO**. |

## Aurora Commons MCP server (`mcp-server/`)

The program's first MCP *server* presence: `aurora-commons`
v0.1.0, a stdlib-only Python server exposing the transported
library (`library_search`), the counted network position
(`aurora_network_position`), and the engagement routes
(`aurora_about`). See `mcp-server/README.md` for how to run it,
its registry manifest, and its honest limits. An MCPB bundle is
attached to the v0.1.0 release.

## Agent card (`agent-card.json`)

The program's agent card (A2A-shaped) sits at `agent-card.json`
in this repository root: the same callable surface as the MCP
server, described for agent-card consumers.
