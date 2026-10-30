import os

os.makedirs('static/images/steps', exist_ok=True)
os.makedirs('static/images', exist_ok=True)

svg_defs = """
<defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
        <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#334155" stroke-width="0.5" stroke-opacity="0.4"/>
    </pattern>
    <linearGradient id="slabGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#94a3b8"/>
        <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <linearGradient id="steelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#f59e0b"/>
        <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="primerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#10b981"/>
        <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
</defs>
"""

steps_data = [
    (
        "step1_surface_prep.svg",
        "STEP 1: REMOVAL OF PLASTER & SURFACE PREPARATION",
        """
        <!-- Concrete Slab Base -->
        <rect x="40" y="45" width="520" height="85" fill="url(#slabGrad)" rx="4"/>
        <text x="50" y="70" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">EXISTING RCC SLAB SUBSTRATE</text>
        
        <!-- Rebar inside slab -->
        <line x1="50" y1="95" x2="550" y2="95" stroke="#334155" stroke-width="6" stroke-dasharray="14,6"/>
        
        <!-- Old Plaster Layer being chipped -->
        <path d="M 40 130 L 250 130 L 250 160 L 40 160 Z" fill="#cbd5e1" stroke="#94a3b8"/>
        <text x="50" y="150" fill="#475569" font-family="sans-serif" font-size="11">Old Deteriorated Plaster (To be removed)</text>
        
        <!-- Chisel & Chipping Action -->
        <polygon points="250,130 280,110 290,120 260,140" fill="#f59e0b"/>
        <line x1="285" y1="115" x2="350" y2="70" stroke="#d97706" stroke-width="8" stroke-linecap="round"/>
        
        <!-- Flying Debris / Chipped pieces -->
        <circle cx="270" cy="150" r="5" fill="#94a3b8"/>
        <polygon points="280,165 290,155 295,170" fill="#cbd5e1"/>
        <circle cx="305" cy="145" r="4" fill="#64748b"/>
        
        <!-- Exposed sound substrate -->
        <path d="M 250 130 L 560 130" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
        <text x="270" y="150" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">Sound Concrete Exposed &amp; Cleaned</text>
        
        <!-- Technical Badge -->
        <rect x="40" y="250" width="520" height="65" fill="#1e293b" rx="6" stroke="#334155"/>
        <text x="60" y="275" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">KEY ACTION: Mechanical Chipping down to Parent Concrete</text>
        <text x="60" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11">Remove all hollow plaster, carbonated crust, dust &amp; grease. Expose sound aggregate surface.</text>
        """
    ),
    (
        "step2_loose_concrete.svg",
        "STEP 2: REMOVAL OF LOOSE & DETERIORATED CONCRETE",
        """
        <!-- Concrete Slab Base -->
        <rect x="40" y="45" width="520" height="90" fill="url(#slabGrad)" rx="4"/>
        <text x="50" y="70" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">RCC SLAB SOFFIT (SPALLED REGION)</text>
        
        <!-- Excavated Cut Zone (Square Shoulders) -->
        <path d="M 140 135 L 140 95 L 460 95 L 460 135" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
        <text x="180" y="80" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="bold">Chipped Cavity to Sound Parent Concrete</text>
        
        <!-- Square shoulder cuts -->
        <line x1="140" y1="135" x2="140" y2="95" stroke="#ef4444" stroke-width="4"/>
        <line x1="460" y1="135" x2="460" y2="95" stroke="#ef4444" stroke-width="4"/>
        <text x="50" y="115" fill="#ef4444" font-family="sans-serif" font-size="10" font-weight="bold">Square Cut (15-20mm)</text>
        <text x="468" y="115" fill="#ef4444" font-family="sans-serif" font-size="10" font-weight="bold">No Feather Edges</text>
        
        <!-- Exposed Rebar with 20mm clearance behind -->
        <circle cx="200" cy="115" r="9" fill="#b45309" stroke="#78350f" stroke-width="2"/>
        <circle cx="300" cy="115" r="9" fill="#b45309" stroke="#78350f" stroke-width="2"/>
        <circle cx="400" cy="115" r="9" fill="#b45309" stroke="#78350f" stroke-width="2"/>
        <text x="215" y="145" fill="#f59e0b" font-family="sans-serif" font-size="10">&gt;20mm Undercut Clearance Behind Rebar</text>
        
        <!-- Technical Badge -->
        <rect x="40" y="250" width="520" height="65" fill="#1e293b" rx="6" stroke="#334155"/>
        <text x="60" y="275" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">KEY ACTION: Geometry of Concrete Demolition</text>
        <text x="60" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11">Cut perimeter edges strictly perpendicular. Under-cut rebar by minimum 20mm to allow complete encasement.</text>
        """
    ),
    (
        "step3_rebar_treatment.svg",
        "STEP 3: TREATMENT OF EXPOSED REINFORCEMENT",
        """
        <!-- Slab Cavity -->
        <rect x="40" y="45" width="520" height="70" fill="url(#slabGrad)" rx="4"/>
        
        <!-- Rebar 1: Corroded -->
        <line x1="60" y1="95" x2="210" y2="95" stroke="#b45309" stroke-width="12" stroke-linecap="round"/>
        <text x="70" y="125" fill="#b45309" font-family="sans-serif" font-size="10" font-weight="bold">Corroded Rust Layer</text>
        
        <!-- Cleaning Wire Brush Action -->
        <rect x="215" y="80" width="25" height="15" fill="#475569" rx="2"/>
        <line x1="215" y1="95" x2="240" y2="95" stroke="#94a3b8" stroke-width="3" stroke-dasharray="2,2"/>
        <line x1="228" y1="80" x2="228" y2="60" stroke="#d97706" stroke-width="4"/>
        
        <!-- Rebar 2: Cleaned Bare Metal (SA 2.5) -->
        <line x1="255" y1="95" x2="370" y2="95" stroke="#cbd5e1" stroke-width="12" stroke-linecap="round"/>
        <text x="260" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10" font-weight="bold">Bare Metal (SA 2.5)</text>
        
        <!-- Rebar 3: Zinc-Rich Primer Applied -->
        <line x1="385" y1="95" x2="530" y2="95" stroke="url(#primerGrad)" stroke-width="14" stroke-linecap="round"/>
        <text x="395" y="125" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="bold">Zinc-Rich Primer Coat</text>
        
        <!-- Additional splice bar indication -->
        <line x1="180" y1="160" x2="480" y2="160" stroke="#0284c7" stroke-width="7" stroke-dasharray="8,4"/>
        <text x="180" y="180" fill="#38bdf8" font-family="sans-serif" font-size="11">Supplementary Rebar Splice (If &gt;15% section loss detected)</text>
        
        <!-- Technical Badge -->
        <rect x="40" y="250" width="520" height="65" fill="#1e293b" rx="6" stroke="#334155"/>
        <text x="60" y="275" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">KEY ACTION: 360° De-rusting &amp; Active Corrosion Inhibition</text>
        <text x="60" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11">Mechanical wire brush to shiny surface. Apply 2 coats of zinc-rich primer to prevent galvanic cell formation.</text>
        """
    ),
    (
        "step4_wire_mesh.svg",
        "STEP 4: FIXING OF WIRE MESH",
        """
        <!-- Slab Substrate -->
        <rect x="40" y="45" width="520" height="70" fill="url(#slabGrad)" rx="4"/>
        
        <!-- Expansion Anchors into Concrete -->
        <rect x="150" y="75" width="12" height="40" fill="#f59e0b" rx="2"/>
        <rect x="300" y="75" width="12" height="40" fill="#f59e0b" rx="2"/>
        <rect x="450" y="75" width="12" height="40" fill="#f59e0b" rx="2"/>
        
        <circle cx="156" cy="115" r="8" fill="#d97706"/>
        <circle cx="306" cy="115" r="8" fill="#d97706"/>
        <circle cx="456" cy="115" r="8" fill="#d97706"/>
        
        <!-- Wire Mesh Grid -->
        <g stroke="#38bdf8" stroke-width="2.5">
            <!-- Horizontal wires -->
            <line x1="80" y1="120" x2="520" y2="120"/>
            <line x1="80" y1="145" x2="520" y2="145"/>
            <line x1="80" y1="170" x2="520" y2="170"/>
            <!-- Vertical wires -->
            <line x1="120" y1="105" x2="120" y2="185"/>
            <line x1="180" y1="105" x2="180" y2="185"/>
            <line x1="240" y1="105" x2="240" y2="185"/>
            <line x1="300" y1="105" x2="300" y2="185"/>
            <line x1="360" y1="105" x2="360" y2="185"/>
            <line x1="420" y1="105" x2="420" y2="185"/>
            <line x1="480" y1="105" x2="480" y2="185"/>
        </g>
        
        <!-- Annotations -->
        <text x="70" y="205" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">Welded Wire Fabric (50mm x 50mm / 75mm x 75mm)</text>
        <text x="325" y="90" fill="#f59e0b" font-family="sans-serif" font-size="11" font-weight="bold">Shear Anchor Expansion Bolts (300-400mm c/c)</text>
        
        <!-- Technical Badge -->
        <rect x="40" y="250" width="520" height="65" fill="#1e293b" rx="6" stroke="#334155"/>
        <text x="60" y="275" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">KEY ACTION: Mechanical Anchoring of Secondary Reinforcement</text>
        <text x="60" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11">Anchors ensure complete composite mechanical action between original slab and new shotcrete overlay.</text>
        """
    ),
    (
        "step5_guniting.svg",
        "STEP 5: GUNITING (PNEUMATIC SHOTCRETING)",
        """
        <!-- Slab Cross Section -->
        <rect x="40" y="45" width="520" height="55" fill="url(#slabGrad)" rx="4"/>
        
        <!-- High-Velocity Gunite Layer being built up -->
        <path d="M 40 100 L 320 100 L 290 145 L 40 145 Z" fill="#475569" stroke="#64748b"/>
        <text x="60" y="125" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="bold">Compacted Gunite Layer (High Density Mortar)</text>
        
        <!-- Guniting Nozzle -->
        <polygon points="480,195 460,185 460,205" fill="#334155"/>
        <line x1="480" y1="195" x2="540" y2="225" stroke="#1e293b" stroke-width="14" stroke-linecap="round"/>
        <line x1="480" y1="195" x2="540" y2="225" stroke="#d97706" stroke-width="6" stroke-linecap="round"/>
        
        <!-- High Pressure Spray Cone -->
        <polygon points="460,185 290,105 300,150 460,205" fill="#94a3b8" fill-opacity="0.35"/>
        <!-- Spray particle dots -->
        <circle cx="360" cy="140" r="3" fill="#cbd5e1"/>
        <circle cx="380" cy="160" r="4" fill="#94a3b8"/>
        <circle cx="410" cy="170" r="3" fill="#cbd5e1"/>
        <circle cx="340" cy="130" r="2" fill="#64748b"/>
        <circle cx="430" cy="185" r="3" fill="#cbd5e1"/>
        
        <text x="330" y="215" fill="#f59e0b" font-family="sans-serif" font-size="11" font-weight="bold">High Velocity Jet (3-4 Bar Pressure)</text>
        <text x="330" y="230" fill="#cbd5e1" font-family="sans-serif" font-size="10">Nozzle Held Perpendicular (90°) at 0.6-1.0m</text>
        
        <!-- Technical Badge -->
        <rect x="40" y="250" width="520" height="65" fill="#1e293b" rx="6" stroke="#334155"/>
        <text x="60" y="275" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">KEY ACTION: Pneumatic Projection &amp; High Compaction</text>
        <text x="60" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11">Dense mortar stream encapsulates rebars and wire mesh with zero air pockets and high bond strength.</text>
        """
    ),
    (
        "step6_curing.svg",
        "STEP 6: CURING AND FINISHING",
        """
        <!-- Slab Base and Finished Layer -->
        <rect x="40" y="45" width="520" height="55" fill="url(#slabGrad)" rx="4"/>
        <rect x="40" y="100" width="520" height="40" fill="#475569" stroke="#10b981" stroke-width="2"/>
        <text x="60" y="125" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">Finished Even Concrete Surface (Smooth Float Finish)</text>
        
        <!-- Moist Curing Burlap / Hessian Cloth -->
        <rect x="60" y="140" width="480" height="18" fill="#d97706" fill-opacity="0.8" stroke="#b45309" stroke-dasharray="4,4"/>
        <text x="170" y="153" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Wet Hessian / Burlap Sheets Underneath</text>
        
        <!-- Water Droplets / Curing Mist -->
        <g fill="#38bdf8">
            <circle cx="120" cy="175" r="4"/><circle cx="180" cy="185" r="5"/><circle cx="240" cy="180" r="4"/>
            <circle cx="300" cy="190" r="5"/><circle cx="360" cy="175" r="4"/><circle cx="420" cy="185" r="5"/>
            <circle cx="480" cy="180" r="4"/>
        </g>
        <text x="190" y="215" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">Continuous Moist Curing (Minimum 14 Days)</text>
        
        <!-- Technical Badge -->
        <rect x="40" y="250" width="520" height="65" fill="#1e293b" rx="6" stroke="#334155"/>
        <text x="60" y="275" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">KEY ACTION: Hydration Control &amp; Shrinkage Prevention</text>
        <text x="60" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11">Prevents plastic &amp; drying shrinkage micro-cracks. Crucial for full compressive &amp; bond strength gain.</text>
        """
    ),
    (
        "step7_ms_steel.svg",
        "STEP 7: INSTALLATION OF MS STEEL SECTIONS",
        """
        <!-- Repaired RCC Slab Soffit -->
        <rect x="40" y="45" width="520" height="60" fill="url(#slabGrad)" rx="4"/>
        <text x="60" y="65" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="bold">REPAIRED &amp; RESTORED RCC SLAB SOFFIT</text>
        
        <!-- Chemical Anchor Bolts -->
        <rect x="100" y="70" width="12" height="55" fill="#f59e0b" rx="2"/>
        <rect x="480" y="70" width="12" height="55" fill="#f59e0b" rx="2"/>
        
        <!-- Non-Shrink Grout Packing Layer -->
        <rect x="120" y="105" width="360" height="10" fill="#10b981" rx="2"/>
        <text x="210" y="113" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold">Non-Shrink Epoxy Grout Packing Pad</text>
        
        <!-- MS Steel I-Beam (ISMB Section) Underneath -->
        <!-- Top Flange -->
        <rect x="80" y="115" width="440" height="15" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
        <!-- Web -->
        <rect x="285" y="130" width="30" height="50" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
        <!-- Bottom Flange -->
        <rect x="80" y="180" width="440" height="16" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
        
        <text x="160" y="155" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">FABRICATED MS STEEL BEAM / CHANNEL (ISMB/ISMC)</text>
        <text x="160" y="170" fill="#cbd5e1" font-family="sans-serif" font-size="10">Transfers flexural tension &amp; reduces effective span deflection</text>
        
        <!-- Base Plates and Stiffeners -->
        <polygon points="100,130 120,130 120,180 100,180" fill="#f59e0b"/>
        <polygon points="480,130 500,130 500,180 480,180" fill="#f59e0b"/>
        <text x="50" y="215" fill="#f59e0b" font-family="sans-serif" font-size="10" font-weight="bold">Baseplate + Chemical Anchor</text>
        <text x="350" y="215" fill="#f59e0b" font-family="sans-serif" font-size="10" font-weight="bold">Anti-Corrosive Red Oxide Enamel Coated</text>
        
        <!-- Technical Badge -->
        <rect x="40" y="250" width="520" height="65" fill="#1e293b" rx="6" stroke="#334155"/>
        <text x="60" y="275" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">KEY ACTION: Structural Load-Bearing Capacity Augmentation</text>
        <text x="60" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11">Structural steel beams provide external flexural support, arrest deflection &amp; increase ultimate load capacity.</text>
        """
    )
]

