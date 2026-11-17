/**
 * CHECKOUT & INTENT LOGIC
 * Handles Stripe session creation and 'Painted Door' intent capture.
 */
async function handleStripeCheckout(productId, email, variant, btn) {
    // 1. Variant Detection Fallback
    if (!variant) {
        const cookie = document.cookie.split('; ').find(row => row.startsWith('tsd_seen='));
        if (cookie) {
            const seen = cookie.split('=')[1].split(',');
            variant = seen[seen.length - 1]; // Use the most recent variant seen
        }
    }

    // 1.5 Capture Source / UTM
    const urlParams = new URLSearchParams(window.location.search);
    const source = urlParams.get('utm_source') || urlParams.get('source') || 'organic';

    const isCLS = window.location.hostname.includes('christopherlynnsystems') || (productId && productId.startsWith('STEADY_HAND'));

    // 2. TSD: Stripe Payment Link (site-config → stripe-payment-links.js)
    if (!isCLS && productId && !productId.startsWith('STEADY_HAND')) {
        const links = window.TSD_STRIPE_PAYMENT_LINKS || {};
        const paymentLink = links[productId];

        if (paymentLink) {
            const checkoutUrl = new URL(paymentLink);
            const refId = `VAR_${variant ? variant.toUpperCase() : 'NONE'}_SRC_${source.toUpperCase()}`;
            checkoutUrl.searchParams.set('utm_source', source);
            if (variant) checkoutUrl.searchParams.set('utm_content', variant);
            if (email) checkoutUrl.searchParams.set('prefilled_email', email);
            checkoutUrl.searchParams.set('client_reference_id', refId);
            window.location.href = checkoutUrl.toString();
            return;
        }

        console.warn('No Stripe Payment Link for product:', productId);
    }

    const originalText = btn ? btn.innerHTML : '';
    if (btn) {
        btn.innerHTML = "Opening Stripe...";
        btn.disabled = true;
    }

    try {
        const body = { productId, source };
        if (email) body.email = email;
        if (variant) body.variant = variant;

        const response = await fetch('/api/create-checkout-session', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });
        const data = await response.json();
        if (data.url) {
            window.location.href = data.url;
        } else {
            throw new Error(data.error || 'Failed to create Stripe checkout session');
        }
    } catch (err) {
        console.error('Checkout Error:', err);
        alert(err.message || 'Checkout initialization failed. Please try again.');
        if (btn) {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
    }
}

