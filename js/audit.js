/**
 * The Residue Audit LOGIC
 * Handles multi-step form navigation and score calculation.
 */
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('auditForm');
    if (!form) return;

    const steps = document.querySelectorAll('.audit-step');
    const progress = document.getElementById('auditProgress');
    const progressPercent = document.getElementById('progressPercent');
    const stepLabel = document.getElementById('stepLabel');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');
    const results = document.getElementById('auditResults');
    
    let currentStep = 1;
    const totalSteps = steps.length;

    const updateUI = () => {
        steps.forEach(s => s.classList.remove('active'));
        const activeStep = document.querySelector(`.audit-step[data-step="${currentStep}"]`);
        if (activeStep) activeStep.classList.add('active');
        
        const percent = ((currentStep - 1) / totalSteps) * 100;
        if (progress) progress.style.width = `${percent}%`;
        if (progressPercent) progressPercent.textContent = `${Math.round(percent)}%`;
        
        if (activeStep && stepLabel) {
            const phase = activeStep.dataset.phase;
            stepLabel.textContent = `Phase ${currentStep <= 5 ? '1' : '2'}: ${phase} Integrity`;
        }
        
        if (prevBtn) prevBtn.style.display = currentStep === 1 ? 'none' : 'block';
        
        if (currentStep === totalSteps) {
            if (nextBtn) nextBtn.style.display = 'none';
            if (submitBtn) submitBtn.style.display = 'block';
        } else {
            if (nextBtn) nextBtn.style.display = 'block';
            if (submitBtn) submitBtn.style.display = 'none';
        }
    };

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const currentInputs = document.querySelectorAll(`.audit-step[data-step="${currentStep}"] input`);
            const answered = Array.from(currentInputs).some(input => input.checked);
            
            if (!answered) {
                alert('Please select an architecture baseline to continue.');
                return;
            }
            
            if (currentStep < totalSteps) {
                currentStep++;
                updateUI();
            }
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            if (currentStep > 1) {
                currentStep--;
                updateUI();
            }
        });
    }

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const data = new FormData(form);
        let workScore = 0;
        let homeScore = 0;
        
        for (let [key, value] of data.entries()) {
            if (key.startsWith('w')) workScore += parseInt(value);
            if (key.startsWith('h')) homeScore += parseInt(value);
        }
        
        form.style.display = 'none';
        const progressContainer = document.querySelector('.audit-progress-container');
        if (progressContainer) progressContainer.style.display = 'none';
        if (results) results.style.display = 'block';
        
        const workScoreEl = document.getElementById('workScore');
        const homeScoreEl = document.getElementById('homeScore');
        if (workScoreEl) workScoreEl.textContent = `${workScore}/15`;
        if (homeScoreEl) homeScoreEl.textContent = `${homeScore}/15`;
        
        const title = document.getElementById('diagnosisTitle');
        const desc = document.getElementById('diagnosisDesc');
        const cta = document.getElementById('unifiedCTA');
        
        const gateTitle = document.getElementById('gateDiagnosisTitle');
        const emailGate = document.getElementById('emailGate');
        const gateForm = document.getElementById('emailGateForm');
        const diagnosisCard = document.getElementById('diagnosisCard');
        
        let diagnosisName = "The Total Steward";
        let segmentTag = "audit_steward";
        
        if (title && desc && cta) {
            // Set a cookie for attribution fallback
            document.cookie = "tsd_seen=AUDIT; Max-Age=86400; Path=/; Domain=.thesystemsdad.com; SameSite=Lax";

            if (workScore < 5 && homeScore < 5) {
                diagnosisName = "The Systemic Collapse";
                segmentTag = "audit_collapse";
                desc.textContent = "Your workday is consuming your family life. When daytime meetings and message-passing push deep work into your evenings, your home life pays the bill. You don't need another generic template; you need to install hard operational firewalls to shut work down at 5:15 PM.";
                cta.innerHTML = `<a href="https://calendar.app.google/8Scpw791cGfqJ4VD9" class="btn btn-primary" style="background-color: #d9534f; border-color: #d43f3a;" target="_blank">Book a 20-Min Margin Diagnostic Call →</a>`;
            } else if (workScore < 9 && homeScore < 9) {
                diagnosisName = "The Overwhelmed Operator";
                segmentTag = "audit_overwhelmed";
                desc.textContent = "You are acting as an expensive switchboard during the day, which leaves you exhausted and reactive at home. When everything depends on your personal stamina to hold together, burnout is inevitable. You need clear systems to eliminate status chasing and protect your evenings.";
                cta.innerHTML = `<a href="https://calendar.app.google/8Scpw791cGfqJ4VD9" class="btn btn-primary" target="_blank">Book a 20-Min Margin Diagnostic Call →</a>`;
            } else if (workScore >= 9 && homeScore < 9) {
                diagnosisName = "The Ghost Leader";
                segmentTag = "audit_ghost";
                desc.textContent = "You have operational leverage at work, but it stops at your front door. You close the laptop on time, but Slack residue and cognitive load keep your head in the office. You need an off-switch to be physically and mentally present with your family.";
                cta.innerHTML = `<a href="https://calendar.app.google/8Scpw791cGfqJ4VD9" class="btn btn-primary" target="_blank">Book a 20-Min Margin Diagnostic Call →</a>`;
            } else if (workScore < 9 && homeScore >= 9) {
                diagnosisName = "The Domestic Anchor";
                segmentTag = "audit_anchor";
                desc.textContent = "You are a present father, but your professional drag is a constant threat. Your manual work routines are stealing the margin you need to actually lead your family. You need to automate the professional floor to protect the domestic ceiling.";
                const isTSD = window.location.hostname.includes('thesystemsdad') || window.location.pathname.includes('_tsd') || !window.location.hostname.includes('christopherlynn');
                cta.innerHTML = isTSD 
                    ? `<a href="/win" class="btn btn-primary">Get the Self-Serve System ($97) →</a>`
                    : `<a href="/services" class="btn btn-primary">Explore Systems & Services →</a>`;
            } else {
                diagnosisName = "The Total Steward";
                segmentTag = "audit_steward";
                desc.textContent = "You are architecting your life in alignment. Systems handle the floor, and presence defines the ceiling. You are in the top 1% of operational leaders. Your next move is establishing the High-Authority Lab.";
                cta.innerHTML = `<a href="lab.html?v=audit&w=${workScore}&h=${homeScore}" class="btn btn-primary">Request Lab Access →</a>`;
            }
            
            title.textContent = diagnosisName;
            if (gateTitle) gateTitle.textContent = "You are " + diagnosisName + ".";
        }
        
        if (gateForm) {
            gateForm.addEventListener('submit', async (ev) => {
                ev.preventDefault();
                const btn = document.getElementById('gateSubmitBtn');
                if (btn) {
                    btn.textContent = "Unlocking...";
                    btn.disabled = true;
                }
                
                const firstName = document.getElementById('gateName').value;
                const email = document.getElementById('gateEmail').value;
                const beehiivKey = "pub_dfce7899-cead-4e58-a72f-3c903d331174";
                
                try {
                    await fetch('https://api.beehiiv.com/v2/publications/' + beehiivKey + '/subscriptions', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': 'Bearer ' + beehiivKey
                        },
                        body: JSON.stringify({
                            email: email,
                            utm_source: 'stewardship_audit',
                            utm_medium: 'website',
                            utm_campaign: segmentTag,
                            referring_site: 'thesystemsdad.com/total-stewardship-audit',
                            custom_fields: [
                                { name: 'first_name', value: firstName },
                                { name: 'audit_segment', value: segmentTag },
                                { name: 'work_score', value: workScore.toString() },
                                { name: 'home_score', value: homeScore.toString() }
                            ]
                        })
                    });
                } catch (err) {
                    console.error("Beehiiv subscribe failed", err);
                }
                
                if (emailGate) emailGate.style.display = 'none';
                if (diagnosisCard) diagnosisCard.style.display = 'block';
            });
        }
        
        if (results) window.scrollTo({ top: results.offsetTop - 100, behavior: 'smooth' });
    });
});
