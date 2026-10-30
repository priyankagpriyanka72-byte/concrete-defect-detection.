"""
AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP
Civil Engineering Knowledge Base & Advisory Engine
Six Defect Categories:
1. Segregation
2. Honeycombing
3. Spalling
4. Crack
5. Void
6. Efflorescence
+ Normal Concrete (No Defect) Validation
+ 7-Step RCC Slab Strengthening Procedure
"""

DEFECT_ADVISORY = {
    "Segregation": {
        "name": "Segregation",
        "category": "Mix & Placement Defect",
        "badge_color": "#f59e0b",
        "description": "The separation of constituent materials in fresh concrete, where coarse aggregate settles to the bottom or separates from mortar paste, resulting in non-homogeneous mechanical strength, honeycombed patches, and porous planes of weakness.",
        "possible_causes": [
            "Dropping concrete from excessive discharge heights (>1.5 meters) into formwork without tremie pipes",
            "Excessive or prolonged mechanical vibration causing coarse aggregate to sink and slurry to rise",
            "Excessive water content or high slump mix lacking cohesive fine aggregate matrix",
            "Poor aggregate gradation (excess coarse stones, deficit in fine sand fraction)",
            "Improper transportation or rough haulage causing paste segregation in transit"
        ],
        "severity_assessment": {
            "preliminary_level": "Moderate to High (Preliminary assessment based on depth and affected structural zone)",
            "classification_guide": "Surface paste separation reduces durability and wear resistance; deep segregation in structural tension/compression zones significantly impairs load-bearing capacity.",
            "structural_safety_disclaimer": "This is a preliminary engineering visual assessment and does NOT substitute for in-situ non-destructive core or UPV testing."
        },
        "prevention_methods": [
            "Limit free fall of concrete to a maximum of 1.0 to 1.5 meters using tremie pipes or down-chutes",
            "Design cohesive concrete mixes with optimal sand-to-coarse aggregate ratio and viscosity-modifying admixtures (VMA)",
            "Control mechanical vibration: insert needle vibrators vertically for 5-15 seconds per point until air bubbling stops, then withdraw slowly",
            "Maintain strict water-cement ratio using high-range water reducers (superplasticizers) rather than adding site water",
            "Ensure proper transit mixer agitation speed during transportation and discharge"
        ],
        "suitable_repair_methods": [
            "Surface segregation: Chip out poorly consolidated stones, apply SBR polymer bonding slurry, and patch with non-shrink polymer repair mortar",
            "Deep structural segregation: Core test to determine distress depth; chip out defective concrete until sound homogeneous matrix is reached; install shuttering and pour free-flowing micro-concrete",
            "Pressure injection: Inject low-viscosity cementitious or epoxy micro-grout to fill internal honeycombed voids",
            "Section enhancement: If compressive capacity is compromised, install external composite wraps or steel encasement"
        ],
        "maintenance_advice": [
            "Perform Ultrasonic Pulse Velocity (UPV) grid testing across the element to verify density uniformity",
            "Apply penetrating silane/siloxane hydrophobic sealer to prevent moisture and chloride ingress into porous zones",
            "Inspect regularly for micro-cracking along segregation boundary interfaces"
        ],
        "slab_strengthening_relevance": "Segregation occurring in slab soffits or beam-slab junctions undermines tensile and shear capacity. Refer to the 7-step RCC slab strengthening procedure for structural consolidation."
    },

    "Honeycombing": {
        "name": "Honeycombing",
        "category": "Compaction & Consolidation Defect",
        "badge_color": "#d97706",
        "description": "Porous voids and stone pockets left in concrete caused by failure of mortar to completely fill spaces around coarse aggregate, resembling a bee's honeycomb with exposed stony aggregate clusters.",
        "possible_causes": [
            "Inadequate, non-uniform, or omitted internal vibration during concrete placement",
            "Congested steel rebar cage obstructing the passage of coarse aggregate into form corners",
            "Oversized maximum aggregate size exceeding clear spacing between rebar or form faces",
            "Low workability (stiff, dry mix) placed without appropriate plasticizing admixtures",
            "Leaking formwork joints allowing fine cement paste and slurry to bleed out under vibration"
        ],
        "severity_assessment": {
            "preliminary_level": "Moderate to High (Preliminary assessment based on depth and rebar exposure)",
            "classification_guide": "Superficial surface honeycombing (<25 mm depth) affects durability; deep honeycombing exposing reinforcement compromises structural bond and fire protection.",
            "structural_safety_disclaimer": "This is a preliminary engineering visual assessment and does NOT substitute for certified structural capacity calculations."
        },
        "prevention_methods": [
            "Ensure aggregate maximum size does not exceed 3/4 of the clear spacing between reinforcement bars",
            "Seal formwork joints with foam gasket tape to prevent slurry leakage during compaction",
            "Adopt systematic needle vibration: vertical immersion at 400-500 mm grid intervals extending 100 mm into prior lift",
            "Achieve required slump and rheology using modern superplasticizers without increasing water-cement ratio",
            "Detail rebar arrangements with clear access windows for vibrator needles and concrete flow"
        ],
        "suitable_repair_methods": [
            "Chip away all loose, poorly consolidated stones until hard, sound parent concrete is exposed",
            "Clean substrate thoroughly using wire brushes and compressed air or water jetting",
            "Apply high-bond epoxy or SBR polymer-modified bonding agent slurry",
            "Patch with non-shrink, high-strength polymer-modified repair mortar or free-flowing micro-concrete",
            "Low-pressure grouting for deep interior voids behind congested reinforcement"
        ],
        "maintenance_advice": [
            "Conduct hammer sounding across surrounding areas to verify complete absence of hidden voids",
            "Verify specified rebar cover depth is restored over the repaired patch",
            "Apply an anti-carbonation barrier coating over the completed repair"
        ],
        "slab_strengthening_relevance": "Honeycombing in slab soffits directly exposes rebars to atmospheric carbonation. See the 7-step RCC slab strengthening procedure for systematic rebar treatment and guniting encasement."
    },

    "Spalling": {
        "name": "Spalling",
        "category": "Corrosion & Durability Distress",
        "badge_color": "#dc2626",
        "description": "Delamination, fracturing, or breaking away of concrete fragments from the surface, typically exposing corroded, rusted reinforcing steel bars beneath.",
        "possible_causes": [
            "Corrosion of embedded reinforcing steel; ferric oxide rust expansion (up to 600% volume increase) exerts high bursting tensile stress",
            "Insufficient concrete clear cover depth over steel reinforcement",
            "Carbonation of concrete cover reducing alkaline pH passivating film around steel",
            "Chloride ion penetration from marine environment, deicing salts, or contaminated mix water",
            "Thermal shock, fire exposure, or cyclic freeze-thaw pore pressure"
        ],
        "severity_assessment": {
            "preliminary_level": "High to Critical (Preliminary assessment; direct structural risk)",
            "classification_guide": "Exposed corroding steel accelerates section loss, reducing shear and flexural capacity; requires immediate structural remediation.",
            "structural_safety_disclaimer": "This is a preliminary engineering visual assessment and does NOT constitute a formal structural safety certificate."
        },
        "prevention_methods": [
            "Provide specified minimum clear concrete cover using dense, non-corrosive concrete spacer blocks",
            "Produce low-permeability dense concrete with low water-cement ratio and supplementary cementitious materials (fly ash, silica fume)",
            "Apply penetrating silane/siloxane water repellents or elastomeric anti-carbonation barrier coatings",
            "Use corrosion-inhibiting admixtures or galvanized/epoxy-coated rebar in aggressive exposure conditions",
            "Ensure rigorous moist curing for a minimum of 14 days to seal surface capillary pores"
        ],
        "suitable_repair_methods": [
            "Saw-cut breakout boundaries perpendicular (square cut minimum 15-20 mm depth) to prevent feather edges",
            "Chip concrete until a minimum 20 mm clearance is established completely around exposed reinforcement",
            "De-rust exposed steel to bare metal (SA 2.5 standard) using mechanical wire cup brushes or sandblasting",
            "Apply two coats of zinc-rich anti-corrosion primer on rebar; splice supplementary bars if section loss exceeds 15%",
            "Apply epoxy/SBR bonding coat followed by structural polymer-modified mortar or pneumatically placed gunite/shotcrete"
        ],
        "maintenance_advice": [
            "Conduct periodic half-cell potential surveys to map active corrosion zones in adjacent concrete",
            "Inspect surrounding slab and beam soffits for rust weeping or hollow drummy sounds under tapping",
            "Reapply protective breathable sealers every 5 to 7 years"
        ],
        "slab_strengthening_relevance": "Spalling in RCC slabs directly correlates with the 7-step strengthening case study: Rebar cleaning, zinc primer, wire mesh fixing, guniting, and MS steel structural sections."
    },

    "Crack": {
        "name": "Crack",
        "category": "Structural & Serviceability Distress",
        "badge_color": "#e11d48",
        "description": "Linear fractures, fissures, or separations in the hardened concrete matrix occurring when internal tensile stresses exceed the tensile capacity of the concrete element.",
        "possible_causes": [
            "Plastic and drying shrinkage due to rapid evaporation of surface moisture during early curing",
            "Thermal expansion and contraction cycles with inadequate relief/expansion joints",
            "Excessive structural loading, flexural overstress, or unanticipated foundation settlement",
            "Corrosion of embedded steel reinforcement exerting bursting tensile stress",
            "Improper placement, spacing, or omission of reinforcement bars"
        ],
        "severity_assessment": {
            "preliminary_level": "Moderate to High (Preliminary assessment; subject to field crack width and activity measurement)",
            "classification_guide": "Hairline cracks (<0.3 mm) are typically serviceability/aesthetic; structural cracks (>0.3 mm or active movement) require formal engineering review.",
            "structural_safety_disclaimer": "This is a preliminary engineering visual assessment and does NOT constitute a certified structural safety certificate."
        },
        "prevention_methods": [
            "Maintain strict water-cement ratio using superplasticizers for desired workability",
            "Ensure continuous moist curing for a minimum of 7 to 14 days immediately after initial set",
            "Provide appropriate control, expansion, and contraction joints at designated spacing",
            "Incorporate synthetic polypropylene micro-fibers or welded wire fabric for secondary shrinkage control",
            "Control peak hydration temperatures in thick pours through stage casting or chilled mix water"
        ],
        "suitable_repair_methods": [
            "Low-pressure epoxy resin injection for non-moving structural cracks to restore monolithic integrity",
            "Routing and elastomeric polyurethane sealing for active, moving thermal joints and cracks",
            "Polymer-modified cementitious pressure grouting for wide, deep fissures",
            "Carbon Fiber Reinforced Polymer (CFRP) composite wrap for flexural/shear crack arrest"
        ],
        "maintenance_advice": [
            "Install tell-tale crack motion monitors or optical gauges and log displacement weekly for 60-90 days",
            "Apply a breathable hydrophobic silane/siloxane surface sealer to halt water and chloride penetration",
            "Inspect underside of slabs or soffits for moisture stains or efflorescence leaching through crack lines"
        ],
        "slab_strengthening_relevance": "Cracking due to severe flexural overstress or rebar corrosion may warrant structural intervention. See observed RCC Slab Strengthening Procedure."
    },

    "Void": {
        "name": "Void (Bugholes / Surface Cavities)",
        "category": "Surface & Formwork Defect",
        "badge_color": "#7c3aed",
        "description": "Small surface cavities, blowholes, or bugholes formed on vertical or formed concrete faces caused by pockets of entrapped air or bleed water migration along the formwork interface.",
        "possible_causes": [
            "Entrapped air bubbles along formwork faces due to inadequate, over-rapid, or non-uniform mechanical vibration",
            "Excessive or non-uniform application of thick form-release oil or grease",
            "High-viscosity, sticky concrete mixes with poor air evacuation characteristics",
            "Impermeable, non-absorptive formwork lining preventing air dissipation",
            "Excessive concrete pour lift heights dropping mix without progressive layer vibration"
        ],
        "severity_assessment": {
            "preliminary_level": "Low to Moderate (Primarily aesthetic & architectural surface defect)",
            "classification_guide": "Small surface voids (<10 mm diameter) do not impair structural strength; clusters or deep voids may reduce effective rebar cover.",
            "structural_safety_disclaimer": "This is a preliminary engineering visual assessment and does NOT constitute a certified structural safety certificate."
        },
        "prevention_methods": [
            "Use properly graded sands and optimize paste viscosity with modern superplasticizers",
            "Apply form-release agents in ultra-thin, uniform coats; avoid pooling",
            "Employ proper internal immersion vibration technique (100-150 mm insertion into lower lift) and form vibrators where accessible",
            "Utilize permeable formwork liners (CPF) for critical architectural fair-faced concrete",
            "Limit pour lift heights to manageable depths (300-500 mm) for progressive air venting"
        ],
        "suitable_repair_methods": [
            "High-pressure water washing or wire brushing to remove form oil residues and loose particles",
            "Pre-wet the cavity area to saturated surface dry (SSD) condition",
            "Scrape-coat application of polymer-modified cementitious fairing coat or cosmetic skim mortar",
            "Work repair paste tightly into voids using rubber float or steel trowel; wipe flush with surface",
            "Moist curing of fairing coat to prevent flash drying and chalking"
        ],
        "maintenance_advice": [
            "Verify complete adhesion of fairing coat by light scraping after 7 days",
            "Apply acrylic or siloxane exterior weatherproofing coat to seal micro-pores",
            "Keep drainage clean to avoid standing water pooling against vertical walls"
        ],
        "slab_strengthening_relevance": "Superficial surface voids generally do not compromise structural load capacity. Comprehensive slab strengthening is rarely required for bugholes alone."
    },

    "Efflorescence": {
        "name": "Efflorescence",
        "category": "Chemical & Moisture Distress",
        "badge_color": "#0284c7",
        "description": "A crystalline, powdery, white or grayish-white deposit of soluble salts (principally calcium carbonate, sodium, and potassium sulfates) formed on the concrete surface as moisture evaporates after leaching through porous capillaries.",
        "possible_causes": [
            "Presence of soluble mineral salts in cement, sand, mixing water, or surrounding soil/groundwater",
            "Ingress of moisture or persistent water seepage through micro-cracks and porous concrete",
            "High capillary porosity resulting from high water-cement ratio or inadequate early curing",
            "Defective waterproofing membranes, failed roof flashings, or leaking pipes feeding moisture into the concrete",
            "Inadequate drainage causing water pooling against exterior concrete surfaces"
        ],
        "severity_assessment": {
            "preliminary_level": "Low to Moderate (Primarily aesthetic indicator of underlying moisture transmission)",
            "classification_guide": "Dry surface salts do not immediately weaken concrete; however, chronic leaching dissolves calcium hydroxide from the matrix, leading to loss of alkalinity and accelerated rebar corrosion.",
            "structural_safety_disclaimer": "This is a preliminary engineering visual assessment and indicates active moisture transmission requiring source inspection."
        },
        "prevention_methods": [
            "Use low-alkali cements, washed salt-free aggregates, and potable mixing water",
            "Incorporate supplementary pozzolanic materials (fly ash, silica fume, GGBS) which chemically bind free calcium hydroxide",
            "Produce dense, impermeable concrete with low water-cement ratio and thorough compaction",
            "Install robust damp-proof courses (DPC), high-grade waterproofing membranes, and ensure positive drainage slopes",
            "Provide complete, continuous 14-day wet curing to minimize interconnecting capillary pores"
        ],
        "suitable_repair_methods": [
            "Dry efflorescence: Remove salts by dry mechanical scrubbing with stiff non-metallic bristle brushes and vacuum clean (avoid water washing which re-dissolves salts)",
            "Hardened carbonate crusts: Apply mild 5-10% diluted sulfamic or citric acid wash; scrub surface and neutralize immediately with abundant clean water",
            "Source elimination: Locate and rectify the water source (repair pipe leaks, reseal joints, re-lay waterproofing membrane)",
            "Crystalline waterproofing: Apply penetrating crystalline waterproofing slurry that migrates into concrete capillaries and crystallizes to block moisture permanently"
        ],
        "maintenance_advice": [
            "Inspect building roof drains, gutters, and expansion joint sealants biannually",
            "Ensure crawlspaces and basements maintain adequate ventilation to reduce vapor pressure",
            "Apply breathable hydrophobic silane/siloxane barrier to repel liquid water while allowing water vapor release"
        ],
        "slab_strengthening_relevance": "Efflorescence itself is a moisture indicator; however, if chronic moisture leaching has caused severe rebar corrosion and spalling on slab soffits, refer to the 7-step RCC slab strengthening procedure."
    },

    "No Defect": {
        "name": "No Defect (Sound Concrete)",
        "category": "Normal Concrete Condition",
        "badge_color": "#059669",
        "description": "The analyzed concrete surface demonstrates sound structural matrix integrity, uniform surface texture, and absence of identifiable segregation, honeycombing, spalling, cracking, voids, or efflorescence deposits.",
        "possible_causes": [
            "Adherence to proper concrete mix design, water-cement ratio, and aggregate gradation",
            "Effective placement, adequate compaction, and high-quality formwork",
            "Adequate and timely moist curing protecting against early shrinkage",
            "Proper structural design and appropriate service load conditions"
        ],
        "severity_assessment": {
            "preliminary_level": "None (Sound Condition)",
            "classification_guide": "Normal serviceable condition. No remedial intervention required at this stage.",
            "structural_safety_disclaimer": "Visual screening indicates sound surface condition. Routine civil maintenance recommended."
        },
        "prevention_methods": [
            "Maintain ongoing protective housekeeping: keep surfaces clean from standing water and chemical spills",
            "Prevent mechanical impact or concentrated point overloading on slab surface",
            "Maintain expansion joints and sealants in building perimeter"
        ],
        "suitable_repair_methods": [
            "No active repair required.",
            "Optional: Apply penetrating hydrophobic sealer (silane/siloxane) as a preventive durability barrier"
        ],
        "maintenance_advice": [
            "Conduct routine visual inspections at regular intervals (every 6 to 12 months)",
            "Ensure rain water downspouts and drainage slopes prevent water stagnation",
            "Log any new hairline marks or environmental exposure changes over service life"
        ],
        "slab_strengthening_relevance": "No structural strengthening required. The concrete is in a sound state."
    }
}

