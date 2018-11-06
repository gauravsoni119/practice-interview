test_cases = input()
week_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
def get_day_of_week_when_syllabus_completed(topics_completed_in_week, topics):
	day = 0
	completed_topics = sum(topics_completed_in_week)
	remaining_topics = topics % completed_topics
	days_to_complete_topics = 0
	i = 0
	if remaining_topics != 0:
		while days_to_complete_topics < remaining_topics:
			days_to_complete_topics = days_to_complete_topics + topics_completed_in_week[i]
			i+= 1
		return week_days[i-1]
	else:
		for i in range(0, len(topics_completed_in_week)):
			if topics_completed_in_week[i] != 0:
				days_to_complete_topics = i
		return week_days[days_to_complete_topics]

for i in range(0, test_cases):
	topics = input()
	
	topics_completed_in_week = raw_input().split()
	topics_completed_in_week = map(int, topics_completed_in_week)
	day = get_day_of_week_when_syllabus_completed(topics_completed_in_week, topics)
	print day
