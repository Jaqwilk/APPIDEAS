# Market, ASO and economics

Snapshot: 14 October 2026. See [sources](sources.md). Numbers below are historical research observations or explicitly illustrative assumptions.

## Keyword evidence from screenshots

| US keyword | Popularity | Difficulty | Interpretation |
|---|---:|---:|---|
| peptide calculator | 49 | 29 | Specific task and a candidate acquisition keyword |
| peptide tracker | 48 | 28 | Specific recurring task and a candidate acquisition keyword |
| peptide | 22 | 16 | Lower and less precise signal |
| peptide calculator & dosage | 5 | 7 | Low difficulty with weak apparent demand |
| peptide library / calendar | 5 | 7 | Supplementary keywords, not a strong acquisition foundation |

The interface appears to be Astro. Its documentation says popularity comes from Apple Ads and difficulty is proprietary. A popularity of 49 is not 49,000 searches; difficulty 29 is not a success probability. Approximately 246–250 indexed apps does not mean that many equally strong competitors. Date/currency/period/scope of the estimate columns are not established by the screenshots.

Visible estimates include PeptidePal 200K revenue/30K downloads, Shotsy 300K/30K, Pep AI 30K/20K, and many others at 1K/1K. These are **unverified tool estimates**, not confirmed monthly earnings, profits, US-only totals or developer financials. The displayed PepCalc is publicly listed as free without visible IAP, which makes interpreting its 1K revenue especially questionable. The cause of the discrepancy is unknown.

Do not calculate customer LTV by dividing a month's estimated revenue by that month's new downloads. Renewals, annual upfront payments, installed-base size and acquisition expense make that misleading.

## Two different markets

1. **GLP-1 treatment tracking:** dose history, reminders, symptoms, weight and appointment preparation. Large audience, but strong specialist and general-health competition.
2. **Other/multiple peptide schedules:** containers, units, reserve stock, corrections and several schedules. A more complex organizing task, with less certain market size and greater medical/regulatory complexity.

KFF's late-2025 poll reported 12% of US adults currently using GLP-1 drugs and 18% ever using them. Gallup's July-2026 publication reported 11% using GLP-1 for weight loss in 2026 versus 3% in 2024. These are different questions and surveys, not one interchangeable series. They do not estimate users of BPC-157 or other research peptides, nor paid tracker demand.

No equally strong representative estimate for the non-GLP-1 peptide-tracker audience was established. Do not turn the GLP-1 population into the app's serviceable paying market.

## Competition outside the selected four

Peptide Tracker & Calculator by David Dzeveckij already advertises private local tracking with lower subscription prices. Flat Six Labs' Peptide Tracker Log & Reminder advertises a broad free tracker. MyFitnessPal supports GLP-1 tracking in selected countries/platforms; Oura has GLP-1 Insights in selected markets. These weaken a generic “basic tracker” proposition. The selected four are important competitors, not an exhaustive or proven revenue ranking of the entire market.

## Illustrative subscription economics

RevenueCat's 2026 report gives a median day-35 download-to-paid conversion of 3.5% for iOS Health & Fitness in its dataset. This is a broad benchmark, not a prediction for this idea.

Assume an annual purchase of $39.99 for every converted user and 15% Apple commission after qualification/enrollment in the relevant Small Business Program:

| Per 1000 installs | Buyers | First annual purchases gross | After commission only |
|---|---:|---:|---:|
| 2% conversion | 20 | $799.80 | $679.83 |
| 3.5% conversion | 35 | $1399.65 | $1189.70 |
| 6% conversion | 60 | $2399.40 | $2039.49 |

Taxes, refunds, support, infrastructure, acquisition and future renewals are omitted. At 3.5%, first-year receipts after commission are approximately $1.19 per install. If an install hypothetically costs $1.50, acquisition cost per buyer is about $42.86, exceeding approximately $33.99 first-year receipts before other costs. Renewals could improve this; they must be measured.

1000 active annual subscriptions at $39.99 correspond to about $3332.50/month gross annualized value and $2832.63/month after commission alone. This is an annualized equivalent, not uniform monthly cash flow or profit.

Treatment discontinuation can also reduce natural tracker retention. A 2025 real-world study reported substantial GLP-1 discontinuation in its cohort; it did not measure app retention. Avoid assuming years of subscription payments from every new user.

## Acquisition hypotheses

- Start with iOS/English/US as a constrained experiment.
- Test relevant high-intent App Store keywords; calculator positioning depends on permitted product scope.
- Show actual logging, correction and supply workflows in marketing.
- Publish useful organizational/export material without therapeutic claims.
- Explore clinician feedback and referral channels, acknowledging Shotsy already does this.
- Organic acquisition may be more forgiving than paid acquisition, but neither is guaranteed. SEO comparison pages from app developers are marketing, not independent rankings.

## Regulatory and data implications from the research

Apple guideline 1.4.2 sets specific requirements for drug-dosage calculators. Similar apps in the store do not guarantee acceptance. FDA distinguishes software functions and intended uses; tracking and user-configured reminders are materially different from recommending treatment or dosing. A disclaimer alone does not settle qualification.

FDA's GLP-1 material describes dosing errors and restrictions concerning unapproved products. Substance status must be checked individually; committee consideration or compounding-list discussion is not drug approval. Do not base revenue on promoting unapproved suppliers.

Consumer apps do not automatically fall under HIPAA, but FTC health-data obligations and other applicable rules can still matter. EU expansion requires a separate review of medical-software qualification and data requirements. These are design constraints to resolve before implementation, not a completed legal assessment.
