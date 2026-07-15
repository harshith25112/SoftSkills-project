# Audio Generation Instructions for Active Listening Challenges

## Overview
This document provides instructions for generating audio files for the Active Listening challenges organized by **difficulty levels** (Easy, Medium, Hard) across three contexts: Academic, Professional, and Personal.

## Audio File Structure

```
public/audio/
├── academic/
│   ├── easy/
│   │   ├── class-announcement.mp3
│   │   └── office-hours.mp3
│   ├── medium/
│   │   ├── final-exam-schedule.mp3
│   │   └── study-group-planning.mp3
│   └── hard/
│       ├── research-project.mp3
│       └── lab-safety.mp3
├── professional/
│   ├── easy/
│   │   ├── meeting-reminder.mp3
│   │   └── email-request.mp3
│   ├── medium/
│   │   ├── daily-standup.mp3
│   │   └── manager-feedback.mp3
│   └── hard/
│       ├── project-requirements.mp3
│       └── quarterly-review.mp3
└── personal/
    ├── easy/
    │   ├── lunch-plans.mp3
    │   └── movie-invitation.mp3
    ├── medium/
    │   ├── weekend-plans.mp3
    │   └── family-schedule.mp3
    └── hard/
        ├── event-planning.mp3
        └── travel-planning.mp3
```

## Difficulty Levels Explained

### 🟢 EASY (Beginner)
- **Duration**: 10-15 seconds
- **Complexity**: Simple sentences, single topic
- **Details**: 2-3 key pieces of information
- **Vocabulary**: Common, everyday words
- **Speed**: Slow to normal pace
- **Example**: "Please remember that your homework is due next Monday."

### 🟡 MEDIUM (Intermediate)
- **Duration**: 15-25 seconds
- **Complexity**: Multiple sentences, related topics
- **Details**: 4-6 key pieces of information
- **Vocabulary**: Professional/academic terms
- **Speed**: Normal pace
- **Example**: "The exam will be on December 18th at 2 PM in the main auditorium. You'll need a calculator and handwritten notes."

### 🔴 HARD (Advanced)
- **Duration**: 25-40 seconds
- **Complexity**: Multiple topics, sequential information
- **Details**: 7+ key pieces of information
- **Vocabulary**: Technical/specialized terms
- **Speed**: Normal to fast pace
- **Example**: Complex project requirements with multiple deadlines, specifications, and stakeholders

## Method 1: Using Free Online TTS Tools

### Recommended Tools:
1. **Google Cloud Text-to-Speech** (Free tier available)
   - https://cloud.google.com/text-to-speech
   - High quality, natural voices
   - Multiple language support

2. **Natural Reader** (Free online)
   - https://www.naturalreaders.com/online/
   - Good quality, easy to use
   - Download as MP3

3. **TTSMaker** (Free, no registration)
   - https://ttsmaker.com/
   - Multiple voices
   - Direct MP3 download

4. **ElevenLabs** (High Quality, Free Tier)
   - https://elevenlabs.io/
   - 10,000 characters/month free
   - Most natural-sounding voices

### Voice Selection by Difficulty:
- **Easy**: Slower, clearer voice (e.g., "en-US-Standard-A")
- **Medium**: Normal pace, professional voice (e.g., "en-US-Standard-D")
- **Hard**: Natural pace, confident voice (e.g., "en-US-Neural2-D")

### Steps:
1. Copy the transcript text from the table below
2. Paste into your chosen TTS tool
3. Select appropriate voice based on difficulty
4. Adjust speed if needed (Easy: 0.9x, Medium: 1.0x, Hard: 1.0-1.1x)
5. Generate and download the MP3 file
6. Rename to match the filename in the table
7. Place in the appropriate difficulty folder

## Method 2: Using Python with gTTS (Google Text-to-Speech)

### Install gTTS:
```bash
pip install gtts
```

### Complete Generation Script:

Save this as `generate_audio.py`:

