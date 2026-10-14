"""Recompute descriptive statistics from preserved CSVs; Python standard library only.

Run from any directory: python path/to/scripts/analyze_reviews.py
Writes research/statistics.json. Regex topics are mentions, not validated sentiment.
"""
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    'ease': r'easy|simple|intuitive|user.friendly',
    'levels': r'level|half.life|concentration',
    'weight_progress': r'weight|progress|goal|graph|chart',
    'site': r'injection site|shot location|rotate|rotation|where.*(?:shot|inject)',
    'reminders': r'remind|notification|countdown',
    'health_sync': r'apple health|health app|sync',
    'nutrition': r'protein|calorie|water|food|nutrition',
    'price_paywall': r'price|cost|expensive|subscription|paywall|paid|pay|free trial|charge|bait|greed',
    'data_loss': r'lost|missing|disappear|gone|wiped|not save|never save|doesn.t save|won.t save',
    'bugs': r'bug|glitch|crash|freeze|freez|doesn.t work|not work|won.t work|stuck|slow|load',
    'requests': r'wish|would like|please add|would be nice|needs to|need to add|missing|suggest|request|hope.*add',
    'export': r'export|pdf|doctor|provider|physician',
    'custom_multi': r'custom|multiple|other peptide|other med|more med|retatrutide|reta',
    'privacy': r'privacy|private|data harvesting|sell.*data',
    'review_nag': r'ask.*review|request.*review|nag|review.*(?:prompt|pop|annoy|ask)',
}
manifest=json.loads((ROOT/'evidence/manifest.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    contents=(ROOT/item['repository_path']).read_bytes()
    assert len(contents)==item['bytes']
    assert hashlib.sha256(contents).hexdigest()==item['sha256'], item['repository_path']

stats={'snapshot_date':'2026-10-14','unit':'written-review records, not all App Store ratings',
       'heuristic_warning':'Regex matches may include praise, negation, requests and false positives; not verified complaint counts.',
       'products':{}}
for path in sorted((ROOT/'evidence/reviews').glob('*.csv')):
    with path.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
    ratings=Counter(int(r['rating']) for r in rows)
    assert all(1<=int(r['rating'])<=5 for r in rows)
    unique_ids=len({r['review_id'] for r in rows})
    assert unique_ids==len(rows),path.name
    recent=[r for r in rows if r['date_utc']>='2026-09-01']
    entry={
        'rows':len(rows),'unique_review_ids':unique_ids,
        'ratings':{str(k):ratings[k] for k in range(1,6)},
        'mean':sum(int(r['rating']) for r in rows)/len(rows),
        'date_min':min(r['date_utc'] for r in rows),'date_max':max(r['date_utc'] for r in rows),
        'countries':dict(Counter(r['country'] for r in rows)),
        'app_ids':sorted({r['app_id'] for r in rows}),
        'developer_replies':sum(r['has_reply'].lower()=='true' for r in rows),
        'repeated_author_title_content_excess':len(rows)-len({(r['author'],r['title'],r['content']) for r in rows}),
        'repeated_author_content_excess':len(rows)-len({(r['author'],r['content']) for r in rows}),
        'since_2026_09_01':{'rows':len(recent),'ratings_1_2':sum(int(r['rating'])<=2 for r in recent),
                             'mean':sum(int(r['rating']) for r in recent)/len(recent) if recent else None},
    }
    if path.name.startswith('shotsy'):
        entry['regex_mentions']={name:{'all':sum(bool(re.search(pattern,r['title']+' '+r['content'],re.I)) for r in rows),
            'rating_1_3':sum(bool(re.search(pattern,r['title']+' '+r['content'],re.I)) for r in rows if int(r['rating'])<=3),
            'rating_4_5':sum(bool(re.search(pattern,r['title']+' '+r['content'],re.I)) for r in rows if int(r['rating'])>=4)}
            for name,pattern in PATTERNS.items()}
        original=json.loads((ROOT/'research/annotations/shotsy-original-heuristics.json').read_text(encoding='utf-8'))
        assert entry['rows']==original['rows']
        for name,value in entry['regex_mentions'].items():assert value['all']==original['heuristic'][name]['all'],name
    if path.name.startswith('pep-ai'):
        after=[r for r in rows if r['date_utc']>='2026-09-30']
        before=[r for r in rows if r['date_utc']<'2026-09-30']
        entry['redesign_period']={label:{'rows':len(group),'ratings_1_2':sum(int(r['rating'])<=2 for r in group),
            'mean':sum(int(r['rating']) for r in group)/len(group)} for label,group in [('before_2026_09_30',before),('from_2026_09_30',after)]}
        codes=json.loads((ROOT/'research/annotations/pepai-topics.json').read_text(encoding='utf-8'))['topics']
        ids={r['review_id'] for r in rows}
        for topic,values in codes.items():assert set(values)<=ids,topic
        entry['qualitative_topic_counts']={k:len(v) for k,v in codes.items()}
    if path.name.startswith('peptidepal'):
        with (ROOT/'research/annotations/peptidepal-topics.csv').open(encoding='utf-8-sig',newline='') as f:tags=list(csv.DictReader(f))
        ids={r['review_id'] for r in rows}
        for t in tags:assert t['review_id'] in ids
        entry['qualitative_topic_counts']=dict(Counter(t['theme'] for t in tags))
    stats['products'][path.stem]=entry
stats['total_records']=sum(v['rows'] for v in stats['products'].values())
assert stats['total_records']==4207
(ROOT/'research/statistics.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'total_records':stats['total_records'],'evidence_integrity':'10 files verified',
                  'counts':{k:v['rows'] for k,v in stats['products'].items()}},indent=2))
