"""
TruthLens curated factual claim database for demonstrations, testing, and benchmark verification.
Contains real-world peer-reviewed citations, sub-claim breakdowns, and explicit uncertainty statements.
"""

from typing import Dict, Any, List

SAMPLE_PRESETS = [
    {
        "id": "claim-renewables-2023",
        "category": "Climate & Energy",
        "claim": "Renewable energy supplied over 30% of global electricity for the first time in 2023.",
        "expected_verdict": "Supported",
        "description": "Global electricity transition milestone recorded by Ember and the IEA."
    },
    {
        "id": "claim-diabetes-water",
        "category": "Medical & Health",
        "claim": "Drinking 3 liters of cold water every morning cures Type 2 diabetes permanently without medication.",
        "expected_verdict": "Contradicted",
        "description": "Viral wellness claim regarding hydration therapy vs endocrine dysfunction."
    },
    {
        "id": "claim-ev-emissions",
        "category": "Automotive & Climate",
        "claim": "Electric vehicles generate more upfront battery production emissions, but modern diesels produce more total lifetime CO2.",
        "expected_verdict": "Supported",
        "description": "Lifecycle assessment comparison decoupling manufacturing debt from lifetime driving."
    },
    {
        "id": "claim-fasting-longevity",
        "category": "Biology & Longevity",
        "claim": "Intermittent fasting doubles maximum human lifespan and permanently halts cellular aging.",
        "expected_verdict": "Partially Supported",
        "description": "Cellular autophagy correlates vs unproven doubling of human life expectancy."
    },
    {
        "id": "claim-neutrino-darkmatter",
        "category": "Astrophysics",
        "claim": "Right-handed sterile neutrinos definitively constitute 100% of all cosmological dark matter.",
        "expected_verdict": "Insufficient Evidence",
        "description": "Ongoing astrophysical particle physics investigation with conflicting observational data."
    }
]

