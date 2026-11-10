# CRP 042 — Living Kernel / Series Closure

**State:** STORY MAP CLOSED · KERNEL OPEN · PROVENANCE PRESERVED  
**As of:** 2026-11-10  
**Canonical repository:** `DavidWise01/crime-and-punishment`  
**Browser entrypoint:** [Living Kernel](../living-kernel.html)  
**Canonical registry:** [registry.json](registry.json)  
**Baseline audit:** [audit-report.json](audit-report.json)  
**Audit source:** [audit.py](audit.py)  
**Recurring GitHub Actions:** [crp-living-audit.yml](../.github/workflows/crp-living-audit.yml)

## Closed narrative

Dostoevsky's public-domain novel has **41 mapped reading sections** in this project, each implemented as a book-side Canvas episode `B001–B041`. The 41 original film-side `F001–F041` episodes are symbolic evidence labs, **not** an adaptation, reproduction of the protected 2000 film, or a claim of shared event witnesses. Each boundary has a crosswalk `witness-crosswalk-001–041.html`. Crosswalk 001 was absent in the source tree and was added as an explicit 042 repair. These 123 page assets have distinct Git blob identities.

**042 is not a fabricated extra chapter.** The novel ends with the beginning of renewal. The kernel governs the story archive's ongoing evidence and verification, not the fictional characters' future.

## Runtime / living process

```text
  CANONICAL SOURCE: GITHUB (one ancestry)
                |
    41 x [BOOK / FILM / CROSSWALK]
                |
    KERNEL/REGISTRY.JSON (path + blob SHA)
                |
           [ BOOT ]      verify shape
                |
           [ SEE  ]      read selected chapter
                |
           [ DO   ]      audit served bytes on request
                |
           [ LEARN]      append classified witness packet
                |
           [ VERIFY ]    hash chain + source lineage
                |
           [ PRESERVE ]  browser export / CI artifact
                |
           [ RETURN ]    next observation, no silent edit
```

**User-facing runtime:** `living-kernel.html` loads `kernel/registry.json`, offers all 41 book/film/crosswalk triples, creates original Canvas2D art, compares published bytes with canonical Git blob IDs on request, and keeps a locally append-only SHA-256 event sequence. Evidence packets require a source label and a chosen classification: observation, inference, unknown or attributed claim. The ledger can be exported as JSON.

**Scope limit:** browser `localStorage` is not tamper-proof, not a signed legal record, not a server-side database, and can be cleared by the browser owner. The Git blob SHA-1 check verifies consistency with the Git registry; it is not a modern cryptographic attestation. There is no autonomous reasoning agent running after the tab closes.

**Unattended verifier:** the read-only GitHub Action runs on matching pushes, by manual dispatch, and every Monday at **12:00 UTC**. It checks the 123 required artifacts, registry blob hashes, HTML titles, and relative link destinations, validates the dashboard JavaScript syntax, then uploads a time-stamped audit JSON artifact with 90-day retention. The action does not rewrite source chapters or assert that GitHub Pages rendered correctly in a browser.

## Three witness roots / independence

1. **Source Git tree:** one canonical owned corpus and its immutable Git commits.
2. **CI audit of a checked-out commit:** an independently executed check of the *same* source ancestry, not a second independent narrative source.
3. **Browser-served Pages bytes:** a deployment consistency observation of the same source ancestry, *not* a third independent account of the novel or film.

The public Pages mirror and gated/private Git information must not be conflated. The public archive contains only material deliberately committed to this public repository. Witness-derived records must retain ancestry and access scope. An outside-source packet, when explicitly entered, must name its actual origin; aliases or mirrors do not create a new witness root.

## Baseline audit

GitHub Actions run [42921135929](https://github.com/DavidWise01/crime-and-punishment/actions/runs/42921135929) confirmed **123/123 required files**, **zero missing/source mismatch errors**, and **27 legacy warnings**. The warnings identify the inherited `PART III / CHAPTER I` header in book pages B015–B041. Several later sprite-triptych captions also retain an inherited template. These remain visible exceptions, not silent successes.

The updated CI workflow also passed its dashboard JavaScript syntax check at [run 42921598958](https://github.com/DavidWise01/crime-and-punishment/actions/runs/42921598958). Full end-to-end visual playback of all 82 episodes and all Pages responses has **not** been independently verified.

For historical integrity, legacy episode files have not been overwritten to cosmetically repair inherited scene labels. Their headers should not be treated as authoritative chapter metadata; the canonical registry, original reading order and release ledger take precedence. Future non-destructive presentation overlays may address the defects while preserving old Git history.

## Invariants / closeout contract

```yaml
STORY_MAP_COMPLETE != PERSON_COMPLETE
BEGINNING_OF_RENEWAL != COMPLETED_REDEMPTION
OBSERVATION != INFERENCE
ACCUSED != PROVEN_GUILTY
SOURCE_MIRROR != INDEPENDENT_WITNESS
GIT_COMMIT != VERIFIED_LIVE_DEPLOYMENT
LOCAL_HASH_CHAIN != SERVER_ATTESTATION
FUTURE_CHANGE_REQUIRES_NEW_EVIDENCE: true
HISTORICAL_CHAPTERS_RETAINED: true
AUTONOMOUS_SOURCE_REWRITES: false
```

**Closure:** 041 / 041 mapped book chapters; 041 / 041 symbolic film-side labs; 041 / 041 witness crosswalks; total 123 required HTML artifacts. **The authored series is closed; the audit and evidence kernel is living.**
