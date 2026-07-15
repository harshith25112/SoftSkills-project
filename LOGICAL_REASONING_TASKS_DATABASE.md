# Logical Reasoning Tasks Database - Complete Guide

## Overview
This database contains **50 ready-made logical reasoning tasks** designed by cognitive science principles for the AI-ERA Soft Skills Academy. All tasks are interactive, game-like, and follow Duolingo-style engagement patterns.

## Structure

### SECTION 1: Difficulty Ladder ✅
**Location:** `src/data/logicalReasoningTasks.ts` - `difficultyLadder` array

Three-tier system:
- **Easy** (15 tasks): Basic patterns, simple sequences, direct deductions
- **Medium** (20 tasks): Multi-step reasoning, 2-3 clue integration, relationship mapping
- **Hard** (15 tasks): Complex puzzles, multi-variable logic grids, abstract analogies

Each level includes:
- Cognitive skills involved
- What makes it harder
- Example puzzle types
- Solving strategies

### SECTION 2: 50 Logical Reasoning Tasks ✅
**Location:** `src/data/logicalReasoningTasks.ts` - `logicalReasoningTasks` array

**Distribution:**
- **Easy:** 15 tasks (LR-001 to LR-015)
  - Academic: 5 tasks
  - Professional: 5 tasks
  - Personal: 5 tasks

- **Medium:** 20 tasks (LR-016 to LR-035)
  - Academic: 7 tasks
  - Professional: 7 tasks
  - Personal: 6 tasks

- **Hard:** 15 tasks (LR-036 to LR-050)
  - Academic: 5 tasks
  - Professional: 5 tasks
  - Personal: 5 tasks

**Task Types Used:**
- Pattern Match (8 tasks)
- Logic Grid (10 tasks)
- Sequence Sort (9 tasks)
- Input→Output Rule (7 tasks)
- Who-Did-It Paradox (6 tasks)
- Cause-Effect Chain (5 tasks)
- Analogical Mapping (4 tasks)
- Contradiction Spotting (1 task)

**Each Task Contains:**
- ✅ Task ID (LR-001 through LR-050)
- ✅ Difficulty level
- ✅ Context (Academic/Professional/Personal)
- ✅ Task Type
- ✅ Task Statement (the puzzle)
- ✅ Four answer choices (A-D)
- ✅ Correct Answer (0-3 index)
- ✅ Hint (doesn't reveal answer)
- ✅ Step-by-step explanation (teaches reasoning)

### SECTION 3: Teaching Module ✅
**Location:** `src/data/logicalReasoningTasks.ts` - `teachingModule` object

200-300 word guide covering:
- How to recognize patterns
- How to break down clues
- How to eliminate distractors
- How to map relationships
- How to use analogy and cause-effect logic

## Usage in Application

### Import the Data:
```typescript
import { logicalReasoningTasks, difficultyLadder, teachingModule } from '../data/logicalReasoningTasks';
```

### Filter by Difficulty:
```typescript
const easyTasks = logicalReasoningTasks.filter(t => t.difficulty === 'Easy');
const mediumTasks = logicalReasoningTasks.filter(t => t.difficulty === 'Medium');
const hardTasks = logicalReasoningTasks.filter(t => t.difficulty === 'Hard');
```

### Filter by Context:
```typescript
const academicTasks = logicalReasoningTasks.filter(t => t.context === 'Academic');
const professionalTasks = logicalReasoningTasks.filter(t => t.context === 'Professional');
const personalTasks = logicalReasoningTasks.filter(t => t.context === 'Personal');
```

### Get Random Task:
```typescript
const randomTask = logicalReasoningTasks[Math.floor(Math.random() * logicalReasoningTasks.length)];
```

### Get Task by ID:
```typescript
const task = logicalReasoningTasks.find(t => t.id === 'LR-001');
```

## Task Quality Features

✅ **Fun & Engaging:** Real-world scenarios, relatable contexts
✅ **No Pattern Repetition:** Each task uses unique puzzle structures
✅ **Solvable by Reasoning:** No external knowledge required
✅ **Educational:** Explanations teach the reasoning process
✅ **Progressive Difficulty:** Builds from simple to complex
✅ **Context-Specific:** Tailored to Academic/Professional/Personal scenarios

## Integration with LogicalReasoningTest Component

The `LogicalReasoningTest.tsx` component can be updated to:
1. Randomly select tasks from this database based on difficulty and context
2. Display tasks in the interactive task section
3. Use the teaching module in the explanation section
4. Reference the difficulty ladder to show user progress

## Next Steps

1. **Update LogicalReasoningTest Component** to use tasks from this database
2. **Add Randomization** - Select random tasks for each test session
3. **Add Progress Tracking** - Track which tasks user has completed
4. **Add Adaptive Difficulty** - Adjust difficulty based on performance
5. **Add Task Analytics** - Track which tasks are hardest/easiest

## Statistics

- **Total Tasks:** 50
- **Easy:** 15 (30%)
- **Medium:** 20 (40%)
- **Hard:** 15 (30%)
- **Academic:** 17 (34%)
- **Professional:** 17 (34%)
- **Personal:** 16 (32%)

All tasks are ready for direct integration into the application!