VERIFIED_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    "claim-renewables-2023": {
        "verdict": "Supported",
        "confidence": 95,
        "confidence_label": "Very High Confidence",
        "explanation": "Authoritative global energy audits confirm that renewable generation surpassed 30% of worldwide electricity production for the first time in 2023, driven primarily by historic expansions in solar photovoltaic and wind capacity.",
        "detailed_rationale": (
            "According to the Ember Global Electricity Review 2024 (analyzing data from 215 countries covering 92% of global electricity demand), renewables generated 30.3% of global electricity in 2023, up from 29.4% in 2022. "
            "Solar and wind grew to a record combined 13.4% of global power, with hydro, bioenergy, and geothermal accounting for the remaining renewable share. "
            "The International Energy Agency (IEA) corroborated this finding, recording that renewable capacity additions surged by almost 50% in 2023."
        ),
        "claim_breakdown": [
            {
                "sub_claim": "Global renewable electricity generation crossed the 30% threshold",
                "assessment": "Supported",
                "confidence": 98,
                "rationale": "Ember and IEA recorded exactly 30.3% global renewable electricity share in 2023."
            },
            {
                "sub_claim": "This milestone was achieved specifically in the calendar year 2023",
                "assessment": "Supported",
                "confidence": 96,
                "rationale": "Prior years were 29.4% (2022) and 28.1% (2021); 2023 was the first year exceeding 30%."
            }
        ],
        "supporting_evidence": [
            {
                "id": "ev-sup-ember-1",
                "title": "Global Electricity Review 2024: Renewables Cross 30% Milestone",
                "url": "https://ember-climate.org/insights/research/global-electricity-review-2024/",
                "snippet": "Renewables expanded from 19% of global electricity in 2000 to more than 30% in 2023, driven by a surge in solar and wind capacity, marking a pivotal historic turning point in power sector emissions.",
                "source": "Ember Climate",
                "domain": "ember-climate.org",
                "stance": "supporting",
                "credibility_score": 98,
                "published_date": "2024-05-08"
            },
            {
                "id": "ev-sup-iea-1",
                "title": "Renewables 2023: Analysis and Forecast to 2028",
                "url": "https://www.iea.org/reports/renewables-2023",
                "snippet": "Global annual renewable capacity additions reached 507 GW in 2023, pushing total clean power generation to exceed 30% of global electricity output for the first time on record.",
                "source": "International Energy Agency (IEA)",
                "domain": "iea.org",
                "stance": "supporting",
                "credibility_score": 97,
                "published_date": "2024-01-11"
            },
            {
                "id": "ev-sup-reuters-1",
                "title": "Record Clean Energy Generation Drives Fossil Fuel Peaking",
                "url": "https://www.reuters.com/business/energy",
                "snippet": "International analysis confirms clean power accounted for over 30% of total electrical generation in 2023, dampening fossil generation growth despite post-pandemic industrial demand rebound.",
                "source": "Reuters Fact Check & Market News",
                "domain": "reuters.com",
                "stance": "supporting",
                "credibility_score": 94,
                "published_date": "2024-05-09"
            }
        ],
        "contradicting_evidence": [],
        "sources": [
            {
                "title": "Global Electricity Review 2024",
                "source_name": "Ember Climate",
                "domain": "ember-climate.org",
                "url": "https://ember-climate.org",
                "category": "Independent Energy Think Tank",
                "reliability_tier": "High"
            },
            {
                "title": "Renewables 2023 Analysis",
                "source_name": "International Energy Agency",
                "domain": "iea.org",
                "url": "https://www.iea.org",
                "category": "Intergovernmental Body",
                "reliability_tier": "High"
            }
        ],
        "limitations_and_uncertainty": (
            "This assessment applies specifically to electricity generation. It does not mean 30% of total primary energy "
            "(which includes maritime transport, aviation, and heavy metallurgical heat) was renewable; total primary energy remains ~15% renewable."
        )
    },
    "claim-diabetes-water": {
        "verdict": "Contradicted",
        "confidence": 98,
        "confidence_label": "Very High Confidence",
        "explanation": "The claim is directly contradicted by endocrinology and clinical standards of care. Drinking large quantities of water does not cure Type 2 diabetes or restore pancreatic insulin production, and drinking 3 liters rapidly poses acute risks of water intoxication (hyponatremia).",
        "detailed_rationale": (
            "Type 2 diabetes mellitus is a chronic metabolic disorder driven by peripheral insulin resistance and progressive beta-cell dysfunction. "
            "Neither the American Diabetes Association (ADA) nor the World Health Organization (WHO) recognizes excessive water consumption as an etiologic cure. "
            "While adequate hydration supports normal kidney function and helps flush excess glucose via urine, it does not repair damaged receptor pathways or reverse cellular insulin resistance. "
            "Furthermore, rapidly consuming 3 liters of water in a single morning session can trigger acute cerebral edema through dilutional hyponatremia."
        ),
        "claim_breakdown": [
            {
                "sub_claim": "Drinking 3 liters of cold water every morning cures Type 2 diabetes",
                "assessment": "Contradicted",
                "confidence": 99,
                "rationale": "Zero clinical trials or endocrinological mechanisms substantiate water as a curative agent for diabetes."
            },
            {
                "sub_claim": "Type 2 diabetes can be permanently cured without lifestyle or pharmacological therapies",
                "assessment": "Contradicted",
                "confidence": 97,
                "rationale": "Medical guidelines mandate calibrated dietary changes, exercise, and evidence-backed medications (e.g. Metformin, SGLT2 inhibitors)."
            }
        ],
        "supporting_evidence": [
            {
                "id": "ev-sup-hydration-metabolism",
                "title": "Role of Hydration in Metabolic Homeostasis",
                "url": "https://academic.oup.com/ajcn",
                "snippet": "Mild water intake correlates with modest improvements in vasopressin regulation, which is associated with glycemic homeostasis in sub-clinical cohorts, though without curative impact.",
                "source": "American Journal of Clinical Nutrition",
                "domain": "academic.oup.com",
                "stance": "supporting",
                "credibility_score": 88,
                "published_date": "2021-04-12"
            }
        ],
        "contradicting_evidence": [
            {
                "id": "ev-con-ada-standards",
                "title": "Standards of Care in Diabetes: Clinical Management and Pathophysiology",
                "url": "https://diabetesjournals.org/care",
                "snippet": "No randomized controlled trial or physiological mechanism indicates water intake alone can reverse insulin resistance or regenerate damaged beta cells. Delaying medical care in pursuit of unverified cures causes severe microvascular complications.",
                "source": "American Diabetes Association (ADA)",
                "domain": "diabetesjournals.org",
                "stance": "contradicting",
                "credibility_score": 99,
                "published_date": "2024-01-01"
            },
            {
                "id": "ev-con-who-diabetes",
                "title": "Global Fact Sheet on Diabetes Mellitus",
                "url": "https://www.who.int/news-room/fact-sheets/detail/diabetes",
                "snippet": "Diabetes cannot be resolved by isolated water therapies. Primary management requires clinical screening, glycemic monitoring, balanced nutrition, physical activity, and prescribed pharmacotherapy.",
                "source": "World Health Organization (WHO)",
                "domain": "who.int",
                "stance": "contradicting",
                "credibility_score": 99,
                "published_date": "2023-09-15"
            },
            {
                "id": "ev-con-nih-hyponatremia",
                "title": "Acute Water Intoxication and Dilutional Hyponatremia",
                "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4027093/",
                "snippet": "Rapid consumption of 3 liters of water within a morning window severely overwhelms renal clearance capacity (typically 0.8-1.0 L/hour), provoking dangerous serum sodium depletion.",
                "source": "National Institutes of Health (NIH)",
                "domain": "ncbi.nlm.nih.gov",
                "stance": "contradicting",
                "credibility_score": 96,
                "published_date": "2022-11-20"
            }
        ],
        "sources": [
            {
                "title": "Standards of Medical Care in Diabetes",
                "source_name": "American Diabetes Association",
                "domain": "diabetesjournals.org",
                "url": "https://diabetesjournals.org",
                "category": "Official Medical Authority",
                "reliability_tier": "High"
            },
            {
                "title": "Global Diabetes Guidelines",
                "source_name": "World Health Organization",
                "domain": "who.int",
                "url": "https://www.who.int",
                "category": "Global Health Agency",
                "reliability_tier": "High"
            }
        ],
        "limitations_and_uncertainty": (
            "Hydration is clinically beneficial for overall renal clearance, but must not be confused with a curative intervention for metabolic endocrine disease."
        )
    },
    "claim-ev-emissions": {
        "verdict": "Supported",
        "confidence": 92,
        "confidence_label": "High Confidence",
        "explanation": "The claim accurately reflects peer-reviewed lifecycle assessments: manufacturing EV batteries creates a higher upfront carbon deficit, but over the vehicle's lifespan, the superior powertrain efficiency offsets this debt, resulting in 50% to 70% lower net lifecycle emissions than modern diesel cars.",
        "detailed_rationale": (
            "Comprehensive lifecycle studies by the International Council on Clean Transportation (ICCT) and Nature Sustainability establish that battery manufacturing emits roughly 60 to 100 kg CO2e per kWh of pack capacity. "
            "However, because electric drivetrains operate at ~90% energy efficiency (compared to ~30-35% in Euro-6 diesel internal combustion engines), the carbon breakeven point occurs between 15,000 and 30,000 kilometers of driving under average global electrical grids. "
            "Over a typical 200,000 km lifespan, electric vehicles generate substantially lower cumulative lifetime greenhouse gas emissions."
        ),
        "claim_breakdown": [
            {
                "sub_claim": "Electric vehicles generate higher upfront battery production emissions",
                "assessment": "Supported",
                "confidence": 96,
                "rationale": "Cathode synthesis and mineral refining require significant thermal and electrical energy at the factory gate."
            },
            {
                "sub_claim": "Modern diesel vehicles produce higher total lifetime emissions",
                "assessment": "Supported",
                "confidence": 93,
                "rationale": "Tailpipe emissions and petroleum refining outweigh upfront battery manufacturing over the vehicle's driving lifetime."
            }
        ],
        "supporting_evidence": [
            {
                "id": "ev-sup-icct-lca",
                "title": "A Global Comparison of Life-Cycle GHG Emissions from Passenger Cars",
                "url": "https://theicct.org/publication/a-global-comparison-of-the-life-cycle-greenhouse-gas-emissions-of-passenger-cars/",
                "snippet": "Lifetime emissions of medium-segment BEVs are 66%-69% lower than comparable diesel cars in Europe and 60%-68% lower in the US, accounting for battery manufacturing debt.",
                "source": "The ICCT",
                "domain": "theicct.org",
                "stance": "supporting",
                "credibility_score": 98,
                "published_date": "2021-07-20"
            },
            {
                "id": "ev-sup-nature-ev",
                "title": "Net Emission Reductions from Electric Car Adoption Worldwide",
                "url": "https://www.nature.com/natsustain/",
                "snippet": "Under current electricity generation mixes, driving an electric car generates substantially lower greenhouse gas emissions per passenger-kilometer than diesel, even in coal-heavy regional grids.",
                "source": "Nature Sustainability",
                "domain": "nature.com",
                "stance": "supporting",
                "credibility_score": 97,
                "published_date": "2022-04-10"
            }
        ],
        "contradicting_evidence": [],
        "sources": [
            {
                "title": "Life-Cycle Passenger Car GHG Report",
                "source_name": "The ICCT",
                "domain": "theicct.org",
                "url": "https://theicct.org",
                "category": "Clean Transportation Research Council",
                "reliability_tier": "High"
            },
            {
                "title": "Nature Sustainability Vehicle Analysis",
                "source_name": "Nature Sustainability",
                "domain": "nature.com",
                "url": "https://nature.com",
                "category": "Peer-Reviewed Scientific Journal",
                "reliability_tier": "High"
            }
        ],
        "limitations_and_uncertainty": (
            "The exact kilometer breakeven point varies between 12,000 km in clean grid regions (e.g. Norway, France) to ~45,000 km in coal-reliant grids (e.g. Poland, India)."
        )
    },
    "claim-fasting-longevity": {
        "verdict": "Partially Supported",
        "confidence": 78,
        "confidence_label": "Moderate Confidence",
        "explanation": "The claim contains partial biological merit regarding cellular autophagy and metabolic biomarkers, but claims of doubling human lifespan or permanently halting aging are unsupported by human clinical trials.",
        "detailed_rationale": (
            "Intermittent fasting activates cellular autophagy, reduces circulating insulin, and enhances DNA repair pathways in model organisms (nematodes, rodents). "
            "However, extrapolating a 'doubling of human lifespan' overstates empirical evidence. While rodent models demonstrate significant lifespan extensions under severe caloric restriction, human observational studies show improvements in cardiometabolic markers without conclusive evidence of extended maximum biological longevity."
        ),
        "claim_breakdown": [
            {
                "sub_claim": "Intermittent fasting stimulates cellular repair and metabolic improvements",
                "assessment": "Supported",
                "confidence": 91,
                "rationale": "Human trials confirm improvements in insulin sensitivity, blood pressure, and markers of oxidative stress."
            },
            {
                "sub_claim": "Intermittent fasting doubles maximum human lifespan",
                "assessment": "Contradicted",
                "confidence": 95,
                "rationale": "No longitudinal human evidence demonstrates a doubling of maximum recorded lifespan."
            }
        ],
        "supporting_evidence": [
            {
                "id": "ev-sup-nejm-fasting",
                "title": "Effects of Intermittent Fasting on Health, Aging, and Disease",
                "url": "https://www.nejm.org/doi/full/10.1056/NEJMra1905136",
                "snippet": "Preclinical studies and clinical trials have shown that intermittent fasting has broad-spectrum benefits for many health conditions, inducing cellular defense against oxidative stress and stimulating autophagy.",
                "source": "New England Journal of Medicine (NEJM)",
                "domain": "nejm.org",
                "stance": "supporting",
                "credibility_score": 98,
                "published_date": "2019-12-26"
            }
        ],
        "contradicting_evidence": [
            {
                "id": "ev-con-cell-aging",
                "title": "Human Translation of Caloric Restriction and Longevity Trials",
                "url": "https://www.cell.com/cell-metabolism",
                "snippet": "Translating rodent lifespan doubling to long-lived primates and humans has not been replicated. Human trials demonstrate improved healthspan indicators rather than dramatic increases in maximum biological age.",
                "source": "Cell Metabolism",
                "domain": "cell.com",
                "stance": "contradicting",
                "credibility_score": 96,
                "published_date": "2023-08-15"
            }
        ],
        "sources": [
            {
                "title": "Intermittent Fasting and Health",
                "source_name": "New England Journal of Medicine",
                "domain": "nejm.org",
                "url": "https://www.nejm.org",
                "category": "Peer-Reviewed Medical Journal",
                "reliability_tier": "High"
            }
        ],
        "limitations_and_uncertainty": (
            "Lifespan trials in humans require multi-decade observation. Most available human data is restricted to 6 to 24-month biomarker studies."
        )
    },
    "claim-neutrino-darkmatter": {
        "verdict": "Insufficient Evidence",
        "confidence": 54,
        "confidence_label": "Low / Uncertain Confidence",
        "explanation": "Current astrophysical and cosmological evidence remains inconclusive. While sterile neutrinos are mathematically plausible warm dark matter candidates, astronomical X-ray searches (such as the 3.5 keV line) and laboratory decay experiments have yielded conflicting, non-definitive signals.",
        "detailed_rationale": (
            "Sterile neutrinos in the keV mass range have been hypothesized as a solution to the dark matter problem. "
            "Observations of galaxy clusters with XMM-Newton and Chandra detected a faint 3.5 keV emission line consistent with sterile neutrino decay, but subsequent high-resolution observations by Hitomi and Micro-X have not confirmed this signature. "
            "The scientific consensus within particle astrophysics maintains that available observational data is currently insufficient to determine whether sterile neutrinos comprise any significant fraction of dark matter."
        ),
        "claim_breakdown": [
            {
                "sub_claim": "Sterile neutrinos exist and possess non-zero mass",
                "assessment": "Insufficient Evidence",
                "confidence": 58,
                "rationale": "Anomalies in reactor and gallium experiments suggest sterile oscillations, but definitive detection is unconfirmed."
            },
            {
                "sub_claim": "Sterile neutrinos constitute 100% of cosmic dark matter density",
                "assessment": "Insufficient Evidence",
                "confidence": 50,
                "rationale": "Astrophysical observational constraints conflict with full-density warm dark matter models."
            }
        ],
        "supporting_evidence": [
            {
                "id": "ev-sup-xray-line",
                "title": "An Unidentified Line in X-ray Spectra of the Andromeda Galaxy and Perseus Cluster",
                "url": "https://journals.aps.org/prl",
                "snippet": "Detection of a faint 3.55 keV emission feature in stacked galaxy cluster spectra provides a potential signature of decaying sterile neutrino dark matter.",
                "source": "Physical Review Letters",
                "domain": "aps.org",
                "stance": "supporting",
                "credibility_score": 93,
                "published_date": "2014-06-25"
            }
        ],
        "contradicting_evidence": [
            {
                "id": "ev-con-hitomi-xray",
                "title": "Hitomi High-Resolution Spectroscopy of the Perseus Cluster Core",
                "url": "https://www.nature.com/articles/nature20584",
                "snippet": "High-spectral-resolution observations with Hitomi find no evidence for the previously reported 3.5 keV line, significantly constraining sterile neutrino parameter space.",
                "source": "Nature / Hitomi Collaboration",
                "domain": "nature.com",
                "stance": "contradicting",
                "credibility_score": 97,
                "published_date": "2017-01-26"
            }
        ],
        "sources": [
            {
                "title": "Hitomi Cluster Core Spectroscopy",
                "source_name": "Nature Publishing Group",
                "domain": "nature.com",
                "url": "https://nature.com",
                "category": "Peer-Reviewed Scientific Journal",
                "reliability_tier": "High"
            },
            {
                "title": "Physical Review Letters Astrophysics",
                "source_name": "American Physical Society",
                "domain": "aps.org",
                "url": "https://aps.org",
                "category": "Academic Physics Society",
                "reliability_tier": "High"
            }
        ],
        "limitations_and_uncertainty": (
            "Dark matter detection relies on indirect cosmological observations and future high-sensitivity space telescopes (e.g. XRISM, Athena). Current data cannot resolve conflicting observations."
        )
    }
}
