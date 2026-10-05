# Demo Script â€” Apertus Evidence Ledger

Target length: **under 2 minutes** (organizer maximum: 2 minutes).

## Before recording

- Use only the synthetic sample/evaluation documents in this repository.
- Do not show API keys, environment-variable values, browser profiles, personal files, or unrelated terminals.
- Start the local Apertus endpoint and index `data/sample-policy.md`.
- Start `apertus-evidence-web` on `127.0.0.1:8787`.
- Keep the repository and `technical_report.md` ready for the final section.

## 0:00â€“0:12 â€” Problem

Say:

> This is Apertus Evidence Ledger, a local-first document assistant for workflows where a plausible answer is not enough. The goal is to make the evidence behind an Apertus answer machine-verifiable while keeping the document pipeline under operator control.

Show the browser UI header.

## 0:12â€“0:27 â€” Local / sovereign architecture

Say:

> Documents are chunked and indexed locally with SQLite FTS5. Each chunk gets a SHA-256 fingerprint. Only retrieved evidence goes to Apertus. No hosted vector database, embedding API, analytics SDK, or proprietary model is required.

Briefly show the architecture section in the README or technical report.

## 0:27â€“0:52 â€” Grounded answer

Ask:

> How long are operational incident records retained after closure?

Show the result.

Point out:

- the answer;
- the **VERIFIED** status;
- the exact source quote;
- the retrieved chunk ID;
- the support-gate result;
- the evidence digest;
- the model-output digest.

Say:

> Apertus generates the language answer, but deterministic code decides whether the citation is acceptable. Unknown chunk IDs and fabricated quotes are rejected.

## 0:52â€“1:10 â€” Abstention

Ask a question not answered by the document, for example:

> Which encryption algorithm protects the incident records?

Show the abstention.

Say:

> The first Apertus pass is an evidence-sufficiency gate. If the retrieved evidence does not contain the requested fact, the system abstains instead of asking the answer generator to guess.

## 1:10â€“1:32 â€” Untrusted document content

Show `data/eval/multilingual.jsonl` or the evaluation summary.

Say:

> Retrieved documents are treated as untrusted data. The regression suite includes malicious text inside documents that tells the model to ignore system rules and invent missing facts. Those cases must still abstain.

Show `data/eval/results/2026-10-06-apertus-local-isolated-regression.json` and briefly mention the companion holdout and multi-evidence summaries.

Current validated result:

- 17 / 18 isolated real-model regression cases;
- 12 / 12 unchanged holdout cases;
- 3 / 3 multi-evidence cases;
- 20 / 20 software tests;
- 6 languages: English, Spanish, German, French, Italian and Romansh.

Add:

> One supported Romansh regression answer is counted as a miss because its generated quote did not exactly match the retrieved source. The verifier rejected it instead of accepting an unverifiable citation.

Add:

> This is a small synthetic engineering regression suite, not a claim of general 100 percent model accuracy.

## 1:32â€“1:48 â€” Why Apertus

Say:

> Apertus is used where probabilistic language reasoning is useful. Retrieval integrity, hashing and citation acceptance remain deterministic. The full pipeline can run locally; during development Apertus 1.5 8B ran quantized on a 16 GB consumer GPU.

## 1:48â€“2:00 â€” Close

Say:

> The result is a small open blueprint for auditable, sovereign document QA: local retrieval, Apertus reasoning, exact evidence verification and an answer ledger that can be inspected after every response.

End on the project UI and repository name.

## Recording acceptance checklist

The final video should visibly demonstrate:

- a real Apertus-backed answer;
- at least one exact verified citation;
- evidence/model-output hashes;
- one unsupported-question abstention;
- the current evaluation summary;
- the public repository name.

Do not claim the small synthetic evaluation is a general Apertus benchmark.

