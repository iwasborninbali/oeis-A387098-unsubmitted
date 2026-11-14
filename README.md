# OEIS A387098: reference for the zero region (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 15 Nov 2026).

- [A387098](https://oeis.org/A387098), Minevich et al., arXiv:2411.02251: **candidate** (2026-11-13: repository built (core c6)). Certificate: complete.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

T(n,k) counts placements of nonattacking kings on an n by n board with exactly k kings in each row and each column, for n≥1 and k≥0. Kings attack across a common side or corner; the empty placement gives T(n,0)=1. The triangle has row offset 1; for the zero-region statement extend this counting definition to all k≥0, including values outside the displayed triangle.

## Terms / result

No term changes. The live [A387098](https://oeis.org/A387098), read 2026-11-13, states the unattributed formula `Conjecture: T(n,k) = 0 for n < 4k, except for T(1,1)=1.` The preprint below establishes this, and T(4k,k)=2 for positive k.

## How it was obtained

Igor Minevich, Gabe Cunningham, K. Aditya Karan and Joshua V. Gyllinsky, *Parks: A Doubly Infinite Family of NP-Complete Puzzles and Generalizations of A002464*, preprint [arXiv:2411.02251](https://arxiv.org/abs/2411.02251), 2024, [doi:10.48550/arXiv.2411.02251](https://doi.org/10.48550/arXiv.2411.02251). Read 2026-11-13: [Section VII, Theorem 3](https://arxiv.org/html/2411.02251) states “there are only 2 possible configurations of trees for the 4c×4r puzzle”, and gives the minimum dimensions 4c×4r except the one-cell case. Taking c=r=k identifies trees with kings. Every king placement meeting the row and column counts can be made a Parks solution by taking each row as a park, so the additional park condition does not exclude a placement.

## Verification

The source theorem, definitions and correspondence were checked directly. The paper's proof and tabulated sequence values were not independently reverified. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Minevich and coauthors proved the relevant result in 2024, before the 2025 OEIS entry. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Open Section VII of the preprint and compare Theorem 3 with the definitions above; allow about ten minutes. No paper is bundled.

## Provenance

Source: `projects/science/athanor-oeis`, commit `11b7ea9cc6f4c0057731d8e36c023f8b36e7c27f`, `tasks/2026-11-12-A387098-zero-region/answers/2026-11-12-chatgpt.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
