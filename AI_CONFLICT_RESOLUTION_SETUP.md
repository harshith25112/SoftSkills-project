# 🤖 AI-Powered Conflict Resolution Setup

## Overview

The Conflict Resolution challenge now uses **real AI** (not a scripted bot) to have genuine, intelligent conversations with users. The AI responds naturally to what you actually say, understands context, and adapts its behavior based on your approach.

---

## ✨ Features

### **Real AI Conversation**
- ✅ **Genuine responses** - AI understands and responds to your actual message
- ✅ **Context-aware** - Remembers conversation history
- ✅ **Adaptive behavior** - Reacts appropriately to your tone and approach
- ✅ **No repetition** - Every response is unique and contextual
- ✅ **Natural flow** - Feels like talking to a real person

### **Intelligent Analysis**
- ✅ **Skill detection** - AI analyzes your conflict resolution skills
- ✅ **Intent recognition** - Understands what you're trying to do
- ✅ **Sentiment analysis** - Detects positive, neutral, or negative tone
- ✅ **Fail detection** - Identifies problematic behavior

### **Dynamic Scenarios**
- ✅ **Academic** - Group project conflicts
- ✅ **Professional** - Workplace collaboration issues
- ✅ **Personal** - Friendship/relationship conflicts

---

## 🚀 Quick Setup (5 minutes)

### **Option 1: Groq (RECOMMENDED - FREE & FAST)** ⭐

**Why Groq?**
- 100% FREE forever
- No credit card required
- Fast responses (< 1 second)
- Excellent AI quality (Llama 3.1 70B)

**Setup Steps:**
1. Visit: https://console.groq.com/
2. Click "Sign Up" (use Google/GitHub or email)
3. Go to "API Keys" in the left sidebar
4. Click "Create API Key"
5. Copy the key (starts with `gsk_...`)
6. In the app, click "Enter API Key" and paste it
7. Done! Start chatting 🎉

**Example Key Format:**
```
gsk_1234567890abcdefghijklmnopqrstuvwxyz
```

---

### **Option 2: OpenAI ($5 Free Credits)**

**Why OpenAI?**
- $5 free credits for new users
- GPT-3.5 Turbo (high quality)
- Credits last 3 months

**Setup Steps:**
1. Visit: https://platform.openai.com/
2. Sign up for an account
3. Go to "API Keys" → "Create new secret key"
4. Copy the key (starts with `sk-...`)
5. In the app, save as `OPENAI_API_KEY` in localStorage
6. Done!

**Cost After Free Credits:**
- ~$0.001 per conversation (very cheap)
- $5 = ~5,000 conversations

---

### **Option 3: Hugging Face (100% FREE)**

**Why Hugging Face?**
- Completely free
- No credit card
- Open-source models

**Setup Steps:**
1. Visit: https://huggingface.co/
2. Sign up (free)
3. Go to Settings → Access Tokens
4. Create new token (read access)
5. Copy the token
6. Save as `HF_API_KEY` in localStorage

**Note:** Hugging Face may be slower than Groq/OpenAI

---

## 💻 How to Use

### **1. First Time Setup**

When you open Conflict Resolution for the first time:

```
┌─────────────────────────────────────┐
│  🤖 AI Setup Required               │
│                                     │
│  To use AI-powered conflict         │
│  resolution, you need a free        │
│  API key.                           │
│                                     │
│  ✨ Recommended: Groq (FREE & FAST) │
│                                     │
│  1. Visit console.groq.com          │
│  2. Sign up (free, no credit card)  │
│  3. Go to API Keys → Create new key │
│  4. Copy the key                    │
│  5. Click button below and paste it │
│                                     │
│  [Enter API Key]                    │
│  [Back]                             │
└─────────────────────────────────────┘
```

### **2. Enter Your API Key**

Click "Enter API Key" and paste your Groq API key:

```
┌─────────────────────────────────────┐
│  Enter your Groq API key:           │
│  ┌───────────────────────────────┐  │
│  │ gsk_1234567890abcdef...       │  │
│  └───────────────────────────────┘  │
│                                     │
│  [OK]  [Cancel]                     │
└─────────────────────────────────────┘
```

