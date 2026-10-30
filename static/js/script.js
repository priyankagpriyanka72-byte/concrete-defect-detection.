/**
 * AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP
 * Frontend Logic & Interactive Controller
 */

// Application State
let currentSelectedFile = null;
let currentBase64Data = null;
let currentSampleName = null;
let cameraStream = null;
let knowledgeBaseData = {};

// Color Map for Classes
const CLASS_COLORS = {
    "Segregation": "#f59e0b",
    "Honeycombing": "#d97706",
    "Spalling": "#dc2626",
    "Crack": "#e11d48",
    "Void": "#7c3aed",
    "Efflorescence": "#0284c7",
    "No Defect": "#059669"
};

// Initialize Application
document.addEventListener("DOMContentLoaded", () => {
    initNavigation();
    initDropzone();
    initFileInputs();
    loadKnowledgeBase();
});

// Navigation Handling
function initNavigation() {
    const tabs = document.querySelectorAll(".nav-tab");
    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            const targetId = tab.getAttribute("data-target");
            switchTab(targetId);
        });
    });
}

function switchTab(targetId) {
    document.querySelectorAll(".nav-tab").forEach(t => {
        t.classList.toggle("active", t.getAttribute("data-target") === targetId);
    });
    document.querySelectorAll(".tab-content").forEach(content => {
        content.classList.toggle("active", content.id === targetId);
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Dropzone & File Input Handling
function initDropzone() {
    const dropZone = document.getElementById("drop-zone");
    if (!dropZone) return;

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.add("dragover");
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.remove("dragover");
        }, false);
    });

    dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files && files.length > 0) {
            handleSelectedFile(files[0]);
        }
    });

    dropZone.addEventListener('click', (e) => {
        if (e.target.tagName !== 'BUTTON') {
            document.getElementById("file-input").click();
        }
    });
}

function initFileInputs() {
    const fileInput = document.getElementById("file-input");
    if (fileInput) {
        fileInput.addEventListener("change", (e) => {
            if (e.target.files && e.target.files.length > 0) {
                handleSelectedFile(e.target.files[0]);
            }
        });
    }

    const mobileCam = document.getElementById("mobile-camera-input");
    if (mobileCam) {
        mobileCam.addEventListener("change", (e) => {
            if (e.target.files && e.target.files.length > 0) {
                handleSelectedFile(e.target.files[0]);
            }
        });
    }
}

function handleSelectedFile(file) {
    const validTypes = ['image/jpeg', 'image/png', 'image/jpg'];
    if (!validTypes.includes(file.type) && !file.name.match(/\.(jpe?g|png)$/i)) {
        alert("Please upload a valid JPG, JPEG, or PNG image file.");
        return;
    }

    currentSelectedFile = file;
    currentBase64Data = null;
    currentSampleName = null;

    const reader = new FileReader();
    reader.onload = (e) => {
        displayPreview(e.target.result);
        document.getElementById("analyse-btn").disabled = false;
        resetResults();
    };
    reader.readAsDataURL(file);
}

function displayPreview(srcUrl) {
    const previewImg = document.getElementById("preview-image");
    const overlayImg = document.getElementById("overlay-image");
    const placeholder = document.getElementById("placeholder-viewport");
    const viewToggles = document.getElementById("view-toggles");

    previewImg.src = srcUrl;
    previewImg.style.display = "block";
    overlayImg.style.display = "none";
    placeholder.style.display = "none";
    viewToggles.style.display = "none";

    // Reset toggles
    document.getElementById("btn-show-original").classList.add("active");
    document.getElementById("btn-show-overlay").classList.remove("active");
}

function clearInspection() {
    currentSelectedFile = null;
    currentBase64Data = null;
    currentSampleName = null;

    document.getElementById("file-input").value = "";
    document.getElementById("mobile-camera-input").value = "";

    const previewImg = document.getElementById("preview-image");
    const overlayImg = document.getElementById("overlay-image");
    const placeholder = document.getElementById("placeholder-viewport");
    const viewToggles = document.getElementById("view-toggles");
    const cvMetricsBar = document.getElementById("cv-metrics-bar");

    previewImg.src = "";
    previewImg.style.display = "none";
    overlayImg.src = "";
    overlayImg.style.display = "none";
    placeholder.style.display = "block";
    viewToggles.style.display = "none";
    cvMetricsBar.style.display = "none";

    document.getElementById("analyse-btn").disabled = true;
    resetResults();
}