for fname, title, content in steps_data:
    svg_code = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 330" width="100%" height="100%">
    <!-- Background Canvas -->
    <rect width="600" height="330" fill="#0b1329" rx="8"/>
    <rect width="600" height="330" fill="url(#grid)"/>
    {svg_defs}
    <!-- Title Banner -->
    <rect x="0" y="0" width="600" height="34" fill="#1e293b"/>
    <text x="20" y="22" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold" letter-spacing="0.5">{title}</text>
    {content}
</svg>"""
    fpath = os.path.join('static/images/steps', fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    print(f"Generated {fpath}")

# Also generate logo.svg
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
    <rect width="80" height="80" rx="16" fill="#0f172a"/>
    <rect x="2" y="2" width="76" height="76" rx="14" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <!-- Structural I-Beam symbol -->
    <path d="M 18 18 L 62 18 L 62 26 L 44 26 L 44 54 L 62 54 L 62 62 L 18 62 L 18 54 L 36 54 L 36 26 L 18 26 Z" fill="#f59e0b"/>
    <!-- AI Eye / Scanner line -->
    <circle cx="40" cy="40" r="7" fill="#38bdf8"/>
    <circle cx="40" cy="40" r="3" fill="#ffffff"/>
    <line x1="14" y1="40" x2="66" y2="40" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,2"/>
</svg>"""

with open('static/images/logo.svg', 'w', encoding='utf-8') as f:
    f.write(logo_svg)
print("Generated static/images/logo.svg")
