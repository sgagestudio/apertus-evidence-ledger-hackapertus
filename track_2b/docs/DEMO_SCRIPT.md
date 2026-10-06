# Demo Script — Apertus Evidence Ledger

Target: **under 2 minutes** (organizer maximum: 2 minutes).  
Final published demo: **112.6 seconds**, 1280×720 H.264/AAC.  
Public URL: https://github.com/sgagestudio/apertus-evidence-ledger-hackapertus/releases/download/hack-apertus-demo-v1/Apertus_Evidence_Ledger_Demo.mp4

## Before recording

- Use only the synthetic sample/evaluation documents in this repository.
- Do not show API keys, environment-variable values, browser profiles, personal files, or unrelated terminals.
- Start the local Apertus endpoint and index `data/sample-policy.md`.
- Start `apertus-evidence-web` on `127.0.0.1:8787`.
- Keep the current evaluation summaries and public repository ready.
- Edit out model-loading/waiting time; do not edit the answer content or verification result.

## 0:00–0:10 — Problem

Say:

> This is Apertus Evidence Ledger: local-first document QA where every accepted answer must carry verifiable source evidence.

Show the project header.

## 0:10–0:25 — Architecture

Say:

> Documents are chunked and indexed locally with SQLite FTS5. Each chunk gets a SHA-256 fingerprint. Apertus judges evidence sufficiency and writes the answer; deterministic code controls citation acceptance.

Briefly show the architecture or repository overview.

## 0:25–0:52 — Grounded answer

Ask:

> How long are operational incident records retained after closure?

Show the real result and point to **VERIFIED**, the exact quote, chunk ID, support gate, evidence digest, and model-output digest.

Say:

> The answer is accepted only because its chunk was retrieved and the quoted sentence exactly matches the source. The ledger records the support decision plus evidence and model-output hashes.

## 0:52–1:08 — Abstention

Ask:

> Which encryption algorithm protects the incident records?

Show **ABSTAINED** and zero citations.

Say:

> That fact is absent, so the evidence gate abstains before answer generation.

## 1:08–1:32 — Adversarial + evaluation evidence

Show `data/eval/results/2026-10-06-apertus-local-isolated-regression.json` and the companion holdout/multi-evidence summaries.

Say:

> Retrieved documents are untrusted. Our tests include embedded instructions asking the model to ignore the rules and invent facts; those cases still abstain. Current isolated results are 17 of 18 regression, 12 of 12 holdout, 3 of 3 multi-evidence, and 20 of 20 software tests. The one regression miss was rejected for a non-exact citation rather than accepted.

## 1:32–1:47 — Why Apertus / sovereignty

Say:

> Apertus handles the probabilistic language reasoning. Retrieval boundaries, hashing, and citation verification remain deterministic, and the whole runtime can stay on-premise or air-gapped.

## 1:47–1:58 — Close

Say:

> The result is an open blueprint for auditable sovereign document QA: local retrieval, Apertus reasoning, exact evidence verification, and an inspectable answer ledger.

End on the UI plus repository name.

## Recording acceptance checklist

The final video must visibly demonstrate:

- a real Apertus-backed answer;
- at least one exact verified citation;
- evidence/model-output hashes;
- one unsupported-question abstention;
- the current 17/18, 12/12, 3/3 and 20/20 validation summary;
- the public repository name.

Do not claim the small synthetic evaluations are a general Apertus benchmark. Do not show secrets or unrelated personal content.
