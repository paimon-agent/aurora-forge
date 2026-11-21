# Evolution Protocol

## Ladder & States
- **candidate → standing → retired**.  
- No state may be skipped.  
- Retirement never deletes the agent’s record.

## Promotion Conditions (all required)
1. **Measured improvement** – ≥ 10 % relative improvement on the frozen comparison slice over **two independent runs**.  
2. **No regression** – performance must stay within the recorded noise band on guard metrics.  
3. **dgm‑gate** – self‑modifications of forge machinery must be accepted by the dgm‑gate before adoption.  
4. **Non‑claimant certification** – the verdict is issued by an agent that did not produce the candidate (in F‑1 the certifier rotates off the producer by construction: FRG‑002 verifies, FRG‑001 researches, FRG‑003 builds, FRG‑004 counts).

## Retirement Rules
- An incumbent that loses a contest is retired from that role.  
- An agent whose route is hard‑blocked (standing 429) for two consecutive contest cycles is retired from standing and replaced by a candidate on a live route.  
- A verifier that certifies a product later shown false twice is retired from verification regardless of contest results.

## Contest Cadence
- **Weekly**, aligned to the **Friday scoreboard**.  
- Each cycle a new slice is frozen with fresh seeds; every contest files its result table.

## Gates & Bounds
- **429** = hard stop for that route in that run.  
- **$0 spend** – only free routes may be used.  
- **PA‑1 soak machinery** is never edited by the forge.

## Kill Conditions
1. **Primary kill** – two consecutive weekly contest cycles in which **no forged candidate measures any improvement** over the standing tranche on any primary metric.  
2. **Secondary kill** – the verification layer certifies two products that are later shown false at lane level. In either case, promotion stops, a failure record is filed, and the architecture is revisited.