function resetResults() {
    document.getElementById("rejection-banner").style.display = "none";
    document.getElementById("results-dashboard").style.display = "none";
}

// Quick Sample Testing
function testSample(sampleName) {
    switchTab("classifier-section");
    currentSelectedFile = null;
    currentBase64Data = null;
    currentSampleName = sampleName;

    const sampleUrl = `/static/images/samples/${sampleName}?v=${Date.now()}`;
    displayPreview(sampleUrl);
    document.getElementById("analyse-btn").disabled = false;
    resetResults();

    // Auto-trigger analysis for rapid testing
    runAnalysis();
}

// Live Camera Modal
function openCameraModal() {
    const modal = document.getElementById("camera-modal");
    const video = document.getElementById("camera-video");
    modal.style.display = "flex";

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ 
            video: { facingMode: { ideal: "environment" }, width: { ideal: 1280 } } 
        })
        .then(stream => {
            cameraStream = stream;
            video.srcObject = stream;
        })
        .catch(err => {
            alert("Could not access camera: " + err.message + ". You can use the 'Device Cam' file picker instead.");
            closeCameraModal();
        });
    } else {
        alert("Camera stream API not supported in this browser. Please use 'Select File' or 'Device Cam'.");
        closeCameraModal();
    }
}

function closeCameraModal() {
    const modal = document.getElementById("camera-modal");
    const video = document.getElementById("camera-video");
    if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
    }
    video.srcObject = null;
    modal.style.display = "none";
}

function captureCameraSnapshot() {
    const video = document.getElementById("camera-video");
    const canvas = document.getElementById("camera-canvas");
    if (!video.videoWidth) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const b64 = canvas.toDataURL("image/jpeg", 0.90);
    closeCameraModal();

    currentSelectedFile = null;
    currentBase64Data = b64;
    currentSampleName = null;

    displayPreview(b64);
    document.getElementById("analyse-btn").disabled = false;
    resetResults();
    runAnalysis();
}

// Toggle Image View between Original & OpenCV Map
function toggleImageView(mode) {
    const previewImg = document.getElementById("preview-image");
    const overlayImg = document.getElementById("overlay-image");
    const btnOriginal = document.getElementById("btn-show-original");
    const btnOverlay = document.getElementById("btn-show-overlay");

    if (mode === 'original') {
        previewImg.style.display = "block";
        overlayImg.style.display = "none";
        btnOriginal.classList.add("active");
        btnOverlay.classList.remove("active");
    } else {
        previewImg.style.display = "none";
        overlayImg.style.display = "block";
        btnOriginal.classList.remove("active");
        btnOverlay.classList.add("active");
    }
}

// Run Analysis
function runAnalysis() {
    const loadingOverlay = document.getElementById("loading-overlay");
    loadingOverlay.style.display = "flex";
    resetResults();

    let requestPromise;

    if (currentSampleName) {
        // Sample test payload
        requestPromise = fetch('/api/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sample_name: currentSampleName })
        });
    } else if (currentSelectedFile) {
        // Direct file upload
        const formData = new FormData();
        formData.append('image', currentSelectedFile);
        requestPromise = fetch('/api/predict', {
            method: 'POST',
            body: formData
        });
    } else if (currentBase64Data) {
        // Camera snapshot base64
        requestPromise = fetch('/api/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image_base64: currentBase64Data })
        });
    } else {
        loadingOverlay.style.display = "none";
        alert("Please select or upload an image first.");
        return;
    }

    requestPromise
        .then(res => res.json())
        .then(data => {
            loadingOverlay.style.display = "none";
            handleAnalysisResponse(data);
        })
        .catch(err => {
            loadingOverlay.style.display = "none";
            alert("Analysis failed: " + err.message);
        });
}