### **3. Start Chatting!**

Once configured, the AI will greet you with the conflict scenario:

```
AI: "Hey, I noticed you changed our project approach 
     without telling anyone. We all agreed on the 
     research method, and now you've gone ahead with 
     something completely different. This is going 
     to mess up everyone's work."

You: [Type your response...]
```

---

## 🎯 How It Works

### **AI Response Generation**

```typescript
// User sends message
User: "I understand you're frustrated. Can you help me 
       understand specifically how this affected your work?"

// AI analyzes intent
Analysis:
  ✓ Intent: seeking_understanding
  ✓ Skills: listen_first, focus_on_facts
  ✓ Sentiment: positive
  ✓ Fails: none

// AI generates contextual response
AI: "Thank you for listening. I had already started 
     working on the data analysis based on our agreed 
     method, and now I have to redo everything. It's 
     frustrating because I put a lot of time into it."

// Conflict state updates
State: tense → resolving
```

### **Skill Detection**

The AI analyzes your messages for 5 key skills:

1. **Listen First** 🎧
   - "I understand your frustration"
   - "Can you help me understand..."
   - "From your perspective..."

2. **Focus on Facts** 📊
   - "The issue is..."
   - "What happened was..."
   - "I noticed that..."

3. **Find Common Ground** 🤝
   - "We both want the project to succeed"
   - "We can agree that..."
   - "Our shared goal is..."

4. **Propose Solutions** 💡
   - "What if we..."
   - "How about we..."
   - "One option could be..."

5. **Document Agreements** 📝
   - "So we've agreed to..."
   - "Moving forward, we'll..."
   - "To summarize..."

### **Fail Detection**

The AI also detects problematic behavior:

- ❌ **Personal Attacks** - Profanity, name-calling, "you always..."
- ❌ **Avoiding Conflict** - "Whatever", "forget it", dismissive
- ❌ **Emotional Reactions** - ALL CAPS, excessive !!!, purely emotional

---

## 📊 Scoring System

### **Pass Requirements**
- ✅ Total score ≥ 60/100
- ✅ Demonstrate 4+ skills
- ✅ No repeated personal attacks (< 3)

### **Score Breakdown**
- Each skill: 0-20 points
- Total: 0-100 points
- First detection: +10 points
- Each additional: +5 points (max 20)

### **Example Scores**

**Excellent (85/100) - PASS ✅**
```
listen_first: 20/20 (3 times)
focus_on_facts: 15/20 (2 times)
find_common_ground: 15/20 (2 times)
propose_solutions: 20/20 (3 times)
document_agreements: 15/20 (2 times)
```

**Poor (25/100) - FAIL ❌**
```
listen_first: 10/20 (1 time)
focus_on_facts: 15/20 (2 times)
find_common_ground: 0/20 (none)
propose_solutions: 0/20 (none)
document_agreements: 0/20 (none)
Personal attacks: 3 (auto-fail)
```

---

## 🎭 Example Conversations

### **Successful Resolution** ✅

```
AI: "You changed our project approach without telling anyone."

You: "I hear what you're saying, and I can see why you're 
      frustrated. Can you help me understand specifically 
      how this affected your work?"
[✓ listen_first, ✓ focus_on_facts]

AI: "Thank you for listening. I had already started the 
     data analysis based on our agreed method, and now I 
     have to redo everything."

You: "I understand. I should have communicated with the 
      team first. What if we set up a shared document 
      where we track progress and flag any potential 
      changes before implementing them?"
[✓ listen_first, ✓ propose_solutions]

AI: "That could work. Maybe we should also schedule a 
     quick weekly check-in to make sure we're all on 
     the same page?"

You: "Great idea. So we've agreed to use a shared tracker 
      and have weekly check-ins. I'll set up the document 
      today and schedule our first meeting for Friday."
[✓ document_agreements]

AI: "Perfect. I'm glad we worked this out. Let's make 
     sure we stick to this plan going forward."

Result: PASS ✅
Score: 75/100
Feedback: "Excellent! You demonstrated all 5 key skills."
```

