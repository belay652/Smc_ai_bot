import streamlit as st
import os

# Page Config
st.set_page_config(page_title="SMC AI Bot Controller", page_icon="📲", layout="centered")

# 1. SECURE LOGIN SYSTEM
USERNAME = "admin"
PASSWORD = "smc123password"  # እዚህ ጋር የምትፈልገውን ምስጢራዊ ፓስወርድ ቀይር

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔐 SMC AI Bot - Mobile Login")
            st.caption("እባክህ ለመግባት የይለፍ ቃልህን አስገባ")
                
                     user_input = st.text_input("Username")
                     pass_input = st.text_input("Password", type="password")
                            
                                if st.button("LOG IN", type="primary"):
                                        if user_input == USERNAME and pass_input == PASSWORD:
                                                    st.session_state.logged_in = True
                                                                st.rerun()
                                                                        else:
                                                                                    st.error("❌ የተሳሳተ Username ወይም Password!")
                                                                                        st.stop()

                                                                                        # 2. MAIN DASHBOARD (AFTER LOGIN)
                                                                                        st.title("📱 SMC AI Trading Bot")
                                                                                        st.caption("24/7 Cloud Automated Trading System ($20 Account Flip)")

                                                                                        if st.sidebar.button("Log Out"):
                                                                                            st.session_state.logged_in = False
                                                                                                st.rerun()

                                                                                                # Account Stats
                                                                                                st.subheader("📊 Account Overview")
                                                                                                col1, col2, col3 = st.columns(3)
                                                                                                col1.metric("Balance", "$20.00")
                                                                                                col2.metric("Target", "$100.00")
                                                                                                col3.metric("Lot Size", "0.01")

                                                                                                st.markdown("---")

                                                                                                # Risk Rules for $20 Account
                                                                                                st.subheader("🛡️ Risk Management Rules")
                                                                                                st.write("• Strategy: Smart Money Concepts (OB + FVG)")
                                                                                                st.write("• Risk per trade: $2.00 (10%)")
                                                                                                st.write("• Daily Loss Limit: $5.00")

                                                                                                st.markdown("---")

                                                                                                # Bot Control Switch
                                                                                                st.subheader("⚙️ Bot Switch")
                                                                                                if "bot_active" not in st.session_state:
                                                                                                    st.session_state.bot_active = False

                                                                                                    col_start, col_stop = st.columns(2)
                                                                                                    with col_start:
                                                                                                        if st.button("🚀 START AI BOT", use_container_width=True, type="primary"):
                                                                                                                st.session_state.bot_active = True
                                                                                                                        st.success("🤖 AI Bot በክላውድ ላይ መስራት ጀምሯል!")

                                                                                                                        with col_stop:
                                                                                                                            if st.button("🛑 STOP AI BOT", use_container_width=True):
                                                                                                                                    st.session_state.bot_active = False
                                                                                                                                            st.warning("⚠️ AI Bot ቆሟል!")

                                                                                                                                            if st.session_state.bot_active:
                                                                                                                                                st.info("🟢 Status: AI BOT IS ACTIVE & MONITORING XAUUSD")
                                                                                                                                                else:
                                                                                                                                                    st.error("🔴 Status: BOT IS STOPPED")