```python
from gtts import gTTS
import os

# Create directory structure
contexts = ['academic', 'professional', 'personal']
difficulties = ['easy', 'medium', 'hard']

for context in contexts:
    for difficulty in difficulties:
        os.makedirs(f'public/audio/{context}/{difficulty}', exist_ok=True)

# Audio data organized by context and difficulty
audio_data = {
    'academic': {
        'easy': {
            'class-announcement.mp3': 'Please remember that your homework assignment is due next Monday. Submit it through the online portal before midnight.',
            'office-hours.mp3': 'My office hours are every Tuesday and Thursday from 2 to 4 PM in room 305. Feel free to drop by if you have questions.'
        },
        'medium': {
            'final-exam-schedule.mp3': 'The final exam will be held on December 18th at 2 PM in the main auditorium. You will have exactly two hours to complete it. Please bring a calculator and one sheet of handwritten notes. The exam covers chapters 8 through 12.',
            'study-group-planning.mp3': 'We should meet this Thursday evening at 6 PM in the library study room on the third floor to review for the midterm. Sarah will bring notes from the last three lectures. Mike will prepare practice problems for statistics.'
        },
        'hard': {
            'research-project.mp3': 'Your research project proposal is due on October 15th. The literature review must be submitted by November 1st with at least 10 peer-reviewed sources. Your methodology section should be ready by November 20th. The complete draft is due December 5th, and final presentations will be held during exam week on December 18th and 19th.',
            'lab-safety.mp3': 'Before entering the chemistry lab, you must wear safety goggles, a lab coat, and closed-toe shoes. All long hair must be tied back. When handling chemicals, always add acid to water, never water to acid. In case of a spill, immediately notify the lab supervisor and use the spill kit located in cabinet B3. The emergency eyewash station is near the exit door.'
        }
    },
    'professional': {
        'easy': {
            'meeting-reminder.mp3': 'Just a reminder that we have a team meeting tomorrow at 10 AM in Conference Room B. Please bring your project updates.',
            'email-request.mp3': 'Could you please send me the sales report from last quarter? I need it for the presentation on Friday. Thank you.'
        },
        'medium': {
            'daily-standup.mp3': 'Yesterday I completed the user authentication module and fixed three bugs in the payment system. Today I will work on the dashboard redesign and attend the client meeting at 3 PM. I am blocked on the API integration until the backend team provides the documentation.',
            'manager-feedback.mp3': 'Your presentation skills have improved significantly this quarter. However, I would like you to focus on providing more detailed project timelines in your reports. Let us schedule a follow-up meeting next Tuesday to discuss your professional development goals.'
        },
        'hard': {
            'project-requirements.mp3': 'We need the mobile app to support both iOS 14 and above and Android 10 and above. The priority features are user authentication with OAuth 2.0, a product catalog with real-time inventory updates, and a shopping cart with multiple payment gateways including PayPal and Stripe. We are targeting a soft launch on March 15th for beta testers, followed by the public release on April 1st. The app must handle at least 10,000 concurrent users.',
            'quarterly-review.mp3': 'This quarter we achieved 125% of our sales target, bringing in 2.5 million in revenue. Customer satisfaction scores increased from 78% to 85%. However, our customer acquisition cost rose by 15%, which we need to address. For next quarter, we are launching three new product lines, expanding to two additional markets, and implementing a new CRM system. We are also hiring five new team members for the sales and marketing departments.'
        }
    },
    'personal': {
        'easy': {
            'lunch-plans.mp3': 'Do you want to grab lunch at the Italian restaurant on Main Street today at noon? I heard they have great pizza.',
            'movie-invitation.mp3': 'There is a new action movie playing at the cinema this Saturday evening. Would you like to join me? The show starts at 7 PM.'
        },
        'medium': {
            'weekend-plans.mp3': 'Let us meet at the coffee shop on Main Street this Saturday at 10 AM. We can grab breakfast and then go to the farmers market. After that, we could visit the new art gallery downtown. I will bring my reusable bags for the market.',
            'family-schedule.mp3': 'Mom has a doctor appointment on Wednesday at 2 PM. Dad will pick up groceries after work on Thursday. I need to take the car on Friday evening for my study group. Can someone give me a ride to soccer practice on Saturday morning at 9 AM?'
        },
        'hard': {
            'event-planning.mp3': 'For Sarah\'s surprise birthday party next Saturday, we need to coordinate several things. Tom will handle the decorations and arrive at 3 PM to set up. Lisa is bringing the cake from the bakery on Elm Street, and she needs to pick it up by 4 PM. I will manage the music playlist and coordinate with the restaurant for the dinner reservation at 7 PM for 15 people. Can you handle sending out the invitations and collecting RSVPs by Wednesday? We also need someone to distract Sarah between 3 and 5 PM while we set up.',
            'travel-planning.mp3': 'For our summer vacation, I found flights to Barcelona departing on July 10th at 6 AM and returning on July 20th at 9 PM. The hotel in the Gothic Quarter costs 120 euros per night, and it includes breakfast. We should book the Sagrada Familia tour for July 12th, the Park Guell visit for July 14th, and the day trip to Montserrat for July 16th. I also want to try that famous tapas restaurant in El Born on our first evening. We need to apply for travel insurance and exchange currency before we leave.'
        }
    }
}

# Generate all files
total_files = 0
for context, difficulties_dict in audio_data.items():
    for difficulty, files in difficulties_dict.items():
        for filename, text in files.items():
            # Adjust speed based on difficulty
            slow = True if difficulty == 'easy' else False
            
            tts = gTTS(text=text, lang='en', slow=slow)
            filepath = f'public/audio/{context}/{difficulty}/{filename}'
            tts.save(filepath)
            print(f'✅ Generated: {filepath}')
            total_files += 1

print(f'\n🎉 Successfully generated {total_files} audio files!')
print(f'   - 6 Academic files (2 easy, 2 medium, 2 hard)')
print(f'   - 6 Professional files (2 easy, 2 medium, 2 hard)')
print(f'   - 6 Personal files (2 easy, 2 medium, 2 hard)')
```

