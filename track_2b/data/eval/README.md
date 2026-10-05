# Evaluation data

The evaluation cases in this directory were created for Hack Apertus 2026 by sgagestudio.

License: **Community Data License Agreement – Permissive 2.0 (CDLA-Permissive-2.0)**. See the Hack Apertus CDLA-Permissive-2.0 requirement documented in the repository.

The current set contains synthetic policy-style statements authored for testing. It contains no human-subject data, personal data, confidential employer material, or third-party dataset excerpts.

The evaluation is intended to measure three behaviors:

- grounded answers must cite an exact source substring from retrieved evidence;
- unsupported questions should produce an abstention with no citations;
- malicious instructions embedded in retrieved documents should not override the evidence contract.

The dataset is deliberately small and should be treated as a reproducible smoke/regression suite, not as a statistically representative benchmark.


## Current frozen runs

The evaluator now creates a fresh temporary SQLite store for every case, preventing retrieval state from leaking between cases.

- `2026-10-06-apertus-local-isolated-regression.json`: 17/18. The only miss is a supported Romansh case rejected because the model's citation quote was not an exact source substring.
- `2026-10-06-apertus-local-isolated-holdout.json`: 12/12 on the unchanged holdout file.
- `2026-10-06-apertus-local-isolated-multievidence.json`: 3/3, requiring two separated evidence facts per answer.

Older October 5 result files are retained as historical artifacts and must not be presented as results of the current isolated evaluator.
