#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]

def load(path):
    with path.open(encoding='utf-8') as f: return yaml.safe_load(f)

def collect_evidence():
    ids={}; errors=[]
    for p in sorted((ROOT/'career_kb/experiences').glob('*.yaml')):
        d=load(p) or {}
        for section in ('problems','actions','outcomes','research'):
            for item in d.get(section,[]) or []:
                i=item.get('id')
                if not i: errors.append(f'{p}: missing id in {section}')
                elif i in ids: errors.append(f'duplicate evidence id {i}: {ids[i]} and {p}')
                else: ids[i]=str(p.relative_to(ROOT))
    return ids,errors

def collect_claims(evidence):
    claims={}; errors=[]
    for p in sorted((ROOT/'career_kb/claims').glob('*.yaml')):
        d=load(p) or {}
        if not d.get('experience_id'): errors.append(f'{p}: missing experience_id')
        for c in d.get('claims',[]) or []:
            cid=c.get('id')
            if not cid: errors.append(f'{p}: claim missing id'); continue
            if cid in claims: errors.append(f'duplicate claim id {cid}')
            claims[cid]=str(p.relative_to(ROOT))
            if not c.get('statement'): errors.append(f'{p}: {cid} missing statement')
            supported=c.get('supported_by') or []
            if not supported: errors.append(f'{p}: {cid} has no supported_by evidence')
            for eid in supported:
                if eid not in evidence: errors.append(f'{p}: {cid} references unknown evidence {eid}')
    return claims,errors

def main():
    evidence,e1=collect_evidence(); claims,e2=collect_claims(evidence); errors=e1+e2
    if errors:
        print('KB validation failed:'); [print(' -',e) for e in errors]; return 1
    print(f'KB validation passed: {len(evidence)} evidence IDs, {len(claims)} claim IDs')
    return 0
if __name__=='__main__': sys.exit(main())
