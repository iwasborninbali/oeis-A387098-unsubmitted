# Independent verification — 2026-11-15

Target: `iwasborninbali/oeis-A387098-unsubmitted`, archived snapshot `779349a89d711baddc3759bf5aa0e2fa0472c0d7`. This review is independent of the producer and prior certificate. The archive contained `README.md`, `CERTIFICATE.md`, `PRIOR-ART.md`, and no pre-existing `verification/` files.

## Claim

**Exact certificate claim:** "Theorem 3 of Minevich et al. implies the zero region in A387098 and T(4k,k)=2 for positive k."

## Source check

**Primary source read:** Igor Minevich, Gabe Cunningham, K. Aditya Karan, Joshua V. Gyllinsky, *Parks: A Doubly Infinite Family of NP-Complete Puzzles and Generalizations of A002464*, [arXiv:2411.02251v1, 4 November 2024, HTML](https://arxiv.org/html/2411.02251), **Section VII, Theorem 3**, immediately after the heading *Minimal Configurations of Trees* (HTML source lines 212–221), with proof in that section (lines 219–251). The theorem says that, except for the `1 × 1` puzzle when `c=r=1`, the minimal dimensions are `4c × 4r`, and states: **"there are only 2 possible configurations of trees for the 4c×4r puzzle"**. It calls them the Shuriken arrangements; figures 14–17 and the proof elaborate. The paper's **Definition 1, Section II** (HTML lines 58–76) requires exactly `c` trees in each column, `r` in each row and each park, and no horizontal, vertical or diagonal touching.

**Mapping to A387098:** OEIS has `T(n,k)` for an `n × n` square, with exactly `k` nonattacking kings per row *and* column. Set `c=r=k` (for positive `k`), `m=n`, and designate each entire row as a separate park. All rows are connected parks and each has `r=k` trees, so this extra Parks condition imposes nothing new. Conversely, forgetting the parks yields the same king configuration. Therefore the theorem gives `T(n,k)=0` for `n<4k`, except `T(1,1)=1`, and exactly `T(4k,k)=2` for `k>=1`. This is an implication/correspondence, **not** an OEIS triangle formula literally printed in the paper. The source **supports the certificate claim exactly as an implication**. It does not address `k=0`, whose empty placement has `T(n,0)=1` by definition.

**Indexing/conventions:** OEIS row offset is **1** (`%O 1,6`); rows begin at `n=1`, column indices begin at `k=0`, with the extra `(1,1)` entry. The displayed triangle normally restricts `k<=floor(n/4)+[n=1]`; the zero region concerns the natural *extended* counting function for disallowed positive `k`. The paper assumes positive `c,r`, and uses `4c` rows by `4r` columns; with `c=r=k` their order is immaterial. Both count placements with cells occupied at most once and kings/trees prohibited from touching, including diagonally. Neither identifies configurations under board symmetries. Thus there is no off-by-one or board-topology mismatch.

**Limit of source check:** The statement, definitions and relevant proof were inspected, but this review does not constitute a line-by-line independent proof validation of Theorem 3. Finite cases are computed below.

## Independent computation

New code: [`verify_kings.py`](verify_kings.py), using only the Python standard library; results: [`output.log`](output.log). For each `n,k`, enumerate exactly `k` nonadjacent bits in a row, allow consecutive rows only if their kings avoid same/neighboring columns, and memoize a dynamic program over `(row number, previous row mask, packed per-column counts in base k+1)`. Accept only final states with every column count equal to `k`. This is exact integer arithmetic, with no use of the source's code, archived verification code, or OEIS program. For `k=0`, return the sole empty placement directly.

**Coverage:** 42 checks: `k=0,1` and `1<=n<=16`; `k=2` at `n=7..11`; `k=3` at `n=11..13`; `k=4` at `n=15..16`. All **42/42 PASS** against the OEIS-listed terms and extended zero-region cases. Specifically: `T(1,1)=1`; `T(3,1)=T(7,2)=T(11,3)=T(15,4)=0`; `T(4,1)=T(8,2)=T(12,3)=T(16,4)=2`. Additional checks: `T(9,2)=664`, `T(10,2)=146510`, `T(11,2)=31197434`, `T(13,3)=42732`; `T(n,1)` through `n=16` agrees throughout. See the log for every output value and memoized-state count. These checks do not prove the infinite claim.

Environment: Python 3.13.5; **CPU 10.858 s; wall 10.865 s** for the logged run (times vary by machine).

SHA-256 (`sha256sum` of the exact UTF-8 bytes, including trailing newline):

```text
f6d2af13dcaee2057f0360b6455b6ad5a4caa7eb541d852ce50e7cca0d747adc  verify_kings.py
7de97e04244e9476f7e462bbf6e02cf3b7dc35799a015408f0491c097c68a58d  output.log
```

## Entry check

Read the current [A387098 live entry](https://oeis.org/A387098) on 2026-11-15 and its [b-file](https://oeis.org/A387098/b387098.txt). The entry's **COMMENTS** already say: `For k >= 1, the first nonzero term in column k appears at row n = 4k, where T(4k, k) = 2`; its **FORMULA** already says: `Conjecture: T(n,k) = 0 for n < 4k, except for T(1,1)=1.` It contains **no reference/link to Minevich et al. or arXiv:2411.02251**, and does not say that the conjecture has been proved. The `%N`, `%C`, `%F`, `%O`, `%Y` fields were also cross-checked against a [search-engine-indexed copy of A387098's internal format](https://oeis.org/A387098/internal); direct requests for the **internal format** and the [official history](https://oeis.org/history?seq=A387098) were rejected (403/disabled), so **the full edit history could not be inspected**. The live entry confirms the current absence of the citation, but historical absence is not independently established.

**Prior art / alternate sources:** This is **not a new mathematical theorem**: the relevant proof is the 2024 preprint, predating A387098's October 2025 authorship date. [OEIS A400547](https://oeis.org/A400547), entered September 2026, already cites Minevich et al. and cross-references A387098; the [OEIS citation index](https://oeis.org/wiki/CiteM) also lists the paper under A002464. Therefore the paper is **already cited elsewhere in OEIS**, but not in **A387098**. A [2025 SSRN posting by the same authors](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5653012), with an expanded title mentioning *OEIS A002464*, appears newer (posted 24 October 2025), but its full paper was blocked and its precise theorem was **not verified**; it cannot be recommended as a better checked replacement. The peer-reviewed 2023 [Laszlo–Mukherjee *Counting Star-Battle Configurations*](https://nsuworks.nova.edu/gscis_facarticles/530/) treats the `k=2` case, not the full positive-`k` generality. No newer **verified** source superseding arXiv Theorem 3 was found.

## Verdict

**COMPLETE — as a new reference and correction of attribution/proof status in A387098, not as a new result or new sequence terms.** The primary source explicitly states the minimum and the two configurations; its definitions align and the row-as-park bijection establishes the advertised implication. The live entry already **states both numerical facts**, including the zero-region statement labeled conjectural, but **does not cite the proof**. The novel contribution to this entry is to supply the 2024 source and remove the unjustified *Conjecture* qualification. Caveats: OEIS's full edit history was inaccessible; the source proof was not re-proved in full; finite enumeration is not a general proof. These caveats do not undermine this *bibliographic* verification, which rests on an independently read explicit theorem.