// Handle Analysis API Response
function handleAnalysisResponse(data) {
    if (data.status === "error") {
        alert("Error: " + data.message);
        return;
    }

    // 1. Validation Rejection (Unrelated objects)
    if (data.status === "rejected" || !data.validation_passed) {
        const rejectionBanner = document.getElementById("rejection-banner");
        document.getElementById("rejection-title").innerText = data.message;
        document.getElementById("rejection-reason").innerText = data.technical_reason || "Image does not exhibit concrete surface properties.";
        rejectionBanner.style.display = "flex";
        
        // Hide defect dashboard
        document.getElementById("results-dashboard").style.display = "none";
        document.getElementById("view-toggles").style.display = "none";
        document.getElementById("cv-metrics-bar").style.display = "none";
        return;
    }

    // 2. Verified Concrete Surface -> Populate Results Dashboard
    document.getElementById("rejection-banner").style.display = "none";
    const resultsDash = document.getElementById("results-dashboard");
    resultsDash.style.display = "flex";

    // Setup OpenCV Inspection Overlay
    if (data.inspection_overlay) {
        const overlayImg = document.getElementById("overlay-image");
        overlayImg.src = data.inspection_overlay;
        document.getElementById("view-toggles").style.display = "flex";
    }

    // Setup CV Metrics Bar
    if (data.cv_stats) {
        document.getElementById("val-edge-density").innerText = (data.cv_stats.edge_pixel_ratio * 100).toFixed(1) + "%";
        document.getElementById("val-cavities").innerText = data.cv_stats.detected_cavities;
        document.getElementById("val-brightness").innerText = data.cv_stats.mean_surface_brightness + "/255";
        document.getElementById("cv-metrics-bar").style.display = "flex";
    }

    // Defect Header
    const defectName = data.predicted_defect;
    const isNoDefect = data.is_no_defect;
    const advisory = data.advisory || {};

    const nameEl = document.getElementById("result-defect-name");
    const descEl = document.getElementById("result-defect-desc");
    const badgeCategory = document.getElementById("result-badge-category");
    const confScoreEl = document.getElementById("result-conf-score");
    const confBox = document.getElementById("confidence-box");
    const soundBanner = document.getElementById("sound-concrete-banner");
    const probBox = document.getElementById("probability-breakdown-box");

    nameEl.innerText = defectName;
    descEl.innerText = advisory.description || "";
    badgeCategory.innerText = advisory.category || "Concrete Inspection";
    badgeCategory.style.color = advisory.badge_color || "#f59e0b";
    badgeCategory.style.background = (advisory.badge_color || "#f59e0b") + "26";

    // Genuine Confidence Score
    if (data.confidence_display) {
        confScoreEl.innerText = data.confidence_display;
        confBox.style.display = "block";
    } else {
        confBox.style.display = "none";
    }

    // Sound Concrete (No Defect) Special Handling
    if (isNoDefect) {
        soundBanner.style.display = "flex";
        nameEl.innerText = "No Defect (Sound Concrete)";
        probBox.style.display = "none";
    } else {
        soundBanner.style.display = "none";
        probBox.style.display = "block";
        renderProbabilityBars(data.class_probabilities, defectName);
    }

    // Causes List
    const causesList = document.getElementById("causes-list");
    causesList.innerHTML = "";
    (advisory.possible_causes || []).forEach(c => {
        const li = document.createElement("li");
        li.innerText = c;
        causesList.appendChild(li);
    });

    // Severity Assessment
    const severityBadge = document.getElementById("severity-badge");
    const severityGuide = document.getElementById("severity-guide");
    const severityDisclaimer = document.getElementById("severity-disclaimer");
    
    if (advisory.severity_assessment) {
        severityBadge.innerText = advisory.severity_assessment.preliminary_level || "Preliminary Assessment";
        severityGuide.innerText = advisory.severity_assessment.classification_guide || "";
        severityDisclaimer.innerText = advisory.severity_assessment.structural_safety_disclaimer || "Preliminary assessment; not a certified structural safety certificate.";
    }

    // Prevention List
    const prevList = document.getElementById("prevention-list");
    prevList.innerHTML = "";
    (advisory.prevention_methods || []).forEach(p => {
        const li = document.createElement("li");
        li.innerText = p;
        prevList.appendChild(li);
    });

    // Repair List
    const repairList = document.getElementById("repair-list");
    repairList.innerHTML = "";
    (advisory.suitable_repair_methods || []).forEach(r => {
        const li = document.createElement("li");
        li.innerText = r;
        repairList.appendChild(li);
    });

    // Maintenance List
    const maintList = document.getElementById("maintenance-list");
    maintList.innerHTML = "";
    (advisory.maintenance_advice || []).forEach(m => {
        const li = document.createElement("li");
        li.innerText = m;
        maintList.appendChild(li);
    });

    // Slab Relevance
    const slabText = document.getElementById("slab-relevance-text");
    if (advisory.slab_strengthening_relevance) {
        slabText.innerText = advisory.slab_strengthening_relevance;
    }
}

