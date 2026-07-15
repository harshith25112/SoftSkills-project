# Audio Generation Guide for Active Listening Challenges

## Overview
This guide explains how to generate audio files for the 15 listening challenges (5 Academic, 5 Professional, 5 Personal).

## Folder Structure
Audio files should be placed in:
```
public/
  audio/
    academic/
      - final-exam-schedule.mp3
      - study-group-planning.mp3
      - lab-partner-discussion.mp3
      - tutoring-request.mp3
      - research-methodology-lecture.mp3
    professional/
      - daily-standup.mp3
      - manager-feedback.mp3
      - client-call-summary.mp3
      - performance-feedback.mp3
      - project-status-update.mp3
    personal/
      - weekend-plans.mp3
      - family-schedule.mp3
      - resolving-misunderstanding.mp3
      - checking-in-friend.mp3
      - birthday-invitation.mp3
```

## Recommended Tools & Services

### Option 1: Free Text-to-Speech Services
1. **Google Text-to-Speech (Free)**
   - Visit: https://cloud.google.com/text-to-speech
   - Use natural voices (e.g., "en-US-Neural2-D" for male, "en-US-Neural2-F" for female)
   - Export as MP3

2. **Amazon Polly (Free Tier)**
   - Visit: https://aws.amazon.com/polly/
   - Free tier: 5 million characters/month
   - Use neural voices for better quality

3. **Microsoft Azure Speech (Free Tier)**
   - Visit: https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/
   - Free tier: 5 hours/month
   - High-quality neural voices

### Option 2: Browser-Based TTS
1. **Natural Reader** (https://www.naturalreaders.com/)
   - Free online TTS
   - Multiple voice options
   - Can download audio

2. **TTSMaker** (https://ttsmaker.com/)
   - Free, no signup required
   - Multiple languages and voices
   - Direct MP3 download

### Option 3: Professional Voice Recording
If you have access to voice actors or want professional quality:
- Use Audacity (free) or Adobe Audition for recording
- Record in a quiet environment
- Export as MP3 at 128kbps or higher

## Voice Recommendations by Category

### Academic Challenges
- **Voice Style**: Clear, professional, slightly formal
- **Suggested Voices**: 
  - Male professor: "en-US-Neural2-D" or "en-GB-Neural2-D"
  - Female student: "en-US-Neural2-F" or "en-AU-Neural2-A"
- **Pace**: Moderate (not too fast, clear enunciation)

### Professional Challenges
- **Voice Style**: Professional, confident, workplace-appropriate
- **Suggested Voices**:
  - Manager/Colleague: "en-US-Neural2-C" or "en-US-Neural2-D"
  - Client: "en-US-Neural2-F" or "en-GB-Neural2-B"
- **Pace**: Moderate to slightly fast (business-like)

### Personal Challenges
- **Voice Style**: Warm, conversational, friendly
- **Suggested Voices**:
  - Friend/Family: "en-US-Neural2-A" or "en-US-Neural2-F"
  - Casual, natural tone
- **Pace**: Natural conversational speed

## Step-by-Step Process

### Using Google Cloud TTS (Example)
1. Sign up for Google Cloud (free trial available)
2. Enable Text-to-Speech API
3. Use the following script or API call:

```python
from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient()

# Example for academic challenge 1
text = "Good afternoon. I've had several students ask about the final exam schedule. The exam will be held on December 18th at 2 PM in the main auditorium, not our usual classroom. You'll have exactly two hours to complete it. Please bring a calculator and one sheet of handwritten notes. The exam covers chapters 8 through 12, focusing primarily on the concepts we discussed in weeks 5 and 6."

synthesis_input = texttospeech.SynthesisInput(text=text)
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Neural2-D",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

with open("public/audio/academic/final-exam-schedule.mp3", "wb") as out:
    out.write(response.audio_content)
```

### Using Online TTS Tools
1. Copy the transcript from `src/modules/activeListening/listeningChallenges.ts`
2. Paste into TTS tool
3. Select appropriate voice
4. Generate and download
5. Rename file to match the `audioUrl` in the challenge data
6. Place in correct folder

## Audio Quality Guidelines

- **Format**: MP3
- **Bitrate**: 128 kbps minimum (192 kbps recommended)
- **Sample Rate**: 44.1 kHz
- **Duration**: Most clips should be 15-45 seconds
- **Volume**: Normalized, consistent across all files
- **No Background Noise**: Clean, clear audio

## Transcripts Location
All transcripts are available in:
`src/modules/activeListening/listeningChallenges.ts`

Each challenge has a `transcript` field containing the exact text to convert to speech.

## Quick Reference: All Transcripts

### Academic
1. **final-exam-schedule.mp3**: Lines 10 in listeningChallenges.ts
2. **study-group-planning.mp3**: Lines 30
3. **lab-partner-discussion.mp3**: Lines 50
4. **tutoring-request.mp3**: Lines 70
5. **research-methodology-lecture.mp3**: Lines 90

### Professional
1. **daily-standup.mp3**: Lines 113
2. **manager-feedback.mp3**: Lines 133
3. **client-call-summary.mp3**: Lines 153
4. **performance-feedback.mp3**: Lines 173
5. **project-status-update.mp3**: Lines 193

### Personal
1. **weekend-plans.mp3**: Lines 216
2. **family-schedule.mp3**: Lines 236
3. **resolving-misunderstanding.mp3**: Lines 256
4. **checking-in-friend.mp3**: Lines 270
5. **birthday-invitation.mp3**: Lines 290

## Testing
After generating audio files:
1. Place files in `public/audio/[category]/` folders
2. Start the React app: `npm start`
3. Navigate to: Communication Skills → Active Listening → Challenges
4. Test each challenge to ensure audio plays correctly

## Troubleshooting
- **Audio not playing**: Check file paths match `audioUrl` in challenge data
- **CORS issues**: Ensure files are in `public/` folder (served statically)
- **File size**: Keep files under 2MB for faster loading
- **Format issues**: Convert to MP3 if using other formats

## Alternative: Use Placeholder Audio
If you need to test the UI without real audio:
1. Use any short MP3 file (even silence)
2. Rename and duplicate for all 15 challenges
3. Replace with real audio later

