import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# -----------------------------
# 画像の Base64 読み込み
# -----------------------------
file_path = "black-gold-design4.jpg"

def get_b64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

bg_tile_src = get_b64(file_path)

# -----------------------------
# Streamlit レイアウト
# -----------------------------
st.set_page_config(layout="wide", page_title="THINK ENGINE - SOLSTICE")

st.markdown("""
<style>
[data-testid="stHeader"] { display: none !important; }
.main .block-container { padding: 0 !important; max-width: 100vw !important; }
[data-testid="stAppViewContainer"], [data-testid="stMain"] { margin: 0; padding: 0; overflow: hidden; background-color: #000; }
iframe { border: none; width: 100vw; height: 100vh; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HTML 本体（英語対応版）
# -----------------------------
fusion_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        html, body {{ margin: 0; padding: 0; overflow: hidden; background: #000; color: #00ffcc; font-family: monospace; width: 100%; height: 100%; }}
        #world-container {{ width: 100%; height: 100%; position: relative; overflow: hidden; }}
        #world {{ width: 100%; height: 100%; position: absolute; top: 0; left: 0; transition: transform 4s ease-in-out; }}
        #world.rotate-phase {{ transform: rotate(180deg); }}
        canvas {{ display: block; position: absolute; top: 0; left: 0; }}
        #bgCanvas {{ z-index: 1; }}
        
        #stage-curtain {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 500; background-image: url('{bg_tile_src}'); background-size: cover; background-position: center; background-repeat: no-repeat; opacity: 0; mix-blend-mode: screen; pointer-events: none; transition: opacity 3s ease; }}
        #ui-layer {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 6000; pointer-events: none; }}
        
        #opening-screen {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 3000; background: rgba(0,0,0,0.85); display: flex; flex-direction: column; justify-content: center; align-items: center; transition: opacity 1s ease-in-out; pointer-events: auto; }}
        .quote-box {{ text-align: center; max-width: 600px; margin: 0 0 50px 0; display: flex; flex-direction: column; justify-content: center; align-items: center; }}
        .quote-text {{ font-size: 24px; font-weight: 300; letter-spacing: 4px; color: #e0e0e0; opacity: 0; transition: opacity 2s ease-in-out; line-height: 2; margin: 15px 0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; text-align: center; }}
        
        #entry-btn {{ background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.4); padding: 14px 40px; font-size: 14px; letter-spacing: 3px; cursor: pointer; opacity: 0; transition: opacity 2s, background 0.3s, color 0.3s; font-family: monospace; border-radius: 4px; pointer-events: auto; }}
        #entry-btn:hover {{ background: #00ffcc; color: #000; border-color: #00ffcc; box-shadow: 0 0 15px rgba(0,255,204,0.4); }}
        #plug {{ position: absolute; left: 50px; top: 50px; width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; cursor: grab; z-index: 7000; user-select: none; font-size: 40px; filter: drop-shadow(0 0 10px #ffff00); background: rgba(255,255,255,0.05); border-radius: 50%; border: 1px dashed #ffff00; opacity: 0; transition: opacity 1s; pointer-events: auto; }}
        
        #left-ui-wrapper {{ position: absolute; top: 20px; left: 20px; z-index: 6500; display: flex; flex-direction: column; gap: 15px; pointer-events: auto; opacity: 0; transition: opacity 1s; }}
        #ui-container {{ background: rgba(0, 15, 10, 0.8); padding: 15px; border: 1px solid #00ffcc; width: 320px; }}
        #collection-library {{ background: rgba(0, 15, 10, 0.8); padding: 15px; border: 1px solid #00ffcc; width: 320px; transition: opacity 1s; }}
        .col-item {{ font-size: 24px; border: 1px solid #00ffcc; padding: 5px; margin-right: 5px; transition: all 1.5s ease; display: inline-block; text-align: center; min-width: 35px; }}
        
        #monologue-panel {{ background: rgba(0, 15, 10, 0.8); padding: 15px; border: 1px solid #00ffcc; width: 320px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.1); }}
        .result-content {{ font-size: 12px; line-height: 1.6; color: #e0faff; border-left: 2px solid #00ffcc; padding-left: 10px; word-break: break-all; }}
        .terminal-header {{ font-size: 11px; color: #00ffcc; margin-bottom: 8px; opacity: 0.7; letter-spacing: 2px; }}

        #revelation-screen {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 4000; display: flex; flex-direction: column; justify-content: center; align-items: center; pointer-events: none; }}
        .revelation-box {{ text-align: center; max-width: 750px; padding: 30px; background: rgba(0,0,0,0.6); border-radius: 8px; backdrop-filter: blur(4px); opacity: 0; transition: opacity 1.5s ease-in-out; display: flex; flex-direction: column; justify-content: center; align-items: center; }}
        .revelation-box.show {{ opacity: 1; }}
        .revelation-symbol {{ font-size: 55px; margin-bottom: 25px; filter: drop-shadow(0 0 15px #ffcc00); animation: pulse 3s infinite alternate; text-align: center; }}
        .revelation-title {{ color: #00ffcc; font-size: 22px; font-weight: bold; margin-bottom: 20px; text-shadow: 0 0 15px #00ffcc; letter-spacing: 3px; text-align: center; }}
        .revelation-text {{ font-size: 20px; font-weight: 300; letter-spacing: 4px; color: #ffffff; line-height: 2.2; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; text-shadow: 0 0 8px rgba(255,255,255,0.5); text-align: center; }}
        
        @keyframes pulse {{ from {{ transform: scale(0.95); opacity: 0.8; }} to {{ transform: scale(1.05); opacity: 1; }} }}
    </style>
</head>
<body>
<div id="world-container">
    <div id="world">
        <canvas id="bgCanvas"></canvas>
    </div>
    <div id="stage-curtain"></div>
    <div id="ui-layer">
        <div id="opening-screen">
            <div class="quote-box">
                <div id="q1" class="quote-text">Tell me.</div>
                <div id="q2" class="quote-text">What was humanity?</div>
            </div>
            <button id="entry-btn" onclick="startObservation()">INITIATE OBSERVATION</button>
        </div>
        
        <div id="plug" onmousedown="dragStart(event, this)">🛰️</div>
        
        <div id="left-ui-wrapper">
            <div id="ui-container">
                <div style="font-size: 18px; font-weight: bold; text-shadow: 0 0 10px #00ffcc;">THINK ENGINE v5.5</div>
                <div style="font-size: 10px; margin-top: 5px; color: #585;">PERMANENT SOLSTICE GRID</div>
                <div id="status-field" style="font-size: 11px; margin-top: 10px; color: #00ffcc;">UNDERSTANDING: 0%</div>
            </div>
            <div id="collection-library">
                <div class="terminal-header">>>> COLLECTED_DATA</div>
                <div id="library-list" style="display: flex; gap: 5px; margin-top: 5px; flex-wrap: wrap;">
                    <span class="col-item" id="slot0">◇</span><span class="col-item" id="slot1">◇</span>
                    <span class="col-item" id="slot2">◇</span><span class="col-item" id="slot3">◇</span>
                    <span class="col-item" id="slot4">◇</span><span class="col-item" id="slot5">◇</span>
                </div>
            </div>
            <div id="monologue-panel" style="display: none;">
                <div class="terminal-header">>>> COGNITIVE_LOG_STREAM</div>
                <div id="log-text" class="result-content">
                    Use [A/D] keys to navigate. Drag 🛰️ over geometric anomalies to discharge.
                </div>
            </div>
        </div>

        <div id="revelation-screen">
            <div id="revelation-container" class="revelation-box">
                <div id="rev-symbol" class="revelation-symbol"></div>
                <div id="rev-title" class="revelation-title"></div>
                <div id="rev-text" class="revelation-text"></div>
            </div>
        </div>
    </div>
</div>

<script>
    const canvas = document.getElementById("bgCanvas");
    const ctx = canvas.getContext("2d");

    function getW() {{ return document.body.offsetWidth || window.innerWidth; }}
    function getH() {{ return document.body.offsetHeight || window.innerHeight; }}

    let cw = canvas.width = getW();
    let ch = canvas.height = getH();
    canvas.style.width = cw + "px";
    canvas.style.height = ch + "px";

    const inputKeys = {{}};
    let _worldX = 0;
    let cluesFound = 0;
    let isReversedPhase = false;
    let isLive = false;
    let isSunActive = false;
    let activeDrag = null;
    let offX, offY;
    let revelationTimeout = null;

    let finalSequenceStage = 0; 

    const viewSize = 250;
    const offscreenCanvas = document.createElement("canvas");
    offscreenCanvas.width = viewSize;
    offscreenCanvas.height = viewSize;
    const offCtx = offscreenCanvas.getContext("2d");

    let audioCtx = null;
    function getAudioCtx() {{
        if (!audioCtx) {{
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }}
        if (audioCtx.state === 'suspended') {{
            audioCtx.resume();
        }}
        return audioCtx;
    }}
    document.addEventListener('click', () => {{ getAudioCtx(); }}, {{ once: false }});

    function updateLog(txt) {{
        const el = document.getElementById("log-text");
        if(el) el.innerText = txt;
    }}

    function triggerRevelation(symbol, title, text, duration = 3500) {{
        const container = document.getElementById("revelation-container");
        const symEl = document.getElementById("rev-symbol");
        const titleEl = document.getElementById("rev-title");
        const textEl = document.getElementById("rev-text");

        if (revelationTimeout) clearTimeout(revelationTimeout);

        symEl.innerText = symbol;
        titleEl.innerHTML = title;
        textEl.innerHTML = text;

        container.classList.add("show");

        if (duration !== "infinite") {{
            revelationTimeout = setTimeout(() => {{
                container.classList.remove("show");
            }}, duration);
        }}
    }}
    
    function dragStart(e, el) {{
        activeDrag = el;
        const rect = el.getBoundingClientRect();
        offX = e.clientX - rect.left;
        offY = e.clientY - rect.top;
        el.style.zIndex = 8000;
    }}
    
    window.onmousemove = (e) => {{
        if(!activeDrag) return;
        activeDrag.style.left = (e.clientX - offX) + "px";
        activeDrag.style.top = (e.clientY - offY) + "px";
        if(isLive) checkHit();
    }};
    window.onmouseup = () => {{ activeDrag = null; }};

    setTimeout(() => {{ document.getElementById("q1").style.opacity = 1; }}, 800);
    setTimeout(() => {{ document.getElementById("q2").style.opacity = 1; }}, 2300);
    setTimeout(() => {{ document.getElementById("entry-btn").style.opacity = 1; }}, 3800);

    function startObservation() {{
        getAudioCtx();
        document.getElementById("opening-screen").style.opacity = 0;
        setTimeout(() => {{ document.getElementById("opening-screen").style.display = "none"; }}, 1000);
        document.getElementById("left-ui-wrapper").style.opacity = 1;
        document.getElementById("plug").style.opacity = 1;
        playAmbientTone(180, 'sine', 0.6);
        isLive = true;
    }}

    const nodes = [];
    for(let i=0; i<45; i++) {{
        nodes.push({{ x: Math.random() * cw, y: Math.random() * ch, vx: (Math.random() - 0.5) * 0.4, vy: (Math.random() - 0.5) * 0.4, r: Math.random() * 2 + 1 }});
    }}
    
    const shapes = [];
    for(let i=0; i<12; i++) {{
        let sType = i%3===0 ? 'tri' : (i%3===1 ? 'rect' : 'diamond');
        let labelName = (sType === 'tri') ? 'ZEBRA' : (sType === 'rect') ? 'PETAL' : 'SHELL';

        shapes.push({{ 
            x: 500 + i*600, 
            y: Math.random() * ch * 0.8 + 50, 
            type: sType, 
            size: Math.random() * 30 + 20, 
            speed: Math.random() * 0.5 + 0.2, 
            found: false, 
            confidence: 0,
            sym: sType === 'tri' ? '△' : (sType === 'rect' ? '□' : '◇'),
            finalLabel: labelName,
            phase: Math.random() * Math.PI * 2
        }});
    }}

    const clues = [
        {{ x: 800,  sym: "❄️", hidden: "◇", finalLabel: "SNOWFLAKE", found: false, confidence: 0, log: "Anomalous connection: [SNOWFLAKE] verified." }},
        {{ x: 1800, sym: "🌿", hidden: "◇", finalLabel: "VEIN", found: false, confidence: 0, log: "Anomalous connection: [VEIN] verified." }},
        {{ x: 2800, sym: "🐚", hidden: "◇", finalLabel: "SPIRAL", found: false, confidence: 0, log: "Anomalous connection: [SPIRAL] verified." }}
    ];

    let sunEventTriggered = false;

    function checkHit() {{
        const p = document.getElementById("plug").getBoundingClientRect();
        const plug = {{ x: p.left + p.width/2, y: p.top + p.height/2 }};

        clues.forEach((clue, index) => {{
            if (clue.found) return;
            let screenX = clue.x - _worldX;
            let screenY = ch * 0.65;
            if (isSunActive) {{ screenX = cw - screenX; screenY = ch - screenY; }}

            let dist = Math.hypot(plug.x - screenX, plug.y - screenY);
            if (dist < 100) {{
                clue.confidence = Math.min(clue.confidence + 0.02, 1.0);
                if (clue.confidence >= 0.95) {{
                    clue.found = true;
                    handleDiscovery(clue.sym, clue.log, clue.finalLabel);
                    playAmbientTone(440 + index * 100, 'sine', 0.5);
                }}
            }}
        }});
        
        shapes.forEach((s, i) => {{
            if (s.found) return;
            let sx = (s.x - _worldX * s.speed);
            let floatY = s.y + Math.sin(Date.now() * 0.002 + s.phase) * 50;
            if (isSunActive) {{ sx = cw - sx; floatY = ch - floatY; }}

            let dist = Math.hypot(plug.x - sx, plug.y - floatY);
            if (dist < 100) {{
                s.confidence = Math.min(s.confidence + 0.03, 1.0);
                if (s.confidence >= 0.95) {{
                    s.found = true;
                    handleDiscovery(s.sym, "Fragment" + s.sym + " integrated.", s.finalLabel);
                    playAmbientTone(660, 'square', 0.5);
                }}
            }}
        }});

        if (cluesFound >= 6) {{
            setTimeout(triggerFinalPattern, 2000);
        }}
    }}

    function handleDiscovery(sym, log, finalLabel) {{
        document.getElementById("slot" + cluesFound).innerText = sym;
        updateLog(log);
        cluesFound++;
        processMeaning(sym, finalLabel);
    }}

    function processMeaning(sym, finalLabel) {{
        if (finalLabel === "SNOWFLAKE") {{
            triggerRevelation("❄️", "[RECIPE: COSMOS]",
                "Snow is a blueprint from the sky.<br>Humans called it a crystal.<br><br>────────────<br><br>Input: Water<br>Output: Order"
            );

        }} else if (finalLabel === "VEIN") {{
            triggerRevelation("🌿", "[RECIPE: COSMOS]",
                "Plants consume the light.<br>Humans called it photosynthesis.<br><br>────────────<br><br>Input: Light<br>Output: Life"
            );
            if (!sunEventTriggered) {{
                setTimeout(triggerSunEvent, 4000);
            }}

        }} else if (finalLabel === "SPIRAL") {{
            triggerRevelation("🐚", "[RECIPE: COSMOS]",
                "Shells grow slightly each day.<br>Humans called it growth.<br><br>────────────<br><br>Input: Time<br>Output: Spiral"
            );
            if (!sunEventTriggered) {{
                setTimeout(triggerSunEvent, 4000);
            }}

        }} else if (finalLabel === "ZEBRA") {{
            triggerRevelation("🦓", "[FRAGMENT: △]",
                "Math weaves the skin of life.<br>Humans called it stripes.<br><br>────────────<br><br>Logic running on flesh.<br>They called it a Zebra."
            );

        }} else if (finalLabel === "PETAL") {{
            triggerRevelation("🌸", "[FRAGMENT: □]",
                "Petals know the sequence.<br>Humans called it Fibonacci.<br><br>────────────<br><br>Input: Growth Rule<br>Output: Beauty"
            );

        }} else if (finalLabel === "SHELL") {{
            triggerRevelation("🐚", "[FRAGMENT: ◇]",
                "A vortex is the body of an equation.<br>Humans called it a spiral."
            );
        }}
    }}

    function triggerSunEvent() {{
        if (sunEventTriggered) return;
        sunEventTriggered = true;

        isSunActive = true;
        triggerRevelation("☀️", "[ENV_SHIFT]",
            "The sun rises.<br>Humans called it a day.",
            4000
        );
        updateLog("System: Stellar simulation activated.");
        document.getElementById("world").classList.add("rotate-phase");
        document.getElementById("stage-curtain").style.opacity = 1.0;
    }}

    function draw() {{
        if (finalSequenceStage === 5) {{
            updateTuring();
            drawTuring();
            requestAnimationFrame(draw);
            return;
        }}

        const activeColor = isSunActive ? "#ffcc00" : "#00ffcc";
        const activeRGB = isSunActive ? "255, 204, 0" : "0, 255, 204";

        ctx.fillStyle = "rgba(0, 0, 0, 0.15)";
        ctx.fillRect(0, 0, cw, ch);
        
        shapes.forEach(s => {{
            let sx = (s.x - _worldX * s.speed);
            let floatY = s.y + Math.sin(Date.now() * 0.002 + s.phase) * 50;
            
            if (finalSequenceStage >= 1) {{
                ctx.fillStyle = `rgba(${{activeRGB}}, 0.65)`;
                ctx.font = "20px monospace";
                ctx.textAlign = "center";
                
                let targetText = s.sym;
                
                if (finalSequenceStage === 1) {{
                    targetText = s.finalLabel;
                }} else if (finalSequenceStage === 2) {{
                    targetText = s.type === 'tri' ? 'VEIN' : (s.type === 'rect' ? 'SNOW' : 'SHELL');
                }} else if (finalSequenceStage === 3) {{
                    targetText = s.type === 'tri' ? 'PATTERN' : (s.type === 'rect' ? 'TIME' : 'LIGHT');
                }} else if (finalSequenceStage >= 4) {{
                    targetText = Math.random() < 0.5 ? "0" : "1";
                    ctx.fillStyle = "rgba(0, 255, 204, 0.2)";
                }}
                ctx.fillText(targetText, sx, floatY);
                return;
            }}

            const p = document.getElementById("plug").getBoundingClientRect();
            const plug = {{ x: p.left + p.width/2, y: p.top + p.height/2 }};
            let dist = Math.hypot(plug.x - sx, plug.y - floatY);

            if (s.found) {{
                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 16px monospace";
                ctx.textAlign = "center";
                ctx.fillText(`[${{s.finalLabel}}]`, sx, floatY);
            }} else if (dist < 320) {{
                let opacity = 0.3 + (s.confidence * 0.6);
                ctx.fillStyle = `rgba(${{activeRGB}}, ${{opacity}})`;
                ctx.font = "italic 16px monospace";
                ctx.textAlign = "center";
                let label = (s.confidence > 0.5) ? s.finalLabel : s.sym;
                ctx.fillText(label, sx, floatY);
            }} else {{
                ctx.fillStyle = `rgba(${{activeRGB}}, 0.3)`;
                ctx.font = "20px monospace";
                ctx.textAlign = "center";
                ctx.fillText("◇", sx, floatY);
            }}
        }});

        nodes.forEach((n, i) => {{
            n.x += n.vx; n.y += n.vy;
            if(n.x < 0) n.x = cw; if(n.x > cw) n.x = 0; if(n.y < 0 || n.y > ch) n.vy *= -1;
            let displayX = (n.x - _worldX * 0.1) % cw;
            if(displayX < 0) displayX += cw;
            ctx.beginPath(); ctx.arc(displayX, n.y, n.r, 0, Math.PI * 2);
            ctx.fillStyle = activeColor;
            
            if (finalSequenceStage >= 4) return;
            ctx.fill();
            
            for(let j=i+1; j<nodes.length; j++) {{
                let displayX2 = (nodes[j].x - _worldX * 0.1) % cw;
                if(displayX2 < 0) displayX2 += cw;
                const dx = displayX - displayX2; const dy = n.y - nodes[j].y; const dist = Math.sqrt(dx*dx + dy*dy);
                if(dist < 150) {{
                    ctx.beginPath();
                    ctx.moveTo(displayX, n.y); ctx.lineTo(displayX2, nodes[j].y);
                    ctx.strokeStyle = `rgba(${{activeRGB}}, ${{1 - dist/150}})`; ctx.lineWidth = 0.5;
                    if (finalSequenceStage < 4) ctx.stroke(); 
                }}
            }}
        }});
        
        if (finalSequenceStage < 4) ctxMainLine(activeRGB);

        if (isLive) {{
            clues.forEach(clue => {{
                let screenX = clue.x - _worldX;
                let floatY = Math.sin(Date.now() * 0.003) * 8;
                ctx.save();
                if (clue.found) {{
                    ctx.shadowBlur = 25;
                    ctx.shadowColor = activeColor;
                    ctx.translate(screenX, ch * 0.65 + floatY);
                    ctx.rotate(Math.sin(Date.now() * 0.02) * 0.1);
                    ctx.font = "50px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(clue.foundSym || clue.sym, 0, 0);
                }} else {{
                    ctx.font = "35px sans-serif"; ctx.textAlign = "center";
                    ctx.fillStyle = activeColor;
                    ctx.fillText(clue.hidden, screenX, ch * 0.65 + floatY);
                }}
                ctx.restore();
            }});
            
            ctx.save();
            ctx.translate(cw / 2, ch * 0.72);
            ctx.shadowBlur = 20;
            ctx.shadowColor = activeColor;
            ctx.fillStyle = activeColor;
            ctx.beginPath(); ctx.arc(0, -20, 15, 0, Math.PI * 2); ctx.fill();
            ctx.strokeStyle = activeColor;
            ctx.lineWidth = 4; ctx.beginPath();
            ctx.moveTo(-8, -5); ctx.lineTo(-8, 10); ctx.moveTo(8, -5); ctx.lineTo(8, 10); ctx.stroke(); 
            if (inputKeys["arrowleft"] || inputKeys["a"] || inputKeys["arrowright"] || inputKeys["d"]) {{
                ctx.fillStyle = "#ffff00"; ctx.fillText("🛰️", Math.random()*20-10, -40);
                if (inputKeys["arrowleft"] || inputKeys["a"]) _worldX -= 6;
                if (inputKeys["arrowright"] || inputKeys["d"]) _worldX += 6;
            }}
            ctx.restore();
            _worldX += 0.5;
            if (_worldX < 0) _worldX = 0;
            document.getElementById("status-field").innerText = `UNDERSTANDING: ${{Math.floor((cluesFound/6)*100)}}%`;
        }}
        requestAnimationFrame(draw);
    }}

    function ctxMainLine(rgb) {{
        ctx.strokeStyle = isReversedPhase ? "rgba(255, 0, 100, 0.6)" : `rgba(${{rgb}}, 0.3)`; 
        ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(0, ch * 0.72); ctx.lineTo(cw, ch * 0.72); ctx.stroke(); 
    }}

    function triggerFinalPattern() {{
        isLive = false;
        document.getElementById("plug").style.display = "none";
        document.getElementById("ui-container").style.display = "none";
        document.getElementById("monologue-panel").style.display = "none";
        
        finalSequenceStage = 1;
        _worldX = 0; 

        const labelMap = ["ZEBRA", "PETAL", "SHELL", "SNOWFLAKE", "VEIN", "SPIRAL"];
        labelMap.forEach((text, idx) => {{
            const el = document.getElementById("slot" + idx);
            if (el) {{
                el.innerText = text;
                el.style.fontSize = "10px";
                el.style.color = "#fff";
                el.style.borderColor = "#fff";
            }}
        }});

        triggerRevelation(
            " ", 
            "[ANALYSIS COMPLETE]", 
            "Humanity thought<br>the world was made of separate phenomena.", 
            "infinite"
        );
        playAmbientTone(261.63, 'sine', 1.0);

        setTimeout(() => {{
            finalSequenceStage = 2;
            triggerRevelation(
                " ", 
                "[ANALYSIS COMPLETE]", 
                "Snow, leaves, shells, stripes...<br><br>They were never separate.", 
                "infinite"
            );
            playAmbientTone(293.66, 'sine', 1.0);
        }}, 3500);

        setTimeout(() => {{
            finalSequenceStage = 3;
            triggerRevelation(
                " ", 
                "[ANALYSIS COMPLETE]", 
                "Different solutions<br>to the same equation.", 
                "infinite"
            );
            playAmbientTone(329.63, 'sine', 1.2);
        }}, 7000);

        setTimeout(() => {{
            finalSequenceStage = 4;
            
            const slots = ["slot0", "slot1", "slot2", "slot3", "slot4", "slot5"];
            slots.forEach((id, idx) => {{
                const el = document.getElementById(id);
                if (el) {{
                    el.innerText = idx % 2 === 0 ? "0" : "1";
                    el.style.color = "#00ffcc";
                    el.style.textShadow = "0 0 10px #00ffcc";
                }}
            }});

            triggerRevelation(
                " ", 
                " ", 
                "INPUT<br>Light・Time・Water<br>↓<br><br>Computation<br>↓<br><br>The Form of Life", 
                "infinite"
            );
            playAmbientTone(392.00, 'sine', 1.5);
        }}, 10500);

        setTimeout(() => {{
            seedTuring();
            isReversedPhase = true;
            finalSequenceStage = 5;
            
            document.getElementById("collection-library").style.opacity = 0;
            document.getElementById("stage-curtain").style.opacity = 0;

            triggerRevelation(
                " ", 
                " ", 
                "The world was computed.<br><br><br><br>Humanity called this:<br>TURING PATTERNS.", 
                "infinite"
            );
            playAmbientTone(440.00, 'sine', 3.0);
        }}, 15000);
    }}
    
    function playAmbientTone(freq, type, duration) {{
        if (finalSequenceStage === 5) return;
        try {{
            const ac = getAudioCtx();
            const osc = ac.createOscillator();
            const gain = ac.createGain();
            osc.type = type;
            osc.frequency.value = freq;
            gain.gain.setValueAtTime(0.04, ac.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.0001, ac.currentTime + duration);
            osc.connect(gain);
            gain.connect(ac.destination);
            osc.start();
            osc.stop(ac.currentTime + duration);
        }} catch(e) {{
            console.warn("AudioContext error:", e);
        }}
    }}
    
    window.onkeydown = (e) => {{ if (finalSequenceStage < 5) inputKeys[e.key.toLowerCase()] = true; }}; 
    window.onkeyup = (e) => {{ if (finalSequenceStage < 5) inputKeys[e.key.toLowerCase()] = false; }}; 
    window.onresize = () => {{ 
        cw = canvas.width = getW();
        ch = canvas.height = getH();
        canvas.style.width = cw + "px";
        canvas.style.height = ch + "px";
    }};
    
    let gridA = Array(viewSize).fill().map(() => Array(viewSize).fill(1.0));
    let gridB = Array(viewSize).fill().map(() => Array(viewSize).fill(0.0));
    let nextA = Array(viewSize).fill().map(() => Array(viewSize).fill(1.0));
    let nextB = Array(viewSize).fill().map(() => Array(viewSize).fill(0.0));
    
    const dA = 1.0, dB = 0.5, feed = 0.0545, kill = 0.062;
    
    function seedTuring() {{
        for (let x = 0; x < viewSize; x++) {{
            for (let y = 0; y < viewSize; y++) {{
                gridA[x][y] = 1.0;
                gridB[x][y] = Math.random() * 0.05;
            }}
        }}
        for(let k=0; k<30; k++) {{
            let rx = Math.floor(Math.random() * (viewSize - 40)) + 20;
            let ry = Math.floor(Math.random() * (viewSize - 40)) + 20;
            for(let i=-6; i<=6; i++) {{
                for(let j=-6; j<=6; j++) {{
                    gridA[rx+i][ry+j] = 0.5;
                    gridB[rx+i][ry+j] = 0.25 + Math.random() * 0.4;
                }}
            }}
        }}
    }}
    
    function updateTuring() {{
        for (let step = 0; step < 4; step++) {{
            for (let x = 0; x < viewSize; x++) {{
                for (let y = 0; y < viewSize; y++) {{
                    let xm1 = (x - 1 + viewSize) % viewSize;
                    let xp1 = (x + 1) % viewSize;
                    let ym1 = (y - 1 + viewSize) % viewSize;
                    let yp1 = (y + 1) % viewSize;

                    let a = gridA[x][y];
                    let b = gridB[x][y];

                    let lapA = (gridA[xm1][y] + gridA[xp1][y] + gridA[x][ym1] + gridA[x][yp1]) * 0.25 - a;
                    let lapB = (gridB[xm1][y] + gridB[xp1][y] + gridB[x][ym1] + gridB[x][yp1]) * 0.25 - b;

                    nextA[x][y] = a + (dA * lapA) - (a * b * b) + (feed * (1.0 - a));
                    nextB[x][y] = b + (dB * lapB) + (a * b * b) - ((kill + feed) * b);
                    
                    if(nextA[x][y] < 0) nextA[x][y] = 0; if(nextA[x][y] > 1) nextA[name="nextA[x][y]"] = 1;
                    if(nextB[x][y] < 0) nextB[x][y] = 0; if(nextB[x][y] > 1) nextB[x][y] = 1;
                }}
            }}
            let temp = gridA; gridA = nextA; nextA = temp;
            temp = gridB; gridB = nextB; nextB = temp;
        }}
    }}
    
    function drawTuring() {{
        let imgData = offCtx.createImageData(viewSize, viewSize);
        let data = imgData.data;
        
        for (let x = 0; x < viewSize; x++) {{
            for (let y = 0; y < viewSize; y++) {{
                let idx = (x + y * viewSize) * 4;
                let val = gridA[x][y] - gridB[x][y];
                let c = Math.floor(val * 255);
                if (c < 0) c = 0; if (c > 255) c = 255;
                
                data[idx + 0] = Math.floor((255 - c) * 0.05);                  
                data[idx + 1] = Math.floor((255 - c) * 0.95);                  
                data[idx + 2] = Math.floor((255 - c) * 0.85) + Math.floor(c * 0.1); 
                data[idx + 3] = 255;                                          
            }}
        }}
        offCtx.putImageData(imgData, 0, 0);
        
        ctx.clearRect(0, 0, cw, ch);
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(offscreenCanvas, 0, 0, viewSize, viewSize, 0, 0, cw, ch);
    }}

    draw();
</script>
</body>
</html>
"""

components.html(fusion_html, height=800, scrolling=False)
