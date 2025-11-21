# Task Management API - Schema Development (2-Day Plan)

## Overview
This document outlines the 2-day development plan for completing the Pydantic schemas for the Task Management API.

---

## Day 1: Core Schemas (Task, Comment, Label)

### Morning Session (3-4 hours)

#### 1. Task Schema (`app/schemas/task.py`)
- [ ] Create `TaskBase` with core fields:
  - `title` (str, 1-200 chars)
  - `description` (Optional[str])
  - `status` (TaskStatus enum: TODO, IN_PROGRESS, DONE)
  - `priority` (TaskPriority enum: LOW, MEDIUM, HIGH)
  - `due_date` (Optional[datetime])

- [ ] Create `TaskCreate` schema:
  - Inherit from `TaskBase`
  - Add `label_ids` (Optional[List[int]])

- [ ] Create `TaskUpdate` schema:
  - All fields optional for partial updates
  - Include `label_ids` for label management

- [ ] Create `TaskRead` schema:
  - Inherit from `TaskBase`
  - Add `id`, `created_at`, `updated_at`
  - Configure `from_attributes = True`

- [ ] Create `TaskReadWithRelations` schema:
  - Inherit from `TaskRead`
  - Add `comments` and `labels` lists
  - Handle TYPE_CHECKING for circular imports

#### 2. Comment Schema (`app/schemas/comment.py`)
- [ ] Create `CommentBase`:
  - `content` (str, 1-1000 chars)
  - `author` (str, 1-100 chars)

- [ ] Create `CommentCreate`:
  - Inherit from `CommentBase`
  - Add `task_id` (int)

- [ ] Create `CommentUpdate`:
  - Optional `content` field only

- [ ] Create `CommentRead`:
  - Inherit from `CommentBase`
  - Add `id`, `task_id`, `created_at`, `updated_at`

### Afternoon Session (3-4 hours)

#### 3. Label Schema (`app/schemas/label.py`)
- [ ] Create `LabelBase`:
  - `name` (str, 1-50 chars)
  - `color` (str, hex color pattern validation)

- [ ] Create `LabelCreate`:
  - Inherit from `LabelBase`

- [ ] Create `LabelUpdate`:
  - Optional `name` and `color` fields

- [ ] Create `LabelRead`:
  - Inherit from `LabelBase`
  - Add `id`

#### 4. Testing & Validation
- [ ] Test all field validations
- [ ] Verify enum values work correctly
- [ ] Check datetime handling
- [ ] Validate hex color pattern

---

## Day 2: Activity Log Schema & Integration

### Morning Session (2-3 hours)

#### 1. Activity Log Schema (`app/schemas/activity_log.py`)
- [ ] Create `ActivityLogRead`:
  - `id` (int)
  - `task_id` (int)
  - `action` (str)
  - `description` (str)
  - `performed_by` (str)
  - `created_at` (datetime)
  - Configure `from_attributes = True`

**Note:** Activity logs are read-only (no Create/Update schemas needed)

### Afternoon Session (3-4 hours)

#### 2. Schema Module Integration (`app/schemas/__init__.py`)
- [ ] Import all schemas:
  - TaskCreate, TaskUpdate, TaskRead, TaskReadWithRelations
  - CommentCreate, CommentUpdate, CommentRead
  - LabelCreate, LabelUpdate, LabelRead
  - ActivityLogRead

- [ ] Export via `__all__` list

#### 3. Final Testing & Documentation
- [ ] Test all schema imports
- [ ] Verify circular import handling with TYPE_CHECKING
- [ ] Test schema serialization/deserialization
- [ ] Validate all Pydantic validations work
- [ ] Document any edge cases or special considerations

#### 4. Code Review Checklist
- [ ] All fields have proper type hints
- [ ] Field validations are appropriate
- [ ] Config classes set correctly
- [ ] No circular import issues
- [ ] Consistent naming conventions
- [ ] All schemas properly exported

---

## Key Considerations

### Validation Rules
- Use `Field()` for length constraints and patterns
- Enum values for status and priority
- Hex color validation: `^#[0-9A-Fa-f]{6}$`
- Datetime fields for timestamps

### Circular Import Prevention
- Use `TYPE_CHECKING` for forward references
- Import related schemas only for type hints
- Keep relationship schemas in separate files

### Pydantic Configuration
- Set `from_attributes = True` for ORM compatibility
- Use `Optional[]` for nullable fields
- Default values where appropriate

---

## Deliverables

By end of Day 2:
- ✅ 4 complete schema modules (task, comment, label, activity_log)
- ✅ 11 total schema classes
- ✅ Proper validation and type safety
- ✅ Clean module exports
- ✅ No circular import issues
- ✅ Ready for API endpoint integration