// Render Probability Bars for 6 Classes
function renderProbabilityBars(probDict, selectedClass) {
    const container = document.getElementById("prob-bars-container");
    container.innerHTML = "";
    if (!probDict) return;

    // Sort by probability descending
    const entries = Object.entries(probDict).sort((a, b) => b[1] - a[1]);

    entries.forEach(([cls, prob]) => {
        const item = document.createElement("div");
        item.className = "prob-item";

        const isTop = cls === selectedClass;
        const color = CLASS_COLORS[cls] || "#f59e0b";

        item.innerHTML = `
            <div class="prob-label-row">
                <span style="color: ${isTop ? color : '#cbd5e1'}; font-weight: ${isTop ? '700' : '500'};">
                    ${cls} ${isTop ? '<i class="fa-solid fa-check" style="font-size:0.75rem; margin-left:4px;"></i>' : ''}
                </span>
                <span style="font-family: var(--font-mono); color: ${color};">${prob.toFixed(1)}%</span>
            </div>
            <div class="prob-track">
                <div class="prob-fill" style="width: ${prob}%; background: ${color};"></div>
            </div>
        `;
        container.appendChild(item);
    });
}

// Switch to RCC Slab Strengthening Section
function viewRCCSlabStrengthening() {
    switchTab("rcc-section");
    const target = document.getElementById("rcc-step-1");
    if (target) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
}

// Load Knowledge Base Data
function loadKnowledgeBase() {
    fetch('/api/knowledge-base')
        .then(res => res.json())
        .then(data => {
            knowledgeBaseData = data;
            renderKnowledgeBase('all');
        })
        .catch(err => {
            console.warn("Could not load knowledge base dynamically:", err);
        });
}

// Filter and Render Knowledge Base
function filterKnowledgeBase(filterKey) {
    document.querySelectorAll(".kb-tab-btn").forEach(btn => {
        btn.classList.toggle("active", btn.innerText.includes(filterKey) || (filterKey === 'all' && btn.innerText.includes('All')));
    });

    renderKnowledgeBase(filterKey);
}

function renderKnowledgeBase(filterKey) {
    const container = document.getElementById("kb-cards-container");
    if (!container || !knowledgeBaseData) return;
    container.innerHTML = "";

    const keys = Object.keys(knowledgeBaseData);
    const targetKeys = filterKey === 'all' ? keys : keys.filter(k => k.toLowerCase() === filterKey.toLowerCase());

    targetKeys.forEach(key => {
        const item = knowledgeBaseData[key];
        const block = document.createElement("div");
        block.className = "kb-defect-block";

        const color = item.badge_color || "#f59e0b";

        block.innerHTML = `
            <div class="kb-defect-header">
                <div>
                    <span class="class-chip" style="background: ${color}26; color: ${color}; margin-bottom: 0.5rem;">
                        ${item.category}
                    </span>
                    <h3>${item.name}</h3>
                </div>
                <button class="btn btn-sm btn-outline" onclick="testSample('${key.toLowerCase()}_sample.jpg')">
                    <i class="fa-solid fa-vial"></i> Test ${item.name}
                </button>
            </div>
            <p style="color: var(--text-sub); margin-bottom: 1.5rem; font-size: 0.95rem;">
                ${item.description}
            </p>
            <div class="advisory-cards-grid">
                <div class="advisory-card">
                    <h4>Possible Causes</h4>
                    <ul class="advisory-list">
                        ${(item.possible_causes || []).map(c => `<li>${c}</li>`).join('')}
                    </ul>
                </div>
                <div class="advisory-card">
                    <h4>Prevention Methods</h4>
                    <ul class="advisory-list">
                        ${(item.prevention_methods || []).map(p => `<li>${p}</li>`).join('')}
                    </ul>
                </div>
                <div class="advisory-card">
                    <h4>Suitable Repair Methods</h4>
                    <ul class="advisory-list">
                        ${(item.suitable_repair_methods || []).map(r => `<li>${r}</li>`).join('')}
                    </ul>
                </div>
                <div class="advisory-card">
                    <h4>Maintenance Advice</h4>
                    <ul class="advisory-list">
                        ${(item.maintenance_advice || []).map(m => `<li>${m}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
        container.appendChild(block);
    });
}