# The 7 Exact Steps for RCC Slab Strengthening
RCC_SLAB_STRENGTHENING_STEPS = [
    {
        "step_number": 1,
        "title": "Removal of plaster and surface preparation",
        "short_technical_explanation": "All existing deteriorated ceiling plaster, loose lime-wash, grease, and carbonated surface crust are completely removed down to the parent RCC substrate using light pneumatic chipping hammers or mechanical wire cup brushes. The concrete surface is then washed with high-pressure water jetting or compressed air to expose a clean, sound aggregate matrix.",
        "key_action": "Chipping and surface scabbing down to sound parent concrete; high-pressure washing.",
        "image_file": "steps/step1_surface_prep.svg",
        "quality_checkpoint": "Parent concrete surface must be completely free of loose dust, oil, and unbonded plaster remnants."
    },
    {
        "step_number": 2,
        "title": "Removal of loose and deteriorated concrete",
        "short_technical_explanation": "All fractured, delaminated, and hollow-sounding concrete is meticulously chipped out using electric or pneumatic breakers until sound, dense parent concrete is reached. The perimeter edges of the breakout area are cut square (perpendicular to the surface, minimum 15-20 mm depth) to eliminate feather-edge joints. Concrete behind corroded reinforcement is undercut by at least 20 mm to allow full 360° mortar encasement.",
        "key_action": "Perpendicular square edge cut (15-20 mm); >20 mm undercut behind corroded rebar.",
        "image_file": "steps/step2_loose_concrete.svg",
        "quality_checkpoint": "No feather edges allowed; sound ringing tone verified via tapping; rebar fully accessible."
    },
    {
        "step_number": 3,
        "title": "Treatment of exposed reinforcement",
        "short_technical_explanation": "Exposed steel reinforcement bars are thoroughly cleaned around their entire circumference using mechanical wire brushes or abrasive grit blasting to remove rust scales down to bright bare metal (SA 2.5 finish). If reinforcement diameter has degraded by more than 15%, supplementary high-yield steel bars are spliced/welded with adequate development length. Two coats of zinc-rich anti-corrosion primer or polymer-modified epoxy barrier are applied immediately.",
        "key_action": "Mechanical de-rusting to SA 2.5; splice supplementary rebar if >15% loss; apply zinc primer.",
        "image_file": "steps/step3_rebar_treatment.svg",
        "quality_checkpoint": "Full 360° primer coverage; no untreated rust left under bars; lap length verified per design."
    },
    {
        "step_number": 4,
        "title": "Fixing of wire mesh",
        "short_technical_explanation": "Welded steel wire fabric (typically 50 mm x 50 mm or 75 mm x 75 mm gauge galvanized mesh) is positioned across the entire repair zone. The mesh is securely fastened to the slab soffit using stainless steel or brass expansion anchors/shear pins drilled into the parent concrete at 300 mm to 400 mm staggered center-to-center grid intervals, with spacer clips maintaining a 15-20 mm cover offset.",
        "key_action": "Welded wire mesh anchor fixing with shear pins/expansion fasteners at 300-400 mm c/c.",
        "image_file": "steps/step4_wire_mesh.svg",
        "quality_checkpoint": "Mesh must be rigidly tied with no sagging or flutter; uniform standoff clearance maintained."
    },
    {
        "step_number": 5,
        "title": "Guniting",
        "short_technical_explanation": "Pneumatically projected dry-mix mortar (guniting) or wet shotcrete is applied under compressed air pressure (3 to 4 bar) through a calibrated nozzle held perpendicular (90°) at 0.6 to 1.0 m from the slab soffit. The high-velocity impact compacts the dense, low water-cement ratio mortar around all rebar and wire mesh with zero voids, achieving exceptional compressive and bond strength.",
        "key_action": "High-velocity pneumatic shotcrete application at 3-4 bar with low water-cement ratio.",
        "image_file": "steps/step5_guniting.svg",
        "quality_checkpoint": "No rebound entrapment; uniform compaction without hollow pockets; complete encasement."
    },
    {
        "step_number": 6,
        "title": "Curing and finishing",
        "short_technical_explanation": "The gunited surface is leveled and smoothed using straightedges and wooden floats to restore the original ceiling profile. The repaired concrete is maintained under continuous moist curing using wet hessian/burlap sheets or an approved membrane-forming curing compound for a minimum of 14 days to prevent early shrinkage micro-cracking and ensure design compressive strength.",
        "key_action": "Wood float finishing followed by continuous moist hessian curing for 14 days minimum.",
        "image_file": "steps/step6_curing.svg",
        "quality_checkpoint": "Surface kept continually damp; no premature dry-out permitted; adhesion tested after cure."
    },
    {
        "step_number": 7,
        "title": "Installation of MS Steel Sections for Structural Strengthening",
        "short_technical_explanation": "To augment flexural capacity, arrest sagging, and supplement the load-bearing capacity of the distress-affected slab, fabricated Mild Steel (MS) structural sections (such as ISMB I-beams or ISMC steel channels) are erected tight against the repaired slab soffit. The steel beams are anchored to perimeter RCC beams or load-bearing masonry walls with heavy-duty chemical anchor bolts and steel baseplates, wedged with non-shrink epoxy grout pads, and coated with red-oxide and fire-resistant paint.",
        "key_action": "Structural steel beam placement, chemical anchoring, non-shrink grout wedging & anti-corrosion coating.",
        "image_file": "steps/step7_ms_steel.svg",
        "quality_checkpoint": "Zero gap between beam and slab; tight non-shrink grout fill; anchor pull-out torque verified."
    }
]

# Mandatory Structural Note as requested in Requirement 6
MANDATORY_STRUCTURAL_NOTE = (
    "IMPORTANT ENGINEERING NOTICE: The actual strengthening method, structural steel section sizing, "
    "anchor embedment depth, and execution sequence must be strictly verified against the approved "
    "site-specific structural design and calculations verified by a certified Structural Engineer."
)

# Case-study contextual clarification as requested in Requirement 7
CASE_STUDY_CLARIFICATION = (
    "Defect repair and structural strengthening are related civil engineering disciplines but are not identical. "
    "Defect repair restores localized cross-sectional integrity and corrosion protection, whereas structural "
    "strengthening augments the overall load-carrying capacity and arrests global deflection. "
    "The 7-step procedure presented here illustrates the observed RCC slab case-study method for heavily distressed "
    "or overloaded slabs, and is not an automatic requirement for minor cosmetic defects."
)
