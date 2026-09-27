# Module 4 Project — Part 2: Study Tracker API Design

**Della McMillan:**
**September 2026:**

---

## The App: Study Tracker
Study Tracker is a REST API that helps students record and monitor their study activity. Students can log study sessions for courses, create weekly study goals, and view progress toward those goals.

## Section 1 — Resources

| Resource      | Key Attributes |
|----------     |---------------|
Students         id, name, email
Courses          id, name, course_code
Study Sessions   id, student_id, course_id, 
                 duration_minutes, notes, studied_at
Goals            id, student_id, course_id, 
                 target_hours, week_start

## Section 2 — Relationships
Students ↔ Courses
many-to-many

Student → Study Sessions
one-to-many

Course → Study Sessions
one-to-many

Student → Goals
one-to-many

Course → Goals
one-to-many

## Section 3 — Endpoints

| Method    URI                 | Description   | Auth Required?   |
|-------    |-----              |-------------  |
POST        /study_sessions     Create a study   Yes
                                session 
GET         /study_sessions     Get the          Yes
                                logged-in 
                                student's study 
                                sessions 
GET       /study_sessions/{id}  Get one          Yes
                                study session
PUT       /study_sessions/{id}  Update a study   Yes
                                session
DELETE    /study_sessions/{id}  Delete           Yes
                                a study session
GET       /study_sessions?      Filter study
          course_id={id}        sessions by      Yes
                                course
GET       /study_sessions?      Filter sessions  Yes
          start_date={date}     by date rang
          &end_date={date}
GET       /students             List students    Yes
GET       /students/{id}        Get a student's  Yes
                                profile
POST     /students              Create a         No
                                student account
GET     /students/{id}/progress View a student's Yes
                                study progress
GET     /courses                List available   No
                                courses
GET     /courses/{id}           Get information  No
                                about one course
POST    /courses                Create a course  Yes
GET     /students/{id}/goals    Get a student's  Yes
                                goals
POST    /students/{id}/goals    Create a study  Yes
                                goal
PUT     /goals/{id}             Update a study  Yes
                                goal
DELETE  /goals/{id}             Delete a study  Yes
                                goal

## Section 4 — Request/Response Schemas
### POST /study_sessions — Create a new session
**Request body:**
{
    "course_id": 5,
    "duration_minutes": 90,
    "notes": "Reviewed REST API authentication and status codes.",
    "studied_at": "2026-09-24T14:00:00"
}

Data types:
course_id: integer
duration_minutes: integer
notes: string
studied_at: datetime

**Success response (201)created:**
{
    "id": 101,
    "student_id": 12,
    "course_id": 5,
    "duration_minutes": 90,
    "notes": "Reviewed REST API authentication and status codes.",
    "studied_at": "2026-09-24T14:00:00"
}
POST /students/{id}/goals — Create a Study Goal

Request body:

{
    "course_id": 5,
    "target_hours": 8,
    "week_start": "2026-09-21T00:00:00"
}

Data types:

course_id: integer
target_hours: integer
week_start: datetime

Success response — 201 Created:

{
    "id": 42,
    "student_id": 12,
    "course_id": 5,
    "target_hours": 8,
    "week_start": "2026-09-21T00:00:00"
}
GET /study_sessions/{id}

Response — 200 OK:

{
    "id": 101,
    "student_id": 12,
    "course_id": 5,
    "duration_minutes": 90,
    "notes": "Reviewed REST API authentication and status codes.",
    "studied_at": "2026-09-24T14:00:00"
}
Response data types:

id: integer
student_id: integer
course_id: integer
duration_minutes: integer
notes: string
studied_at: datetime

### GET /students/{id}/progress
**Response (200):**
{
    "student_id": 12,
    "course_id": 5,
    "course_name": "REST API Fundamentals",
    "target_hours": 8,
    "completed_hours": 6,
    "goal_met": false
}
Response data types:

student_id: integer
course_id: integer
course_name: string
target_hours: integer
completed_hours: integer
goal_met: boolean
---

## Section 5 — Authentication

| Endpoint         | Auth Required   | Notes |
|----------        |--------------   |-------|
GET /courses            No          Public course information
GET /courses/{id}       No          Public course information
POST /students          No          Used to create an account
POST /study_sessions    Yes         Logged-in student creates
                                    their own session
GET /study_sessions     Yes         Student sees their own 
                                    sessions
GET                     Yes         Student can access their own 
/students/{id}/progress             progress
DELETE                  Yes         Only the session owner 
/study_sessions/{id}                can delete it

POST                    Yes       Student creates 
/students/{id}/goals              their own goal

DELETE /goals/{id}        Yes       Only the goal 
                                    owner can delete it
**Auth method and rationale:**
The Study Tracker API uses JWT Bearer token authentication.

After logging in, the client sends the JWT in the HTTP Authorization header:

Authorization: Bearer <token>

JWT authentication is appropriate because the server can identify the authenticated student on each protected request without requiring the client to send a student ID as proof of identity.

Public course information can be accessed without authentication. Personal study sessions, goals, and progress require authentication. Students can modify or delete only their own study sessions and goals.

## Section 6 — Error Responses for POST /study_sessions

| Status Code           | When it occurs |
|-------------          |---------------|
201 Created             The study session was successfully created
400 Bad Request         Required request data is missing or malformed
401 Unauthorized        Authentication is missing or the JWT is invalid
404 Not Found           The specified course does not exist
422 Unprocessable       The JSON is valid, but a field fails
    Content             validation, such as a negative
                        duration    
500 Internal Server     An unexpected server error 
    Error               prevents creation

Example 400 response:

{
    "error": "duration_minutes is required"
}

Example 401 response:

{
    "error": "Authentication required"
}

Example 404 response:

{
    "error": "Course not found"
}
Example 422 response:

{
    "error": "duration_minutes must be greater than zero"
}

