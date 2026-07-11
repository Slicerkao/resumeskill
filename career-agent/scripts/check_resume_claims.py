#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]

def load(p):
    with p.open(encoding='utf-8') as f:return yaml.safe_load(f)

def indexes():
    evidence=set(); claims={}
    for p in (ROOT/'career_kb/experiences').glob('*.yaml'):
        d=load(p) or {}
        for sec in ('problems','actions','outcomes','research'):
            evidence.update(x['id'] for x in d.get(sec,[]) or [] if x.get('id'))
    for p in (ROOT/'career_kb/claims').glob('*.yaml'):
        for c in (load(p) or {}).get('claims',[]) or []: claims[c['id']]=c
    return evidence,claims

def main(path):
    d=load(Path(path)); evidence,claims=indexes(); errors=[]; n=0
    for section,entries in (d.get('sections') or {}).items():
        for entry in entries or []:
            for b in entry.get('bullets',[]) or []:
                n+=1; cids=b.get('claim_ids') or []; eids=b.get('evidence_ids') or []
                if not cids: errors.append(f'{section} bullet {n}: no claim_ids')
                for c in cids:
                    if c not in claims: errors.append(f'{section} bullet {n}: unknown claim {c}')
                for e in eids:
                    if e not in evidence: errors.append(f'{section} bullet {n}: unknown evidence {e}')
                required=set()
                for c in cids:
                    if c in claims: required.update(claims[c].get('supported_by') or [])
                if not required.issubset(set(eids)):
                    errors.append(f'{section} bullet {n}: missing supporting evidence {sorted(required-set(eids))}')
    if errors:
        print('Claim validation failed:'); [print(' -',e) for e in errors]; return 1
    print(f'Claim validation passed: {n} bullets')
    return 0
if __name__=='__main__':
    if len(sys.argv)!=2: print('usage: check_resume_claims.py MANIFEST.yaml'); sys.exit(2)
    sys.exit(main(sys.argv[1]))
