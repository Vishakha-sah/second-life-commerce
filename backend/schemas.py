from pydantic import BaseModel, Field
from typing import List, Optional

# --- Member A's AI Vision Requirements ---
class DamageLocation(BaseModel):
    box_2d: List[int] = Field(..., description="[ymin, xmin, ymax, xmax] coordinates")
    label: str

class GradeResponse(BaseModel):
    grade: str # e.g., "Good", "Like New"
    damage_list: List[str]
    confidence: float
    damage_locations: List[DamageLocation]

# --- Frontend Questionnaire Requirements ---
class QuestionnaireOption(BaseModel):
    id: str
    text: str

class Question(BaseModel):
    id: str
    question: str
    type: str # "radio" or "text"
    options: Optional[List[QuestionnaireOption]] = None

class QuestionnaireResponse(BaseModel):
    questions: List[Question]

# --- Frontend User Submit Contract ---
class UserAnswers(BaseModel):
    answers: dict

# --- Final Decision Requirements (Renamed to match Team Schema) ---
class RoutingDecisionResponse(BaseModel):
    decision: str # "resell", "refurbish", "donate", "recycle"
    reason: str
    second_life_score: float
    green_points_earned: int
    alternative_route: Optional[dict] = None
# --- Return Regret Predictor Contracts ---
class RegretRequest(BaseModel):
    category: str
    return_reason: str

class RegretResponse(BaseModel):
    regret_probability: float  # e.g., 85.5% probability that user will regret returning it
    insight_message: str       # Psychological retail actionable advice    
# --- Premium Analytics Contracts ---
class CO2ImpactResponse(BaseModel):
    product_id: str
    kg_co2_saved: float
    car_trip_equivalent_km: float
    insight_text: str

# --- Marketplace Filter Contracts ---
class MarketplaceListing(BaseModel):
    product_id: str
    ai_grade: str
    calculated_score: int
    final_action: str
    allocated_points: int

class ListingsResponse(BaseModel):
    listings: List[MarketplaceListing]    
# --- Admin & Redemption Contracts ---
class ReviewItem(BaseModel):
    product_id: str
    ai_grade: str
    calculated_score: int
    status: str # "flagged_for_review"

class AdminQueueResponse(BaseModel):
    flagged_items: List[ReviewItem]

class RedeemRequest(BaseModel):
    user_id: str
    points_to_redeem: int

class RedeemResponse(BaseModel):
    success: bool
    coupon_code: str
    discount_amount_inr: float
    remaining_points: int    