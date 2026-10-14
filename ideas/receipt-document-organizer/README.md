# Receipt scanner and document organizer

Status: **conditional second alternative**; resolve search intent before product selection. Snapshot: 14 October 2026.

## Original idea and revised interpretation

The original idea was a home purchase record: product photo, receipt, warranty/return information and a prepared document set for a claim. The screenshots show interest in receipt scanning, but do not establish demand for this particular home/warranty workflow.

Retain the broader scanning/document direction for an intent check. A personal warranty organizer, business expense tool and receipt-reward app are different markets and should not be merged into one vague MVP.

## Observed ASO

| Exact keyword | Popularity | Difficulty |
|---|---:|---:|
| receipt scanner | 51 | 43 |
| receipt organizer | 32 | 54 |
| free receipt scanner | 15 | 26 |
| free receipt organizer | 5 | 13 |
| receipt scanner for money | 5 | 17 |
| receipt scanner for taxes | 5 | 16 |

Sources: [scanner screenshot](evidence/receipt-scanner.png), [organizer screenshot](evidence/receipt-organizer.png), [structured results](evidence/aso-results.json), [integrity manifest](evidence/manifest.json).

Scanner's popularity 51 is interesting, but difficulty 43 is above the peptide reference of 28–29. A difference in index values is not a measured percentage difference in traffic. “For money”/“for taxes” suggestions indicate alternative possible uses; their low scores do not establish which use dominates the main keyword.

## Proposed scope if the home-document audience is validated

Capture/import a receipt; confirm extracted merchant/date/amount; attach product photo/name; enter return/warranty dates from actual terms; search records and export a document bundle. User-confirmed dates, no universal warranty duration or automatic legal conclusions.

Potential differentiator: fast retrieval of a complete purchase record when a return, repair or claim is needed. Basic scanning already exists widely; this needs task testing, not a claim of exclusivity.

## Risks

- Broad scanning demand may belong to expenses or rewards, not warranties.
- Home-document use may be sporadic and poorly suited to an annual subscription.
- OCR requires confirmation and correction; do not silently trust extracted totals/dates.
- Financial purchase documents require careful storage, export and privacy design.
- A receipt-reward product would need a separate commercial/data model, not just a scanner.

## Competitor examples examined

[Vaultable](https://vaultable.app/en/app) advertises purchase records, returns and warranties. [iTems](https://www.items-home.com/us) and [House Manager](https://house-app.com/home-inventory-app/) describe home inventory/document organization. These are public descriptions, not reviewed install flows or proof of successful monetization.

## Next investigation

Inspect the top apps for receipt scanner and classify their actual job: expenses, documents, rewards or general scanning. Then collect pricing and reviews for the relevant subgroup. Unmeasured keywords: home inventory, warranty tracker, return tracker. The uploaded scanner/organizer results cannot substitute for those measurements.
