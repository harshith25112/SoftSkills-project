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
            'event-planning.mp3': "For Sarah's surprise birthday party next Saturday, we need to coordinate several things. Tom will handle the decorations and arrive at 3 PM to set up. Lisa is bringing the cake from the bakery on Elm Street, and she needs to pick it up by 4 PM. I will manage the music playlist and coordinate with the restaurant for the dinner reservation at 7 PM for 15 people. Can you handle sending out the invitations and collecting RSVPs by Wednesday? We also need someone to distract Sarah between 3 and 5 PM while we set up.",
            'travel-planning.mp3': 'For our summer vacation, I found flights to Barcelona departing on July 10th at 6 AM and returning on July 20th at 9 PM. The hotel in the Gothic Quarter costs 120 euros per night, and it includes breakfast. We should book the Sagrada Familia tour for July 12th, the Park Guell visit for July 14th, and the day trip to Montserrat for July 16th. I also want to try that famous tapas restaurant in El Born on our first evening. We need to apply for travel insurance and exchange currency before we leave.'
        }
    }
}

# Generate all files
total_files = 0
print('🎵 Starting audio file generation...\n')

for context, difficulties_dict in audio_data.items():
    print(f'📁 Generating {context.upper()} context files...')
    for difficulty, files in difficulties_dict.items():
        print(f'  🔹 {difficulty.capitalize()} level:')
        for filename, text in files.items():
            # Adjust speed based on difficulty
            slow = True if difficulty == 'easy' else False
            
            tts = gTTS(text=text, lang='en', slow=slow)
            filepath = f'public/audio/{context}/{difficulty}/{filename}'
            tts.save(filepath)
            print(f'    ✅ {filename}')
            total_files += 1
    print()

print(f'🎉 Successfully generated {total_files} audio files!')
print(f'   - 6 Academic files (2 easy, 2 medium, 2 hard)')
print(f'   - 6 Professional files (2 easy, 2 medium, 2 hard)')
print(f'   - 6 Personal files (2 easy, 2 medium, 2 hard)')
print(f'\n📊 Total storage: ~5-8 MB')
print(f'⏱️  Generation time: ~2-3 minutes')
print(f'\n✨ All audio files are ready for use!')
print(f'\n🚀 Next steps:')
print(f'   1. Run: npm start')
print(f'   2. Navigate to: Communication Skills → Active Listening')
print(f'   3. Test each context and difficulty level')
print(f'   4. Verify audio plays and validation works')