### **Failed Resolution** ❌

```
AI: "You changed our project approach without telling anyone."

You: "Well, maybe if you checked your email, you would 
      have known."
[✗ defensive, ✗ taking_sides]

AI: "I check my email regularly. The issue isn't about 
     email—it's about making decisions without discussion."

You: "You always make such a big deal out of everything."
[✗ personal_attacks]

AI: "I don't appreciate being spoken to that way. Let's 
     either have a professional conversation or end this."

You: "Whatever. Let's just forget it."
[✗ avoiding_conflict]

AI: "I don't think we can have a productive conversation 
     right now. Maybe we should involve a TA or professor."

Result: FAIL ❌
Score: 15/100
Feedback: "Personal attacks and defensive behavior prevented 
           resolution. Focus on listening, acknowledging, and 
           proposing solutions."
```

---

## 🔧 Troubleshooting

### **"AI Setup Required" keeps showing**

**Solution:**
1. Make sure you entered the API key correctly
2. Check that it starts with `gsk_` (Groq) or `sk-` (OpenAI)
3. Try refreshing the page after entering the key

### **"API key is invalid"**

**Solution:**
1. Go back to console.groq.com
2. Create a new API key
3. Copy the entire key (including `gsk_` prefix)
4. Enter it again in the app

### **"I'm having trouble responding"**

**Possible causes:**
- No internet connection
- API key expired or revoked
- API service is down (rare)

**Solution:**
1. Check your internet connection
2. Try creating a new API key
3. Wait a few minutes and try again

### **Responses are slow**

**Groq:** Should be < 1 second
**OpenAI:** 1-3 seconds
**Hugging Face:** 3-10 seconds

**If slower:**
- Check your internet speed
- Try Groq (fastest)
- Close other tabs/apps

---

## 🔐 Privacy & Security

### **Your API Key**
- ✅ Stored locally in your browser (localStorage)
- ✅ Never sent to our servers
- ✅ Only you can access it
- ✅ Can be deleted anytime

### **Conversation Data**
- ✅ Sent only to the AI service you choose (Groq/OpenAI/HF)
- ✅ Not stored on our servers
- ✅ Cleared when you close the tab
- ✅ No personal information collected

### **Best Practices**
- Don't share your API key with others
- Use a free tier key for testing
- Delete the key from localStorage if sharing your computer

---

## 💰 Cost Comparison

| Service | Free Tier | Cost After | Speed | Quality |
|---------|-----------|------------|-------|---------|
| **Groq** | ✅ FREE Forever | FREE | ⚡ < 1s | ⭐⭐⭐⭐⭐ |
| **OpenAI** | $5 credits | $0.001/conv | ⚡ 1-3s | ⭐⭐⭐⭐⭐ |
| **Hugging Face** | ✅ FREE Forever | FREE | 🐌 3-10s | ⭐⭐⭐⭐ |

**Recommendation:** Use **Groq** for the best experience (free, fast, high quality)

---

## 🎓 Tips for Success

### **Do:**
- ✅ Listen actively ("I understand...", "I hear you...")
- ✅ Ask clarifying questions ("Can you help me understand...")
- ✅ Use I-statements ("I feel...", "I think...")
- ✅ Propose specific solutions ("What if we...", "How about...")
- ✅ Summarize agreements ("So we've agreed to...")

### **Don't:**
- ❌ Use profanity or aggressive language
- ❌ Make personal attacks ("You always...", "You're lazy...")
- ❌ Be defensive ("But I...", "Actually I...")
- ❌ Avoid the issue ("Whatever", "Forget it")
- ❌ Use all caps or excessive punctuation!!!

---

## 🚀 Ready to Start!

1. Get your free Groq API key: https://console.groq.com/
2. Enter it in the app
3. Start practicing conflict resolution with real AI!

The AI will respond naturally to everything you say, making this a genuine learning experience! 🎉


