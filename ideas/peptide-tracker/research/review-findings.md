# Review findings

Read [methodology](evidence-and-methodology.md) before interpreting counts. Topic categories overlap. Counts describe supplied written reviews, not all users. Detailed Polish reports contain dates, titles, IDs, replies and historical-fix context.

## Exact rating distribution

| Product | 1★ | 2★ | 3★ | 4★ | 5★ | Mean |
|---|---:|---:|---:|---:|---:|---:|
| PeptidePal | 62 | 9 | 8 | 4 | 29 | 2.3661 |
| Pep AI | 65 | 12 | 8 | 7 | 46 | 2.6884 |
| PepCalc | 0 | 1 | 0 | 1 | 2 | 4.0000 |
| Shotsy | 134 | 76 | 117 | 345 | 3281 | 4.6603 |

## PeptidePal

Liked: one place instead of notes, specialized library, reminders, community for some users and responsive improvements. October 5 “LOVE This App” (14631875334, 5★) is fresh positive evidence.

Qualitatively coded complaints/requests: price/trial/payment/value 26; history/editing/dates 18; onboarding/account 12; AI 6; support 5; calculation persistence/units 4. The duplicate author's repeated text is counted once for topics.

Evidence:

- 14551515036, 2026-09-15, 1★: wants time tracking without extended onboarding and account friction.
- 14623800201, 2026-10-03, 1★: wants calculations retained.
- 14523306731, 2026-09-07, 3★: actual use date differs from scheduled day.
- 14349785670, 2026-07-26, 1★: expects inventory subtraction; developer says configuration enables it.
- 14298951375, 2026-07-13, 5★: asks for CSV, symptoms, timing and schedule changes.

Inference: shorten first use and make correction and supply linkage explicit. Do not claim editing/supply subtraction are absent today.

## Pep AI

Liked: many schedules, inventory, replacing notebooks, all-in-one health features for some users, and fast feedback implementation.

Qualitatively coded themes: negative redesign reaction 28; removed/hard-to-find calculator/conversion/units after redesign 15; data/saving/login 12; billing/trial/cancellation 10; AI complaints 7. Lists of IDs are preserved in [annotations](annotations/pepai-topics.json).

From September 30 onward: 34 records, 27 rated 1–2★, mean 1.7941. Earlier: 104 records, mean 2.9808. The comparison describes a selected corpus and does not measure churn or establish update causality.

Evidence:

- 14625335194, 2026-10-04, 2★: updates and clutter disrupt quick daily recording.
- 14298998225, 2026-07-13, 1★: repeat setup and returning as a new user.
- 14406725241, 2026-08-09, 2★: units do not fit every substance; IU/syringe units need correct distinctions.
- 14549731895, 2026-09-14, 2★: complicated configuration and reported Apple/Stripe duplicate subscriptions.
- 14532254005, 2026-09-10, 2★: willing to pay after understanding value, not immediately.
- 14515589996, 2026-09-06, 5★: tried the product and found payment worthwhile.

Subsequent releases/replies report calculator restoration in 4.0.1, syringe-unit visibility in 4.0.2 and Classic look in 4.0.3. Some users confirm restoration. Proposed differentiation is stable behavior and optional modules, not just dark mode.

## PepCalc

Only four written reviews. Two independent comments ask for an easy mcg/mg switch (December 2025 and September 2026). Positive comments praise ease, reduced mental arithmetic and presentation without rounding. The listing advertises both units; this mismatch requires hands-on verification, not an assertion of a confirmed current bug.

There is no evidence in this tiny export of demand for AI, reminders, exports, backup or a subscription. Better unit ergonomics is a task-level opportunity, not evidence of a paying market.

## Shotsy

Strong positive signal: 3626 records rated 4–5★ (91.73%). Liked: ease, progress graphs, injection-site memory, widgets, estimated levels and integration. Users also value the free version, so praise does not automatically imply willingness to pay.

Recent period September 1–October 12: 190 records, mean 4.3789; 21 rated 1–2★ and 33 rated 1–3★. This does not measure the whole user base.

Recurring qualitative issues: price/trial/upgraded rights, disappearing records, reminders, sync, device migration, editing and premature rating prompts. Historical fixes must be considered.

Useful positive-rated requests:

- 12112742006, 2024-12-27, 5★: vial size, remaining stock and reorder reminder.
- 12843773301, 2025-07-02, 5★: refill reminders handled elsewhere.
- 13310247996, 2025-10-25, 5★: more detailed report rather than summaries alone.
- 14241028586, 2026-06-29, 5★: unit logging and skipping when stock has run out.
- 14526787312, 2026-09-08, 5★: cannot find multiple-medication tracking, although it exists.

Critical examples:

- 14621169806, 2026-10-03, 3★: unreliable saves.
- 14581750760, 2026-09-22, 2★: saving problems.
- 14651916457, 2026-10-11, 3★: notifications.
- 14116767761, 2026-05-28, 3★: migration between platforms.

The original keyword scan counted 1598 weight/progress matches, 1048 ease matches and 477 level matches. These are broad regex matches, not sentiment-validated feature endorsements. In particular, 147 “lost/missing” matches are NOT 147 data-loss incidents. Patterns and exact results are preserved in annotations/.

## Cross-product conclusions

1. The task is organization and remembering, not necessarily medical education.
2. First-use/payment transparency and discoverability repeatedly matter.
3. Users need correction, backdating and actual-vs-planned distinction.
4. Some users like wider health features; others want a smaller stable tool. Optionality is preferable to forcing every module on everyone.
5. Inventory must explain its state and connect to actual recorded use.
6. Data durability and portability underpin trust.
7. Positive reviews with specific requests can be more informative than general one-star price complaints.
8. Estimated medication levels must not be described as measurements or used as proof of clinical accuracy.

Neither the source CSVs nor these conclusions establish customer acquisition costs, population market share, revenue causation or willingness to pay for our proposed combination.
