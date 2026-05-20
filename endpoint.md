# Vectra Email Automator: Frontend to Backend API Map

This document outlines all the locations in the frontend codebase that are currently relying on Mock Data, Local Storage, or local React State, and lists the required backend API endpoints that need to be developed to fully integrate the application.

---

## 1. Authentication
**File Locations:** 
- `frontend/src/pages/auth/LoginPage.jsx`
- `frontend/src/pages/auth/SignupPage.jsx`

**Required Endpoints:**
- `POST /api/auth/login` - Authenticate user and return JWT/session token.
- `POST /api/auth/register` - Create a new user account.
- `GET /api/auth/me` - Fetch the current authenticated user's profile data.

---

## 2. Organisation & Workspace Management
**File Location:** 
- `frontend/src/context/OrganisationContext.jsx`
*(Currently persisting to `localStorage` under `vectra_organisations`)*

**Required Endpoints:**
- `GET /api/organisations` - Fetch all organisations for the current user.
- `POST /api/organisations` - Create a new organisation workspace.
- `PUT /api/organisations/:id` - Update organisation details.
- `DELETE /api/organisations/:id` - Delete an organisation.
- `POST /api/organisations/:id/groups` - Create a new audience group within an organisation.
- `DELETE /api/organisations/:id/groups/:groupId` - Delete an audience group.
- `PUT /api/organisations/:id/groups/:groupId/recipients` - Bulk update/upload recipients (used for CSV imports).
- `PUT /api/organisations/:id/groups/:groupId/name` - Rename an existing group.
- `POST /api/organisations/:id/activities` - Log an activity event (e.g., imports, setting changes) to the organisation's feed.

---

## 3. Email Scheduler & Campaigns
**File Location:** 
- `frontend/src/context/SchedulerContext.jsx`
*(Currently persisting to `localStorage` under `vectra_schedules` with `MOCK_SCHEDULES` fallback)*

**Required Endpoints:**
- `GET /api/schedules` - Fetch all email schedules.
- `POST /api/schedules` - Create a new email schedule/campaign.
- `PUT /api/schedules/:id` - Update schedule configuration.
- `DELETE /api/schedules/:id` - Delete a schedule.
- `POST /api/schedules/:id/toggle` - Toggle schedule state between `active` and `paused`.
- `GET /api/templates` - Fetch available email templates (`MOCK_TEMPLATES`).

---

## 4. Community Discussion Module
**File Location:** 
- `frontend/src/context/CommunityContext.jsx`
*(Currently managed via local React state array `threads` and `MOCK_THREADS`)*

**Required Endpoints:**
- `GET /api/community/threads` - Fetch paginated community threads.
- `POST /api/community/threads` - Create a new discussion thread.
- `POST /api/community/threads/:id/replies` - Add a reply to a specific thread.
- `POST /api/community/threads/:id/helpful` - Toggle the "helpful/like" status on a thread for the current user.
- `POST /api/community/threads/:id/bookmark` - Toggle bookmark status on a thread.
- `POST /api/community/threads/:id/solved` - Mark a thread as solved (usually restricted to author/admin).
- `POST /api/community/replies/:replyId/helpful` - Toggle "helpful" status on a specific reply.

---

## 5. Guides & Knowledge Base
**File Locations:** 
- `frontend/src/lib/mockGuidesData.js`
- `frontend/src/pages/GuidesPage.jsx`
*(Currently hardcoded JSON data mimicking an API response)*

**Required Endpoints:**
- `GET /api/guides` - Fetch guides (can optionally accept query params like `?type=official` or `?type=community`).
- `GET /api/guides/featured` - Fetch the hero featured guide.
- `GET /api/guides/tips` - Fetch the quick productivity tips array.
- `POST /api/guides/:id/bookmark` - Save a guide to the user's bookmarks (Currently managed by local state `bookmarkedIds` in `GuidesPage.jsx`).
