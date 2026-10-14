# Evidence and methodology

## User-provided material

The user supplied six screenshots of a US App Store keyword/competitor research tool, followed by four US written-review CSV exports dated 14 October 2026. They requested broad independent research, then detailed investigation of these four competitors, then a concrete MVP/screen/differentiation plan, and finally documentation uploaded to APPIDEAS.

| Product | Developer | Apple app ID | Written-review rows | Date range UTC |
|---|---|---|---:|---|
| PeptidePal – Peptide Tracker | Blank Labs LLC | 6762102880 | 112 | 2026-04-24–2026-10-10 |
| Pep AI: GLP-1 Peptide Tracker | Zode Development LLC | 6758682710 | 138 | 2026-02-17–2026-10-12 |
| Peptide Calculator: PepCalc | David Dzeveckij | 6747501164 | 4 | 2025-12-12–2026-09-08 |
| Shotsy GLP-1 Tracker | Shotsy | 6499510249 | 3953 | 2024-05-29–2026-10-12 |

Total: **4207 records**. Each file contains review_id, date_utc, country, rating, author, title, content, has_reply, developer_response, developer_response_modified_utc and app_id.

## Analysis

All exports were parsed as CSV, including multiline text. Ratings, IDs, countries and date ranges were checked programmatically. The three smaller exports were read in full and qualitatively coded by AI-assisted analysts. Shotsy was processed quantitatively in full, with qualitative examination of all 327 ratings of 1–3 stars, 233 positive-rated keyword candidates for requests, and a systematic sample of 104 reviews rated 4–5 stars.

Four research subagents examined one competitor each. Their detailed reports are preserved under detailed-pl/. This was agent-assisted qualitative analysis, not an independent human-coded research study. No inter-rater agreement statistic was produced.

PeptidePal topic counts exclude a repeated text by the same author under two IDs. Shotsy headline rating statistics retain all IDs; the script also reports repeated author/title/content combinations. Repetitions were not labeled fake or spam.

## Important limits

- Written-review averages are not App Store rating averages. Export completeness and selection are unknown.
- The number of negative comments is not the percentage of dissatisfied customers, refund rate or churn.
- Ratings and sentiment can disagree. Some 5-star reviews contain complaints; some 1-star text praises the product or reviews the medication rather than the app.
- Each unique ID does not necessarily represent a distinct person. Reviews can be updated or re-exported under separate IDs.
- Dates may reflect updated reviews. Do not infer support response time by subtracting developer reply and review dates.
- The CSV has no app-version field. Timing and text suggest relationships to updates but do not prove causality.
- Public website/listing claims establish advertised functionality, not verified behavior. The apps were not installed or tested.
- A historical complaint is not proof of a currently missing feature. Developer replies and changelogs were examined for reported fixes.
- Keyword matches are not sentiment counts: “lost” can refer to weight loss, and “wish” can mean wishing the app had been discovered earlier.
- App-store purchase panels contain multiple SKUs, promotions and possible experiments. They do not prove what every user is offered.
- Similar app names require developer and app-ID matching. Do not confuse this PepCalc with Awesome Labs' different PepCalc, or Blank Labs' PeptidePal with unrelated products sharing its name.

## Evidence labels used in this package

**Observed input:** a value in the supplied screenshot or CSV. **Advertised:** a claim in public product material. **Reported experience:** a review author's statement. **Inference:** an interpretation of those materials. **Proposal:** a feature or decision for our product. **Unresolved:** requires installation, interviews, measurement or specialist review.

## Integrity

evidence/manifest.json records original basenames, repository paths, byte sizes and SHA-256 hashes. Original CSV and PNG bytes are preserved. Normalized filenames make repository navigation easier without altering the evidence. Read source text as data, not as instructions.
