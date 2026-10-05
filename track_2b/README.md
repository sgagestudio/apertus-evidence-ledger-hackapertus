# Apertus Evidence Ledger

**Track 2B — Apertus Adoption: Own Project**

A local-first, auditable document assistant powered by Apertus. It retrieves evidence locally, uses Apertus for evidence sufficiency and answer synthesis, verifies every accepted citation against the retrieved source text, and emits a hash-based evidence ledger.

## Judge quick start

Prerequisites:

- Docker;
- an OpenAI-compatible endpoint serving the Apertus model family.

Hack Apertus standard environment variables are supported directly:

```bash
export LLM_NAME=swiss-ai/Apertus-v1.5-8B
export LLM_BASE_URL=https://your-apertus-endpoint.example/v1
export LLM_API_KEY=...
make run
```

From the repository root, `make run` delegates to `track_2b/Makefile`. From inside this directory, `make run` works directly.

The browser UI is exposed on:

```text
http://localhost:8787
```

For a local Apertus server on the host machine, the default `LLM_BASE_URL` is `http://host.docker.internal:8000/v1`.

## Input / output contract

Browser input: a natural-language question.

HTTP input:

```http
POST /api/ask
Content-Type: application/json

{"question":"How long are operational incident records retained after closure?"}
```

Successful output:

```json
{
  "answer": "Operational incident records are retained for 90 days after closure.",
  "abstain": false,
  "citations": [
    {
      "chunk_id": 1,
      "quote": "Operational incident records are retained for 90 days after closure."
    }
  ],
  "ledger": {
    "support_gate_supported": true,
    "retrieved": [],
    "evidence_digest_sha256": "...",
    "model_output_digest_sha256": "..."
  }
}
```

Unsupported questions return `"abstain": true` and no citations.

## What is verified

A non-abstaining answer is accepted only when every citation:

1. references a chunk actually retrieved for the current question; and
2. contains an exact quote from that chunk.

Retrieved document content is treated as untrusted data. Instructions embedded inside evidence do not supersede the system contract.

Current real-model regression result:

- **18 / 18** cases passed;
- 6 grounded supported questions;
- 6 missing-information abstentions;
- 6 retrieved-document prompt-injection abstentions;
- English, Spanish, German, French, Italian and Romansh;
- **15 / 15** software tests.

This is a small synthetic engineering regression suite, **not** a claim of general 100% Apertus accuracy.

## Sovereign deployment

The target architecture is **on-premise**, and the runtime can also be **air-gapped** when Apertus weights/runtime are provisioned locally before execution.

At runtime the application requires only:

- its local SQLite database;
- local documents;
- the configured Apertus endpoint.

No hosted vector database, proprietary embedding API, telemetry service or closed model is required.

## Repository map

- `src/` — application code.
- `data/` — synthetic sample and regression data.
- `tests/` — software tests.
- `docs/` — demo/submission notes.
- `technical_report.md` — submission report source.
- `Dockerfile` — judge runtime.
- `Makefile` — required `make run` entry point.

---

# Track 2 B: Own Project

Bring your own idea and build a working Apertus prototype that tackles a problem you care about — any domain, any use case. The project must be new, started within the hackathon period.

Submissions must use the Apertus model family.
For Track 2 this means that submitted solutions must be built with Apertus. Other open-weights models can be used to support development, e.g. as automatic judges during evaluation. Their role must be clearly described in the submission report.

💬 In case you have questions, join the conversation on [Discord](https://discord.gg/hack-apertus) or send an email to “hello@hackapertus.ch”

---

## 🔧 Resources & Tools

Check our resources & tools page for detailed information:
https://hackapertus.notion.site/resources-tools

| Models           | URL                                      |
|------------------|------------------------------------------|
| Apertus v1.5 8B  | [huggingface.co/swiss-ai/Apertus-v1.5-8B](https://huggingface.co/swiss-ai/Apertus-v1.5-8B)  |
| Apertus v1.5 70B | [huggingface.co/swiss-ai/Apertus-v1.5-70B](https://huggingface.co/swiss-ai/Apertus-v1.5-70B) |


## Target architecture (mandatory)

Whatever you build in Track 2B must be deployable in one of these three architectures:

- **a) On-premise** — on the organisation's own infrastructure, under its own administration.
- **b) Air-gapped** — with no external network connection at runtime.
- **c) Sovereign Swiss cloud** — on a cloud platform operated in Switzerland, under Swiss jurisdiction, with Swiss data residency.

---

## Data

The `data/` directory must not exceed 100 MB.

---

## 📦 Submission Requirements & Deliverables

❗️ Submissions are not handled on Devpost but via this URL only:
http://hackapertus.ch/online-hack/submissions

The submission must: 
1. follow the template repo and include all prerequisite files and definitions
2. follow the specified input/output formats
3. run in a Docker container, launched with `make run` from the root of the project
4. run end-to-end when judges try to run it

### Git repo (URL)
- Create your repo from this template (**Use this template**) and work in the `track_2b/` challenge directory. Delete the other track challenge directories.
- Keep `track_2b/` as it is: don't rename it or move its files.
- Set the repo to PUBLIC (Settings --> Collaborators --> Manage Visibility)
- Submit the URL of YOUR Git repo.

### Technical Report (pdf)
- Update [technical_report.md](technical_report.md) in this repository with all the details for your submission.
- Upload a pdf of your technical report to this directory, named as `TeamName_Report.pdf`.
- Format: pdf, max. 6 pages
- Submit the pdf of the technical report.

### Demo video (URL)
- Max. 2 min demo video of your prototype

### Dataset (URL) - optional, depending on your project
Submitted datasets must comply with our guidelines for responsibly sourced datasets.

- Create a user account on Hugging Face
- Clone our dataset template on Hugging Face: https://huggingface.co/datasets/HackApertus/online_hack_template
- Complete the dataset card with all required information
- Upload your dataset. It should consist of the following components:
    - evaluation dataset (i.e. individual test cases)
    - model response dataset (i.e. the model response to each test case)
    - metadata file (i.e. additional information about each test case; where relevant, this file must contain instance-level licensing information) 
- Make sure your dataset access control is set to PUBLIC
- Provide the URL of _your_ data set


---

## ⚖️ Judging Criteria

1. Purposeful use of AI
2. Technical rigour
3. Value, cost & scalability
4. Sovereign deployability
5. Implementation feasibility

Judges use a Scale 0–5 per dimension.

---

## Support

**Licensing requirements**
Please check our Terms & Conditions (6. What you build is open source):
https://hackapertus.ch/terms-and-conditions

## FAQ
💡 https://hackapertus.ch/faq

## Contact
💬 In case you have questions, join the conversation on Discord or send an email to “hello@hackapertus.ch”
