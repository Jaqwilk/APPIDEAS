# MVP requirements

Status: proposed specification. Initial platform/language/market assumptions: iPhone, English, USA. No implementation stack or release date was selected.

## Included

| ID | Capability | First-release scope |
|---|---|---|
| MVP-01 | Schedules | Multiple user-defined items; selected weekdays or every N days; time; start; optional end; pause |
| MVP-02 | Actual-use record | Scheduled or additional entry; actual date/time; amount/unit; optional container/site/note |
| MVP-03 | Status | Planned, recorded, explicitly skipped, awaiting confirmation; absence of an entry is not proof of a missed administration |
| MVP-04 | Reminders | Based on user-entered schedule; permission requested in context; show next configured reminder |
| MVP-05 | Supply | In-use/reserve/finished containers, initial stock, actual usage, manual corrections, empty/discarded status |
| MVP-06 | Correction | Edit amount/date/container; undo; delete; reconcile corresponding supply movement |
| MVP-07 | Site history | Simple site map/list and previous sites; tracking rather than unsupported therapeutic claims |
| MVP-08 | Symptoms | Date, symptom, severity and note; explicit “no symptoms” distinct from no entry |
| MVP-09 | Weight | Manual value, chronological list and basic chart |
| MVP-10 | Data ownership | Offline records; backup, restore and CSV export from first release |
| MVP-11 | Report | Selected date range; recorded use, symptoms, weight and notes; basic and detailed presentation |

## Excluded at launch

AI/chatbot, social feed, mascot, comprehensive food database/scanning, hundreds-of-compounds encyclopedia, medication-level simulation, Watch app, automatic dose escalation and a sophisticated on/off-cycle generator. Health-platform sync and widgets are next-stage candidates.

A dose/reconstitution calculator is a separate gated module, not a dependency for releasing the diary. Resolve product qualification/store requirements and deterministic verification before adding it. Basic unit handling remains essential in the diary.

## Quantity and supply rules

- Mass (mg/mcg), volume (mL), biological activity (IU), count and syringe scale are different dimensions.
- Changing mg/mcg preserves physical quantity, not the original numeric value.
- Same-dimension stock use can be subtracted directly with supported normalization.
- If the recorded amount is mass but stock is volume, request the actual used volume or leave stock unchanged with a clear explanation. Do not invent a concentration or conversion.
- No universal conversion of IU to mass, or synonym treatment of IU and syringe markings.
- Each record retains its original amount/unit and relevant container context.
- Supply changes only for actual recorded usage, not planned or explicitly skipped events.
- Editing/deleting a record updates the linked usage transaction atomically. Moving an entry to a different container restores one and consumes the other.
- A manual count adjustment is a separate event with a reason. Discarding residual contents is not logged as administration.
- Forecast exhaustion is separate from recorded remaining stock. Only show a forecast when compatible schedule and stock data exist; otherwise explain what is missing.
- Dates such as opened/expiry are user-entered from instructions/labels. Do not silently generate clinical beyond-use advice.

## Schedule/history rules

Changing an actual entry does not silently rewrite future schedules. A schedule change has an effective date and preserves prior plan context. Time zone, daylight-saving and travel behavior must be specified and tested before implementation; never relabel historical actual times silently.

“Not recorded” is the default for past planned times without confirmation. A user can explicitly choose skipped or enter actual use later. Recording historical use must not require recreating a complex protocol.

## Conceptual data objects

Item; Schedule and effective-dated revisions; Scheduled occurrence; Actual-use record; Container; Inventory transaction; Symptom observation; Weight observation; Backup/export metadata; Purchase entitlement. These are conceptual requirements, not a prescribed database/schema or technology choice.

## Data and privacy

Local-first routine recording, no compulsory account for basic use, clear optional backup setup, and tested restore. Encryption and backup storage/provider details remain implementation decisions requiring security review. Do not promise backup until recovery has been demonstrated. If AI is later added, explain and consent to context transmission separately.

## Monetization hypothesis

| Free | Pro |
|---|---|
| One active schedule and one active container | Multiple active schedules and containers plus reserve management |
| Recording, reminders, correction, symptoms and weight | Combined multi-schedule/supply view and advanced filters |
| Backup, restore, CSV and basic PDF | Detailed configurable reports and additional summaries |

Initial test offer: $4.99/month or $39.99/year, 14-day Pro trial. This is a proposal, not a benchmark-backed optimal price. Show prices and free scope before personal setup. Use one clear entitlement/billing path initially and show purchase channel, renewal/trial end and cancellation destination.

After Pro ends, preserve all history, export and recovery. User selects one active schedule/container for Free; other plans and histories are archived/readable, not deleted. Do not create silent duplicate subscriptions or cut access to retained records.

## Acceptance criteria

- A new user records an actual entry without assistance.
- Editing date/amount/container and undo preserve history and supply consistency.
- Repeated save taps do not create duplicate records.
- Offline recording works and success is not shown before local persistence.
- Backup restores correctly after reinstall and on another supported device.
- No-container entry explicitly reports that supply did not change.
- Declined notification permission is visible and recoverable, not falsely presented as an active reminder.
- Expired Pro retains history/export and does not silently delete plans.
- Negative or incompatible inventory states are explained rather than silently accepted or clamped.
- Larger text and assistive navigation do not hide critical controls.
