import streamlit as st
import tempfile
from functions.pipeline import process_video

st.set_page_config(
    page_title="Viral Reel Machine",
    page_icon="💾",
    layout="wide"
)

# =========================
# WINDOWS 98 RETRO CSS
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'VT323', monospace !important;
    font-size: 20px;
}

/* ── Bliss wallpaper background ── */
/* Save the Bliss image as assets/bliss.jpg in your project folder */
.stApp {
    background-image: url("https://i.pinimg.com/1200x/25/aa/1a/25aa1a16b78d63f639b04b8427d4f2d6.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, header, footer { visibility: hidden; }
.block-container {
    padding-top: 10px !important;
    padding-bottom: 60px !important;
    max-width: 900px !important;
}

/* ── Win98 window chrome ── */
.win98-window {
    background: #c0c0c0;
    border-top:    2px solid #ffffff;
    border-left:   2px solid #ffffff;
    border-right:  2px solid #808080;
    border-bottom: 2px solid #808080;
    box-shadow: 1px 1px 0 #000, 2px 2px 0 #000;
    margin-bottom: 12px;
}

.win98-titlebar {
    background: linear-gradient(to right, #000080, #1084d0);
    color: #ffffff;
    font-family: 'VT323', monospace;
    font-size: 22px;
    padding: 4px 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    user-select: none;
}

.win98-titlebar-buttons {
    display: flex;
    gap: 2px;
}

.win98-titlebar-btn {
    background: #c0c0c0;
    border-top:    2px solid #ffffff;
    border-left:   2px solid #ffffff;
    border-right:  2px solid #808080;
    border-bottom: 2px solid #808080;
    width: 18px;
    height: 18px;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #000;
    font-weight: bold;
    cursor: default;
}

.win98-content {
    padding: 14px 16px;
    font-family: 'VT323', monospace;
    font-size: 20px;
    color: #000;
}

/* ── Inset panel (sunken box) ── */
.win98-inset {
    background: #ffffff;
    border-top:    2px solid #808080;
    border-left:   2px solid #808080;
    border-right:  2px solid #ffffff;
    border-bottom: 2px solid #ffffff;
    padding: 10px 14px;
    margin-bottom: 10px;
    font-family: 'VT323', monospace;
    font-size: 20px;
    color: #000;
}

/* ── Reel result box ── */
.reel-box {
    background: #ffffff;
    border-top:    2px solid #808080;
    border-left:   2px solid #808080;
    border-right:  2px solid #ffffff;
    border-bottom: 2px solid #ffffff;
    padding: 12px 16px;
    margin-top: 10px;
    font-family: 'VT323', monospace;
    color: #000;
}

.reel-box h2 {
    font-size: 24px;
    margin: 0 0 6px 0;
}

.reel-box p {
    margin: 0;
    font-size: 18px;
    color: #444;
}

/* ── Streamlit buttons → Win98 look ── */
.stButton > button {
    background: #c0c0c0 !important;
    color: #000 !important;
    font-family: 'VT323', monospace !important;
    font-size: 22px !important;
    border-top:    2px solid #ffffff !important;
    border-left:   2px solid #ffffff !important;
    border-right:  2px solid #808080 !important;
    border-bottom: 2px solid #808080 !important;
    border-radius: 0 !important;
    padding: 6px 20px !important;
    height: 44px !important;
    width: 100% !important;
    box-shadow: none !important;
}

.stButton > button:active {
    border-top:    2px solid #808080 !important;
    border-left:   2px solid #808080 !important;
    border-right:  2px solid #ffffff !important;
    border-bottom: 2px solid #ffffff !important;
}

.stButton > button:hover {
    background: #d4d0c8 !important;
}

/* ── File uploader → Win98 inset ── */
[data-testid="stFileUploader"] {
    background: #ffffff !important;
    border-top:    2px solid #808080 !important;
    border-left:   2px solid #808080 !important;
    border-right:  2px solid #ffffff !important;
    border-bottom: 2px solid #ffffff !important;
    padding: 16px !important;
    border-radius: 0 !important;
}

[data-testid="stFileUploader"] section {
    background: transparent !important;
}

[data-testid="stFileUploader"] label {
    font-family: 'VT323', monospace !important;
    font-size: 20px !important;
}

/* ── Success / spinner messages ── */
.stAlert, [data-testid="stAlert"] {
    font-family: 'VT323', monospace !important;
    font-size: 20px !important;
    border-radius: 0 !important;
}

/* ── Desktop icon area ── */
.desktop-icons {
    display: flex;
    gap: 24px;
    padding: 12px 8px 8px 8px;
}

.desktop-icon {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 80px;
    color: #ffffff;
    font-family: 'VT323', monospace;
    font-size: 16px;
    text-shadow: 1px 1px 2px #000;
    cursor: default;
}

.desktop-icon img {
    width: 64px;
    height: 64px;
    image-rendering: pixelated;
    margin-bottom: 4px;
}

/* ── Win98 taskbar ── */
.win98-taskbar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 36px;
    background: #c0c0c0;
    border-top: 2px solid #ffffff;
    display: flex;
    align-items: center;
    z-index: 99999;
    padding: 0 4px;
    gap: 6px;
}

.win98-start-btn {
    background: #c0c0c0;
    border-top:    2px solid #ffffff;
    border-left:   2px solid #ffffff;
    border-right:  2px solid #808080;
    border-bottom: 2px solid #808080;
    padding: 2px 10px;
    font-family: 'VT323', monospace;
    font-size: 18px;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 5px;
    cursor: default;
}

.win98-taskbar-clock {
    margin-left: auto;
    border-top:    2px solid #808080;
    border-left:   2px solid #808080;
    border-right:  2px solid #ffffff;
    border-bottom: 2px solid #ffffff;
    padding: 2px 10px;
    font-family: 'VT323', monospace;
    font-size: 17px;
    background: #c0c0c0;
}

.win98-taskbar-task {
    background: #c0c0c0;
    border-top:    2px solid #808080;
    border-left:   2px solid #808080;
    border-right:  2px solid #ffffff;
    border-bottom: 2px solid #ffffff;
    padding: 2px 12px;
    font-family: 'VT323', monospace;
    font-size: 17px;
    display: flex;
    align-items: center;
    gap: 4px;
}

/* ── Spinner ── */
[data-testid="stSpinner"] {
    font-family: 'VT323', monospace !important;
    font-size: 20px !important;
}

/* Custom cursor */
html { cursor: url("https://cur.cursors-4u.net/cursors/cur-9/cur817.cur"), auto; }

</style>
""", unsafe_allow_html=True)

# =========================
# DESKTOP ICONS
# =========================

st.markdown("""
<div class="desktop-icons">
    <div class="desktop-icon">
        <img src="https://win98icons.alexmeub.com/icons/png/computer_explorer-4.png" />
        <span>My Computer</span>
    </div>
    <div class="desktop-icon">
        <img src="https://win98icons.alexmeub.com/icons/png/video_control_panel-0.png" />
        <span>Videos</span>
    </div>
    <div class="desktop-icon">
        <img src="https://win98icons.alexmeub.com/icons/png/recycle_bin_empty-4.png" />
        <span>Recycle Bin</span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# MAIN WINDOW
# =========================

st.markdown("""
<div class="win98-window">
    <div class="win98-titlebar">
        <span>💾 Viral Reel Machine v1.0 — [untitled]</span>
        <div class="win98-titlebar-buttons">
            <div class="win98-titlebar-btn">_</div>
            <div class="win98-titlebar-btn">□</div>
            <div class="win98-titlebar-btn">✕</div>
        </div>
    </div>
    <div class="win98-content">
""", unsafe_allow_html=True)

# ── File Explorer sub-window ──
st.markdown("""
<div class="win98-window">
    <div class="win98-titlebar">
        <span>📁 File Explorer</span>
        <div class="win98-titlebar-buttons">
            <div class="win98-titlebar-btn">_</div>
            <div class="win98-titlebar-btn">□</div>
            <div class="win98-titlebar-btn">✕</div>
        </div>
    </div>
    <div class="win98-content">
        <div class="win98-inset">
            Select a video file to analyze (.mp4 .mov .avi .mkv)
        </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose Video",
    type=["mp4", "mov", "avi", "mkv"]
)

st.markdown("</div></div>", unsafe_allow_html=True)

# ── Process button & results ──
if uploaded_file:

    st.markdown(f"""
    <div class="win98-inset">
        ✅ &nbsp; Loaded: <strong>{uploaded_file.name}</strong>
    </div>
    """, unsafe_allow_html=True)

    if st.button("▶  Process Video"):

        processing_window = st.empty()

        processing_window.markdown("""
        <div class="win98-window">
            <div class="win98-titlebar">
                <span>⚙ Processing...</span>
            </div>
            <div class="win98-content">
                <div class="win98-inset">
                    ⏳ &nbsp; Analyzing video segments... please wait.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.spinner("Analyzing video..."):

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            ) as tmp:
                tmp.write(uploaded_file.read())
                temp_path = tmp.name

            result = process_video(temp_path)

        processing_window.empty()

        st.markdown("""
        <div class="win98-inset">✅ &nbsp; Processing complete!</div>
        """, unsafe_allow_html=True)

        # ── Results sub-window ──
        st.markdown("""
        <div class="win98-window">
            <div class="win98-titlebar">
                <span>🎬 Generated Reels</span>
                <div class="win98-titlebar-buttons">
                    <div class="win98-titlebar-btn">_</div>
                    <div class="win98-titlebar-btn">□</div>
                    <div class="win98-titlebar-btn">✕</div>
                </div>
            </div>
            <div class="win98-content">
        """, unsafe_allow_html=True)

        reels = result["reels"]

        for reel in reels:
            st.markdown(
                f"""
                <div class="reel-box">
                    <h2>🎞 {reel['hook_title']}</h2>
                    <p>▶ Start: {reel['start']}s &nbsp;&nbsp; ⏹ End: {reel['end']}s</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            try:
                st.video(reel["path"])
            except:
                st.warning(f"Could not load video: {reel['path']}")

        st.markdown("</div></div>", unsafe_allow_html=True)

# close main window
st.markdown("</div></div>", unsafe_allow_html=True)

# =========================
# WIN98 TASKBAR
# =========================

st.markdown("""
<div class="win98-taskbar">
    <div class="win98-start-btn">
        <img src="https://win98icons.alexmeub.com/icons/png/windows_nt_small-0.png"
             style="width:18px;height:18px;image-rendering:pixelated;" />
        Start
    </div>
    <div class="win98-taskbar-task">💾 Viral Reel Machine v1.0</div>
    <div class="win98-taskbar-clock" id="taskbar-clock">00:00</div>
</div>

<script>
(function tick(){
    const el = document.getElementById('taskbar-clock');
    if(el){
        const n = new Date();
        el.textContent = n.toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});
    }
    setTimeout(tick, 5000);
})();
</script>
""", unsafe_allow_html=True)