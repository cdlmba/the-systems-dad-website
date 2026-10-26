---
name: Google Auth + Whop Payment Gating
description: Reusable technical pattern for integrating Google Identity with Whop.com membership gating in a secure, SDK-free architecture.
---

# Google Auth + Whop Payment Gating Protocol (SDK-Free)

This skill provides a standardized workflow for securing a web application using Google OAuth for identity and Whop for payment verification.

## 🏢 Architecture Overview

1.  **Identity Control**: `@react-oauth/google` provides a verified email via JWT.
2.  **Access Control**: A Vercel Serverless Function (`api/verify-access.ts`) proxies the request to the Whop V2 API.
3.  **Performance Layer**: Vercel KV caches verified memberships to avoid constant API hits.
4.  **Admin Bypass**: A whitelist of emails that grant immediate access (VITE_ADMIN_EMAILS).

---

## 🛠 Required Environment Variables

Add these to your project's `.env` and Production Environment:

```env
# Google
VITE_GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com

# Whop
WHOP_API_KEY=apik_xxx (Company Key)
VITE_WHOP_CLIENT_ID=app_xxx
VITE_WHOP_PRODUCT_ID=prod_xxx

# Admin Whitelist
VITE_ADMIN_EMAILS=your@email.com,admin@example.com

# Vercel KV
KV_REST_API_URL=xxx
KV_REST_API_TOKEN=xxx
```

---

## 📦 Core Logic Snippets

### 1. Verification Backend (SDK-Free V2 API)
Use direct `fetch` instead of the `@whop-sdk` to ensure stability on Vercel Edge/Serverless and easier versioning.

```typescript
const isWhitelisted = ADMIN_EMAILS.includes(email.toLowerCase());
if (isWhitelisted) return res.json({ success: true, method: 'admin' });

// Verify by membershipId
const response = await fetch(`https://api.whop.com/api/v2/memberships/${membershipId}`, {
    headers: { 'Authorization': `Bearer ${WHOP_API_KEY}` }
});

const membership = await response.json();
const hasAccess = membership.product_id === PRODUCT_ID && membership.status === 'active';
```

### 2. Frontend Decoupling
The frontend should decode the Google JWT and pass only the `email` to the backend.

```typescript
const handleGoogleSuccess = async (credentialResponse) => {
    const decoded = jwt_decode(credentialResponse.credential);
    const result = await verifyAccess(decoded.email);
    if (result.success) unlockApp();
};
```

---

## 🔒 Security Best Practices

1.  **Origin Protection**: Always list `http://localhost:5173` and your production domain in the **Google Cloud Console** under "Authorized JavaScript Origins".
2.  **Secret Isolation**: Never prefix `WHOP_API_KEY` with `VITE_`. It must never reach the browser.
3.  **Graceful KV Failure**: Wrap KV calls in `try/catch` and check for config variables to ensure the app works in local environments without a Redis connection.
4.  **Whop Iframe Support**: If embedding in Whop, always check for the `x-whop-user-token` header passed by the provider.

---

## 🔄 Deployment Checklist

- [ ] Add `CNAME` record to DNS provider for custom domain.
- [ ] Add custom domain to Google OAuth origins.
- [ ] Add custom domain to Whop redirect URIs.
- [ ] Sync Webhook in Whop Dashboard (`/api/whop-webhook`).