function showStewardshipInviteModal(variant) {
    const modalHtml = `
        <div id="stewardshipInviteModal" class="modal-overlay active" style="z-index: 10000; background: rgba(0,0,0,0.9); backdrop-filter: blur(15px); position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;">
            <div class="modal-content" style="max-width: 550px; text-align: center; border: 1px solid var(--primary-color); background: #1a1a1a; padding: 4rem 3rem; border-radius: 2rem; position: relative; box-shadow: 0 0 50px var(--primary-glow);">
                <span class="modal-close" onclick="this.closest('.modal-overlay').remove()" style="position: absolute; top: 1.5rem; right: 1.5rem; cursor: pointer; font-size: 2rem; color: #fff; opacity: 0.5;">&times;</span>
                
                <span style="color: var(--primary-color); text-transform: uppercase; letter-spacing: 3px; font-size: 0.8rem; font-weight: 800; display: block; margin-bottom: 1rem;">Invitation Only</span>
                <h2 style="font-size: 2.5rem; color: #fff; margin-bottom: 1.5rem; line-height: 1.1;">Secure Your <br>Architecture.</h2>
                
                <p style="color: var(--text-color-muted); font-size: 1.1rem; line-height: 1.6; margin-bottom: 2.5rem;">
                    You caught us in the final synchronization. The **Fatherhood Operating System** is moving from Private Beta to Public Deployment. 
                    <br><br>
                    Drop your email below to secure the **$149 Early-Adopter rate** (50% off launch price) and get the Zero Residue checklist immediately.
                </p>
                
                <form id="inviteForm" onsubmit="handleInviteSubmit(event, '${variant}')" style="display: flex; flex-direction: column; gap: 1rem;">
                    <input type="email" id="inviteEmail" placeholder="Best Email Address" required style="width: 100%; padding: 1.25rem; border-radius: 1rem; border: 1px solid var(--border-color); background: rgba(255,255,255,0.05); color: #fff; font-size: 1.1rem;">
                    <button type="submit" id="inviteSubmit" class="cta-button cta-button-primary" style="width: 100%; padding: 1.25rem; background: var(--primary-color); color: white; border: none; border-radius: 1rem; font-weight: 800; font-size: 1.2rem; cursor: pointer; transition: all 0.3s ease;">
                        Reserve My System &rarr;
                    </button>
                </form>
                
                <div id="inviteStatus" style="display: none; margin-top: 2rem; padding: 1.5rem; border-radius: 1rem; font-weight: 700;"></div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHtml);
}

async function handleInviteSubmit(e, variant) {
    e.preventDefault();
    const email = document.getElementById('inviteEmail').value;
    const submitBtn = document.getElementById('inviteSubmit');
    const status = document.getElementById('inviteStatus');
    
    submitBtn.disabled = true;
    submitBtn.innerHTML = "Syncing...";

    try {
        const response = await fetch('/api/capture-audit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                email: email, 
                source: `BUY_INTENT_${variant.toUpperCase()}`,
                variant: variant
            })
        });

        if (response.ok) {
            status.innerHTML = "✅ Access Reserved. Check your inbox for the Zero Residue Protocol.";
            status.style.display = 'block';
            status.style.background = 'rgba(74, 222, 128, 0.1)';
            status.style.color = '#4ade80';
            e.target.style.display = 'none';
            
            setTimeout(() => {
                const modal = document.getElementById('stewardshipInviteModal');
                if (modal) modal.remove();
            }, 4000);
        } else {
            throw new Error('Sync failed');
        }
    } catch (err) {
        status.innerHTML = "❌ Synchronization failed. Please try again.";
        status.style.display = 'block';
        status.style.background = 'rgba(239, 68, 68, 0.1)';
        status.style.color = '#ef4444';
        submitBtn.disabled = false;
        submitBtn.innerHTML = "Reserve My System &rarr;";
    }
}

function showMarginResetInviteModal(variant) {
    const modalHtml = `
        <div id="marginResetInviteModal" class="modal-overlay active" style="z-index: 10000; background: rgba(0,0,0,0.95); backdrop-filter: blur(20px); position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;">
            <div class="modal-content" style="max-width: 550px; text-align: center; border: 1px solid #f59e0b; background: #0a0a0a; padding: 4rem 3rem; border-radius: 1.5rem; position: relative; box-shadow: 0 0 50px rgba(245, 158, 11, 0.2);">
                <span class="modal-close" onclick="this.closest('.modal-overlay').remove()" style="position: absolute; top: 1.5rem; right: 1.5rem; cursor: pointer; font-size: 2rem; color: #fff; opacity: 0.5;">&times;</span>
                
                <span style="color: #f59e0b; text-transform: uppercase; letter-spacing: 3px; font-size: 0.75rem; font-weight: 800; display: block; margin-bottom: 1rem;">Beta Deployment</span>
                <h2 style="font-size: 2.5rem; color: #fff; margin-bottom: 1.5rem; line-height: 1.1; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 900;">The 25 Minutes <br>That Matter.</h2>
                
                <p style="color: #94a3b8; font-size: 1.1rem; line-height: 1.6; margin-bottom: 2.5rem; font-family: 'Montserrat', sans-serif;">
                    The **MarginReset Kit** is currently in restricted deployment. We are synchronizing the final protocols for the $97 Gear launch.
                    <br><br>
                    Secure your spot in the **Beta Wave** tonight. You'll get the 'Shutdown Protocol' immediately and a 40% discount on the full kit at launch.
                </p>
                
                <form id="mrInviteForm" onsubmit="handleInviteSubmit(event, '${variant}')" style="display: flex; flex-direction: column; gap: 1rem;">
                    <input type="email" id="inviteEmail" placeholder="Work Email Preferred" required style="width: 100%; padding: 1.25rem; border-radius: 0.75rem; border: 1px solid rgba(245, 158, 11, 0.3); background: rgba(245, 158, 11, 0.05); color: #fff; font-size: 1.1rem;">
                    <button type="submit" id="inviteSubmit" class="cta-button" style="width: 100%; padding: 1.25rem; background: #f59e0b; color: #0a0a0a; border: none; border-radius: 0.75rem; font-weight: 800; font-size: 1.2rem; cursor: pointer; transition: all 0.3s ease;">
                        Reserve My Kit &rarr;
                    </button>
                </form>
                
                <div id="inviteStatus" style="display: none; margin-top: 2rem; padding: 1.5rem; border-radius: 0.75rem; font-weight: 700;"></div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHtml);
}
