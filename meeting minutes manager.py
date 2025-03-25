class Meeting:
    def __init__(self, meeting_id, title, date, participants, start_time, end_time):
        self.meeting_id = meeting_id
        self.title = title
        self.date = date
        self.participants = participants  # This should be a list of participant names
        self.start_time = start_time
        self.end_time = end_time
        self.minutes = {}

    def join_participant(self, participant):
        self.participants.append(participant)
        print(f"{participant} joined the meeting {self.title}.")

    def leave_participant(self, participant):
        if participant in self.participants:
            self.participants.remove(participant)
            print(f"{participant} left the meeting {self.title}.")
        else:
            print(f"{participant} was not found in the participants list of the meeting {self.title}.")

    def postpone_meeting(self, new_start_time, new_end_time):
        self.start_time = new_start_time
        self.end_time = new_end_time
        print(f"Meeting '{self.title}' has been postponed to {self.start_time} - {self.end_time}.")

    def prepone_meeting(self, new_start_time, new_end_time):
        self.start_time = new_start_time
        self.end_time = new_end_time
        print(f"Meeting '{self.title}' has been preponed to {self.start_time} - {self.end_time}.")

    def record_meeting_minutes(self, minute_id, minutes):
        self.minutes[minute_id] = minutes
        print(f"Meeting minutes recorded for meeting '{self.title}'.")

    def retrieve_meeting_records(self, record_id):
        return self.minutes.get(record_id, None)


class MeetingManager:
    def __init__(self):
        self.meetings = []

    def show_options(self):
        print("""
        1. Add Meeting
        2. List All Meetings
        3. Search Meeting
        4. Delete Meeting
        5. Join Participant to Meeting
        6. Leave Participant from Meeting
        7. Postpone Meeting
        8. Prepone Meeting
        9. Record Meeting Minutes
        10. Retrieve Meeting Records
        11. Exit
        """)

    def run(self):
        while True:
            self.show_options()
            option = input("Enter your option: ").strip()
            if option == '1':
                self.add_meeting()
            elif option == '2':
                self.list_all_meetings()
            elif option == '3':
                keyword = input("Enter Title to search meetings: ").strip()
                self.search_meetings(keyword)
            elif option == '4':
                meeting_id = input("Enter Meeting ID to delete: ").strip()
                self.delete_meeting(meeting_id)
            elif option == '5':
                self.join_participant_to_meeting()
            elif option == '6':
                self.leave_participant_from_meeting()
            elif option == '7':
                self.postpone_meeting()
            elif option == '8':
                self.prepone_meeting()
            elif option == '9':
                self.record_meeting_minutes()
            elif option == '10':
                self.retrieve_meeting_records()
            elif option == '11':
                print("Exiting the program...")
                break
            else:
                print("Invalid option. Please try again.")

    def add_meeting(self):
        meeting_id = input("Enter Meeting ID: ").strip()
        title = input("Enter Meeting Title: ").strip()
        date = input("Enter Meeting Date (YYYY-MM-DD): ").strip()
        participants_input = input("Enter Participants (comma-separated): ").strip()
        participants = participants_input.split(",")
        start_time = input("Enter Start Time (HH:MM): ").strip()
        end_time = input("Enter End Time (HH:MM): ").strip()
        meeting = Meeting(meeting_id, title, date, participants, start_time, end_time)
        self.meetings.append(meeting)
        print("Meeting added successfully.")

    def list_all_meetings(self):
        if not self.meetings:
            print("No meetings found.")
        else:
            for i, meeting in enumerate(self.meetings, 1):
                print(f"Meeting {i}:")
                print("Meeting ID:", meeting.meeting_id)
                print(f"Title: {meeting.title}")
                print(f"Date: {meeting.date}")
                print(f"Participants: {', '.join(meeting.participants)}")
                print(f"Start Time: {meeting.start_time}")
                print(f"End Time: {meeting.end_time}\n")

    def search_meetings(self, keyword):
        found = False
        for meeting in self.meetings:
            if keyword.lower() in meeting.title.lower():
                found = True
                print(f"Meeting on {meeting.date}:")
                print(f"Meeting ID: {meeting.meeting_id}")
                print(f"Title: {meeting.title}")
                print(f"Participants: {', '.join(meeting.participants)}")
                print(f"Start Time: {meeting.start_time}")
                print(f"End Time: {meeting.end_time}\n")
        if not found:
            print("No meetings found.")

    def delete_meeting(self, meeting_id):
        for i, meeting in enumerate(self.meetings):
            if meeting.meeting_id == meeting_id:
                del self.meetings[i]
                print("Meeting deleted successfully.")
                return
        print("Meeting ID not found.")

    def join_participant_to_meeting(self):
        meeting_id = input("Enter Meeting ID to join: ").strip()
        participant = input("Enter Participant's name: ").strip()
        for meeting in self.meetings:
            if meeting.meeting_id == meeting_id:
                meeting.join_participant(participant)
                return
        print("Meeting ID not found.")

    def leave_participant_from_meeting(self):
        meeting_id = input("Enter Meeting ID to leave: ").strip()
        participant = input("Enter Participant's name: ").strip()
        for meeting in self.meetings:
            if meeting.meeting_id == meeting_id:
                meeting.leave_participant(participant)
                return
        print("Meeting ID not found.")

    def postpone_meeting(self):
        meeting_id = input("Enter Meeting ID to postpone: ").strip()
        for meeting in self.meetings:
            if meeting.meeting_id == meeting_id:
                new_start_time = input("Enter new Start Time (HH:MM): ").strip()
                new_end_time = input("Enter new End Time (HH:MM): ").strip()
                meeting.postpone_meeting(new_start_time, new_end_time)
                return
        print("Meeting ID not found.")


# Create an instance of MeetingManager and start the program
manager = MeetingManager()
manager.run()