Run with:
```bash
python generate_audio.py
```

## Complete Transcripts Reference Table

### 🎓 ACADEMIC CONTEXT

| Difficulty | File Name | Transcript | Duration |
|------------|-----------|------------|----------|
| **EASY** | | | |
| | class-announcement.mp3 | Please remember that your homework assignment is due next Monday. Submit it through the online portal before midnight. | ~10s |
| | office-hours.mp3 | My office hours are every Tuesday and Thursday from 2 to 4 PM in room 305. Feel free to drop by if you have questions. | ~12s |
| **MEDIUM** | | | |
| | final-exam-schedule.mp3 | The final exam will be held on December 18th at 2 PM in the main auditorium. You will have exactly two hours to complete it. Please bring a calculator and one sheet of handwritten notes. The exam covers chapters 8 through 12. | ~20s |
| | study-group-planning.mp3 | We should meet this Thursday evening at 6 PM in the library study room on the third floor to review for the midterm. Sarah will bring notes from the last three lectures. Mike will prepare practice problems for statistics. | ~18s |
| **HARD** | | | |
| | research-project.mp3 | Your research project proposal is due on October 15th. The literature review must be submitted by November 1st with at least 10 peer-reviewed sources. Your methodology section should be ready by November 20th. The complete draft is due December 5th, and final presentations will be held during exam week on December 18th and 19th. | ~30s |
| | lab-safety.mp3 | Before entering the chemistry lab, you must wear safety goggles, a lab coat, and closed-toe shoes. All long hair must be tied back. When handling chemicals, always add acid to water, never water to acid. In case of a spill, immediately notify the lab supervisor and use the spill kit located in cabinet B3. The emergency eyewash station is near the exit door. | ~35s |

### 💼 PROFESSIONAL CONTEXT

| Difficulty | File Name | Transcript | Duration |
|------------|-----------|------------|----------|
| **EASY** | | | |
| | meeting-reminder.mp3 | Just a reminder that we have a team meeting tomorrow at 10 AM in Conference Room B. Please bring your project updates. | ~10s |
| | email-request.mp3 | Could you please send me the sales report from last quarter? I need it for the presentation on Friday. Thank you. | ~10s |
| **MEDIUM** | | | |
| | daily-standup.mp3 | Yesterday I completed the user authentication module and fixed three bugs in the payment system. Today I will work on the dashboard redesign and attend the client meeting at 3 PM. I am blocked on the API integration until the backend team provides the documentation. | ~22s |
| | manager-feedback.mp3 | Your presentation skills have improved significantly this quarter. However, I would like you to focus on providing more detailed project timelines in your reports. Let us schedule a follow-up meeting next Tuesday to discuss your professional development goals. | ~20s |
| **HARD** | | | |
| | project-requirements.mp3 | We need the mobile app to support both iOS 14 and above and Android 10 and above. The priority features are user authentication with OAuth 2.0, a product catalog with real-time inventory updates, and a shopping cart with multiple payment gateways including PayPal and Stripe. We are targeting a soft launch on March 15th for beta testers, followed by the public release on April 1st. The app must handle at least 10,000 concurrent users. | ~38s |
| | quarterly-review.mp3 | This quarter we achieved 125% of our sales target, bringing in 2.5 million in revenue. Customer satisfaction scores increased from 78% to 85%. However, our customer acquisition cost rose by 15%, which we need to address. For next quarter, we are launching three new product lines, expanding to two additional markets, and implementing a new CRM system. We are also hiring five new team members for the sales and marketing departments. | ~35s |

### 👥 PERSONAL CONTEXT

