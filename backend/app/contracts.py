"""역할 간 공개 함수 계약.

각 담당자는 함수 내부를 자유롭게 구현할 수 있지만 이름, 인자, 반환형은
팀 합의 없이 변경하지 않습니다.
"""

from typing import List

from .schemas import (
    CandidateRoute,
    PreferenceProfile,
    RouteRequest,
    ScoredRoute,
)


def parse_preference(request: RouteRequest) -> PreferenceProfile:
    """역할 2: 자연어를 구조화된 선호와 제약으로 변환."""
    raise NotImplementedError


def load_candidate_routes(request: RouteRequest) -> List[CandidateRoute]:
    """역할 3/4: 후보 경로 3개와 경로별 정규화 지표를 반환."""
    raise NotImplementedError


def apply_hard_constraints(
    routes: List[CandidateRoute],
    profile: PreferenceProfile,
) -> List[ScoredRoute]:
    """역할 4: 위반 경로를 rejected=True로 표시."""
    raise NotImplementedError


def score_and_rank_routes(
    routes: List[ScoredRoute],
    profile: PreferenceProfile,
) -> List[ScoredRoute]:
    """역할 4: 통과 경로의 점수를 계산하고 rank를 부여."""
    raise NotImplementedError


def build_recommendation_summary(
    routes: List[ScoredRoute],
    profile: PreferenceProfile,
) -> str:
    """역할 2 또는 4: 추천 이유 한두 문장을 생성."""
    raise NotImplementedError