| Difficulty | File Name | Transcript | Duration |
|------------|-----------|------------|----------|
| **EASY** | | | |
| | lunch-plans.mp3 | Do you want to grab lunch at the Italian restaurant on Main Street today at noon? I heard they have great pizza. | ~10s |
| | movie-invitation.mp3 | There is a new action movie playing at the cinema this Saturday evening. Would you like to join me? The show starts at 7 PM. | ~12s |
| **MEDIUM** | | | |
| | weekend-plans.mp3 | Let us meet at the coffee shop on Main Street this Saturday at 10 AM. We can grab breakfast and then go to the farmers market. After that, we could visit the new art gallery downtown. I will bring my reusable bags for the market. | ~20s |
| | family-schedule.mp3 | Mom has a doctor appointment on Wednesday at 2 PM. Dad will pick up groceries after work on Thursday. I need to take the car on Friday evening for my study group. Can someone give me a ride to soccer practice on Saturday morning at 9 AM? | ~22s |
| **HARD** | | | |
| | event-planning.mp3 | For Sarah's surprise birthday party next Saturday, we need to coordinate several things. Tom will handle the decorations and arrive at 3 PM to set up. Lisa is bringing the cake from the bakery on Elm Street, and she needs to pick it up by 4 PM. I will manage the music playlist and coordinate with the restaurant for the dinner reservation at 7 PM for 15 people. Can you handle sending out the invitations and collecting RSVPs by Wednesday? We also need someone to distract Sarah between 3 and 5 PM while we set up. | ~40s |
| | travel-planning.mp3 | For our summer vacation, I found flights to Barcelona departing on July 10th at 6 AM and returning on July 20th at 9 PM. The hotel in the Gothic Quarter costs 120 euros per night, and it includes breakfast. We should book the Sagrada Familia tour for July 12th, the Park Guell visit for July 14th, and the day trip to Montserrat for July 16th. I also want to try that famous tapas restaurant in El Born on our first evening. We need to apply for travel insurance and exchange currency before we leave. | ~42s |

## Audio Quality Guidelines

### General Specifications:
- **Format**: MP3
- **Bitrate**: 128 kbps minimum (192 kbps recommended)
- **Sample Rate**: 44.1 kHz
- **Volume**: Normalized, consistent across all files
- **Clarity**: Clear pronunciation, no background noise

### Difficulty-Specific Guidelines:

**🟢 EASY:**
- Duration: 10-15 seconds
- Speed: 0.9x (slightly slower)
- Pauses: Clear pauses between sentences
- Emphasis: Stress key words

**🟡 MEDIUM:**
- Duration: 15-25 seconds
- Speed: 1.0x (normal)
- Pauses: Natural pauses
- Emphasis: Professional tone

**🔴 HARD:**
- Duration: 25-40 seconds
- Speed: 1.0-1.1x (normal to slightly faster)
- Pauses: Minimal pauses
- Emphasis: Natural, conversational

## Validation Rules

The Active Listening challenges use **strict validation** based on the transcript:

1. **Similarity Threshold**: 70% or higher to pass
2. **Key Details**: Must capture critical information
3. **Context Matching**: Answer must match audio exactly
4. **Fail Condition**: < 70% similarity = FAIL

### Difficulty Impact on Validation:
- **Easy**: More forgiving (common words, simple structure)
- **Medium**: Standard validation (professional terms)
- **Hard**: Strict validation (technical terms, multiple details)

## Testing After Generation

1. Place all generated MP3 files in their respective difficulty folders
2. Start the React app: `npm start`
3. Navigate to: Communication Skills → Active Listening
4. Select a context (Academic, Professional, or Personal)
5. Test each difficulty level:
   - ✅ Audio plays correctly
   - ✅ Audio matches the transcript
   - ✅ Validation works (70% threshold)
   - ✅ Difficulty progression feels appropriate

## Troubleshooting

### Audio not playing:
- Check file path matches exactly (case-sensitive)
- Verify file is in correct difficulty folder
- Check file format is MP3
- Ensure file is not corrupted

### Validation always failing:
- Verify transcript in code matches audio exactly
- Check similarity threshold (should be 70%)
- Test with exact transcript text first

### Difficulty feels wrong:
- Adjust TTS speed settings
- Re-generate with different voice
- Check transcript complexity matches difficulty

## Summary

**Total Files to Generate: 18**
- Academic: 6 files (2 easy, 2 medium, 2 hard)
- Professional: 6 files (2 easy, 2 medium, 2 hard)
- Personal: 6 files (2 easy, 2 medium, 2 hard)

**Estimated Generation Time:**
- Using Python script: 2-3 minutes
- Using online tools: 15-20 minutes

**Storage Requirements:**
- Total size: ~5-8 MB (all 18 files)
- Per file: ~200-500 KB

Run the Python script for fastest generation, or use online tools for highest quality!
